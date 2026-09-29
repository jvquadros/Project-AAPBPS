# sample_tickets.py
# Synthetic tickets processed by main.py (15 tickets, IDs 1001 to 1015).
# Keeping the data in its own module leaves main.py in charge of running
# the program only.
#
# AI disclosure (PUCPR Resolution 274/2024): During the preparation of this code,
# the author(s) used Claude (Anthropic, model claude-opus-5) to write the mock
# ticket list and to move it into this module in the AI refactoring cycle
# (AI log Entry 015). After using this tool, the author(s) reviewed and edited
# the content as needed and take full responsibility for the content.

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
