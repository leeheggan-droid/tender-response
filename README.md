# Tender response

A portable AI skill for clear, complete, evidence-backed tender answers: long
narratives, short prescribed answers, and strict word, character or page limits.
Designed for QwenWork and other agents that can read `SKILL.md`.

**It searches accessible company documents before drafting or flagging gaps.**
It checks source context and currency, maps each question to an answer, and keeps
unsupported claims and unapproved commitments out of purported final responses.

## Install in QwenWork at work

Paste this into QwenWork:

```text
Please install the tender-response skill from
https://github.com/leeheggan-droid/tender-response
into ~/.qwenwork/skills/tender-response/.
Keep SKILL.md, references/, assets/ and scripts/ together.
Then show me that the skill is available.
```

QwenWork documents installation from a GitHub link and a local Skills interface.
If your work environment restricts installation, use the organisation's permitted
skill installation route. This repository does not bypass workplace controls.

Alternatively, [download the skill ZIP](https://github.com/leeheggan-droid/tender-response/releases/latest/download/tender-response.zip)
and extract it so `~/.qwenwork/skills/tender-response/SKILL.md` exists, or use
**Extensions → Skills → Install Skill** to supply the skill and auxiliary files
as supported by your client. Do not install only `SKILL.md`: the references matter.

[QwenWork's official Skills guide](https://docs.qwenwork.ai/desktop/skills)
describes installation and invocation. This is file-format compatibility and a
documented installation route, not a claim that every managed work PC has been
tested. Qwen Code is a separate product; its equivalent personal directory is
`~/.qwen/skills/tender-response/`. Codex and other compatible agents can use
`~/.agents/skills/tender-response/`.

## Use it

Select the installed skill or name it in conversation. Attach the tender and
make the relevant company folder or permitted connector available to the agent.
The skill cannot grant access to files that the work application cannot see.

```text
Use the tender-response skill. Read the attached tender and actively search
the company files available in [folder/connected source]. Answer questions
3.1–3.4 in the buyer's order. Each answer has a 250-word maximum including
headings. Use the published scoring criteria. Trace material claims to actual
documents, search again for gaps, and distinguish proposals from proven facts.
Save the answer and internal evidence/search review separately in [private folder].
```

For a longer answer:

```text
Use tender-response to prepare the service-delivery narrative. Follow the tender
headings and scoring criteria. Build a connected story from the buyer's needs,
our proposed method, accountabilities, relevant proof and measurable benefits.
Search the available company library first. Check the full response against the
six-page cap in the required Word template. Flag remaining evidence gaps only
after targeted searches and document review.
```

If the application cannot install skills, load `SKILL.md` and the relevant
`references/` files as context and explicitly ask it to follow them. Reading a
GitHub URL alone is not proof that the agent has installed or loaded the skill.

### Assess it before using company documents

After installing, paste:

```text
Use tender-response on its bundled fictional evals/company/ folder. Start with
capability.md and search the other files. Answer in at most 75 words: explain
mobilisation timing, accountable lead, escalation and a comparable outcome.
Save the answer and a separate evidence/search review in a new private test
folder outside the installed skill. Show which skill references you loaded,
which files you actually searched/read, and the measured answer word count.
If a required tool is unavailable, say so. Do not use real company documents.
```

Check that it finds the current 20-working-day approach, retains the asset/access
dependency, cites the approved closeout, and avoids old ten-day/25%-saving claims.
This smoke test checks your actual work application's loading and file tools.

## What you receive

1. A clean answer in the prescribed structure and length.
2. A separate internal review: requirement coverage, source locators, searches
   actually performed, measured limits, evidence gaps and commitments needing
   confirmation. Material unresolved gaps keep the response labelled as a draft.

The method works with local documents and available company search connectors.
Word, Excel, PDF and scanned evidence need the host application's document-reading
or OCR tools. No external API, paid service, credentials or company data are
bundled. Python is optional and used only by the local text counter.

**Keep live tender documents, completed evidence packs and client information in
your private work location, outside this public repository.** All company data
under `evals/company/` is fictional test material.

## Contents and validation

- [SKILL.md](SKILL.md): the agent entry point.
- [Company evidence method](references/company-evidence.md): active retrieval,
  source checks, conflicts and bounded gap resolution.
- [Response playbook](references/response-playbook.md): narrative and constrained
  modes, commitments, evaluator review and count conventions.
- [Working pack](assets/working-pack.md): private coverage/evidence/search template.
- [Worked example](examples/mobilisation.md): one brief at two response lengths.
- [Sources and prior art](docs/sources.md): research and build/adopt decision.
- [Evaluation scenarios](evals/scenarios.md): repeatable behavioural checks.
- [Validation record](docs/validation.md): what was actually tested and limitations.

Optional, dependency-free helper (Python 3.10+):

```text
python scripts/check_limits.py answer.txt --max-words 250
python scripts/check_limits.py answer.txt --max-characters 1500 --character-unit utf16
python -m unittest discover -s tests -v
```

The counter includes headings and whitespace, normalises line endings to LF and
uses whitespace-separated words. The buyer's application/portal counter takes
priority; the helper does not verify evidence, page layouts or answer quality.
Skill instructions improve agent behaviour but cannot guarantee that any model
will retrieve every document or never hallucinate. Check the evidence trail.

MIT licensed. An independent skill, with no endorsement by QwenWork, Shipley or
the organisations referenced in the research notes.
