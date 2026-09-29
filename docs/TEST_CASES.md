# Test Cases: NexoTech Solutions Ticket Routing

| Field | Value |
|---|---|
| Project | Ticket routing system for NexoTech Solutions |
| Course | AI-Assisted Python for Business Problem Solving (PSI163), PUCPR, 2026/2 |
| Indicator | ID1.2: conditional structures, repetition and functions, tested with different input values |
| Based on | `docs/PROBLEM_ANALYSIS.md` v1.1, business rules BR0 to BR4 |
| Code under test | `calculations.py` → `route_ticket(category, priority)`, which uses `clean_text()` from `validations.py`; `main.py` for the summary |
| Version | 1.1, 2026-09-29 |

---

## 1. Rules under test

| Rule | Summary |
|---|---|
| **BR0: Input cleaning** | Category and priority are converted to lowercase and surrounding spaces are removed before any rule runs. A missing value (`None`) becomes empty text |
| **BR1: Routing** | Access, Software → L1 Helpdesk · Infrastructure, Hardware → L2 Field Team · Finance → Admin · General → Triage |
| **BR2: Resolution deadline** | High → 4 hours · Medium → 24 hours · Low → 72 hours |
| **BR3: Unknown category** | A category outside the six above (after cleaning) → Triage. The deadline still follows BR2 |
| **BR4: Unknown priority** | A priority outside High / Medium / Low (after cleaning) → Triage, deadline 0 (no deadline), status "Needs review" |
| **Status** | "Routed" for every ticket, except those caught by BR4, which get "Needs review" |

---

## 2. How to run these tests

**Single test cases (section 3):**

1. Open a terminal inside the `support-triage` folder and start Python with `python`.
2. Import the function once:
   ```
   >>> from calculations import route_ticket
   ```
3. For each test, call the function with that test's inputs, exactly as written in the table. Write `None` without quotes for a missing value, and `""` for empty text. For example, an input that is not in the table:
   ```
   >>> route_ticket("Software", "HIGH")
   {'queue': 'L1 Helpdesk', 'deadline_hours': 4, 'status': 'Routed'}
   ```
4. Write what the function returns in **Actual Result** as `queue / deadline / status`, e.g. `L1 Helpdesk / 4 / Routed`.
5. Fill in **Passed:** **Yes** only if all three values match the expected columns, **No** otherwise. Record every **No** in section 6.

**Summary check (section 5):** run `python main.py` and compare the end-of-run summary with the expected values.

---

## 3. Test table

| Test ID | Rules | Scenario description | Input: Category | Input: Priority | Expected Queue | Expected Deadline (hours) | Expected Status | Actual Result | Passed |
|---|---|---|---|---|---|---|---|---|---|
| TC01 | BR1, BR2 | Access ticket, high priority | Access | High | L1 Helpdesk | 4 | Routed | | |
| TC02 | BR1, BR2 | Access ticket, low priority | Access | Low | L1 Helpdesk | 72 | Routed | | |
| TC03 | BR1, BR2 | Software ticket, medium priority | Software | Medium | L1 Helpdesk | 24 | Routed | | |
| TC04 | BR1, BR2 | Software ticket, high priority | Software | High | L1 Helpdesk | 4 | Routed | | |
| TC05 | BR1, BR2 | Infrastructure ticket, high priority | Infrastructure | High | L2 Field Team | 4 | Routed | | |
| TC06 | BR1, BR2 | Infrastructure ticket, low priority | Infrastructure | Low | L2 Field Team | 72 | Routed | | |
| TC07 | BR1, BR2 | Hardware ticket, medium priority | Hardware | Medium | L2 Field Team | 24 | Routed | | |
| TC08 | BR1, BR2 | Hardware ticket, low priority | Hardware | Low | L2 Field Team | 72 | Routed | | |
| TC09 | BR1, BR2 | Finance ticket, high priority | Finance | High | Admin | 4 | Routed | | |
| TC10 | BR1, BR2 | Finance ticket, medium priority | Finance | Medium | Admin | 24 | Routed | | |
| TC11 | BR1, BR2 | Finance ticket, low priority | Finance | Low | Admin | 72 | Routed | | |
| TC12 | BR1, BR2 | General ticket, medium priority | General | Medium | Triage | 24 | Routed | | |
| TC13 | BR1, BR2 | General ticket, high priority | General | High | Triage | 4 | Routed | | |
| TC14 | BR1, BR2 | General ticket, low priority | General | Low | Triage | 72 | Routed | | |
| TC15 | BR0, BR1, BR2 | Category written in lowercase | `"access"` | Medium | L1 Helpdesk | 24 | Routed | | |
| TC16 | BR0, BR1, BR2 | Category written in uppercase | `"ACCESS"` | Low | L1 Helpdesk | 72 | Routed | | |
| TC17 | BR0, BR1, BR2 | Priority written in lowercase | Finance | `"high"` | Admin | 4 | Routed | | |
| TC18 | BR0, BR1, BR2 | Extra spaces in the category, priority in uppercase | `"  Hardware "` | `"MEDIUM"` | L2 Field Team | 24 | Routed | | |
| TC19 | BR3, BR2 | Category not in the list | Printer | High | Triage | 4 | Routed | | |
| TC20 | BR3, BR2 | Category missing | `None` | Low | Triage | 72 | Routed | | |
| TC21 | BR3, BR2 | Category is empty text | `""` | Medium | Triage | 24 | Routed | | |
| TC22 | BR4 | Priority not in the list | Access | Urgent | Triage | 0 | Needs review | | |
| TC23 | BR4 | Priority is empty text | Hardware | `""` | Triage | 0 | Needs review | | |
| TC24 | BR4 | Priority missing | Software | `None` | Triage | 0 | Needs review | | |
| TC25 | BR3, BR4 | Category and priority both unknown | Printer | Urgent | Triage | 0 | Needs review | | |
| TC26 | BR3, BR4 | Category and priority both missing | `None` | `None` | Triage | 0 | Needs review | | |

---

## 4. Coverage

### 4.1 By rule

The course asks for each business rule to be tested with at least three different input values.

| Rule | Tests | Different inputs tested |
|---|---|---|
| BR0: Input cleaning | TC15 to TC18 | Lowercase category, uppercase category, lowercase priority, extra spaces + uppercase priority |
| BR1: Routing | TC01 to TC18 | All 6 categories, each at least twice |
| BR2: Deadline | TC01 to TC21 | High (TC01, 04, 05, 09, 13, 17, 19), Medium (TC03, 07, 10, 12, 15, 18, 21), Low (TC02, 06, 08, 11, 14, 16, 20) |
| BR3: Unknown category | TC19, TC20, TC21, TC25, TC26 | Unlisted value, `None`, empty text |
| BR4: Unknown priority | TC22 to TC26 | Unlisted value, empty text, `None` |

### 4.2 Queue × priority

Every queue is tested with every priority.

| Queue | High | Medium | Low |
|---|---|---|---|
| L1 Helpdesk | TC01, TC04 | TC03, TC15 | TC02, TC16 |
| L2 Field Team | TC05 | TC07, TC18 | TC06, TC08 |
| Admin | TC09, TC17 | TC10 | TC11 |
| Triage (General) | TC13 | TC12 | TC14 |

---

## 5. End-of-run summary check (`main.py`)

`main.py` processes 14 synthetic tickets (IDs 1001 to 1014). After `python main.py`, the summary must show:

| Summary line | Expected | Tickets counted | Actual | Passed |
|---|---|---|---|---|
| L1 Helpdesk | 4 (28.6%) | 1001, 1002, 1007, 1010 | | |
| L2 Field Team | 3 (21.4%) | 1003, 1004, 1008 | | |
| Admin | 2 (14.3%) | 1005, 1009 | | |
| Triage | 5 (35.7%) | 1006, 1011, 1012, 1013, 1014 | | |
| **Total processed** | **14** | 1001 to 1014 | | |
| Needs review | 3: [1012, 1013, 1014] | 1012 (Urgent), 1013 (missing priority), 1014 (both missing) | | |

---

## 6. Failures found

Fill in one row per failed test. After the fix, re-run the test and record the result.

| Test ID | What happened | Cause | Fix applied | Re-test passed |
|---|---|---|---|---|
| | | | | |

---

## 7. Notes on edge cases

- **Capitalization and spaces (TC15 to TC18).** BR0 cleans the values before any rule runs, so `"access"`, `"ACCESS"` and `"  Hardware "` are recognized. The program still displays the original value, so the messy input stays visible in the output.
- **Missing values (TC20, TC23, TC24, TC26).** `clean_text()` turns `None` into empty text. The rules then treat it like any other unrecognized value, so the program never crashes on a missing field.
- **Both unknown (TC25, TC26).** BR3 would send the ticket to Triage anyway, and BR4 then sets the deadline and status. The final result is the same as any other BR4 case.
- **Test data only.** All tickets and test inputs are synthetic. No real people, companies or records are used.

---

*During the preparation of this document, the author(s) used Claude (Anthropic, model claude-opus-5) to derive the test cases, coverage tables and run procedure from the team's business rules (BR0 to BR4). After using this tool, the author(s) reviewed and edited the content as needed and take full responsibility for the content.*
