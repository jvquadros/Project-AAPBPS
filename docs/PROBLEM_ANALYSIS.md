# Problem Analysis: NexoTech Solutions Ticket Routing

| Field | Value |
|---|---|
| Project | Ticket routing system for NexoTech Solutions |
| Course | AI-Assisted Python for Business Problem Solving (PSI163), PUCPR, 2026/2 |
| Indicator | ID1.1: analyze an organizational problem, identify inputs, processing and outputs, and decompose it into logical steps |
| Version | 1.1, 2026-09-29 (v1.0 approved by the team; v1.1 adds BR0, input cleaning; see section 7) |

---

## 0. Business context

**NexoTech Solutions** is a fictional IT support company invented for this course. All tickets used in this project are synthetic. No real people, companies or records are involved.

NexoTech's help desk receives support tickets and passes each one to one of four teams (queues):

| Queue | Handles |
|---|---|
| **L1 Helpdesk** | First-level support: access problems and software issues |
| **L2 Field Team** | Second-level technicians: infrastructure and hardware problems |
| **Admin** | Finance-related requests |
| **Triage** | General requests and any ticket that needs a person to review it |

---

## 1. Guiding questions

| # | Question | Answer |
|---|---|---|
| 1 | **What problem are we trying to solve?** | Today someone has to read every ticket just to decide which team should handle it and how fast it must be solved. This is slow and inconsistent: tickets wait unassigned, some reach the wrong team, and urgent tickets are not clearly separated from routine ones. The system must **send each ticket to the correct queue and assign it a resolution deadline automatically**, following fixed business rules. |
| 2 | **What information is available? What is missing?** | *Available:* each ticket has an ID, a description, a **category** (Infrastructure, Finance, Access, Software, Hardware, General) and a **priority** (High, Medium, Low). *Missing in this phase:* the exact time the ticket was opened (so the deadline is given in hours, not as a date and time); how busy each team is; any check that the requester chose the right category. |
| 3 | **What rules must be respected?** | The input cleaning rule (capitalization and extra spaces are ignored), the routing rule (category → queue), the resolution deadline rule (priority → hours), and the two validation rules for categories and priorities that are not recognized. See section 4. |
| 4 | **What should the solution produce?** | For each ticket: its **queue**, its **resolution deadline in hours** and its **status** ("Routed" or "Needs review"). After all tickets are processed: a **summary** with the number of tickets in each queue and the number that need review. |

---

## 2. Input → Processing → Output

| Input | Processing | Output |
|---|---|---|
| A list of support tickets. Each ticket has: **ticket ID**, **description**, **category**, **priority** | 1. Read the ticket's fields.<br>2. Clean the category and priority: lowercase, no surrounding spaces (BR0).<br>3. Find the queue from the category (BR1, BR3).<br>4. Find the resolution deadline from the priority (BR2).<br>5. If the priority is not recognized, send the ticket to Triage with no deadline and mark it for review (BR4).<br>6. Count the ticket in its queue. | For each ticket: **queue**, **deadline (hours)**, **status**.<br>At the end: a **summary** of tickets per queue and the number of tickets needing review. |

### 2.1 Input fields

| Field | Data type | Example | Used for |
|---|---|---|---|
| `ticket_id` | integer | `1001` | Identifying the ticket in the output |
| `description` | text | `"Cannot log in to the VPN"` | Shown in the output. Not used by the rules in this phase |
| `category` | text | `"Access"`, `"access"` or `"ACCESS"` (any capitalization) | Routing (BR0, BR1, BR3) |
| `priority` | text | `"High"`, `"high"` or `"HIGH"` (any capitalization) | Resolution deadline (BR0, BR2, BR4) |

### 2.2 Output fields

| Field | Data type | Example |
|---|---|---|
| `queue` | text | `"L1 Helpdesk"` |
| `deadline_hours` | integer | `4` (0 means no deadline has been set) |
| `status` | text | `"Routed"` or `"Needs review"` |

---

## 3. Step-by-step logical breakdown

### 3.1 Decomposition

1. Load the list of tickets to process.
2. Take the next ticket and read its ID, description, category and priority.
3. **Clean** the category and priority: convert them to lowercase, remove surrounding spaces, and turn a missing value into empty text (BR0).
4. Decide the **queue** from the category (BR1). An unrecognized category goes to Triage (BR3).
5. Decide the **resolution deadline** from the priority (BR2).
6. If the priority is not recognized, send the ticket to **Triage**, set **no deadline**, and mark it **"Needs review"** (BR4). Otherwise mark it **"Routed"**.
7. Display the result for this ticket: ID, category, priority, queue, deadline, status.
8. Add 1 to the count for the ticket's queue. If the ticket needs review, also record its ID in the "needs review" list.
9. Repeat steps 2 to 8 until every ticket has been processed.
10. Display the summary: tickets per queue and tickets needing review.

### 3.2 Computational thinking applied

| Element | How it applies to NexoTech |
|---|---|
| **Decomposition** | The problem splits into input cleaning, two independent decisions (**routing** and **deadline**), validation and a final summary (steps 1 to 10 above). |
| **Pattern recognition** | Every ticket goes through the same steps; only the values change. The steps are defined once and repeated for each ticket. Categories that share a queue are grouped (Access + Software, Infrastructure + Hardware). |
| **Abstraction** | Kept: ticket ID, category, priority, and the description (for display only). Ignored: the requester's name and contact details, device model, location, time of day. They are not needed to route a ticket, and leaving them out also avoids handling personal data. |
| **Algorithm design** | The finite, ordered sequence of steps in section 3.1, written as pseudocode in section 5. |

---

## 4. Business rules

### BR0: Input cleaning (applied first)

Before any other rule runs, the category and priority are converted to **lowercase** and **surrounding spaces are removed**. A missing value becomes empty text. This means "Access", "access", "ACCESS" and " Access " are all the same category, and every rule below compares the cleaned values.

### BR1: Routing by category

A ticket is sent to a queue according to its category.

| Category | Queue |
|---|---|
| Access | L1 Helpdesk |
| Software | L1 Helpdesk |
| Infrastructure | L2 Field Team |
| Hardware | L2 Field Team |
| Finance | Admin |
| General | Triage |

### BR2: Resolution deadline by priority

A ticket must be resolved within a number of hours that depends on its priority.

| Priority | Resolution deadline |
|---|---|
| High | 4 hours |
| Medium | 24 hours |
| Low | 72 hours |

### BR3: Unrecognized category

If a ticket's category, after cleaning, is not one of the six listed in BR1 (including a missing category), it is treated like a General ticket and sent to **Triage**, where a person decides where it belongs.

### BR4: Unrecognized priority

If a ticket's priority, after cleaning, is not High, Medium or Low (including a missing priority), the ticket gets **no deadline** (0 hours), is sent to **Triage**, and is marked **"Needs review"** so that a person can set the correct priority. It does **not** get a default deadline, because a wrong default (for example, 72 hours on an urgent ticket) could delay a critical problem.

### Status

Every ticket that passes BR4 is marked **"Routed"**. A ticket caught by BR4 is marked **"Needs review"**.

---

## 5. Pseudocode

The algorithm below processes **one ticket**. It uses only the keywords START, READ, CALCULATE, DISPLAY and END, plus IF / ELIF / ELSE / END IF for the decisions.

```
START
    READ ticket_id
    READ description
    READ category
    READ priority

    CALCULATE clean_category = category in lowercase, without surrounding spaces
    CALCULATE clean_priority = priority in lowercase, without surrounding spaces
    CALCULATE status = "Routed"

    IF clean_category is "access" OR clean_category is "software"
        CALCULATE queue = "L1 Helpdesk"
    ELIF clean_category is "infrastructure" OR clean_category is "hardware"
        CALCULATE queue = "L2 Field Team"
    ELIF clean_category is "finance"
        CALCULATE queue = "Admin"
    ELSE
        CALCULATE queue = "Triage"
    END IF

    IF clean_priority is "high"
        CALCULATE deadline_hours = 4
    ELIF clean_priority is "medium"
        CALCULATE deadline_hours = 24
    ELIF clean_priority is "low"
        CALCULATE deadline_hours = 72
    ELSE
        CALCULATE deadline_hours = 0
        CALCULATE queue = "Triage"
        CALCULATE status = "Needs review"
    END IF

    DISPLAY ticket_id
    DISPLAY category
    DISPLAY priority
    DISPLAY queue
    DISPLAY deadline_hours
    DISPLAY status
END
```

**Notes on the pseudocode**

- **Cleaning (BR0).** The two cleaning steps run before any decision, so every comparison uses lowercase values. The original values are kept for display.
- **Routing decision (BR1, BR3).** Four paths. The final ELSE covers both "General" and any unrecognized category, so every ticket always gets a queue.
- **Deadline decision (BR2, BR4).** Four paths. The final ELSE handles an unrecognized priority. It overrides the queue with "Triage" and marks the ticket for review, so BR4 is applied in one single place.
- **Repetition.** The whole block runs once for each ticket in the list (steps 2 to 9 of section 3.1). The counts per queue and the final summary (steps 8 and 10) sit around this block. In Python they become a `for` loop with counters, which is ST2 content.
- **Decision values.** Each branch of both decisions will be tested with at least three different input values in `docs/TEST_CASES.md`.

---

## 6. Assumptions

1. The **category** comes with the ticket; the requester chooses it when opening the ticket. In this phase the system does not check the category against the description text.
2. Deadlines are **counted in hours from the moment the ticket is opened**. Turning them into an exact due date and time is outside this phase.
3. The tickets processed in this phase are a **small synthetic sample**: a list of dictionaries defined in `main.py`. There is no database or external data source.

---

## 7. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-09-29 | First version. Approved by the team, including BR3, BR4, the status field, the end-of-run summary and the single-ticket pseudocode. |
| 1.1 | 2026-09-29 | Added BR0 (input cleaning): capitalization and surrounding spaces are ignored. Pseudocode, IPO table and decomposition updated to match. Team decision. |

---

*During the preparation of this document, the author(s) used Claude (Anthropic, model claude-opus-5) to structure the problem analysis (guiding questions, IPO table, decomposition, business rules and pseudocode) from the business rules defined by the team, to propose the handling of unrecognized categories and priorities (BR3, BR4), and to write the input cleaning rule (BR0) requested by the team. After using this tool, the author(s) reviewed and edited the content as needed and take full responsibility for the content.*
