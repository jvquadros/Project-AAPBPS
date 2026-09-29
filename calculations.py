# calculations.py
# Business rules for NexoTech Solutions ticket routing (BR1 to BR4), plus the
# percentage calculation used in the end-of-run summary.
# These functions only calculate and return results. They never print and
# never create or read ticket data, so each rule can be tested on its own.
#
# AI disclosure (PUCPR Resolution 274/2024): During the preparation of this code,
# the author(s) used Claude (Anthropic, model claude-opus-5) to implement the
# team's routing and deadline rules (BR1 to BR4) as functions, to apply the
# corrections the team accepted in the AI debugging cycle (AI log Entry 013),
# and to add calculate_percentage() in the AI refactoring cycle (AI log
# Entry 015). After using this tool, the author(s) reviewed and edited the
# content as needed and take full responsibility for the content.

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
    """Return the queue for a category (BR1).

    Any category that is not recognized goes to Triage (BR3).
    """
    # BR0 runs here too, so this function also works when it is tested on its own
    clean_category = clean_text(category)

    if clean_category == "access" or clean_category == "software":
        return L1_HELPDESK
    elif clean_category == "infrastructure" or clean_category == "hardware":
        return L2_FIELD_TEAM
    elif clean_category == "finance":
        return ADMIN
    else:
        # "general", plus any unrecognized or missing category (BR3)
        return TRIAGE


def get_deadline_hours(priority):
    """Return the resolution deadline in hours for a priority (BR2).

    An unknown priority returns NO_DEADLINE instead of a default value,
    because a wrong default could delay an urgent ticket (BR4).
    """
    # BR0 runs here too, so this function also works when it is tested on its own
    clean_priority = clean_text(priority)

    if clean_priority == "high":
        return 4
    elif clean_priority == "medium":
        return 24
    elif clean_priority == "low":
        return 72
    else:
        return NO_DEADLINE


def route_ticket(category, priority):
    """Apply BR0 to BR4 to one ticket and return its queue, deadline and status."""
    # Needed below to tell a "general" ticket apart from an unrecognized category
    clean_category = clean_text(category)

    queue = get_queue(category)
    deadline_hours = get_deadline_hours(priority)

    if deadline_hours == NO_DEADLINE:
        # BR4: a person must set the priority before anyone works on the ticket
        queue = TRIAGE
        status = STATUS_NEEDS_REVIEW
    elif queue == TRIAGE and clean_category != "general":
        # BR3: the category was not recognized, so a person must decide where it belongs
        status = STATUS_NEEDS_REVIEW
    else:
        status = STATUS_ROUTED

    return {"queue": queue, "deadline_hours": deadline_hours, "status": status}


def calculate_percentage(count, total):
    """Return count as a percentage of total (for example 3 of 15 -> 20.0).

    Returns 0.0 when total is 0, to avoid a division by zero.
    """
    if total == 0:
        return 0.0
    return count / total * 100
