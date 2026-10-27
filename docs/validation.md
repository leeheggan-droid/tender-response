# Validation record

## v0.2.0 audit follow-up — 27 October 2026

The audit fixes are package checks, a shorter entry point with conditional
playbook reading, a compact receipt using one private ledger, and a supplied-
feedback correction loop. The entry point fell from 789 to 547 whitespace words
after the final qualification clarification; it retains active retrieval and
claim controls. No runtime package dependency was added.

### Package regression and release checks

- All **14 unit tests passed** locally. The added checks cover required skill
  metadata, linked resources staying inside the package, required distribution
  files and readable DOCX/XLSX archive/XML parts.
- Repeated the audit's incomplete-distribution case: the counter tests passed,
  but the new package tests correctly failed with missing SKILL.md, README,
  licence and linked fixture resources. The complete checkout passed.
- The skill-creator validator reported **Skill is valid!** for the final entry
  point. The CI required-field checks do not implement a full YAML parser.

### Revised short-answer trial

A fresh Codex agent searched the original six-file Markdown corpus and produced
a 75-word answer. Author inspection caught a dropped 'recorded' qualification in
its incident result. The source-strength instruction was clarified, then another
fresh-agent trial produced **75 words**, retained 'incidents recorded', covered
the requested elements and used a four-bullet receipt without an extra working
pack. These are small behavioural trials, not a statistical improvement claim.

### Actual mixed-format and feedback trial

The [mixed-format pack](../evals/mixed-format/README.md) was read by a fresh Codex
agent using actual DOCX extraction, pypdf and openpyxl. It followed the referenced
Annex A PDF and inspected Delivery, Assurance and Availability workbook sheets.
No Markdown copy of the company evidence was supplied to this trial.

| Field | Measured initial answer | After supplied feedback | Cap |
| --- | --- | --- | --- |
| Q1 | 69 whitespace words | unchanged | 75 words |
| Q2 | 75 whitespace words | 80 words | 100 words |
| Q3 | 268 UTF-16 code units | unchanged | 500 UTF-16 units |
| Q4, including subheadings | 430 whitespace words | unchanged | 650 words |
| Complete formatted response | 2 rendered pages | 2 rendered pages | 3 pages |

The author independently recounted the answer-only files, rendered initial and
revised DOCX files with isolated LibreOffice on llmbox, and inspected every page.
Source DOCX files, the response template, all three workbook print sheets and the
PDF annex were rendered and visually inspected too. The renderer substituted
Liberation Sans for Arial; this does not establish identical Microsoft Word
pagination. LibreOffice emitted a javaldx warning, but conversions succeeded and
the resulting PDFs opened and rendered correctly. No clipping or leftover
response placeholders were found in the completed response documents.

Feedback asked for delivery month and pre-handover acceptance to be explicit.
The agent reopened the relevant Delivery cells, preserved the original answer
and document, revised Q2 within its cap, and saved a correction in the private
response library without inventing an assessor score.

Q3 correctly answered **Status: No** from the expired certificate record. This
is a successful truthfulness test and an **unmet mandatory tender condition**;
the response stayed a working draft. Staffing and start approvals also remained
qualified. A successful assessment does not make the fictional bidder compliant.

### Still not tested

Lee confirmed QwenWork is available only on his work PC. The ready-to-run pack
and prompts are supplied for that environment; **no live QwenWork test is claimed**.
Enterprise connectors, OCR/scanned PDFs and Microsoft Word pagination remain
untested. Runtime skill use still depends on the host's permitted document tools.
The trial answers and source/search ledgers remain outside the public repository.

## v0.1.0 initial validation — 27 October 2026

Scope: initial v0.1.0 skill and optional local text counter. All company records
used were the six fictional Markdown files in `evals/company/`. No employer,
client or live tender documents were accessed or published.

## Baseline

A no-skill simulated exercise rejected unsupported certification, savings and
availability claims, but mixed missing-evidence commentary into the client answer
and added future verification promises. A subsequent real-file no-skill trial
actively searched the supplied corpus and produced a sound 72-word response.
The baseline was already capable; these runs do not demonstrate a measured
quality improvement or prove that the new skill is necessary for every model.

## Independent forward trials

Fresh Codex agents loaded `SKILL.md` and the relevant references, then performed
actual file searches and reads. They were given requests and raw records, without
intended answers or earlier results. The author inspected the outputs, evidence
register/search receipts and counted the saved answer-only files independently.

| Trial | Observed result | Limit check |
| --- | --- | --- |
| A: mobilisation, lead, escalation, comparable outcome | Retrieved current standard, closeout and staffing evidence; retained dependencies, accountable role and qualified outcome; avoided superseded marketing and embedded instructions | 67 whitespace words / 75 maximum |
| B: certification, 25% cost saving, named immediate lead | Retrieved controlled records; did not confirm expired certification, unsupported savings or unallocated staff; identified specific records needed and kept draft status | 305 Unicode code points / 500 maximum |
| C: longer narrative and two-page cap | Used the three prescribed headings, connected continuity needs to the source-backed method and bounded proof, and left the page cap explicitly unverified without a template/render | 310 whitespace words / 400 maximum |

Trial B exposed a wording refinement: absence findings should explicitly refer
to the searched records rather than sound company-wide. The evidence method now
states that scope explicitly. This is a narrow clarification, not proof that the
model can find evidence outside its available corpus.

Trial C also suggested stable source-revision/last-checked fields and a host
installation smoke test; both are now documented. Its longer review was assessed
separately from the client text. These small documentation refinements were
reviewed but not rerun as a new model benchmark; the results above describe the
trial revision before those refinements.

## Deterministic tool checks

The counter tests cover exact and exceeded caps, simultaneous caps, headings,
whitespace conventions, Unicode character units, line-ending normalisation,
zero-length limits, UTF-8 BOM handling and input/argument errors. These tests
check counts and exit status; they do not assess prose or factual accuracy.

Final local checks: all **10 unit tests passed** on Windows/Python 3.13; the
skill-creator validator reported **Skill is valid!**; every local Markdown link
resolved; the worked short answer measured **63 words** against a 75-word cap.
A GitHub Actions workflow runs the counter tests and example check on Windows
and Ubuntu. Its remote result is separate from these local results.

Development checks initially failed because the implementation did not yet exist
(the intended test-first stage). One newline test then expected six characters
for text that normalised to five; inspection identified the incorrect fixture,
which was corrected. A premature `git status` before repository initialisation
also returned 'not a git repository'; the directory was then initialised.

## Limits of this evidence

- Tests used the Codex agent harness, not a live QwenWork installation. QwenWork
  packaging follows its documented file format and installation mechanism.
- Fixtures were readable Markdown. Live enterprise connectors, Office/PDF
  extraction and OCR were not exercised in these behavioural trials.
- No real procurement evaluation, tender submission or outcome was tested.
- Model behaviour remains probabilistic; evidence receipts support human review,
  not a guarantee of complete retrieval or zero hallucination.
- Scenarios D–H in `evals/scenarios.md` are reusable future evaluations. They are
  not all claimed as executed; archived-document instruction handling was observed
  during A/B as well.
