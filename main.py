import os
import time
import gradio as gr
from dotenv import load_dotenv
from core.graph import create_graph
from ui.ui import create_ui
from openai import OpenAI
from fpdf import FPDF



load_dotenv()

# Initialize OpenAI Client and Graph
client = OpenAI()
graph_app = create_graph()


def is_safe(text):
    """
    Checks for prohibited content using OpenAI Moderation API.
    """
    try:
        response = client.moderations.create(input=text)
        output = response.results[0]
        return not output.flagged
    except Exception:
        return True  # Fallback if API fails


def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)

    # PDF එක support නොකරන characters (Smart quotes, dashes) සාමාන්‍ය ඒවට replace කරනවා
    clean_text = text.replace("**", "")  # Markdown bold අයින් කරනවා
    clean_text = clean_text.replace("’", "'").replace("‘", "'")  # Smart quotes fix
    clean_text = clean_text.replace("“", '"').replace("”", '"')  # Double quotes fix
    clean_text = clean_text.replace("–", "-").replace("—", "-")  # Long dashes fix

    clean_text = clean_text.encode('latin-1', 'replace').decode('latin-1')

    pdf.multi_cell(0, 10, txt=clean_text)

    file_path = "Business_Strategic_Report.pdf"
    pdf.output(file_path)
    return file_path


def execution_logic(business_idea):
    if not business_idea.strip() or len(business_idea) < 10:
        yield "The concept is too short.", gr.update(visible=False)
        return

    try:
        yield "Engaging multi-agent pipeline: Researching market data...", gr.update(visible=False)

        result = graph_app.invoke({"business_idea": business_idea})
        full_report = result.get("final_output", "Error: Failed to synthesize report.")

        displayed_text = ""
        # 1. Streaming Effect
        for line in full_report.split("\n"):
            displayed_text += line + "\n"
            yield displayed_text, gr.update(visible=False)
            time.sleep(0.05)

        # 2. Create PDF after streaming ends
        pdf_path = create_pdf(full_report)

        # 3. Show Download Button
        yield displayed_text, gr.update(value=pdf_path, visible=True)

    except Exception as e:
        yield f"System Error: {str(e)}", gr.update(visible=False)

# Get UI and CSS from ui.py
app_interface, style_css = create_ui(execution_logic)

if __name__ == "__main__":
    print("InsightEdge Engine is starting...")

    # Launch with Authentication and Custom CSS
    app_interface.launch(
        share=True,
        auth=(os.getenv("APP_USERNAME"), os.getenv("APP_PASSWORD")),
        auth_message="InsightEdge Intelligence: Enter credentials to proceed.",
        css=style_css,
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="slate",
            font=[gr.themes.GoogleFont("Inter"), "sans-serif"]
        )
    )