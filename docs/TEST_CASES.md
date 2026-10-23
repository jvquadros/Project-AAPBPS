# Test Cases: NexoTech Solutions Ticket Routing

| Field | Value |
|---|---|
| Project | Ticket routing system for NexoTech Solutions |
| Course | AI-Assisted Python for Business Problem Solving (PSI163), PUCPR, 2026/2 |
| Indicator | ID1.2: conditional structures, repetition and functions, tested with different input values (Summative item 2.3) |
| Based on | `docs/PROBLEM_ANALYSIS.md` v1.6, business rules BR0 to BR4 and the summary calculation (section 2.4) |
| Code under test | `validations.py` → `clean_text()`, `is_missing()`; `calculations.py` → `get_queue()`, `get_deadline_hours()`, `route_ticket()`, `calculate_percentage()`; `main.py` → `format_deadline()`, the keyboard entry (`ask_yes_or_no()` from `validations.py`, `read_manual_ticket()`, `get_next_ticket_id()` from `calculations.py`) and the end-of-run summary (tickets from `sample_tickets.py`) |
| Version | 1.6, 2026-10-12 (see section 8) |
| Result | **All tests executed and passed:** 30/30 routing, 33/33 function, 5/5 keyboard, 7/7 summary checks (see section 9) |

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

1. Open a terminal inside the project folder and start Python with `python`.
2. Import the functions once:
   ```
   >>> from validations import clean_text, is_missing
   >>> from calculations import get_queue, get_deadline_hours, route_ticket, calculate_percentage, get_next_ticket_id
   >>> from main import format_deadline
   ```
   The last import runs the whole program once, because `main.py` calls `main()` at the end. The program first asks "Add a ticket manually? (yes/no)": type `no`. It then prints its output, and after that `format_deadline()` is ready to test. (If you type `yes` here, the typed ticket stays in the `tickets` list for the rest of the Python session, so FT31 would return 1017 instead of 1016. Restart Python to start again.)
3. For each test, call the function with that test's input, exactly as written in the table. When a row shows two inputs (`calculate_percentage()`), pass them in that order, e.g. `calculate_percentage(3, 15)`. Write `None` without quotes for a missing value, and `""` for empty text. For example, with an input that is not in the tables:
   ```
   >>> route_ticket("Software", "HIGH")
   {'queue': 'L1 Helpdesk', 'deadline_hours': 4, 'status': 'Routed'}
   >>> get_queue("SOFTWARE")
   'L1 Helpdesk'
   ```
4. Write what the function returns in **Actual Result**. For `route_ticket()`, use the form `queue / deadline / status`, e.g. `L1 Helpdesk / 4 / Routed`.
5. Fill in **Passed:** **Yes** only if the actual result matches the expected one, **No** otherwise. Record every **No** in section 6.

**Summary check (section 5):** run `python main.py`, answer `no` to "Add a ticket manually?", and compare the end-of-run summary with the expected values.

**Keyboard tests (section 3.3):** run `python main.py` and type the inputs listed for each test, pressing Enter after each one. Write what the program shows in **Actual Result**.

---

## 3. Test tables

### 3.1 Full routing: `route_ticket(category, priority)`

| Test ID | Rules | Scenario description | Input: Category | Input: Priority | Expected Queue | Expected Deadline (hours) | Expected Status | Actual Result | Passed |
|---|---|---|---|---|---|---|---|---|---|
| TC01 | BR1, BR2 | Access ticket, high priority | Access | High | L1 Helpdesk | 4 | Routed | L1 Helpdesk / 4 / Routed | Yes |
| TC02 | BR1, BR2 | Access ticket, low priority | Access | Low | L1 Helpdesk | 72 | Routed | L1 Helpdesk / 72 / Routed | Yes |
| TC03 | BR1, BR2 | Software ticket, medium priority | Software | Medium | L1 Helpdesk | 24 | Routed | L1 Helpdesk / 24 / Routed | Yes |
| TC04 | BR1, BR2 | Software ticket, high priority | Software | High | L1 Helpdesk | 4 | Routed | L1 Helpdesk / 4 / Routed | Yes |
| TC05 | BR1, BR2 | Infrastructure ticket, high priority | Infrastructure | High | L2 Field Team | 4 | Routed | L2 Field Team / 4 / Routed | Yes |
| TC06 | BR1, BR2 | Infrastructure ticket, low priority | Infrastructure | Low | L2 Field Team | 72 | Routed | L2 Field Team / 72 / Routed | Yes |
| TC07 | BR1, BR2 | Hardware ticket, medium priority | Hardware | Medium | L2 Field Team | 24 | Routed | L2 Field Team / 24 / Routed | Yes |
| TC08 | BR1, BR2 | Hardware ticket, low priority | Hardware | Low | L2 Field Team | 72 | Routed | L2 Field Team / 72 / Routed | Yes |
| TC09 | BR1, BR2 | Finance ticket, high priority | Finance | High | Admin | 4 | Routed | Admin / 4 / Routed | Yes |
| TC10 | BR1, BR2 | Finance ticket, medium priority | Finance | Medium | Admin | 24 | Routed | Admin / 24 / Routed | Yes |
| TC11 | BR1, BR2 | Finance ticket, low priority | Finance | Low | Admin | 72 | Routed | Admin / 72 / Routed | Yes |
| TC12 | BR1, BR2 | General ticket, medium priority | General | Medium | Triage | 24 | Routed | Triage / 24 / Routed | Yes |
| TC13 | BR1, BR2 | General ticket, high priority | General | High | Triage | 4 | Routed | Triage / 4 / Routed | Yes |
| TC14 | BR1, BR2 | General ticket, low priority | General | Low | Triage | 72 | Routed | Triage / 72 / Routed | Yes |
| TC15 | BR0, BR1, BR2 | Category written in lowercase | `"access"` | Medium | L1 Helpdesk | 24 | Routed | L1 Helpdesk / 24 / Routed | Yes |
| TC16 | BR0, BR1, BR2 | Category written in uppercase | `"ACCESS"` | Low | L1 Helpdesk | 72 | Routed | L1 Helpdesk / 72 / Routed | Yes |
| TC17 | BR0, BR1, BR2 | Priority written in lowercase | Finance | `"high"` | Admin | 4 | Routed | Admin / 4 / Routed | Yes |
| TC18 | BR0, BR1, BR2 | Extra spaces in the category, priority in uppercase | `"  Hardware "` | `"MEDIUM"` | L2 Field Team | 24 | Routed | L2 Field Team / 24 / Routed | Yes |
| TC19 | BR3, BR2 | Category not in the list | Printer | High | Triage | 4 | Needs review | Triage / 4 / Needs review | Yes |
| TC20 | BR3, BR2 | Category missing | `None` | Low | Triage | 72 | Needs review | Triage / 72 / Needs review | Yes |
| TC21 | BR3, BR2 | Category is empty text | `""` | Medium | Triage | 24 | Needs review | Triage / 24 / Needs review | Yes |
| TC22 | BR4 | Priority not in the list | Access | Urgent | Triage | 0 | Needs review | Triage / 0 / Needs review | Yes |
| TC23 | BR4 | Priority is empty text | Hardware | `""` | Triage | 0 | Needs review | Triage / 0 / Needs review | Yes |
| TC24 | BR4 | Priority missing | Software | `None` | Triage | 0 | Needs review | Triage / 0 / Needs review | Yes |
| TC25 | BR3, BR4 | Category and priority both unknown | Printer | Urgent | Triage | 0 | Needs review | Triage / 0 / Needs review | Yes |
| TC26 | BR3, BR4 | Category and priority both missing | `None` | `None` | Triage | 0 | Needs review | Triage / 0 / Needs review | Yes |
| TC27 | BR0, BR1, BR2 | General in uppercase with spaces: still a valid category, so "Routed" (General vs. unknown boundary after cleaning) | `" GENERAL "` | Low | Triage | 72 | Routed | Triage / 72 / Routed | Yes |
| TC28 | BR3, BR2 | Misspelled category (near miss of Access) | `"Acess"` | High | Triage | 4 | Needs review | Triage / 4 / Needs review | Yes |
| TC29 | BR0, BR3, BR2 | Category with only spaces | `"   "` | Medium | Triage | 24 | Needs review | Triage / 24 / Needs review | Yes |
| TC30 | BR4 | Misspelled priority (near miss of High) | Access | `"Hight"` | Triage | 0 | Needs review | Triage / 0 / Needs review | Yes |

### 3.2 Individual functions

The course asks for every function to be tested with different input values. These rows test each helper function on its own.

| Test ID | Function | Scenario description | Input | Expected Result | Actual Result | Passed |
|---|---|---|---|---|---|---|
| FT01 | `clean_text()` | Mixed capitalization | `"Access"` | `"access"` | `"access"` | Yes |
| FT02 | `clean_text()` | Surrounding spaces and uppercase | `"  HIGH "` | `"high"` | `"high"` | Yes |
| FT03 | `clean_text()` | Missing value | `None` | `""` | `""` | Yes |
| FT04 | `clean_text()` | Number instead of text | `3` | `"3"` | `"3"` | Yes |
| FT05 | `is_missing()` | Missing value | `None` | `True` | `True` | Yes |
| FT06 | `is_missing()` | Only spaces | `"   "` | `True` | `True` | Yes |
| FT07 | `is_missing()` | Empty text | `""` | `True` | `True` | Yes |
| FT08 | `is_missing()` | Normal text | `"Finance"` | `False` | `False` | Yes |
| FT09 | `get_queue()` | Access, normal capitalization | `"Access"` | `"L1 Helpdesk"` | `"L1 Helpdesk"` | Yes |
| FT10 | `get_queue()` | Software, lowercase | `"software"` | `"L1 Helpdesk"` | `"L1 Helpdesk"` | Yes |
| FT11 | `get_queue()` | Infrastructure, uppercase | `"INFRASTRUCTURE"` | `"L2 Field Team"` | `"L2 Field Team"` | Yes |
| FT12 | `get_queue()` | Hardware | `"Hardware"` | `"L2 Field Team"` | `"L2 Field Team"` | Yes |
| FT13 | `get_queue()` | Finance with surrounding spaces | `" finance "` | `"Admin"` | `"Admin"` | Yes |
| FT14 | `get_queue()` | General | `"General"` | `"Triage"` | `"Triage"` | Yes |
| FT15 | `get_queue()` | Category not in the list | `"Printer"` | `"Triage"` | `"Triage"` | Yes |
| FT16 | `get_queue()` | Missing category | `None` | `"Triage"` | `"Triage"` | Yes |
| FT17 | `get_deadline_hours()` | High | `"High"` | `4` | `4` | Yes |
| FT18 | `get_deadline_hours()` | Medium, lowercase | `"medium"` | `24` | `24` | Yes |
| FT19 | `get_deadline_hours()` | Low, uppercase with spaces | `" LOW "` | `72` | `72` | Yes |
| FT20 | `get_deadline_hours()` | Priority not in the list | `"Urgent"` | `0` | `0` | Yes |
| FT21 | `get_deadline_hours()` | Missing priority | `None` | `0` | `0` | Yes |
| FT22 | `format_deadline()` | High-priority deadline | `4` | `"4 hours"` | `"4 hours"` | Yes |
| FT23 | `format_deadline()` | Medium-priority deadline | `24` | `"24 hours"` | `"24 hours"` | Yes |
| FT24 | `format_deadline()` | Low-priority deadline | `72` | `"72 hours"` | `"72 hours"` | Yes |
| FT25 | `format_deadline()` | No deadline set (BR4) | `0` | `"not set (priority must be reviewed)"` | `"not set (priority must be reviewed)"` | Yes |
| FT26 | `calculate_percentage()` | Part of the total | `3, 15` | `20.0` | `20.0` | Yes |
| FT27 | `calculate_percentage()` | Largest queue in the sample | `6, 15` | `40.0` | `40.0` | Yes |
| FT28 | `calculate_percentage()` | All tickets in one queue | `15, 15` | `100.0` | `100.0` | Yes |
| FT29 | `calculate_percentage()` | Queue with no tickets | `0, 15` | `0.0` | `0.0` | Yes |
| FT30 | `calculate_percentage()` | Empty ticket list (total 0, no division by zero) | `0, 0` | `0.0` | `0.0` | Yes |
| FT31 | `get_next_ticket_id()` | The 15 sample tickets (highest ID 1015) | `tickets` from `sample_tickets.py` | `1016` | `1016` | Yes |
| FT32 | `get_next_ticket_id()` | Empty list | `[]` | `1` | `1` | Yes |
| FT33 | `get_next_ticket_id()` | A ticket without an ID is skipped | `[{"ticket_id": 5}, {"category": "Access"}]` | `6` | `6` | Yes |

For FT31, import the list first: `>>> from sample_tickets import tickets`, then call `get_next_ticket_id(tickets)`.

### 3.3 Keyboard input (`main.py`)

These tests check the `input()` part of the program: the yes/no question, the manual ticket, and how it is routed and counted. Run `python main.py` for each one and type the inputs in order; `(Enter)` means press Enter without typing anything.

| Test ID | Scenario description | Keyboard input, in order | Expected result | Actual Result | Passed |
|---|---|---|---|---|---|
| MT01 | User does not add a ticket | `no` | Only the 15 sample tickets are processed; the summary matches section 5 | 15 tickets processed (1001 to 1015), no ticket 1016. Summary: L1 Helpdesk 4 (26.7%), L2 Field Team 3 (20.0%), Admin 2 (13.3%), Triage 6 (40.0%), total 15, needs review 5 [1011, 1012, 1013, 1014, 1015] | Yes |
| MT02 | Manual ticket, lowercase category, uppercase priority | `yes` · `Password expired on laptop` · `access` · `HIGH` | Ticket **1016** is shown with `Category: access` and `Priority: HIGH`, routed to **L1 Helpdesk / 4 hours / Routed**. Summary: L1 Helpdesk 5 (31.2%), L2 Field Team 3 (18.8%), Admin 2 (12.5%), Triage 6 (37.5%), total 16, needs review 5 | Ticket 1016: Password expired on laptop · Category: access · Priority: HIGH → **L1 Helpdesk / 4 hours / Routed**. Summary: L1 Helpdesk 5 (31.2%), L2 Field Team 3 (18.8%), Admin 2 (12.5%), Triage 6 (37.5%), total 16, needs review 5 [1011, 1012, 1013, 1014, 1015] | Yes |
| MT03 | Manual ticket with an unknown category | `yes` · `Scanner offline` · `Printer` · `Low` | Ticket 1016: **Triage / 72 hours / Needs review** (BR3). Summary: Triage 7 (43.8%), total 16, needs review 6, including 1016 | Ticket 1016: Scanner offline · Category: Printer · Priority: Low → **Triage / 72 hours / Needs review**. Summary: L1 Helpdesk 4 (25.0%), L2 Field Team 3 (18.8%), Admin 2 (12.5%), Triage 7 (43.8%), total 16, needs review 6 [1011, 1012, 1013, 1014, 1015, 1016] | Yes |
| MT04 | Invalid answer to the question | `maybe` · `no` | Prints `Please answer yes or no.` and asks again; after `no`, the result is the same as MT01 | `Please answer yes or no.` printed once and the question asked again; after `no`: 15 tickets processed (1001 to 1015), no ticket 1016. Summary: L1 Helpdesk 4 (26.7%), L2 Field Team 3 (20.0%), Admin 2 (13.3%), Triage 6 (40.0%), total 15, needs review 5 [1011, 1012, 1013, 1014, 1015] | Yes |
| MT05 | Uppercase answer and empty fields | `YES` · `(Enter)` · `(Enter)` · `(Enter)` | `YES` is accepted. Ticket 1016 shows `(missing)` for the description, category and priority, and is routed to **Triage / deadline not set / Needs review** (BR3, BR4). Needs review 6 | Ticket 1016: (missing) · Category: (missing) · Priority: (missing) → **Triage / not set (priority must be reviewed) / Needs review**. Summary: L1 Helpdesk 4 (25.0%), L2 Field Team 3 (18.8%), Admin 2 (12.5%), Triage 7 (43.8%), total 16, needs review 6 [1011, 1012, 1013, 1014, 1015, 1016] | Yes |

---

## 4. Coverage

### 4.1 By rule

The course asks for each business rule to be tested with at least three different input values.

| Rule | Tests | Different inputs tested |
|---|---|---|
| BR0: Input cleaning | TC15 to TC18, TC27, TC29, FT01 to FT04 | Lowercase, uppercase, extra spaces, spaces only, `None`, a number |
| BR1: Routing | TC01 to TC18, TC27, FT09 to FT14 | All 6 categories, each at least twice |
| BR2: Deadline | TC01 to TC21, TC27 to TC29, FT17 to FT19 | High (TC01, 04, 05, 09, 13, 17, 19, 28), Medium (TC03, 07, 10, 12, 15, 18, 21, 29), Low (TC02, 06, 08, 11, 14, 16, 20, 27) |
| BR3: Unknown category | TC19 to TC21, TC25, TC26, TC28, TC29, FT15, FT16 | Unlisted value, misspelled value, `None`, empty text, spaces only |
| BR4: Unknown priority | TC22 to TC26, TC30, FT20, FT21 | Unlisted value, misspelled value, empty text, `None` |

### 4.2 By function

| Function | Direct tests | Also exercised by |
|---|---|---|
| `clean_text()` | FT01 to FT04 | Every TC test, through `route_ticket()` |
| `is_missing()` | FT05 to FT08 | `main.py` output ("(missing)") |
| `get_queue()` | FT09 to FT16 | Every TC test |
| `get_deadline_hours()` | FT17 to FT21 | Every TC test |
| `route_ticket()` | TC01 to TC30 | `main.py` run (section 5) |
| `format_deadline()` | FT22 to FT25 | `main.py` output ("Deadline:" lines) |
| `calculate_percentage()` | FT26 to FT30 | `main.py` summary percentages (section 5) |
| `get_next_ticket_id()` | FT31 to FT33 | MT02, MT03, MT05 (the manual ticket gets ID 1016) |
| `ask_yes_or_no()` | — (needs the keyboard) | MT01 (no), MT02 and MT03 (yes), MT04 (invalid answer), MT05 (uppercase YES) |
| `read_manual_ticket()` | — (needs the keyboard) | MT02, MT03, MT05 |

### 4.3 Queue × priority

Every queue is tested with every priority.

| Queue | High | Medium | Low |
|---|---|---|---|
| L1 Helpdesk | TC01, TC04 | TC03, TC15 | TC02, TC16 |
| L2 Field Team | TC05 | TC07, TC18 | TC06, TC08 |
| Admin | TC09, TC17 | TC10 | TC11 |
| Triage (General) | TC13 | TC12 | TC14, TC27 |

---

## 5. End-of-run summary check (`main.py`)

`main.py` processes the 15 synthetic tickets in `sample_tickets.py` (IDs 1001 to 1015). Ticket 1015 has no `description` and no `priority` key at all. After `python main.py`, answering `no` to "Add a ticket manually?", the output must show:

| Check | Expected | Tickets | Actual | Passed |
|---|---|---|---|---|
| L1 Helpdesk | 4 (26.7%) | 1001, 1002, 1007, 1010 | 4 (26.7%) | Yes |
| L2 Field Team | 3 (20.0%) | 1003, 1004, 1008 | 3 (20.0%) | Yes |
| Admin | 2 (13.3%) | 1005, 1009 | 2 (13.3%) | Yes |
| Triage | 6 (40.0%) | 1006, 1011, 1012, 1013, 1014, 1015 | 6 (40.0%) | Yes |
| **Total processed** | **15** | 1001 to 1015 | **15** | Yes |
| Needs review | 5: [1011, 1012, 1013, 1014, 1015] | 1011 (unknown category), 1012 (Urgent), 1013 (missing priority), 1014 (both missing), 1015 (no description or priority key) | 5: [1011, 1012, 1013, 1014, 1015] | Yes |
| Missing fields do not crash the program | The program finishes. Ticket 1015 shows `Ticket 1015: (missing)` and `Priority: (missing)` | 1015 | The program finished with no error. Ticket 1015 shows `Ticket 1015: (missing)` and `Priority: (missing)` | Yes |

---

## 6. Failures found

Fill in one row per failed test. After the fix, re-run the test and record the result.

| Test ID | What happened | Cause | Fix applied | Re-test passed |
|---|---|---|---|---|
| — | No test failed in the run of 2026-10-12 (section 9) | — | — | — |

---

## 7. Notes on edge cases

- **Capitalization and spaces (TC15 to TC18, FT01, FT02).** BR0 cleans the values before any rule runs, so `"access"`, `"ACCESS"` and `"  Hardware "` are recognized. `get_queue()` and `get_deadline_hours()` also clean their own input, so they give correct results when tested on their own. The program still displays the original value, so the messy input stays visible in the output.
- **General vs. unknown category (TC12 to TC14 and TC27 vs. TC19 to TC21, TC28 and TC29).** Both go to Triage, but only an unrecognized category is marked "Needs review", because General is a valid category. TC27 checks this boundary after cleaning: `" GENERAL "` is still General, so it stays "Routed".
- **Near misses (TC28, TC30).** A misspelled value is not corrected or guessed: "Acess" is an unrecognized category (BR3) and "Hight" an unrecognized priority (BR4), so a person reviews the ticket.
- **Missing values and missing keys (TC20, TC23, TC24, TC26, ticket 1015).** `clean_text()` turns `None` into empty text. `main.py` reads each field with `.get()`, so a key that is absent from the ticket also becomes `None` instead of stopping the program.
- **Both unknown (TC25, TC26).** BR4 sets the deadline to 0; the queue is Triage and the status is "Needs review" either way.
- **Rounding of percentages.** The expected percentages follow the rounding rule in `PROBLEM_ANALYSIS.md` section 2.4: one decimal place, with an exact half rounded to the even digit, so 5 of 16 tickets (31.25%) is shown as 31.2% and 3 of 16 (18.75%) as 18.8% (MT02). Because each share is rounded on its own, the shares in MT03 and MT05 add up to 100.1%.
- **Typed values are kept as typed.** A manual ticket is displayed exactly as entered (MT02 shows `access` and `HIGH`), and BR0 cleans the values only for the rules.
- **Test data only.** All tickets and test inputs are synthetic. No real people, companies or records are used.

---

## 8. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-09-29 | First version (22 tests). |
| 1.1 | 2026-09-29 | Supabase removed; capitalization ignored (BR0); 26 tests; summary check based on `main.py`. |
| 1.2 | 2026-09-29 | Corrections accepted in the AI debugging cycle (AI log Entry 013): TC19 to TC21 now expect "Needs review" (BR3); 21 direct function tests added (FT01 to FT21); summary check updated for 15 tickets, including ticket 1015 without a description or priority key. |
| 1.3 | 2026-09-29 | AI refactoring cycle (AI log Entry 015): 9 direct tests added for the new functions `format_deadline()` (FT22 to FT25) and `calculate_percentage()` (FT26 to FT30); the sample tickets now come from `sample_tickets.py`. All other expected results are unchanged, because the refactoring did not change the program's behavior. |
| 1.4 | 2026-10-12 | Keyboard input added (Option A, AI log Entry 020): 3 tests for `get_next_ticket_id()` (FT31 to FT33) and 5 keyboard tests (MT01 to MT05); run instructions now say to answer `no` for the summary check. All earlier expected results are unchanged. |
| 1.5 | 2026-10-12 | All tests executed: Actual Result and Passed filled in for the 26 routing tests, 33 function tests, 5 keyboard tests and 7 summary checks; no failures (section 6); test execution record added (section 9). No expected result changed. AI log Entry 021. |
| 1.6 | 2026-10-12 | 4 boundary tests added and executed after the mock grading (AI log Entries 023 and 024): TC27 (General in uppercase with spaces stays "Routed"), TC28 (misspelled category), TC29 (category with only spaces), TC30 (misspelled priority); all passed. Coverage tables and notes updated; the rounding note now points to the rule in `PROBLEM_ANALYSIS.md` section 2.4; a note on importing `main.py` was added to section 2. No earlier expected or actual result changed. |

---

## 9. Test execution record

| Item | Value |
|---|---|
| Date | 2026-10-12 (TC01 to TC26, FT01 to FT33, MT01 to MT05 and section 5); 2026-10-12, after the mock grading (TC27 to TC30) |
| Code version | Commit `b6bff8d` (the keyboard-input change, AI log Entry 020): `main.py`, `calculations.py`, `validations.py`, `sample_tickets.py`. The code has not changed since that commit |
| Python version | 3.11.15 |
| Executed by | Claude (AI assistant), at the team's request (AI log Entry 021), by running the real code. The results were not predicted or typed by hand |
| Method | **3.1:** each row's inputs passed to `route_ticket()`; the returned dictionary written as `queue / deadline / status`. **3.2:** each function called with the row's input; `format_deadline()` imported from `main.py` with `no` typed at the question, as described in section 2. **3.3 and 5:** `python main.py` run once per test, with the listed keyboard input typed in order; the printed ticket block and summary written in Actual. A row is **Yes** only when the actual result is equal to the expected result (same value and same type for 3.2) |
| Results | 3.1 routing: **30/30 passed** · 3.2 functions: **33/33 passed** · 3.3 keyboard: **5/5 passed** · 5 summary: **7/7 passed** |
| Failures | None (section 6) |

**Team verification.** Before the submission, at least one team member should re-run a sample of these tests on their own computer, following section 2 (suggested: TC16, TC22, FT25, FT30, MT02 and MT04), and confirm that the results are the same. Record the result below.

| Date | Team member | Tests re-run | Same results? | Results |
|---|---|---|---|---|
| 2026-10-16 | Marlon Zanelato Filho | TC16 | Yes | Ticket 1016: ACCESS Category: Access Priority: low;Queue: L1 Helpdesk Deadline: 72 hours Status: Routed |
| 2026-10-16 | Marlon Zanelato Filho | TC22 | Yes | Ticket 1016: (missing) Category: Access Priority: Urgent Queue: Triage Deadline: not set (priority must be reviewed) Status: Needs review |
| 2026-10-16 | Marlon Zanelato Filho | FT25 | Yes | the command used before main() was format_deadline(4); Ticket 1016: ACCESS Category: Access Priority: low Queue: L1 Helpdesk Deadline: 72 hours Status: Routed |
| 2026-10-16 | Marlon Zanelato Filho | FT30 | Yes | the printed result was 0.0 |
| 2026-10-16 | Marlon Zanelato Filho | MT02 | Yes | Ticket 1016: (missing) Category: access Priority: HIGH Queue: L1 Helpdesk Deadline: 4 hours Status: Routed |
| 2026-10-16 | Marlon Zanelato Filho | MT04 | Yes | Add a ticket manually? (yes/no): maybe Please answer yes or no. |

all tests were done restarting the program to see if the changes done would save on the file

| Date | Team member | Tests re-run | Same results? |
|---|---|---|---|
| 10-17-2026 | Wesley Lopes | TC16 | yes |
| 10-17-2026 | Wesley Lopes | TC22 | yes |
| 10-17-2026 | Wesley Lopes | FT25 | yes |
| 10-17-2026 | Wesley Lopes | FT30 | yes |
| 10-17-2026 | Wesley Lopes | MT02 | yes |
| 10-17-2026 | Wesley Lopes | MT04 | yes |

---

*During the preparation of this document, the author(s) used Claude (Anthropic, model claude-opus-5) to derive the test cases, coverage tables and run procedure from the team's business rules (BR0 to BR4), to update them after the AI debugging cycle, to add tests for the functions created in the AI refactoring cycle, to add tests for the keyboard input, to execute all the tests and record their actual results (section 9), and to add and execute the boundary tests TC27 to TC30. After using this tool, the author(s) reviewed and edited the content as needed and take full responsibility for the content.*
