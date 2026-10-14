"""Application configuration loaded from environment variables."""

from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv

from models import ApprovedRules


def _load_environment() -> None:
    """Load .env from either the project directory or its parent directory."""

    env_path = Path.cwd() / ".env"
    if not env_path.exists():
        env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        env_path = Path(__file__).resolve().parents[2] / ".env"
    load_dotenv(dotenv_path=env_path, override=True)


def _as_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    model_name: str
    send_emails: bool
    demo_recipient: str
    resend_api_key: str
    resend_from: str
    gradio_server_name: str
    gradio_server_port: int
    approved_rules: ApprovedRules

    @classmethod
    def from_environment(cls) -> "Settings":
        _load_environment()
        return cls(
            model_name=os.getenv("OPENAI_MODEL", "gpt-5.4-mini"),
            send_emails=_as_bool(os.getenv("SEND_EMAILS"), default=True),
            demo_recipient=os.getenv("RESEND_TO", "").strip(),
            resend_api_key=os.getenv("RESEND_API_KEY", "").strip(),
            resend_from=os.getenv("RESEND_FROM", "").strip(),
            gradio_server_name=os.getenv("GRADIO_SERVER_NAME", "0.0.0.0"),
            gradio_server_port=int(os.getenv("GRADIO_SERVER_PORT", "7860")),
            approved_rules=ApprovedRules(
                company_name=os.getenv("BUSINESS_NAME", "ComplAI"),
                approved_services=[
                    "SOC 2 readiness assessment",
                    "AI-assisted control mapping",
                    "Evidence organization and audit preparation",
                ],
                approved_claims=[
                    "ComplAI helps teams organize evidence for SOC 2 preparation.",
                    "ComplAI can help identify control gaps and outstanding evidence.",
                ],
                pricing_policy="Do not quote or discount pricing without human approval.",
            ),
        )


settings = Settings.from_environment()
