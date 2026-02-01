import gradio as gr


def create_ui(generate_fn):
    custom_css = """
    #header { text-align: center; padding-bottom: 20px; }
    #generate-btn { background-color: #007bff; color: white; border-radius: 8px; font-weight: bold; }
    #generate-btn:hover { background-color: #0056b3; }
    .gradio-container { max-width: 1100px !important; }
    """

    with gr.Blocks(theme=gr.themes.Base(primary_hue="blue", secondary_hue="slate"), css=custom_css) as demo:
        # Header Section
        with gr.Div(elem_id="header"):
            gr.Markdown("# 🚀 **InsightEdge**")
            gr.Markdown("### *Autonomous Market Intelligence & Strategy Engine*")
            gr.Markdown(
                "Leveraging Multi-Agent AI to transform your business ideas into comprehensive strategic reports.")

        gr.Spacer()

        with gr.Row():
            # Left Panel: Input Area
            with gr.Column(scale=1):
                gr.Markdown("### **1. Idea Configuration**")
                input_txt = gr.Textbox(
                    label="Business Concept",
                    placeholder="Describe your business idea (e.g., A subscription-based AI legal assistant for SMEs)...",
                    lines=5,
                    elem_id="input-box"
                )

                gr.Markdown("---")
                gr.Markdown("**Agents involved in this process:**")
                gr.Markdown("✅ *Market Trends Researcher*")
                gr.Markdown("✅ *Competitor Insight Analyst*")
                gr.Markdown("✅ *Strategic Growth Consultant*")

                submit_btn = gr.Button("GENERATE STRATEGY REPORT", variant="primary", elem_id="generate-btn")

            # Right Panel: Output Area
            with gr.Column(scale=2):
                gr.Markdown("### **2. Strategic Analysis Report**")
                output_md = gr.Markdown(
                    value="*Analysis report will be rendered here after processing...*",
                    label="Final Output"
                )

        gr.Markdown("---")
        with gr.Row():
            gr.Markdown("✨ **Powered by LangGraph & GPT-4o**")
            gr.Markdown("🔍 **Real-time Web Intelligence by Tavily**")

        # Action Binding
        submit_btn.click(
            fn=generate_fn,
            inputs=input_txt,
            outputs=output_md
        )

    return demo