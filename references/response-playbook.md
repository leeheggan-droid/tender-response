# Narrative, constrained and prescribed responses

## Map the question before composing

Split compound questions into assessable parts: explain the method, identify the
owner, provide a timetable, describe a control, evidence an outcome. Distinguish
delivery requirements from the required form of the answer. An eloquent paragraph
about capability does not answer 'how', and a policy title does not demonstrate
implementation. Map each required element to evidence and an answer location.

Use the actual evaluation descriptors to decide the depth needed. Prioritise
mandatory coverage, then the matters carrying marks and buyer value. Do not
predict a score as if awarded by the evaluator. A self-review can say which
descriptor is supported and which remains weak.

## Build a narrative that answers

Use a connected line of reasoning: the buyer needs an outcome; the proposed
method addresses it; accountable people and controls make the method credible;
relevant evidence shows why it is credible; the resulting benefit matters to this
buyer. State the answer in the opening rather than starting with company history.

Develop only the parts the question calls for:

- Explain actions, sequence, timing, responsibilities, interfaces and dependencies.
- Use a short, relevant example: comparable setting, actual action, verified
  outcome, measurement basis and why it is applicable here.
- Explain how progress is measured, reviewed, corrected and escalated.
- Connect differentiators to evidence and buyer benefit. Do not claim superiority
  or uniqueness without a defensible basis or speculate about competitors.

Use the buyer's headings and vocabulary naturally. Define necessary technical
terms. Prefer specific verbs and clear transitions over adjectives such as
'world-class'. Vary paragraph length for readability without creating a checklist
of disconnected assertions. Do not append an executive summary to every answer.

For a large tender pack, outline the complete response before drafting sections.
Maintain a shared response spine: buyer priorities, supported propositions,
delivery model and intended outcomes. Allocate any overall limit across sections
as well as checking field limits. Keep a common facts/roles/commitments register
so separately drafted answers remain one coherent offer; cross-reference only
where permitted and keep each independently scored answer complete.

A long response needs a through-line, consistent terminology, useful headings
and selective proof. Each section should advance an answerable requirement.
Use graphics only if permitted and if they convey information more efficiently;
check captions, font requirements and whether their words count. Avoid duplicated
case studies and repeated generic win themes across sections.

## Compress without losing the answer

1. Record the cap, counting rules and whether it applies per field, subpart or
   whole answer. Track simultaneous word, character, page and attachment limits.
2. Reserve enough space for each mandatory element. Allocate the remainder using
   published weighting and importance, not equal slices by default. If no weights
   exist, use the detail required to answer each element and label that judgement.
3. Draft a compact complete answer directly; do not first generate a long essay
   when the final field is tiny. Leave reasonable counting headroom when possible.
4. Remove generic openings, repeated benefits, duplicated proof and unnecessary
   qualifiers. Combine related actions with their owner and control. Keep the
   conditions that make a claim true, plus the evidence that makes it credible.
5. Recount the exact final text and recheck every requirement after editing.

Space pressure never justifies invented abbreviations, removing a material
dependency, changing a proposed target to a proven result, or silently omitting a
subquestion. External links, footnotes and annexes are not a way around a cap;
use them only when expressly permitted and do not rely on evaluators reading them.
Do not fill spare words merely to reach a maximum.

For a very short field, a useful pattern is: direct answer; how and who; relevant
proof or control. Follow the requested order instead when prescribed. For yes/no
questions, select the evidence-supported answer and explain only in the allowed
field. Do not select 'yes' to a mandatory condition supported only by a future
intention. Where complete coverage cannot fit, show the best compliant draft and
state the specific unresolved trade-off privately. Seek a clarification only if
it is actually needed, after doing the work possible now.

## Separate proposal from promise

An approved operating model can support 'we propose' with stated dependencies.
It does not automatically authorise a new SLA, discount, staffing allocation or
unconditional start date. If the owner has not approved a tender-specific
commitment, keep it in the internal review or clearly label it as a proposal in
the draft. Do not fill gaps with 'we will confirm', 'we guarantee', or invented
future actions presented as authorised promises.

If a mandatory requirement lacks evidence, keep the response visibly incomplete
for review. Do not hide the issue in a polished narrative or falsely claim
compliance. Internal placeholders belong in a clearly labelled working draft,
not in a purported ready-to-submit answer.

## Review as an evaluator

Perform a separate critical pass over the exact answer:

| Check | What must be visible |
| --- | --- |
| Coverage | Every question verb, subpart, mandatory condition and requested example |
| Responsiveness | A direct answer tied to the buyer's actual scope and outcomes |
| Credibility | Traceable evidence, valid comparisons, dates, units and qualifications |
| Delivery | A workable mechanism and accountable role where requested |
| Narrative | A clear connection from need to method, evidence and buyer value |
| Compliance | Correct structure, count, file type, attachments and page layout |
| Consistency | Matching roles, timelines, figures and commitments across all answers |

Check facts against sources rather than merely rereading fluent text. Search
again if the review reveals a gap. Flag inconsistencies across sections for
resolution, not quiet deletion. Revalidate the exact text after any material edit.

## Count honestly

The optional counter accepts a UTF-8 plain-text file containing only the final
submission field:

```text
python scripts/check_limits.py answer.txt --max-words 250
python scripts/check_limits.py answer.txt --max-characters 1500 --character-unit utf16
python scripts/check_limits.py answer.txt --max-words 250 --max-characters 1500
```

It splits words on whitespace; hyphenated words and URLs each count as one token
under that convention. Character modes are Unicode code points, UTF-16 code units
and UTF-8 bytes. Spaces and line breaks count. It normalises CRLF/CR to LF on read
and does not trim text. These are explicit local conventions, not a replica of
every portal or Microsoft Word counter. Use the actual portal/required application
if its convention differs. Chinese text, formatted tables and punctuation-heavy
content particularly need the specified counting method.

If no counting tool is available, label the count unverified and request the
portal check; never assert an exact count from intuition. For page caps, render
with the required template, margins, fonts and spacing, inspect page count and
clipping, and check that tables and captions remain readable. Plain text cannot
verify a formatted page limit.
