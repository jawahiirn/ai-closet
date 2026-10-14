"""Typed data exchanged between proposal workflow stages."""

from pydantic import BaseModel, Field


class ApprovedRules(BaseModel):
    """Information the proposal agent is allowed to use as company policy."""

    company_name: str
    approved_services: list[str]
    approved_claims: list[str]
    pricing_policy: str


class ProspectResearch(BaseModel):
    """Structured findings returned by the research agent."""

    company: str
    industry: str
    summary: str
    relevant_needs: list[str]
    evidence: list[str]
    sources: list[str]


class ProposalDraft(BaseModel):
    """A proposal email ready for the emailer agent."""

    subject: str
    body: str
    proposed_services: list[str]
    assumptions: list[str] = Field(default_factory=list)


class WorkflowResult(BaseModel):
    """Complete result shown by the Gradio application."""

    company: str
    research: ProspectResearch
    proposal: ProposalDraft
    email_status: str
