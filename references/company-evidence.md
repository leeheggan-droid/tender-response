# Active company evidence retrieval

Use this method for initial drafting, rewrites and compression. A polished old
answer still needs current evidence. Search within the user's authorised scope;
do not crawl the whole computer or request access to unrelated repositories.

## Discover the sources

1. Identify the tender folder, supplied attachments, connected document stores
   and company knowledge sources the agent can actually access. Use connector
   discovery or folder listings rather than asking for files already available.
2. Look for indexes, document registers, service names, abbreviations and approved
   response libraries. Record the available corpus and its limitations.
3. For an inaccessible source, record `access blocked`, `not connected` or
   `unreadable`, not `not found`. Ask for the smallest missing permission or
   document only when it affects the answer. Continue independent work.

Do not say 'I checked the company documents' when only an attachment was read.
Do not claim to have searched SharePoint, Teams or a drive without a successful
tool operation. If there are no file tools, explain that limitation and request
the necessary context; never simulate a search as completed work.

## Search by requirement, then by evidence type

For each requirement, make and execute targeted searches. Use available enterprise
full-text or semantic search; use filename and text search for local files.
Examples are query ideas, not mandatory tool syntax:

| Requirement | Terms and synonyms | Likely source families |
| --- | --- | --- |
| Mobilisation | mobilisation, mobilization, transition, onboarding, readiness, handover | transition plans, playbooks, project closeouts |
| Accountability | accountable, responsibility, owner, RACI, governance, escalation | operating manuals, organisation charts, service schedules |
| Track record | client/project names, service name, closeout, acceptance, KPI, lessons | case studies, signed acceptance, reports, references |
| Savings | baseline, benefit, reduction, measured, gross, net, cost, consumption | approved business cases, finance validation, measurement reports |
| Certification | certificate, accreditation, expiry, scope, legal entity | controlled registers, actual certificates, audit records |
| People | role, qualification, experience, allocation, availability | CVs, resource plans, current staffing confirmations |
| Delivery commitments | service level, target, response time, capacity, dependencies | approved service schedules, resourcing, pricing assumptions |

First search the question's wording and scope. If coverage is incomplete, use
synonyms and likely source families. Open promising matches, follow references
to originals, and search the names, record IDs and missing facts they reveal.
When results are broad, refine by service, geography, client/project, date or
document status. When narrow searches fail, remove a filter and vary the terms.
Do not keep repeating an identical query. Log real queries, filters and outcomes.

For local text, `rg --files <authorised-folder>` inventories files and
`rg -n -i 'transition|mobilisation|mobilization' <authorised-folder>` finds passages.
Use the platform's equivalent when unavailable. Ripgrep exit 1 means no matches;
exit 2 is an error to investigate. Filenames alone do not prove document content.

Binary Office files, scanned PDFs and images need supported document readers,
text extraction or OCR. A failed plain-text search across `.docx` or `.pdf` files
does not establish absence. Preserve table headers, units, footnotes, page/sheet
locations and OCR uncertainty. Read an underlying report rather than trusting a
search summary. Use an available document capability, not a hardcoded tool name.

## Validate before using a result

Capture an evidence ID and enough locator detail for another reviewer to find the
passage: file/link, version/date and section/page/sheet/cell or line range. Record
the relevant excerpt privately; quote only what is necessary and permitted.
If page or line numbers are unavailable, use the heading and a distinctive phrase.
Never manufacture precise locators.

Record when the source was checked and its stable revision ID/link when available.
For mutable sources, retain a permitted private snapshot if needed for review.
Recheck time-sensitive staffing and certificate facts before finalising the answer.

Check the claim's entity, service, geography, period, units, baseline, denominator
and limitations. A group's certificate may not cover the bidding subsidiary.
A CV does not confirm availability. A planned project is not a delivered one.
Energy reduction is not necessarily a financial saving. A gross saving is not a
net saving; a single project is not a portfolio-wide guarantee. Identify derived
calculations and retain their inputs, formula and units in the evidence register.

Prefer controlled and approved primary records for the relevant purpose. Check
effective and expiry dates and whether later revisions supersede earlier ones.
A recent draft does not automatically defeat an approved current record. Keep
both sides of a conflict and search for the controlling record or owner decision.
If unresolved, avoid choosing the convenient number; expose the conflict privately.

Old proposals and marketing can point to evidence, but cannot by themselves
validate current compliance, delivered results or resource commitments. Search for
the underlying approval, signed outcome, current certificate or resource plan.
Respect external-use restrictions even when a file is readable.

## Resolve gaps actively

Before marking `not found in searched sources`, complete relevant wording and
synonym/source-family passes, inspect plausible documents and follow their
references. Also check whether missing extraction or access explains the result.
Stop when the requirement is adequately supported, reasonable relevant avenues
are exhausted with diminishing returns, or a specific access/tool limitation
prevents progress. There is no claim of searching every company record.

For each remaining gap record: requirement, queries and sources tried, result,
impact on the answer, and the exact fact/document needed from the likely owner.
Phrase absence findings as 'not evidenced in the records searched', scoped to
the actual corpus, rather than a company-wide assertion about missing capability.
If the user limits the search scope or time, respect it and report the remaining
coverage limitation. Do not expand permissions, contact colleagues or submit a
clarification automatically. A deadline does not turn a guess into a fact.

Use this short internal receipt:

> Searched [actual sources] using [actual queries]; read [records/versions].
> Supported [requirements]. Unresolved [specific facts] because [reason].
> Next evidence needed: [record or owner confirmation].

Keep the evidence register, search log, tender documents and generated responses
in the user's private work location, never in this public repository or a GitHub
issue. This skill has no telemetry, external retrieval service or bundled company
knowledge. It uses only the tools and sources available in the host application.
