"""Gradio entrypoint for the AI proposal workflow."""

import gradio as gr

from config import settings
from styles import APP_CSS
from workflow import run_proposal_workflow


def _format_result(result) -> str:
    sources = "\n".join(f"- {source}" for source in result.research.sources)
    return f"""## Proposal for {result.company}

**Subject:** {result.proposal.subject}

{result.proposal.body}

### Research Summary

{result.research.summary}

### Sources

{sources or '- No sources returned.'}

### Email Status

{result.email_status}
"""


async def generate_proposal(company: str, industry: str, additional_context: str) -> str:
    """Handle the Gradio form submission."""

    try:
        result = await run_proposal_workflow(company, industry, additional_context)
    except Exception as exc:
        return f"**Workflow error:** `{exc}`"
    return _format_result(result)


with gr.Blocks(title="AI Proposal Writer") as demo:
    gr.Markdown(
        """
        <div class="hero">
        <h1>AI Proposal Writer</h1>
        <p>Research a prospect, write a tailored proposal, and send the demo email to your configured RESEND_TO address.</p>
        </div>
        """
    )

    with gr.Row():
        company_input = gr.Textbox(label="Prospective company", placeholder="Dcastalia Limited")
        industry_input = gr.Textbox(label="Industry", placeholder="Software development")

    context_input = gr.Textbox(
        label="Additional context",
        placeholder="Known pain points, role of the recipient, or campaign context",
        lines=4,
    )
    submit_button = gr.Button("Research, write, and send", variant="primary")
    output = gr.Markdown(elem_classes=["output"])

    submit_button.click(
        fn=generate_proposal,
        inputs=[company_input, industry_input, context_input],
        outputs=output,
    )


if __name__ == "__main__":
    demo.queue().launch(
        server_name=settings.gradio_server_name,
        server_port=settings.gradio_server_port,
        css=APP_CSS,
    )
