"""Deterministic Python orchestration for the proposal workflow."""

from agents import Runner, trace

from config import settings
from emailer_agent import emailer_agent
from models import WorkflowResult
from proposal_agent import proposal_agent
from research_agent import research_agent


async def run_proposal_workflow(
    company: str,
    industry: str,
    additional_context: str = "",
) -> WorkflowResult:
    """Research a prospect, write a proposal, and send it to RESEND_TO."""

    company = company.strip()
    industry = industry.strip() or "the company's industry"
    additional_context = additional_context.strip() or "No additional context provided."

    if not company:
        raise ValueError("A target company is required.")

    research_request = f"""
Research this prospect:
Company: {company}
Industry: {industry}
Additional context: {additional_context}
""".strip()

    with trace("Proposal workflow"):
        research_result = await Runner.run(research_agent, research_request)
        research = research_result.final_output

        proposal_request = f"""
Target company: {company}
Industry: {industry}

Approved business information:
{settings.approved_rules.model_dump_json(indent=2)}

Prospect research:
{research.model_dump_json(indent=2)}

Create the tailored cold sales email.
""".strip()
        proposal_result = await Runner.run(proposal_agent, proposal_request)
        proposal = proposal_result.final_output

        email_request = f"""
Subject: {proposal.subject}
Body:
{proposal.body}
""".strip()
        email_result = await Runner.run(emailer_agent, email_request)

    return WorkflowResult(
        company=company,
        research=research,
        proposal=proposal,
        email_status=email_result.final_output,
    )
