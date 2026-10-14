"""Small UI styling layer for the Gradio application."""

APP_CSS = """
:root { --ink: #1d2433; --muted: #667085; --accent: #b04a2f; --paper: #f6f1e9; }
body, .gradio-container { background: var(--paper) !important; }
.gradio-container { max-width: 980px !important; margin: 0 auto; }
h1, h2, h3 { color: var(--ink) !important; }
.hero { border-left: 4px solid var(--accent); padding-left: 18px; margin-bottom: 24px; }
.output { background: white; border: 1px solid #e4ded4; padding: 18px; }
button.primary { background: var(--accent) !important; border-color: var(--accent) !important; }
"""
