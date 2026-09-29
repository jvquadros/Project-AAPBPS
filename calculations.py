# calculations.py
# Business rules for NexoTech Solutions ticket routing (BR1 to BR4).
# These functions only calculate and return results. They never print and
# never create or read ticket data, so each rule can be tested on its own.
#
# AI disclosure (PUCPR Resolution 274/2024): During the preparation of this code,
# the author(s) used Claude (Anthropic, model claude-opus-5) to implement the
# team's routing and deadline rules (BR1 to BR4) as functions. After using this
# tool, the author(s) reviewed and edited the content as needed and take full
# responsibility for the content.

from validations import clean_text

# Queue names are written once, so the rules and the summary always use the same text.
L1_HELPDESK = "L1 Helpdesk"
L2_FIELD_TEAM = "L2 Field Team"
ADMIN = "Admin"
TRIAGE = "Triage"

# Tuple: the four queues never change while the program runs,
# and this fixed order is the order used in the end-of-run summary.
QUEUES = (L1_HELPDESK, L2_FIELD_TEAM, ADMIN, TRIAGE)

STATUS_ROUTED = "Routed"
STATUS_NEEDS_REVIEW = "Needs review"

# 0 hours means that no deadline has been set (BR4).
NO_DEADLINE = 0


def get_queue(category):
    """Return the queue for a cleaned category (BR1).

    Any category that is not recognized goes to Triage (BR3).
    """
    if category == "access" or category == "software":
        return L1_HELPDESK
    elif category == "infrastructure" or category == "hardware":
        return L2_FIELD_TEAM
    elif category == "finance":
        return ADMIN
    else:
        # "general", plus any unrecognized or missing category (BR3)
        return TRIAGE


def get_deadline_hours(priority):
    """Return the resolution deadline in hours for a cleaned priority (BR2).

    An unknown priority returns NO_DEADLINE instead of a default value,
    because a wrong default could delay an urgent ticket (BR4).
    """
    if priority == "high":
        return 4
    elif priority == "medium":
        return 24
    elif priority == "low":
        return 72
    else:
        return NO_DEADLINE


def route_ticket(category, priority):
    """Apply BR0 to BR4 to one ticket and return its queue, deadline and status."""
    # BR0 runs first, so "ACCESS", "access" and " Access " are treated the same
    clean_category = clean_text(category)
    clean_priority = clean_text(priority)

    queue = get_queue(clean_category)
    deadline_hours = get_deadline_hours(clean_priority)

    if deadline_hours == NO_DEADLINE:
        # BR4: a person must set the priority before anyone works on the ticket
        queue = TRIAGE
        status = STATUS_NEEDS_REVIEW
    else:
        status = STATUS_ROUTED

    return {"queue": queue, "deadline_hours": deadline_hours, "status": status}
