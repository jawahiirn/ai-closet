"""Side-effecting tools used by the emailer agent."""

import resend
from agents import function_tool

from config import settings


resend.api_key = settings.resend_api_key


@function_tool
def send_demo_email(subject: str, body: str) -> str:
    """Send the proposal email to the configured RESEND_TO demo recipient."""

    if not settings.send_emails:
        return "Email sending is disabled by SEND_EMAILS."
    if not settings.resend_api_key:
        return "Error: RESEND_API_KEY is not configured."
    if not settings.resend_from:
        return "Error: RESEND_FROM is not configured."
    if not settings.demo_recipient or "@" not in settings.demo_recipient:
        return "Error: RESEND_TO is not configured with a valid email address."
    if not subject.strip() or not body.strip():
        return "Error: subject and body are required."

    try:
        response = resend.Emails.send(
            {
                "from": settings.resend_from,
                "to": [settings.demo_recipient],
                "subject": subject,
                "text": body,
            }
        )
    except Exception as exc:
        return f"Error sending email: {exc}"

    email_id = response.get("id") if isinstance(response, dict) else getattr(response, "id", response)
    return f"Email sent to {settings.demo_recipient} (id={email_id})"
