# Validation record — 27 October 2026

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
