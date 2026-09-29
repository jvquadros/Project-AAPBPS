# main.py
# Runs the NexoTech Solutions ticket routing on a local list of tickets:
# routes each ticket, prints its result, then prints an end-of-run summary.
#
# How to run (inside the support-triage folder):  python main.py
#
# AI disclosure (PUCPR Resolution 274/2024): During the preparation of this code,
# the author(s) used Claude (Anthropic, model claude-opus-5) to write the mock
# ticket list, the processing loop, the summary counters and the output
# formatting, and to apply the corrections the team accepted in the AI
# debugging cycle (AI log Entry 013). After using this tool, the author(s)
# reviewed and edited the content as needed and take full responsibility for
# the content.

from validations import is_missing
from calculations import route_ticket, QUEUES, STATUS_NEEDS_REVIEW, NO_DEADLINE

# List of dictionaries: one dictionary per ticket.
# All tickets are synthetic. Some values are messy on purpose, to show the
# cleaning rule (BR0) and the unknown-value rules (BR3 and BR4). Ticket 1015
# has no "description" or "priority" key at all, to show that a missing field
# does not crash the program.
tickets = [
    {"ticket_id": 1001, "description": "Cannot log in to the VPN",
     "category": "Access", "priority": "High"},
    {"ticket_id": 1002, "description": "Spreadsheet app crashes on startup",
     "category": "Software", "priority": "Medium"},
    {"ticket_id": 1003, "description": "Office network is down",
     "category": "Infrastructure", "priority": "High"},
    {"ticket_id": 1004, "description": "Laptop screen is flickering",
     "category": "Hardware", "priority": "Low"},
    {"ticket_id": 1005, "description": "Invoice shows the wrong amount",
     "category": "Finance", "priority": "Medium"},
    {"ticket_id": 1006, "description": "Question about support hours",
     "category": "General", "priority": "Low"},
    {"ticket_id": 1007, "description": "Password reset link expired",
     "category": "access", "priority": "medium"},
    {"ticket_id": 1008, "description": "Keyboard is not responding",
     "category": "HARDWARE", "priority": "HIGH"},
    {"ticket_id": 1009, "description": "Refund request for a duplicate charge",
     "category": "  Finance ", "priority": "Low"},
    {"ticket_id": 1010, "description": "Email client license expired",
     "category": "Software", "priority": "Low"},
    {"ticket_id": 1011, "description": "Paper jams on every print",
     "category": "Printer", "priority": "Medium"},
    {"ticket_id": 1012, "description": "Server room temperature alarm",
     "category": "Infrastructure", "priority": "Urgent"},
    {"ticket_id": 1013, "description": "New employee needs an account",
     "category": "Access", "priority": None},
    {"ticket_id": 1014, "description": "Something is not working",
     "category": None, "priority": None},
    {"ticket_id": 1015, "category": "Hardware"},
]


def show_value(value):
    """Return a field as it was received, or "(missing)" when it is empty."""
    if is_missing(value):
        return "(missing)"
    return value


def print_ticket_result(ticket, result):
    """Show the routing result of one ticket."""
    # .get() returns None when a key is missing, and show_value() turns None into "(missing)"
    print("-" * 50)
    print(f"Ticket {show_value(ticket.get('ticket_id'))}: "
          f"{show_value(ticket.get('description'))}")
    print(f"  Category: {show_value(ticket.get('category'))}  |  "
          f"Priority: {show_value(ticket.get('priority'))}")
    print(f"  Queue:    {result['queue']}")
    if result["deadline_hours"] == NO_DEADLINE:
        print("  Deadline: not set (priority must be reviewed)")
    else:
        print(f"  Deadline: {result['deadline_hours']} hours")
    print(f"  Status:   {result['status']}")


def print_summary(queue_counts, total_tickets, needs_review_ids):
    """Show how many tickets went to each queue and which ones need review."""
    print("=" * 50)
    print("END-OF-RUN SUMMARY")
    print("=" * 50)

    if total_tickets == 0:
        # Avoids a division by zero when the ticket list is empty
        print("No tickets were processed.")
        return

    for queue in QUEUES:
        count = queue_counts[queue]
        share = count / total_tickets * 100
        print(f"{queue}: {count} ticket(s) ({share:.1f}%)")

    print("-" * 50)
    print(f"Total processed: {total_tickets}")
    print(f"Needs review: {len(needs_review_ids)} ticket(s) {needs_review_ids}")


# ---------------- Program execution ----------------

# Dictionary of counters: one counter per queue, each starting at zero
queue_counts = {}
for queue in QUEUES:
    queue_counts[queue] = 0

total_tickets = 0
needs_review_ids = []

print("=" * 50)
print("NEXOTECH SOLUTIONS - TICKET ROUTING")
print("=" * 50)

for ticket in tickets:
    # .get() instead of ticket["..."]: a missing key gives None instead of a KeyError
    result = route_ticket(ticket.get("category"), ticket.get("priority"))
    print_ticket_result(ticket, result)

    queue_counts[result["queue"]] = queue_counts[result["queue"]] + 1
    total_tickets = total_tickets + 1
    if result["status"] == STATUS_NEEDS_REVIEW:
        needs_review_ids.append(ticket.get("ticket_id"))

print_summary(queue_counts, total_tickets, needs_review_ids)
