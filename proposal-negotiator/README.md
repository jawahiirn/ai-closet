# Proposal Negotiator

A small Gradio application that researches a prospect, writes a tailored cold sales email, and sends the demo email through Resend.

## Architecture

```text
Gradio UI
   -> workflow.py
      -> research_agent.py -> OpenAI WebSearchTool
      -> proposal_agent.py
      -> emailer_agent.py -> tools.py -> Resend
```

Each agent has one responsibility. `workflow.py` performs the orchestration explicitly in Python.

## Setup

```bash
cp .env.example .env
```

Set these values in `.env`:

- `OPENAI_API_KEY`
- `RESEND_API_KEY`
- `RESEND_FROM`
- `RESEND_TO`

The demo intentionally sends to `RESEND_TO`. The emailer tool does not accept a recipient from the model or UI.

Install dependencies and start the app:

```bash
uv sync
uv run python app.py
```

Alternatively:

```bash
pip install -r requirements.txt
python app.py
```

Open the Gradio URL shown in the terminal, enter a company, and submit the form.

## Safety

This is configured for a demo and sends email by default when `SEND_EMAILS=true`. Set `SEND_EMAILS=false` to disable delivery while developing. Replace the example approved business rules in `config.py` before using real proposals.

Never commit `.env` or API keys.
