import gradio as gr

def create_ui(generate_fn):
    custom_css = """
    .gradio-container { font-family: 'Inter', sans-serif; }
    .header-box { 
        text-align: center; padding: 40px 20px; 
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
        border-radius: 16px; margin-bottom: 24px; color: white; 
    }
    .panel-bg { 
        background-color: var(--background-fill-primary); 
        border: 1px solid var(--border-color-primary); 
        border-radius: 12px; padding: 24px; box-shadow: var(--shadow-drop);
    }

    /* Workflow step styling */
    .workflow-container { display: flex; gap: 10px; margin-top: 20px; flex-direction: column; }
    .step { 
        padding: 12px; border-radius: 8px; border: 1px dashed #3b82f6;
        background: rgba(59, 130, 246, 0.05); font-size: 0.9em;
    }
    .step-title { font-weight: bold; color: #3b82f6; display: block; margin-bottom: 4px; }

    #generate-btn { 
        background: linear-gradient(90deg, #2563eb, #3b82f6) !important; 
        color: white !important; font-weight: 700 !important; 
        border-radius: 8px; height: 54px; border: none; margin-top: 15px;
    }
    .report-area { color: var(--body-text-color) !important; font-size: 1.1em; line-height: 1.8; }
    .report-area b, .report-area strong { color: #2563eb !important; }
    """

    with gr.Blocks(title="InsightEdge AI") as demo:
        with gr.Column(elem_classes="header-box"):
            gr.HTML("<h1 style='color: white; font-size: 2.5em; font-weight: 800; margin: 0;'>INSIGHTEDGE</h1>")
            gr.HTML("<p style='color: rgba(255,255,255,0.9);'>Strategic Multi-Agent Intelligence Engine</p>")

        with gr.Row(equal_height=True):
            with gr.Column(scale=1):
                with gr.Column(elem_classes="panel-bg"):
                    gr.Markdown("### **1. Concept Input**")
                    input_txt = gr.Textbox(
                        label=None,
                        placeholder="Describe your business vision...",
                        lines=10, container=False
                    )

                    gr.HTML("<p style='font-size: 0.85em; margin-top: 10px; opacity: 0.8;'>Intelligence Layer: <b>GPT-5.2 (2025-12-11)</b></p>")

                    gr.HTML("""
                    <div class="workflow-container">
                        <div class="step">
                            <span class="step-title">Agent 01: Market Researcher</span>
                            Scans global trends and validates market demand.
                        </div>
                        <div class="step">
                            <span class="step-title">Agent 02: Competitor Analyst</span>
                            Identifies market gaps and competitive positioning.
                        </div>
                        <div class="step">
                            <span class="step-title">Agent 03: Strategic Consultant</span>
                            Synthesizes the final actionable business report.
                        </div>
                    </div>
                    """)

                    submit_btn = gr.Button("RUN STRATEGIC ANALYSIS", elem_id="generate-btn")

            with gr.Column(scale=2):
                with gr.Column(elem_classes="panel-bg"):
                    gr.Markdown("### **2. Strategic Report**")
                    output_md = gr.Markdown(
                        value="*Awaiting input. The multi-agent pipeline will render the report here.*",
                        elem_classes="report-area",
                        line_breaks=True
                    )
                    download_btn = gr.DownloadButton("DOWNLOAD AS PDF", visible=False)

        gr.HTML(
            "<div style='text-align: center; margin-top: 30px; opacity: 0.6; font-size: 0.8em; line-height: 1.6;'>"
            "Powered by LangGraph Agentic Framework"
            "</div>")

        submit_btn.click(fn=generate_fn, inputs=input_txt, outputs=[output_md, download_btn])
    return demo, custom_css