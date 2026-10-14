"""Email-sending agent."""

from agents import Agent, ModelSettings

from config import settings
from tools import send_demo_email


emailer_agent = Agent(
    name="Emailer Agent",
    model=settings.model_name,
    instructions="""
Send exactly the subject and body provided by the workflow.
Do not rewrite or expand the email.
Call send_demo_email exactly once.
""".strip(),
    tools=[send_demo_email],
    model_settings=ModelSettings(tool_choice="required"),
)
