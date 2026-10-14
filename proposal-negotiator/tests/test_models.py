from models import ApprovedRules, ProposalDraft


def test_proposal_draft_requires_subject_and_body() -> None:
    proposal = ProposalDraft(
        subject="A useful subject",
        body="A useful body",
        proposed_services=["SOC 2 readiness assessment"],
    )

    assert proposal.subject == "A useful subject"
    assert proposal.assumptions == []


def test_approved_rules_store_business_constraints() -> None:
    rules = ApprovedRules(
        company_name="Example",
        approved_services=["Assessment"],
        approved_claims=["Approved claim"],
        pricing_policy="Approval required",
    )

    assert rules.approved_services == ["Assessment"]
    assert "approval" in rules.pricing_policy.lower()
