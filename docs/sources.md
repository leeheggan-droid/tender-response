# Research and prior art

Reviewed 27 October 2026. This skill is independently written. No proprietary
manual, third-party skill instructions or employer documents are redistributed.

## Proposal-writing practice

### Shipley Associates — Proposal Writer Playbook

[Publisher's online edition](https://digital.shipleywins.com/view/320547/)

The playbook treats proposals as customer-focused persuasion grounded in
compliance and responsiveness. It emphasises planning, organisation, supporting
material and review before and after drafting. We apply those principles through
the requirement map, answer-first narrative, buyer benefits and critical review.
We do not reproduce its toolkit or claim certification or endorsement.

### Government Commercial Agency — How to write an effective tender bid

[Official supplier guide](https://www.gca.gov.uk/how-to-supply/write-effective-bids)

The guide recommends answering all requirements, tailoring to the buyer, using
relevant recent evidence and measurable outcomes, and following format and word
limits. Those principles inform coverage, evidence selection and final checks.
The actual tender's rules and scoring criteria remain authoritative for each bid;
this is general writing practice, not jurisdiction-specific procurement advice.

APMP material was also located in search, but two candidate official PDF URLs
returned HTTP 404 on retrieval. It is not treated as a read source or bundled.

## Technical packaging

### Agent Skills specification

[Open specification](https://agentskills.io/specification)

The skill uses standard YAML `name`/`description` metadata and a `SKILL.md` entry
point with relative supporting files. It avoids agent-specific tool names and
mandatory plugins. The optional counter is ordinary local Python with no external
dependencies or network requests.

### QwenWork and Qwen Code

[QwenWork desktop Skills](https://docs.qwenwork.ai/desktop/skills)
documents the `~/.qwenwork/skills/` directory, GitHub-source installation, local
upload and skill invocation. [Qwen Code Skills](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/)
documents its separate `.qwen/skills` and `.agents/skills` discovery paths.
These are distinct products. We provide QwenWork instructions first and preserve
portable file-based use for applications with other installation mechanisms.

## Existing open-source tender skills

- [vulh1209/claude-tender-skill](https://github.com/vulh1209/claude-tender-skill)
  was cloned and its README and tender API skill inspected. It is an MIT-licensed
  Claude Code integration for a specific construction-tender backend, including
  search, pricing and evaluation endpoints. Useful precedent for document search,
  but its backend and token requirement do not fit a portable work-document
  writing skill. No code or instructions were copied.
- [podcctv/Tender-skills](https://github.com/podcctv/Tender-skills) was discovered
  and its repository metadata/top-level tree inspected. No licence was reported
  by GitHub at review time; its contents were not adopted. This is a discovery
  record, not a quality assessment.
- [benctse/rfp-skill](https://github.com/benctse/rfp-skill) was cloned and its RFP
  workflow/scoring instructions inspected during the follow-up audit. Relevant
  precedent: verify capabilities against current sources and resolve unknowns.
  Its commercetools-specific integration and configuration are not adopted.
- [serzh261/proposal-writing-skill](https://github.com/serzh261/proposal-writing-skill)
  was cloned; its entry point, drafting, review and case-study instructions were
  inspected. Relevant precedent: criterion-linked themes, defensible project
  evidence and separate content/format review. Firm-specific facts and lifecycle
  procedures are not adopted. No third-party instructions were copied.

The follow-up also checked [Agent Skills authoring guidance](https://agentskills.io/skill-creation/best-practices)
and [evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills).
The revisions reduce unconditional reading, keep one evidence record and test
observable package/answer outcomes. The supplied-feedback procedure also reflects
the government guide's recommendation to learn from assessor feedback.

## Build versus adopt

Adopt established writing principles and the portable Agent Skills format. Build
only the missing combination: active company-file retrieval, claim traceability,
buyer-aligned narrative, strict-limit compression and private review receipts.
Use existing host search and document readers rather than building a separate
RAG service, web app or tender backend. This keeps installation small and avoids
copying confidential company knowledge into the public distribution.
