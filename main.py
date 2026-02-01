import os
import time
import gradio as gr
from dotenv import load_dotenv
from core.graph import create_graph
from ui.ui import create_ui
from openai import OpenAI

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


def execution_logic(business_idea):
    # 1. Validation for empty or short input
    if not business_idea.strip() or len(business_idea) < 10:
        yield "The concept is too short for a meaningful analysis. Please provide more detail."
        return

    # 2. Safety Check
    if not is_safe(business_idea):
        yield "Policy Violation: Your input contains prohibited content. Please provide a valid business concept."
        return

    try:
        # Initial status updates to the user
        yield "Initializing strategic analysis engine..."
        time.sleep(1)
        yield "Engaging multi-agent pipeline: Researching market data..."

        # Invoke the LangGraph to get the full report
        result = graph_app.invoke({"business_idea": business_idea})
        full_report = result.get("final_output", "Error: Failed to synthesize report.")

        # 3. Simulated Streaming Effect
        # මුළු report එකම වචනයෙන් වචනය UI එකට stream කරනවා
        displayed_text = ""
        # පේළි වලට කඩලා stream කරනවා
        for line in full_report.split("\n"):
            displayed_text += line + "\n"
            yield displayed_text
            time.sleep(0.05)  # පේළියක් ලියවෙන්න යන වෙලාව  # Adjusted speed for a smooth professional look

    except Exception as e:
        yield f"System Error: {str(e)}"


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