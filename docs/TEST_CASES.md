# Test Cases: NexoTech Solutions Ticket Routing

| Field | Value |
|---|---|
| Project | Ticket routing system for NexoTech Solutions |
| Course | AI-Assisted Python for Business Problem Solving (PSI163), PUCPR, 2026/2 |
| Indicator | ID1.2: conditional structures, repetition and functions, tested with different input values |
| Based on | `docs/PROBLEM_ANALYSIS.md` v1.2, business rules BR0 to BR4 |
| Code under test | `validations.py` → `clean_text()`, `is_missing()`; `calculations.py` → `get_queue()`, `get_deadline_hours()`, `route_ticket()`, `calculate_percentage()`; `main.py` → `format_deadline()` and the end-of-run summary (tickets from `sample_tickets.py`) |
| Version | 1.3, 2026-09-29 (see section 8) |

---

## 1. Rules under test

| Rule | Summary |
|---|---|
| **BR0: Input cleaning** | Category and priority are converted to lowercase and surrounding spaces are removed before any rule runs. A missing value (`None`), or a field that is absent from the ticket, becomes empty text |
| **BR1: Routing** | Access, Software → L1 Helpdesk · Infrastructure, Hardware → L2 Field Team · Finance → Admin · General → Triage |
| **BR2: Resolution deadline** | High → 4 hours · Medium → 24 hours · Low → 72 hours |
| **BR3: Unknown category** | A category outside the six above (after cleaning) → Triage, status "Needs review". The deadline still follows BR2 |
| **BR4: Unknown priority** | A priority outside High / Medium / Low (after cleaning) → Triage, deadline 0 (no deadline), status "Needs review" |
| **Status** | "Needs review" when BR3 or BR4 applies, "Routed" otherwise. A General ticket is "Routed" |

---

## 2. How to run these tests

1. Open a terminal inside the `support-triage` folder and start Python with `python`.
2. Import the functions once:
   ```
   >>> from validations import clean_text, is_missing
   >>> from calculations import get_queue, get_deadline_hours, route_ticket, calculate_percentage
   >>> from main import format_deadline
   ```
   The last import runs the whole program once and prints its output first. That is expected: `main.py` calls `main()` at the end. After that, `format_deadline()` is ready to test.
3. For each test, call the function with that test's input, exactly as written in the table. When a row shows two inputs (`calculate_percentage()`), pass them in that order, e.g. `calculate_percentage(3, 15)`. Write `None` without quotes for a missing value, and `""` for empty text. For example, with an input that is not in the tables:
   ```
   >>> route_ticket("Software", "HIGH")
   {'queue': 'L1 Helpdesk', 'deadline_hours': 4, 'status': 'Routed'}
   >>> get_queue("SOFTWARE")
   'L1 Helpdesk'
   ```
4. Write what the function returns in **Actual Result**. For `route_ticket()`, use the form `queue / deadline / status`, e.g. `L1 Helpdesk / 4 / Routed`.
5. Fill in **Passed:** **Yes** only if the actual result matches the expected one, **No** otherwise. Record every **No** in section 6.

**Summary check (section 5):** run `python main.py` and compare the end-of-run summary with the expected values.

---

## 3. Test tables

### 3.1 Full routing: `route_ticket(category, priority)`

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
| TC19 | BR3, BR2 | Category not in the list | Printer | High | Triage | 4 | Needs review | | |
| TC20 | BR3, BR2 | Category missing | `None` | Low | Triage | 72 | Needs review | | |
| TC21 | BR3, BR2 | Category is empty text | `""` | Medium | Triage | 24 | Needs review | | |
| TC22 | BR4 | Priority not in the list | Access | Urgent | Triage | 0 | Needs review | | |
| TC23 | BR4 | Priority is empty text | Hardware | `""` | Triage | 0 | Needs review | | |
| TC24 | BR4 | Priority missing | Software | `None` | Triage | 0 | Needs review | | |
| TC25 | BR3, BR4 | Category and priority both unknown | Printer | Urgent | Triage | 0 | Needs review | | |
| TC26 | BR3, BR4 | Category and priority both missing | `None` | `None` | Triage | 0 | Needs review | | |

### 3.2 Individual functions

The course asks for every function to be tested with different input values. These rows test each helper function on its own.

| Test ID | Function | Scenario description | Input | Expected Result | Actual Result | Passed |
|---|---|---|---|---|---|---|
| FT01 | `clean_text()` | Mixed capitalization | `"Access"` | `"access"` | | |
| FT02 | `clean_text()` | Surrounding spaces and uppercase | `"  HIGH "` | `"high"` | | |
| FT03 | `clean_text()` | Missing value | `None` | `""` | | |
| FT04 | `clean_text()` | Number instead of text | `3` | `"3"` | | |
| FT05 | `is_missing()` | Missing value | `None` | `True` | | |
| FT06 | `is_missing()` | Only spaces | `"   "` | `True` | | |
| FT07 | `is_missing()` | Empty text | `""` | `True` | | |
| FT08 | `is_missing()` | Normal text | `"Finance"` | `False` | | |
| FT09 | `get_queue()` | Access, normal capitalization | `"Access"` | `"L1 Helpdesk"` | | |
| FT10 | `get_queue()` | Software, lowercase | `"software"` | `"L1 Helpdesk"` | | |
| FT11 | `get_queue()` | Infrastructure, uppercase | `"INFRASTRUCTURE"` | `"L2 Field Team"` | | |
| FT12 | `get_queue()` | Hardware | `"Hardware"` | `"L2 Field Team"` | | |
| FT13 | `get_queue()` | Finance with surrounding spaces | `" finance "` | `"Admin"` | | |
| FT14 | `get_queue()` | General | `"General"` | `"Triage"` | | |
| FT15 | `get_queue()` | Category not in the list | `"Printer"` | `"Triage"` | | |
| FT16 | `get_queue()` | Missing category | `None` | `"Triage"` | | |
| FT17 | `get_deadline_hours()` | High | `"High"` | `4` | | |
| FT18 | `get_deadline_hours()` | Medium, lowercase | `"medium"` | `24` | | |
| FT19 | `get_deadline_hours()` | Low, uppercase with spaces | `" LOW "` | `72` | | |
| FT20 | `get_deadline_hours()` | Priority not in the list | `"Urgent"` | `0` | | |
| FT21 | `get_deadline_hours()` | Missing priority | `None` | `0` | | |
| FT22 | `format_deadline()` | High-priority deadline | `4` | `"4 hours"` | | |
| FT23 | `format_deadline()` | Medium-priority deadline | `24` | `"24 hours"` | | |
| FT24 | `format_deadline()` | Low-priority deadline | `72` | `"72 hours"` | | |
| FT25 | `format_deadline()` | No deadline set (BR4) | `0` | `"not set (priority must be reviewed)"` | | |
| FT26 | `calculate_percentage()` | Part of the total | `3, 15` | `20.0` | | |
| FT27 | `calculate_percentage()` | Largest queue in the sample | `6, 15` | `40.0` | | |
| FT28 | `calculate_percentage()` | All tickets in one queue | `15, 15` | `100.0` | | |
| FT29 | `calculate_percentage()` | Queue with no tickets | `0, 15` | `0.0` | | |
| FT30 | `calculate_percentage()` | Empty ticket list (total 0, no division by zero) | `0, 0` | `0.0` | | |

---

## 4. Coverage

### 4.1 By rule

The course asks for each business rule to be tested with at least three different input values.

| Rule | Tests | Different inputs tested |
|---|---|---|
| BR0: Input cleaning | TC15 to TC18, FT01 to FT04 | Lowercase, uppercase, extra spaces, `None`, a number |
| BR1: Routing | TC01 to TC18, FT09 to FT14 | All 6 categories, each at least twice |
| BR2: Deadline | TC01 to TC21, FT17 to FT19 | High (TC01, 04, 05, 09, 13, 17, 19), Medium (TC03, 07, 10, 12, 15, 18, 21), Low (TC02, 06, 08, 11, 14, 16, 20) |
| BR3: Unknown category | TC19, TC20, TC21, TC25, TC26, FT15, FT16 | Unlisted value, `None`, empty text |
| BR4: Unknown priority | TC22 to TC26, FT20, FT21 | Unlisted value, empty text, `None` |

### 4.2 By function

| Function | Direct tests | Also exercised by |
|---|---|---|
| `clean_text()` | FT01 to FT04 | Every TC test, through `route_ticket()` |
| `is_missing()` | FT05 to FT08 | `main.py` output ("(missing)") |
| `get_queue()` | FT09 to FT16 | Every TC test |
| `get_deadline_hours()` | FT17 to FT21 | Every TC test |
| `route_ticket()` | TC01 to TC26 | `main.py` run (section 5) |
| `format_deadline()` | FT22 to FT25 | `main.py` output ("Deadline:" lines) |
| `calculate_percentage()` | FT26 to FT30 | `main.py` summary percentages (section 5) |

### 4.3 Queue × priority

Every queue is tested with every priority.

| Queue | High | Medium | Low |
|---|---|---|---|
| L1 Helpdesk | TC01, TC04 | TC03, TC15 | TC02, TC16 |
| L2 Field Team | TC05 | TC07, TC18 | TC06, TC08 |
| Admin | TC09, TC17 | TC10 | TC11 |
| Triage (General) | TC13 | TC12 | TC14 |

---

## 5. End-of-run summary check (`main.py`)

`main.py` processes the 15 synthetic tickets in `sample_tickets.py` (IDs 1001 to 1015). Ticket 1015 has no `description` and no `priority` key at all. After `python main.py`, the output must show:

| Check | Expected | Tickets | Actual | Passed |
|---|---|---|---|---|
| L1 Helpdesk | 4 (26.7%) | 1001, 1002, 1007, 1010 | | |
| L2 Field Team | 3 (20.0%) | 1003, 1004, 1008 | | |
| Admin | 2 (13.3%) | 1005, 1009 | | |
| Triage | 6 (40.0%) | 1006, 1011, 1012, 1013, 1014, 1015 | | |
| **Total processed** | **15** | 1001 to 1015 | | |
| Needs review | 5: [1011, 1012, 1013, 1014, 1015] | 1011 (unknown category), 1012 (Urgent), 1013 (missing priority), 1014 (both missing), 1015 (no description or priority key) | | |
| Missing fields do not crash the program | The program finishes. Ticket 1015 shows `Ticket 1015: (missing)` and `Priority: (missing)` | 1015 | | |

---

## 6. Failures found

Fill in one row per failed test. After the fix, re-run the test and record the result.

| Test ID | What happened | Cause | Fix applied | Re-test passed |
|---|---|---|---|---|
| | | | | |

---

## 7. Notes on edge cases

- **Capitalization and spaces (TC15 to TC18, FT01, FT02).** BR0 cleans the values before any rule runs, so `"access"`, `"ACCESS"` and `"  Hardware "` are recognized. `get_queue()` and `get_deadline_hours()` also clean their own input, so they give correct results when tested on their own. The program still displays the original value, so the messy input stays visible in the output.
- **General vs. unknown category (TC12 to TC14 vs. TC19 to TC21).** Both go to Triage, but only an unrecognized category is marked "Needs review", because General is a valid category.
- **Missing values and missing keys (TC20, TC23, TC24, TC26, ticket 1015).** `clean_text()` turns `None` into empty text. `main.py` reads each field with `.get()`, so a key that is absent from the ticket also becomes `None` instead of stopping the program.
- **Both unknown (TC25, TC26).** BR4 sets the deadline to 0; the queue is Triage and the status is "Needs review" either way.
- **Test data only.** All tickets and test inputs are synthetic. No real people, companies or records are used.

---

## 8. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-09-29 | First version (22 tests). |
| 1.1 | 2026-09-29 | Supabase removed; capitalization ignored (BR0); 26 tests; summary check based on `main.py`. |
| 1.2 | 2026-09-29 | Corrections accepted in the AI debugging cycle (AI log Entry 013): TC19 to TC21 now expect "Needs review" (BR3); 21 direct function tests added (FT01 to FT21); summary check updated for 15 tickets, including ticket 1015 without a description or priority key. |
| 1.3 | 2026-09-29 | AI refactoring cycle (AI log Entry 015): 9 direct tests added for the new functions `format_deadline()` (FT22 to FT25) and `calculate_percentage()` (FT26 to FT30); the sample tickets now come from `sample_tickets.py`. All other expected results are unchanged, because the refactoring did not change the program's behavior. |

---

*During the preparation of this document, the author(s) used Claude (Anthropic, model claude-opus-5) to derive the test cases, coverage tables and run procedure from the team's business rules (BR0 to BR4), to update them after the AI debugging cycle, and to add tests for the functions created in the AI refactoring cycle. After using this tool, the author(s) reviewed and edited the content as needed and take full responsibility for the content.*
