"""Proposal-writing agent."""

from agents import Agent

from config import settings
from models import ProposalDraft


proposal_agent = Agent(
    name="Proposal Agent",
    model=settings.model_name,
    instructions="""
You are a proposal specialist.
Write one concise, professional cold sales email for the target company.
Use research only as evidence for personalization.
Use only the approved services and approved claims supplied in the request.
Never invent pricing, delivery promises, certifications, guarantees, or client results.
If information is missing, use conservative language and record the assumption.
Return a subject and plain-text email body.
""".strip(),
    output_type=ProposalDraft,
)
