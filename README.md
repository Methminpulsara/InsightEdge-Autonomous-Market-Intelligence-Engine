# InsightEdge: Autonomous Multi-Agent Intelligence Engine

InsightEdge is a strategic business intelligence tool that leverages a coordinated pipeline of AI agents to analyze business ideas. Unlike a simple chatbot, it orchestrates specialized agents to deliver comprehensive market research, competitor analysis, and actionable business strategies.

## Overview

InsightEdge is not just a chatbot—it's a coordinated pipeline of AI agents designed for strategic business intelligence. Built with LangGraph and GPT-5.2, it automates the process of evaluating business concepts by simulating a multi-agent workflow. Users input a business idea, and the system generates a detailed Markdown report with a Go/No-Go verdict, complete with a downloadable PDF.

## How It Works (The Multi-Agent Pipeline)

The system operates as a Directed Acyclic Graph (DAG) where data flows sequentially through specialized agents:

1. **Research Agent**: Utilizes Tavily Search to gather current market trends and demand data for the business idea.
2. **Analyst Agent**: Performs SWOT analysis and identifies competitor gaps based on the research data.
3. **Strategist Agent**: Compiles all insights into a final Markdown report, including an executive summary, SWOT analysis, market entry strategy, and a Go/No-Go recommendation. The report is also converted into a downloadable PDF.

## Technical Architecture

InsightEdge uses LangGraph's StateGraph to manage the agent orchestration. The `AgentState` TypedDict passes data between nodes in the DAG:

- **Nodes**: Each agent (Research, Analyst, Strategist) is a node in the graph.
- **Edges**: Data flows from Research → Analyst → Strategist → End.
- **State Management**: The `AgentState` includes fields like `business_idea`, `market_research_data`, `competitor_data`, and `final_output` to maintain context across agents.

This architecture ensures modular, scalable, and traceable AI workflows.

## Environment Setup

Create a `.env` file in the root directory with the following variables:

```
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key

# UI Authentication
APP_USERNAME=admin
APP_PASSWORD=password123
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/insight_edge.git
   cd insight_edge
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r req.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

The Gradio UI will launch, allowing you to input business ideas and generate reports.

## Tech Stack

- **Python**: Core language.
- **LangChain**: For prompt engineering and LLM integration.
- **LangGraph**: For multi-agent orchestration and state management.
- **OpenAI (GPT-5.2)**: Primary LLM for agent reasoning.
- **Gradio**: Web UI for user interaction.
- **Tavily API**: For web search and market data retrieval.
- **FPDF2**: For PDF generation.

## Usage

1. Launch the app via `python main.py`.
2. Enter a business idea in the input field.
3. Click "RUN STRATEGIC ANALYSIS" to trigger the multi-agent pipeline.
4. View the generated report and download the PDF.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.
