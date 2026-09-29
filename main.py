# main.py
# Runs the NexoTech Solutions ticket routing on the sample tickets:
# routes each ticket, prints its result, then prints an end-of-run summary.
#
# How to run (inside the support-triage folder):  python main.py
#
# AI disclosure (PUCPR Resolution 274/2024): During the preparation of this code,
# the author(s) used Claude (Anthropic, model claude-opus-5) to write the
# processing loop, the summary counters and the output formatting, to apply the
# corrections the team accepted in the AI debugging cycle (AI log Entry 013),
# and to reorganize the code into functions in the AI refactoring cycle
# (AI log Entry 015). After using this tool, the author(s) reviewed and edited
# the content as needed and take full responsibility for the content.

from validations import is_missing
from calculations import route_ticket, calculate_percentage
from calculations import QUEUES, STATUS_NEEDS_REVIEW, NO_DEADLINE
from sample_tickets import tickets

# Width of the separator lines, written once so it can be changed in one place
LINE_WIDTH = 50


def print_banner(title):
    """Print a title between two lines of "=" characters."""
    print("=" * LINE_WIDTH)
    print(title)
    print("=" * LINE_WIDTH)


def create_queue_counters():
    """Return a dictionary with one counter per queue, each starting at zero."""
    queue_counts = {}
    for queue in QUEUES:
        queue_counts[queue] = 0
    return queue_counts


def format_deadline(deadline_hours):
    """Return the deadline as text for the output (0 means no deadline, BR4)."""
    if deadline_hours == NO_DEADLINE:
        return "not set (priority must be reviewed)"
    return f"{deadline_hours} hours"


def show_value(value):
    """Return a field as it was received, or "(missing)" when it is empty."""
    if is_missing(value):
        return "(missing)"
    return value


def print_ticket_result(ticket, result):
    """Show the routing result of one ticket."""
    # .get() returns None when a key is missing, and show_value() turns None into "(missing)"
    print("-" * LINE_WIDTH)
    print(f"Ticket {show_value(ticket.get('ticket_id'))}: "
          f"{show_value(ticket.get('description'))}")
    print(f"  Category: {show_value(ticket.get('category'))}  |  "
          f"Priority: {show_value(ticket.get('priority'))}")
    print(f"  Queue:    {result['queue']}")
    print(f"  Deadline: {format_deadline(result['deadline_hours'])}")
    print(f"  Status:   {result['status']}")


def print_summary(queue_counts, total_tickets, needs_review_ids):
    """Show how many tickets went to each queue and which ones need review."""
    print_banner("END-OF-RUN SUMMARY")

    if total_tickets == 0:
        # With no tickets there is nothing to count or compare
        print("No tickets were processed.")
        return

    for queue in QUEUES:
        count = queue_counts[queue]
        share = calculate_percentage(count, total_tickets)
        print(f"{queue}: {count} ticket(s) ({share:.1f}%)")

    print("-" * LINE_WIDTH)
    print(f"Total processed: {total_tickets}")
    print(f"Needs review: {len(needs_review_ids)} ticket(s) {needs_review_ids}")


def main():
    """Route every ticket, print each result, then print the summary."""
    queue_counts = create_queue_counters()
    total_tickets = 0
    needs_review_ids = []

    print_banner("NEXOTECH SOLUTIONS - TICKET ROUTING")

    for ticket in tickets:
        # .get() instead of ticket["..."]: a missing key gives None instead of a KeyError
        result = route_ticket(ticket.get("category"), ticket.get("priority"))
        print_ticket_result(ticket, result)

        queue_counts[result["queue"]] = queue_counts[result["queue"]] + 1
        total_tickets = total_tickets + 1
        if result["status"] == STATUS_NEEDS_REVIEW:
            needs_review_ids.append(ticket.get("ticket_id"))

    print_summary(queue_counts, total_tickets, needs_review_ids)


# Everything above only defines functions; this line runs the program
main()
