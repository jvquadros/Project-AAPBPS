# AI Interaction Log
**Course:** AI-Assisted Python for Business Problem Solving (PSI163) — PUCPR, 2026/2
**Professor:** Evandro Alberto Zatti
**Student:** João Vitor da Silva de Quadros
**AI tool:** Claude (Anthropic), model `claude-opus-5`, via Claude Cowork
**Log started:** 2026-09-18

> PUCPR Resolution 274/2024 — mandatory disclosure statement (to be included in every delivered artifact):
> "During the preparation of this [CONTENT TYPE], the author(s) used [Claude, Anthropic, claude-opus-5] to [REASONS]. After using this tool, the author(s) reviewed and edited the content as needed and take full responsibility for the content."

---

## Entry 001 — 2026-09-18 — Course material comprehension

**Prompt type:** Zero-shot, document comprehension + context loading
**Goal:** Load all course material into the assistant's context so subsequent prompts are grounded in the professor's actual scope and constraints.

**Prompt used:**
```
Please abstract the attached archives, my course have an project we have to develop,
and its entirely AI assisted, so ill use you as my LLM helper.
First of all, abstract and comprehend the attached pdfs.
Every prompt must and will be saved as material we have to deliver,
and every prompt must be in english.
```
**Attachments:** Syllabus (Plano de Ensino v2), ST1_1 Foundations of Computational Thinking, ST1_2 Introduction to Python, ST1_3 AI-Assisted Development, ST1 Mini-Case, ST2_1 Control Flow, ST2_2 Data Structures, ST2_3 Functions and Modularization, ST2 Mini-Case, ST2 Course Project.

**Relevant AI response (summary):** Structured abstract of all 10 documents: course competences (C1/A1), learning outcomes RA1/RA2, indicators ID1.1–ID1.4 and ID2.1–ID2.3, the six study themes TE1–TE6, the assessment calendar (RA1 due 03/10, RA2 due 28/11, recovery 28/11), the IPO model, the four elements of computational thinking, Python fundamentals, the five-element prompt structure (Context, Task, Inputs, Constraints, Expected Output), the five prompting types, and the explicit Hands-On requirements of the ST2 Course Project deck.

**Accepted:** The document abstract and the extracted requirement checklist — verified against the source PDFs.
**Rejected:** Nothing yet (no code produced at this stage).
**Justification:** This entry establishes the factual baseline. No design or implementation decision was delegated to the AI; the assistant only read and organized material provided by the professor.

---

## Entry 002 — 2026-09-18 — Project scoping decisions

**Prompt type:** Clarification / constraint setting (human-directed)
**Goal:** Fix the project's domain and working model before any implementation.

**Prompt used (student decisions, given in response to the assistant's scoping questions):**
```
Business domain: an invented small business (fictional but plausible).
Team: I have teammates.
Data: we'll develop it in parts, no need to generate everything for now.
For now, just understand what we have to do.
```

**Relevant AI response (summary):** Requirements breakdown only — no code, no data, no artifacts generated. The assistant produced the RA1 and RA2 obligation lists mapped to the professor's indicators (ID1.1–ID1.4, ID2.1–ID2.3), the ST2 Course Project hands-on checklist, the artifact inventory expected at each delivery, and the remaining calendar.

**Accepted:** The scoping constraints were set by the student, not the AI. The assistant's requirement mapping was accepted after verification against the syllabus and the Course Project deck.
**Rejected:** The assistant's suggestion to use a real business domain (the student's family restaurant operation) was rejected in favour of an invented small business, to keep the dataset fully controllable and avoid exposing real client/payment information — an ethical and data-protection consideration relevant to ID2.3.
**Justification:** Deliberate decision to sequence the work incrementally rather than let the AI generate a complete solution up front. This preserves authorship: each component will be specified by the team first, then assisted, then reviewed.

---

## Entry 003 — 2026-09-18 — Project instructions document

**Prompt type:** Structured output prompting — synthesis into a normative reference
**Goal:** Consolidate every rule, constraint, requirement and deadline scattered across ten course documents into one authoritative document that can be attached to the project's persistent context.

**Prompt used:**
```
Now elaborate a document with every instruction and orientation that the project
must follow, I'll attach it to the context and memory of the project.
```

**Relevant AI response (summary):** Produced `PROJECT_INSTRUCTIONS.md` — 13 sections covering identification, non-negotiable working rules, scope decisions, the RA1/RA2 assessment structure mapped to indicators ID1.1–ID1.4 and ID2.1–ID2.3, mandatory technical content with binary minimums, code standards derived from the decks, the AI usage protocol including the five-element prompt structure and the two mandatory prompt patterns, build order, the Resolution 274/2024 disclosure statement, delivery checklists, the full calendar, bibliography, and the list of known gaps in available material.

**Accepted:** The full structure. Requirements were cross-checked against the syllabus (Sections 3, 4, 5) and the ST2 Course Project deck before acceptance.
**Rejected:** The assistant's initial framing of the code standards as stylistic recommendations — rewritten as binding rules, since readability for beginners is an explicit constraint in the professor's own prompt patterns and therefore a grading concern rather than a preference. Also rejected: any invented rubric weightings; the document states plainly that the rubric has not been obtained and that a later rubric supersedes it.
**Justification:** Building the normative reference before the code is itself an application of ID1.1 — understanding the problem and its constraints before implementation. Recording the known gaps rather than filling them with plausible guesses is a deliberate guard against AI hallucination, which the course identifies as a primary risk of AI-assisted work.

---

## Entry 004 — 2026-09-18 — Trello board update from the Project Plan

**Prompt type:** Zero-shot, task execution (tool use: Trello connector)
**Goal:** Bring the Trello board in line with everything decided so far: the chosen idea, the Project Plan (Idea 2 — Intelligent Support Ticket Triage via NLP) and the Project Instructions.

**Prompt used:**
```
Access the Trello board via the connector and insert everything that've been stabillished
and its missing there, including the project Plan?
```

**Inputs read by the AI before acting:** current state of the Trello board "Projeto AAPBPS" (lists, cards, labels, members), `PROJECT_INSTRUCTIONS.md`, this log, the Project Plan PDF and `relatorio_tecnico_ia.pdf` (the two candidate ideas).

**Relevant AI response (summary):**
- Added the lists "📌 To Do — Current Sprint" and "👀 In Review" (Project Plan §8 workflow).
- Wrote summaries into the Project Plan card and the Syllabus card, and created a "📘 Project Instructions" reference card.
- Filled the three Idea Decision cards (chosen idea + justification, MVP scope) and moved them to Done.
- Added Sprint 0 cards (roles and check-in, GitHub repo, LLM provider) to To Do.
- Updated every RA1/RA2 card with its sprint, ID reference, due date and a checklist; created the missing cards: category list and label mapping, baseline classifier, test case table, debugging and refactoring cycles, mock platform, webhook endpoint, LLM classifier, ticket log, LLM vs. baseline evaluation, RA2 submission, stretch goals.
- Moved the presentation due date to 27/11 (Class 17), per the course calendar.
- Attached colour labels by card type (green data, purple ml, blue backend, yellow docs, orange presentation); label names must be set by hand because the connector cannot rename labels.
- Created two cards in "🚧 Blocked / Questions": conflicts between the Project Plan and the Project Instructions (library list vs. beginner-level rule, notebook vs. .py modules, log file name, peer review date, data source), and the missing course material (ST1 Course Project deck, pandas slides, rubrics).

**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review — record here which board changes the group kept, changed or reverted, and why._

---

## Entry 005 — 2026-09-19 — Aligning the Project Plan with the course rules

**Prompt type:** Zero-shot, task execution (tool use: Trello connector + project documents)
**Goal:** Resolve the conflicts between the group's Project Plan (Idea 2, 18/09) and the course rules recorded in `PROJECT_INSTRUCTIONS.md`, in favour of the course rules.

**Prompt used:**
```
may you please allign with the course rules please
```

**Context:** Entry 004 had flagged the conflicts in the Trello card "Align the Project Plan with the course rules": the plan's stack (FastAPI, Pydantic, scikit-learn, httpx, pytest, SQLite, Streamlit) versus the beginner-level / course-libraries rule; notebooks versus `.py` modules; the AI log file name; the peer review date; public versus synthetic data.

**Relevant AI response (summary):**
- Kept Idea 2 and the LLM inside the product, but replaced every tool outside the course: the FastAPI webhook service became a batch triage program over an inbox folder of JSON files with queue files as output; TF-IDF + Logistic Regression became a keyword-rule baseline (dictionary + `if`/`elif`/`else`), which also serves as the mandatory business rule; macro F1 became accuracy per category and a `pd.crosstab` confusion table; SQLite became a CSV log + `logging`; pytest became robustness rows in the test case table; the LLM is called with `requests`.
- Set the deliverable format to `.py` modules (`main.py`, `calculations.py`, `validations.py`, `analysis.py`, later `api_client.py`, `reports.py`); synthetic data only; `docs/AI_INTERACTION_LOG.md` as the log name; peer review in Class 8 (25/09).
- Re-sequenced the RA2 sprints to follow the class calendar (queue files after Class 11, batch/log/errors after Class 12, LLM after Class 13, web collection after Class 14, charts after Class 15) and moved the LLM provider choice out of Sprint 0.
- Proposed four business rules for the problem analysis (classification, label validation, routing, response deadline) — to be confirmed by the team.
- Updated the Trello board (Project Plan card rewritten as the aligned version, card names, descriptions, due dates, checklists) and `PROJECT_INSTRUCTIONS.md` to v1.1 (sections 3, 5.5, 8, 10 and a change log in section 14).

**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review — note in particular whether the group accepts dropping the web service and scikit-learn, and the proposed business rules._

---

## Entry 006 — 2026-09-29 — ST1/ST2 requirements abstract for the RA1 submission

**Prompt type:** Zero-shot, document comprehension + structured summary (tool use: connected course folder)
**Goal:** Extract, from the course PDFs, everything ST1 and ST2 require for the first submission (RA1, due 03/10), as a checklist the team can work from.

**Prompt used:**
```
May you check the folder that contais all the pdfs avaible about the course and please
abstract everything about the ST1 and ST2 that must be ready for this first submit that
we have to do this week

please abstract so then after we can work on it
```

**Inputs read by the AI:** Syllabus (Plano de Ensino v2), ST1_1, ST1_2, ST1_3, ST1 Mini-Case, ST2_1, ST2_2, ST2_3, ST2 Mini-Case, ST2 Course Project, plus `Trabalho/relatorio_tecnico_ia.pdf` and `Trabalho/…Project Plan.pdf` for context.

**Relevant AI response (summary):** Produced `RA1_ST1_ST2_REQUIREMENTS.md` (saved to the project and to the `Trabalho` folder):
- Submission facts: Summative 1, 5.0 points, team delivery of source code + supporting data files + documentation by 03/10 (Class 9 on 02/10), recovery 28/11.
- ST1 requirements, derived from the syllabus indicators and the deck objectives, since ST1 has no Course Project deck: problem analysis (four guiding questions, the four elements of computational thinking, IPO, business rules, algorithm, pseudocode), the Python basics expected in the code, and the AI-use rules and prompt structure.
- ST2 explicit minimums from the Course Project deck, as a binary checklist: `if`/`elif`/`else` rule tested with ≥3 inputs; test case table; list, dictionary, list of dictionaries; ≥2 single-responsibility functions; the verbatim debugging and refactoring prompts; the five fields of each AI log entry. Also the constructs taught in ST2_1–ST2_3.
- A proposed mapping of each requirement onto the triage project's files (marked as a proposal for the team).
- Open points: an individual RA1 assessment appears in the syllabus with no date; rubrics, ST3 pandas decks and submission format still missing; `validation.py` (deck) vs. `validations.py` (instructions); the Project Plan PDF in `Trabalho/` is the pre-alignment version; log entries 004–005 still pending team review.

**Verification:** Every quoted requirement, prompt and date was checked by text search against the extracted PDF text; the two diagram slides whose text did not extract (IPO model, project structure) were checked visually.
**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review — confirm or change the proposed mapping in section 4 of the abstract (e.g. which rule is the graded `if`/`elif`/`else` rule)._

---

## Entry 007 — 2026-09-29 — First-delivery scope and first step

**Prompt type:** Zero-shot, planning question (tool use: Trello connector, read-only)
**Goal:** Narrow the first delivery to ST1 and ST2 and identify the first concrete step.

**Prompt used:**
```
For this first delivery is just ST1 and ST2, whats the first step for now?
```

**Inputs read by the AI:** the Trello board "Projeto AAPBPS" (all lists and cards, read-only), `RA1_ST1_ST2_REQUIREMENTS.md`, `PROJECT_INSTRUCTIONS.md`.

**Relevant AI response (summary):**
- Board state: no card had changed since 19/09. All RA1 cards were still in the backlog, and the Sprint 0 cards (roles, GitHub repo) were still open with no owners.
- Recommended first step: the problem analysis (`docs/PROBLEM_ANALYSIS.md`, ID1.1), preceded by four team decisions: the invented company, the category list, the team queue for each category, and the response deadline for each priority.
- Consequence of the ST1/ST2-only scope: pandas cleaning, exploratory analysis and the 300–500-ticket dataset are not needed for this delivery; a small hard-coded list of sample tickets (list of dictionaries) covers ST2. The scope note in `RA1_ST1_ST2_REQUIREMENTS.md` was updated accordingly.
- Flagged that the syllabus still lists ID1.3 (DataFrames) under RA1, to be confirmed with the professor.

**Note:** the ST1/ST2-only scope was set by the student, not suggested by the AI.
**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review_

---

## Entry 008 — 2026-09-29 — Problem analysis (ID1.1)

**Prompt type:** Structured prompt following the five-element structure from ST1_3 (Context, Objective/Task, Inputs, Expected Processing, Expected Output, Technical Constraints); zero-shot with structured output
**Goal:** Produce `docs/PROBLEM_ANALYSIS.md`, the foundational step before any code.

**Team decisions supplied in the prompt (not made by the AI):** company name NexoTech Solutions; six categories; four queues and the category → queue mapping; resolution deadlines High 4 h / Medium 24 h / Low 72 h; strict pseudocode keywords.

**Prompt used:**
```
Context: I am working on a university project for a Python-based ticket routing system for a
fictional IT support company called "NexoTech Solutions". Objective: Create the problem analysis
documentation (`docs/PROBLEM_ANALYSIS.md`), which is the foundational step before writing the
code. Inputs: The system will receive support tickets containing Categories (Infrastructure,
Finance, Access, Software, Hardware, General) and Priorities (High, Medium, Low). Expected
Processing: The analysis must define the routing of tickets to specific Queues (Access & Software
-> L1 Helpdesk; Infrastructure & Hardware -> L2 Field Team; Finance -> Admin; General -> Triage).
It must also define resolution Deadlines based on priority (High = 4 hours, Medium = 24 hours,
Low = 72 hours). Expected Output: A structured Markdown document containing:

1. Four guiding questions defining the problem scope.
2. An Input -> Processing -> Output table.
3. A step-by-step logical breakdown of the system.
4. Business rules clearly stated in plain English.
5. Pseudocode representing the logic. Technical Constraints: The pseudocode MUST strictly follow
this keyword format: START, READ, CALCULATE, DISPLAY, END. It must include the conditional logic
(if/elif/else structure) for routing and deadlines. Do not write actual Python code yet.
```

**Relevant AI response (summary):** `docs/PROBLEM_ANALYSIS.md` v1.0, containing: business context with the four queues; the four guiding questions; an IPO table plus input/output field tables with data types; a 9-step decomposition and a table applying the four elements of computational thinking; business rules BR1 (routing) and BR2 (deadline) exactly as supplied; pseudocode for one ticket using only START / READ / CALCULATE / DISPLAY / END and IF / ELIF / ELSE / END IF; an assumptions section; the PUCPR disclosure statement.

**Additions the AI made beyond the prompt (the team must accept or reject each):**
1. BR3: an unrecognized category is treated as General and sent to Triage.
2. BR4: an unrecognized priority gets no deadline (0 hours), goes to Triage and is marked "Needs review", with no default deadline.
3. A `status` output field ("Routed" / "Needs review").
4. An end-of-run summary (tickets per queue, tickets needing review), which later justifies the ST2 counters.
5. The computational-thinking table and the assumptions section (category chosen by the requester; deadline in hours from opening; small synthetic sample).
6. One-line descriptions of what each queue handles.
7. No loop keyword in the pseudocode, to respect the strict keyword list; the repetition over all tickets is explained in a note instead.

**Verification:** A script checked that every pseudocode line starts with an allowed keyword, and that the document contains no Python code. A simulation of the pseudocode's two decisions matched the prompt's routing and deadline tables for all 18 valid category/priority combinations. Unknown-category and unknown-priority cases behaved as BR3 and BR4 describe.

**Accepted:** All the AI's additions to the problem analysis: BR3 (unknown category → Triage), BR4 (unknown priority → no deadline, Triage, "Needs review"), the `status` field, the end-of-run summary, and single-ticket pseudocode with no loop keyword. `PROBLEM_ANALYSIS.md` v1.0 is approved.
**Rejected:** Working out the category from keywords in the ticket description (the keyword-rule classifier proposed in Entry 005). For this delivery the category is provided explicitly with each ticket.
**Justification:** Dropping keyword extraction keeps the first delivery small and stable, and focused on the ST1/ST2 constructs (decisions, data structures, functions). The additions were accepted because they give every possible input a defined result, and BR4 prevents an urgent ticket from receiving a wrong default deadline.
**Team decision after review (architecture):** Tickets are stored in a Supabase table instead of a hard-coded list. The program fetches incoming tickets from the table, applies BR1–BR4, and writes the queue, deadline and status back to each record. This decision was made by the team, not proposed by the AI. Reason: _[team to fill in]_
**Update:** reversed in Entry 010. Supabase was dropped, and tickets come from a local list of dictionaries.

---

## Entry 009 — 2026-09-29 — Test case table and Supabase architecture update

**Prompt type:** Structured prompt (Context, Objective, Expected Output, Coverage); zero-shot with structured output
**Goal:** Produce `docs/TEST_CASES.md` from the approved business rules, and a paste-ready completion of Entry 008.

**Team decisions supplied in the prompt (not made by the AI):** approval of `PROBLEM_ANALYSIS.md` v1.0 with all additions; category provided explicitly; NLP/keyword extraction dropped for this delivery; Supabase as the project database (fetch incoming tickets, write back queue, deadline and status).

**Prompt used:**
```
Context: The problem analysis is approved. I accept all your additions (Unknown category, unknown
priority, status field, end-of-run summary, single-ticket pseudocode). Regarding the category
decision: keep it simple, it is explicitly provided. We are dropping the NLP/keyword extraction
idea for this delivery to ensure stability. NEW ARCHITECTURE UPDATE: I have integrated Supabase to
serve as our project's database. Instead of a hardcoded list, the Python system will fetch incoming
tickets from a Supabase table, process the routing/deadlines, and update the database records with
their assigned Queue, Deadline, and Status. Objective: Create the `docs/TEST_CASES.md` document
based on our approved business rules. Expected Output: A structured Markdown document featuring a
test table. The table MUST include columns for Test ID, Scenario Description, Inputs (Category,
Priority), Expected Queue, Expected Deadline, and a blank column for "Actual DB Result" (to be
filled when we run the code). Coverage: Include at least 15 test cases covering various
combinations and the edge cases (unknown category/priority). AI Log: Please also provide a short
summary of these decisions (including the Supabase integration) formatted so I can paste it into
Entry 008 of our AI Log.
```

**Relevant AI response (summary):**
- `docs/TEST_CASES.md` v1.0 with 22 test cases: 14 valid combinations covering all six categories and every queue × priority pair; 3 unknown or missing categories (BR3); 3 unknown or missing priorities (BR4); 2 with both unknown. Also a run procedure for the Supabase flow, a coverage-by-rule table, an end-of-run summary check and a failure log template.
- The Accepted / Rejected / Justification text for Entry 008 (above).
- Concerns raised about the Supabase integration: database/API integration is TE5 (RA2, Class 13 on 30/10) and falls outside rule 5 of `PROJECT_INSTRUCTIONS.md` (beginner level, course libraries only, provider SDKs out of scope); the professor needs credentials to run the code; API keys must never be committed; the network dependency adds risk close to the deadline. Recommendation: keep the business-rule functions independent of the database and keep a local sample list as an offline fallback.

**Additions the AI made beyond the prompt (the team must accept or reject each):**
1. An **Expected Status** column (from the approved status field).
2. A **Passed** column, required by the ST2 Course Project deck (input values, expected result, actual result, whether the test passed).
3. A **Rules** column linking each test to BR1–BR4.
4. Lowercase edge cases (TC16 `access`, TC19 `high`) that expose the exact-value matching of the approved rules.
5. A reserved ticket ID range (9001–9022) for test rows in Supabase.
6. The end-of-run summary check (4 / 4 / 3 / 11, 5 needing review).

**Verification:** A script parsed the test table and ran the approved rule logic on every input: all 22 expected results matched, the summary counts matched, and the Actual and Passed columns were confirmed blank.

*Team review, given in the prompt of Entry 010:*
**Accepted:** The test table and the additions: the Expected Status, Passed and Rules columns, and the end-of-run summary check. The AI's concerns about Supabase were accepted, and the team dropped Supabase (Entry 010).
**Rejected:** Exact-value matching. The team decided that the program must ignore capitalization ("access", "ACCESS" and "Access" all go to L1 Helpdesk), so the lowercase tests now expect the normal result (rule BR0, Entry 010). The Supabase-specific parts (the run procedure against the table, the reserved ticket IDs 9001–9022 and the "Actual DB Result" column) were removed together with Supabase.
**Justification:** In the team's words, the Supabase risks were real and the delivery must strictly follow the ST1/ST2 scope, using only a local, hard-coded list of dictionaries, as the professor demonstrated.

---

## Entry 010 — 2026-09-29 — First version of the Python code (ST1/ST2)

**Prompt type:** Structured prompt (Context with team decisions, Objective, a specification for each file, Output); zero-shot code generation
**Goal:** Write `validations.py`, `calculations.py` and `main.py` from the approved rules, remove Supabase from the docs, and explain how to run the code.

**Team decisions supplied in the prompt (not made by the AI):** ignore capitalization in category and priority; drop Supabase entirely for this delivery; use only a local, hard-coded list of dictionaries, as the professor demonstrated; the responsibility of each file (validations = input cleaning, calculations = rules separate from the data, main = mock tickets, processing, summary counters and output).

**Note on numbering:** the prompt asked for this to be logged as Entry 009. Entry 009 already holds the previous prompt (the test case table), so this prompt is logged as Entry 010 to keep one entry per prompt.

**Prompt used:**
```
Context: Folder re-added. The TEST_CASES.md is looking great. Decisions on your alerts:

1. Case sensitivity: Yes, update the rules and tests to ignore capitalization (e.g., "access",
   "ACCESS", and "Access" should all go to L1 Helpdesk).
2. Architecture correction: You were absolutely right about the risks. We are DROPPING Supabase
   entirely for this delivery. We must strictly adhere to the ST1/ST2 scope. We will use ONLY a
   local, hard-coded list of dictionaries representing the tickets, exactly as the professor
   demonstrated. Objective: Now, write the actual Python code.
3. `validations.py`: To handle inputs and clean them (lowercase conversion).
4. `calculations.py`: The core logic rules (queues and deadlines) decoupled from data fetching.
5. `main.py`: A script that creates a local list of 10-15 mock tickets (dictionaries), processes
   them using the other modules, applies the end-of-run summary counters, and prints the outputs
   clearly. Output: Generate the Python files, update the docs to remove any mention of Supabase,
   and briefly explain how to run the code. Please log this as Entry 009.
```

**Relevant AI response (summary):**
- `validations.py`: `clean_text()` (lowercase, surrounding spaces removed, `None` turned into empty text) and `is_missing()`.
- `calculations.py`: named constants for the queues and statuses, and the `QUEUES` tuple; `get_queue()` (BR1/BR3, `if`/`elif`/`else` with `or`); `get_deadline_hours()` (BR2/BR4); `route_ticket()`, which applies BR0 and then BR1–BR4 and returns a dictionary. The module never prints and never holds ticket data.
- `main.py`: 14 synthetic tickets as a list of dictionaries, including messy capitalization, extra spaces, an unknown category, an unknown priority and missing values; a `for` loop; a dictionary of counters per queue; a total counter; a list of the ticket IDs that need review; formatted output with f-strings (percentages to one decimal place).
- `docs/PROBLEM_ANALYSIS.md` v1.1: new rule BR0 (input cleaning); pseudocode, IPO table and decomposition updated; change log added.
- `docs/TEST_CASES.md` v1.1: Supabase removed ("Actual DB Result" became "Actual Result", and the run procedure now calls `route_ticket()` in the Python shell); 26 test cases, including 4 new capitalization and spacing cases (TC15–TC18); the summary check is now based on the 14 tickets in `main.py`.
- The history of the Supabase decision was kept in this log instead of being deleted, because its reversal is part of the evidence of critical AI use (ID1.4).

**Constructs covered (ID1.2):** variables and the four basic types (`str`, `int`, `float` for the percentage, `bool` from `is_missing()`); comparison and logical operators (`==`, `or`); `if`/`elif`/`else`; `for` loops; counters; a list, dictionaries, a list of dictionaries and a tuple; seven functions with parameters and return values; imports across three files; f-strings with formatting.

**Additions the AI made beyond the prompt (the team must accept or reject each):**
1. `clean_text()` also removes surrounding spaces and turns `None` into empty text; the prompt asked only for lowercase conversion.
2. `is_missing()`, used to show "(missing)" in the output.
3. `route_ticket()` calls `clean_text()` itself, so each test case can be run with raw inputs in a single call.
4. Named constants for the queue and status names, and the `QUEUES` tuple, so each name is written only once.
5. The summary also lists the IDs of the tickets that need review, and shows each queue's share as a percentage.
6. A guard against division by zero when the ticket list is empty.
7. A PUCPR disclosure comment at the top of each Python file.

**Verification:** `main.py` ran without errors, and its summary matched the expected values in `TEST_CASES.md` section 5. All 26 test inputs were run through `route_ticket()`, and every result matched the expected queue, deadline and status. Checks confirmed: no classes, comprehensions, lambdas or third-party imports; ASCII-only source files; all three files compile; the pseudocode still uses only the allowed keywords. The team must still read and understand every line before accepting the code (ST1_3: never accept generated code only because it runs), and must fill the Actual Result column by running the tests themselves.

*Team review, given in the prompt of Entry 011:*
**Accepted:** The code, approved by the team, and all seven additions: handling of extra spaces and missing values in `clean_text()`, `is_missing()`, the self-cleaning `route_ticket()`, the named constants and the `QUEUES` tuple, the needs-review ID list and the percentages in the summary, the empty-list guard, and the disclosure comments.
**Rejected:** None.
**Justification:** In the team's words, the additions "add great robustness".

---

## Entry 011 — 2026-09-29 — GitHub push, Trello update and preparation of the AI cycles

**Prompt type:** Zero-shot, task execution (tool use: Trello connector; connected project folder)
**Goal:** Share the files with the team through GitHub, bring the Trello board up to date, and prepare the mandatory debugging and refactoring cycles.

**Prompt used:**
```
Context: Excellent work! The code is approved. I accept all your additions (handling extra
spaces/missing values, self-cleaning in `route_ticket`, percentages, and the empty list
protection). They add great robustness. Team Access (CRITICAL): Right now, the files are only
on my local machine. My team needs access to them via GitHub. I know I have to run commands in
the CMD to push them. Trello Board: Our Trello board is outdated. We need to move the completed
tasks (Problem Analysis, Test Cases, Python Code generation) to 'Done', and remove/cancel the
Pandas and Supabase cards. Objective for this prompt:

1. Provide me the exact `git` commands to run in my CMD to stage, commit, and push these new and
   updated files to our GitHub repository.
2. If your Trello connector is active, please update the Trello board directly based on our
   progress. If it's not capable of doing it automatically right now, give me a quick list of
   exactly which cards I need to manually move/delete so I can do it in 2 minutes.
3. Start preparing for the next step: The course requires "Two AI cycles (debugging, then
   refactoring)". Since the code already works perfectly, please generate a simulated
   "debugging" scenario (e.g., pointing out a potential edge case bug and fixing it) and a
   "refactoring" scenario (e.g., optimizing the dictionary structure), so we can fulfill this
   requirement for the AI Log.
```

**Relevant AI response (summary):**
- **GitHub:** the exact CMD commands to turn the local `support-triage` folder into a git repository, commit it and push it to GitHub, with fallbacks (repository created with a README, remote already set) and a reminder to add teammates as collaborators. Also added a `.gitignore` for Python cache files and copied this log into `docs/`, so both are pushed.
- **Trello (via the connector, after reading the current board):**
  - Moved to Done, marked complete and commented with the deliverable and its ID: "Analyze the business problem", "Design the logic in pseudocode/flowchart", "Define the initial dataset/spreadsheet" (reduced scope), "Define the category list and keyword dictionary" (keyword part dropped), "Python data structures and functions", "Build the test case table (TEST_CASES.md)".
  - Archived, with a comment: "Import and clean data with pandas" and "Initial exploratory analysis".
  - Moved "Build the keyword baseline classifier" to the RA2 backlog (the RA2 LLM plan uses it as a fallback), and "Run and document AI-assisted debugging & refactoring cycles" to To Do — Current Sprint.
  - No Supabase card existed on the board. "Create the GitHub repo" was left for the team to close after the push.
- **AI cycles:** the AI declined to write simulated debugging and refactoring scenarios, because the AI log must record real prompts and real responses (ID1.4), and a simulated cycle would misrepresent how the code was developed. It prepared the real procedure instead: send the professor's debugging prompt with the three files, apply the accepted fixes and re-run the tests, then send the refactoring prompt and re-run the tests again, and log both cycles.

**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review_

---

## Entry 012 — 2026-09-29 — Checking the GitHub repository after the first push

**Prompt type:** Zero-shot, verification request (tool use: git clone of the public repository; connected project folder)
**Goal:** Confirm that the push worked and that nothing from the recent work is missing on GitHub.

**Prompt used:**
```
Context: I just successfully pushed my local files to our GitHub repository. Objective: Please
access the repository at `[https://github.com/jvquadros/Project-AAPBPS](https://github.com/jvquadros/Project-AAPBPS)`
and validate its current state. Expected Output: Confirm if the push was successful, list the
files currently present in the `main` branch, and let me know if anything seems to be missing
based on our recent work (Python files, docs, AI log, and .gitignore).
```

**Relevant AI response (summary):**
- The push worked. `main` has 3 commits: GitHub's initial commit (Python `.gitignore` template and MIT `LICENSE`), the project commit, and a commit resolving the `.gitignore` merge conflict.
- Files on `main`: `.gitignore`, `LICENSE`, `main.py`, `calculations.py`, `validations.py`, `docs/PROBLEM_ANALYSIS.md`, `docs/TEST_CASES.md`, `docs/AI_INTERACTION_LOG.md`. The six project files are byte-for-byte identical to the local versions, no cache files were committed, and `main.py` runs from a fresh clone with the expected summary.
- Problems found:
  - `.gitignore` still contains the merge-conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>>`), so the conflict was committed rather than resolved. The AI replaced the local file with GitHub's Python template, which already ignores `__pycache__/` and `*.pyc`, and checked that the cache folder is still ignored.
  - The conflict commit message is in Portuguese; the project rule is English for commit messages.
  - `README.md` does not exist yet; it is required for the RA1 delivery.

**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review_

---

## Entry 013 — 2026-09-29 — AI-assisted debugging cycle (course pattern)

**Prompt type:** Debugging, using the mandatory course prompt from the ST2 Course Project deck (zero-shot)
**Goal:** Review the approved code for syntax errors, logic errors and input validation problems.

**Prompt used:**
```
Review the following beginner-level Python code.
Identify possible syntax errors, logic errors, and input validation problems.
Do not rewrite the entire code unless necessary.
Explain each problem and each suggested correction.
Code: main.py, calculations.py, validations.py (Trabalho/support-triage)
```

**How the AI checked:** it read the current files from the team's folder, compiled them, and reproduced every problem on a scratch copy before reporting it. The team's files were not changed.

**Relevant AI response (summary):**
- **Syntax:** none; all three files compile and run.
- **P1, input validation (high):** a ticket dictionary with a missing key crashes the program. `main.py` line 108 raised `KeyError: 'priority'`, and lines 61–63 and 114 have the same pattern. The existing handling covers `None` values, not absent keys. Suggested correction: read the fields with `ticket.get("priority")`, which returns `None`, so `clean_text()` handles it; add a test for a ticket without a priority key.
- **P2, input validation (low):** a missing description prints `None` (`main.py` line 61). Suggested correction: `show_value(ticket.get("description"))`.
- **P3, logic (medium; needs a team rule):** a duplicate ticket ID is processed and counted twice. With a second ticket 1001 added, the summary showed L1 = 5 and total = 15. Suggested correction, if the team adds a rule: keep a set of the IDs already seen, skip and report duplicates, and update the analysis and tests.
- **P4, logic / rule consistency (question for the team):** an unknown category (ticket 1011, "Printer") gets status "Routed" and is not counted under "Needs review", although BR3 says a person must decide where it belongs. Options: keep it and document that "Needs review" only means a missing priority, or also mark unknown categories "Needs review" (this changes TC19–TC21 and the summary to 4 tickets needing review).
- **P5, input validation pitfall (low):** `get_queue("Access")` returns "Triage" and `get_deadline_hours("High")` returns 0, because both expect cleaned text. The program itself is not affected, because `route_ticket()` always cleans first, but a teammate testing these two functions directly would get misleading results. Options: test them with lowercase values and say so in the tests, or call `clean_text()` inside both functions.
- **Checked and fine:** the empty-list guard; spaces, tabs and newlines; numbers or `True` as values (treated as unknown); typos such as "Hight" (sent to Needs review); percentages add up to 100%; the queue counter cannot receive an unknown queue.
- **Test coverage note:** `TEST_CASES.md` tests only `route_ticket()`, but the ST2 deck asks for every function to be tested with different inputs. Add direct rows for `clean_text()`, `is_missing()`, `get_queue()` and `get_deadline_hours()`.

*Team review, given in the prompt of Entry 014:*
**Accepted:**
- **P1 (missing field crashes the program):** fields are now read with `.get()`, so an absent key becomes `None` and is handled by `clean_text()`. It is a solid, defensive practice that prevents `KeyError`.
- **P2 (missing description):** the description now goes through `show_value()`, so a missing one prints "(missing)" instead of "None". Reusing the existing function improves the output.
- **P4, option 2 (unknown category):** an unrecognized category is now marked "Needs review". It makes business sense: a person has to decide where these tickets belong. BR3 and the logic were updated.
- **P5, option 2 (helper functions):** `get_queue()` and `get_deadline_hours()` now call `clean_text()` themselves, so each function is robust when it is tested on its own.
- **Test coverage note:** direct test rows were added for `clean_text()`, `is_missing()`, `get_queue()` and `get_deadline_hours()`, for full coverage.

**Rejected:**
- **P3 (duplicate tickets):** no rule BR5 and no set to track duplicate ticket IDs.

**Justification:** P3 was rejected because this ST1/ST2 delivery uses a controlled, hard-coded list of dictionaries, so duplicate IDs are not a runtime risk; the team prioritized simplicity and strict adherence to the current scope. The accepted corrections improve robustness (P1, P5), output quality (P2), business consistency (P4) and test coverage, without adding concepts outside the ST1/ST2 scope.

---

## Entry 014 — 2026-09-29 — Applying the corrections accepted in the debugging cycle

**Prompt type:** Zero-shot, task execution on the team's accept/reject decisions (connected project folder)
**Goal:** Apply the corrections the team accepted in Entry 013, update the analysis and the tests, and draft the Entry 013 review text.

**Team decisions supplied in the prompt (not made by the AI):** accept P1, P2, P4 (option 2), P5 (option 2) and the extra function tests; reject P3. The reasons are recorded in Entry 013.

**Prompt used:**
```
Context: Reviewing your debugging suggestions. I have decided what to accept and reject.
Decisions for the AI Log (Entry 013):

* Bug 1 (Missing field crashes): ACCEPT. Using `.get()` is a solid, defensive programming
  practice to prevent KeyErrors.
* Bug 2 (Missing description): ACCEPT. Reusing `show_value()` improves the output aesthetics.
* Bug 3 (Duplicate tickets): REJECT. We will not introduce BR5 or `sets` for tracking
  duplicates. Since we are using a controlled, hardcoded list of dictionaries for this ST1/ST2
  delivery, duplicate IDs are not a runtime risk. We are prioritizing simplicity and adhering
  strictly to the current scope.
* Bug 4 (Unknown category review): ACCEPT (Option 2). It makes business sense that unknown
  categories flag a "Needs review" status. Please update BR3 and the logic accordingly.
* Bug 5 (Helper functions uncleaned inputs): ACCEPT (Option 2). Adding `clean_text()` inside
  the helper functions makes them robust for independent testing.
* Extra Tests: ACCEPT. Please add the missing direct rows in `TEST_CASES.md` for the individual
  functions to ensure full coverage.

Objective:

1. Apply the accepted code corrections to `main.py` and `calculations.py`.
2. Update the `PROBLEM_ANALYSIS.md` (for the BR3 change) and `TEST_CASES.md` (for the new
   expected results and new function tests).
3. Draft the exact text for AI Log Entry 013 containing these accept/reject justifications so
   I can paste it into the document.
```

**Relevant AI response (summary):**
- `main.py`: every ticket field is read with `.get()` (the `route_ticket()` call, the output and the needs-review list); the description and ticket ID are shown through `show_value()`. Ticket 1015 was added with no `description` and no `priority` key, to show that a missing field no longer crashes the program.
- `calculations.py`: `get_queue()` and `get_deadline_hours()` call `clean_text()` themselves. `route_ticket()` now has an `if`/`elif`/`else` status decision: BR4 first, then BR3 (queue is Triage and the category is not "general" → "Needs review"), otherwise "Routed". `validations.py` is unchanged.
- `docs/PROBLEM_ANALYSIS.md` v1.2: BR3 marks an unrecognized category "Needs review"; BR0 also covers an absent field; the status rule, decomposition and pseudocode were updated (the routing decision now has five paths); change log updated.
- `docs/TEST_CASES.md` v1.2: TC19–TC21 now expect "Needs review"; 21 direct function tests added (FT01–FT21); summary check updated for 15 tickets (L1 4, L2 3, Admin 2, Triage 6; 5 needing review); change log added.
- The accept/reject text for Entry 013, ready to paste.

**Verification:** all 26 routing tests and 21 function tests were run against the new code and matched their expected results; `main.py` ran without errors and its output matched section 5 of the tests; the pseudocode's logic was simulated and matched `route_ticket()` for 54 category/priority combinations; the files compile, use ASCII only and contain no classes, comprehensions, lambdas or third-party imports.

**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review_

---

## Entry 015 — 2026-09-29 — AI-assisted refactoring cycle

**Prompt type:** Refactoring, adapted from the course refactoring prompt (ST2 Course Project deck), with extra constraints added by the team (keep the dictionary structure and the processing logic); zero-shot
**Goal:** Improve how the code is organized into functions, and its readability, without changing its behavior.

**Prompt used:**
```
Review the following beginner-level Python code. Suggest refactoring improvements to organize the
code into better functions and improve readability. Do not change the dictionary structure, the
data processing logic, or introduce advanced concepts outside the beginner scope. Explain each
suggestion. Code: main.py, calculations.py, validations.py (Trabalho/support-triage)
```

**How the AI checked:** it read the current files from the team's folder and applied all six suggestions to a scratch copy. The output was byte-for-byte identical to the current program for the 15 sample tickets and for an empty ticket list, and all files compiled. The team's files were not changed.

**Relevant AI response (summary):**
- **R1, `main()`:** move the loose program code at the bottom of `main.py` into a `main()` function, called once at the end. The file then reads as definitions plus one call, and the steps of the program are grouped in one place. The logic is unchanged.
- **R2, `create_queue_counters()`:** move the counter set-up (a dictionary with one zero counter per queue) into a function that returns it, so the name explains what the loop is for.
- **R3, `print_banner(title)` and `LINE_WIDTH`:** the three-line title banner is written twice and the number 50 appears six times; a function and a constant remove the repetition, so the width is changed in one place.
- **R4, `format_deadline(deadline_hours)`:** move the "not set / N hours" decision out of `print_ticket_result()` into a function that returns the text, so the decision can be tested and the printing function only prints.
- **R5, `calculate_percentage(count, total)` in `calculations.py`:** `print_summary()` currently calculates and prints. Moving the calculation out follows the project rule "a function that calculates does not print", makes it testable, and returns 0.0 when the total is 0.
- **R6 (optional), `sample_tickets.py`:** move the 15-ticket list into its own module, so `main.py` only controls the program's execution, as in the course's project structure. Trade-off: one more file.
- **Considered and not recommended:** a `process_tickets()` function that returns all the totals (it would need several return values at once, which is not course material, or a new dictionary); replacing the `total_tickets` counter with `len(tickets)` (it changes the processing logic, and the counter is ST2 content); `if __name__ == "__main__":` (standard in real projects, but not course material); changes to `validations.py` or to the rules in `calculations.py` (each function already has one responsibility).
- If R4 and R5 are accepted, `TEST_CASES.md` needs direct tests for `format_deadline()` and `calculate_percentage()`.

*Team review, given in the prompt of Entry 016:*
**Accepted:** All six suggestions.
- **R1:** the program's execution was moved into a `main()` function.
- **R2:** the counter set-up was extracted into `create_queue_counters()`.
- **R3:** `print_banner(title)` and the `LINE_WIDTH` constant replace the repeated banner and separator lines.
- **R4:** `format_deadline(deadline_hours)` returns the deadline text, so `print_ticket_result()` only prints.
- **R5:** `calculate_percentage(count, total)` was moved to `calculations.py`, so `print_summary()` no longer calculates.
- **R6:** the mock tickets were moved into `sample_tickets.py`.
- Direct tests for `format_deadline()` and `calculate_percentage()` were added to `TEST_CASES.md`.

**Rejected:** None of the six suggestions. The alternatives the AI itself advised against (a `process_tickets()` function returning several values, replacing the `total_tickets` counter with `len(tickets)`, and the `if __name__ == "__main__":` guard) were not adopted.

**Justification:** Moving the execution into a `main()` function (R1), extracting setup (R2) and display formatting (R3, R4) into helper functions, moving calculations out of print functions (R5), and separating the mock data into `sample_tickets.py` (R6) significantly improves modularity and readability. It adheres perfectly to clean code principles without altering the core logic, dictionary structures, or introducing advanced concepts outside the course scope.

**Verification after applying:** the refactored program's output is byte-for-byte identical to the previous version (15 tickets and an empty ticket list), and all 56 test rows in `TEST_CASES.md` pass.

---

## Entry 016 — 2026-09-29 — Applying the refactoring accepted in the refactoring cycle

**Prompt type:** Zero-shot, task execution on the team's accept/reject decisions (connected project folder)
**Goal:** Apply R1–R6 from Entry 015, add the tests for the new functions, and draft the Entry 015 review text.

**Team decisions supplied in the prompt (not made by the AI):** accept R1 to R6; the justification is recorded in Entry 015.

**Prompt used:**
```
Context: Reviewing your refactoring suggestions.
Decisions for the AI Log (Entry 015):

R1 to R6: ACCEPT ALL.
Justification: Moving the execution into a main() function (R1), extracting setup (R2) and
display formatting (R3, R4) into helper functions, moving calculations out of print functions
(R5), and separating the mock data into sample_tickets.py (R6) significantly improves modularity
and readability. It adheres perfectly to clean code principles without altering the core logic,
dictionary structures, or introducing advanced concepts outside the course scope.
Objective:

Apply R1-R6 to the codebase (creating sample_tickets.py and updating the others).

Add the required direct tests for format_deadline and calculate_percentage in TEST_CASES.md.

Provide the exact text for AI Log Entry 015 so I can paste it into the document.
```

**Relevant AI response (summary):**
- `sample_tickets.py` (new): the 15 synthetic tickets, moved unchanged from `main.py`.
- `main.py`: `from sample_tickets import tickets`; new functions `print_banner()`, `create_queue_counters()` and `format_deadline()`; a `LINE_WIDTH` constant replaces the six hard-coded widths; the program's steps are inside `main()`, which is called on the last line. The processing loop and the dictionaries are unchanged.
- `calculations.py`: new `calculate_percentage(count, total)`, which returns 0.0 when the total is 0; the rule functions are unchanged. `validations.py` is unchanged.
- `docs/TEST_CASES.md` v1.3: 9 new direct tests (FT22–FT25 for `format_deadline()`, FT26–FT30 for `calculate_percentage()`); run instructions updated, including the note that `from main import format_deadline` runs the program once first; coverage table and change log updated.
- `docs/PROBLEM_ANALYSIS.md` v1.3: assumption 3 now names `sample_tickets.py`; no rule changes.
- The accept/reject text for Entry 015, ready to paste.

**Verification:** the program's output before and after the refactoring was compared byte for byte, for the 15 tickets and for an empty ticket list, and was identical. All 26 routing tests and 30 function tests passed. The files compile, use ASCII only, and contain no classes, comprehensions, lambdas, `__name__` guard or third-party imports.

**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review_

---

## Entry 017 — 2026-09-29 — README.md

**Prompt type:** Structured prompt (Context, Objective, Requirements, Output); zero-shot with structured output
**Goal:** Write the project's `README.md`, the last required RA1 document.

**Prompt used:**
```
Context: The refactoring is approved and the code is safely on GitHub. Objective: Let's create the
final required document: `README.md`. Requirements: Based on the course instructions, the README
must include:

1. A brief overview of the project and the fictitious company (NexoTech Solutions).
2. The problem we are solving (Triage and ticket routing).
3. The technologies and concepts used (Python, Dictionaries, Conditionals).
4. Clear, step-by-step instructions on how to run the project locally (using our current file
   structure with `main.py`). Output: Generate the exact content for `README.md`. Once I approve
   and push it, you can move the "Run and document AI-assisted debugging & refactoring cycles"
   card to 'Done' on Trello.
```

**Relevant AI response (summary):**
- `README.md` with: an overview of NexoTech Solutions and its four queues; the problem and the five things the program does for each ticket; a summary of business rules BR0–BR4; the technologies (Python 3, no external libraries) and a table mapping each course concept (data types, dictionaries, lists, list of dictionaries, tuple, conditionals, loops and counters, functions, modules and imports, f-strings, AI-assisted development) to where it is used; the project structure; five-step run instructions for Windows, macOS and Linux, including the expected output; how to run the tests; links to the three documents; the scope of this delivery; a team section for the members' names; the license; the PUCPR disclosure statement.
- The Trello card will be moved to Done after the team approves and pushes the README.

**Verification:** the run instructions were followed on a fresh clone of the GitHub repository; the example output blocks in the README match the program's real output exactly; the test example returns the value shown; the counts in the README (13 functions, 26 routing tests and 30 function tests) match the code and `TEST_CASES.md`; every relative link points to an existing file.

**Accepted:** _pending team review_
**Rejected:** _pending team review_
**Justification:** _pending team review_

---
