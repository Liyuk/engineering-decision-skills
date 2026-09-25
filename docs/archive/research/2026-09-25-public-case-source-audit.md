# Public case source audit for five-skill demonstrations

- **Research date:** 2026-09-25
- **Purpose:** Check whether the first-party cases in `public-case-materials.md` support the facts and boundaries needed for a user-facing demonstration of the five skills, and identify a better source for retrospective learning.
- **Method:** Read the linked GitHub, GitLab, and Google publications directly. Treat them as evidence of what those organizations publicly reported, not as independent audits or universal prescriptions.

## Findings by case

### 1. `tech-planning`: GitHub gh-ost

**Source:** [gh-ost: GitHub’s online schema migration tool for MySQL](https://github.blog/news-insights/company-news/gh-ost-github-s-online-migration-tool-for-mysql/) (2016-08-01).

The existing case summary is substantially supported. GitHub says it performed schema changes multiple times daily and compares three approaches: replica migration, MySQL Online DDL, and schema migration tools. It describes replica migration's host, tracking, and delivery overhead; Online DDL's replication lag, inability to throttle or pause, and operational risks; and gh-ost's triggerless design, throttling, dynamic control, auditability, and replica testing (article sections “existing landscape,” “Pauseable,” “Dynamically controllable,” “Auditable,” and “Trustable”).

**What a skill demonstration may reasonably conclude:** The public case supports assessing a migration plan against workload impact, operability, throttling/pause controls, topology, verification, and operational ownership. It supports a conditional recommendation to test options against the user's own workload and constraints.

**Claim limits:** It is a 2016 vendor-authored account of GitHub’s motivations and tool behavior. It is not a current benchmark of all migration tools, an independent comparison, or evidence that gh-ost is best for a different user's database. The report should label GitHub's historical account as sourced context and leave local table size, write rate, lag tolerance, rollback needs, staff, version, and measured performance unknown unless supplied.

### 2. `metric-decision`: GitLab MR Rate

**Source:** [How we measure engineering productivity at GitLab](https://about.gitlab.com/blog/measuring-engineering-productivity-at-gitlab/) (2020-08-27; republished 2020-09-02).

The existing case summary is supported. The article defines MR Rate as team MRs in a month divided by team members employed during that month. It describes mislabeled data and team differences in community contribution; says a high rate can reflect quantity over quality; explains use of companion indicators; and explicitly says GitLab chose not to make MR Rate an individual metric or use it to measure individual underperformance.

**What a skill demonstration may reasonably conclude:** An aggregate rate alone does not establish an individual’s productivity or quality. Before setting targets, check the exact cohort and denominator, label/authorship rules, review and quality measures, team composition, and how collaboration is counted. A team can use a trend as a prompt to investigate.

**Claim limits:** This is GitLab’s own 2020 practice, not an externally validated productivity metric or a policy every organization should copy. The article later mentions managers using individual values for coaching; do not simplify that into a claim that GitLab never looks at individual MR counts. It says the metric is not used as an individual performance measure.

### 3. `tech-review`: GitHub automated MySQL schema migration

**Source:** [Automating MySQL schema migrations with GitHub Actions and more](https://github.blog/enterprise-software/automation/automating-mysql-schema-migrations-with-github-actions-and-more/) (2020-02-14; updated 2021-08-12).

The source supports evaluating an end-to-end production workflow. GitHub's account describes peer/schema review and database-infrastructure agreement before production deployment; selecting clusters and execution methods; checking whether another migration is already running; tracking long-running work and production impact; cleanup and follow-up; and friction from review queues, availability, and context-switching. Later sections describe schema-as-code and generated SQL analysis in CI.

**What a skill demonstration may reasonably conclude:** A proposal that only specifies “one approval, apply everywhere, exit code zero” leaves decision-relevant questions about blast radius, target selection, concurrent work, execution monitoring, pause/rollback or recovery, post-migration verification, and ownership. Findings should cite details in the proposal; the GitHub article is comparative context, not proof that every omitted control is mandatory.

**Claim limits:** GitHub describes its own workflow and automation effort, not a complete security review or formal specification. The article was updated in 2021 and should not be presented as current GitHub architecture. The synthetic proposal's missing controls are supplied by the evaluator; they must not be attributed to GitHub.

### 4. `eng-reporting`: Google satellite incident

**Source:** Google SRE Workbook, [Postmortem Practices for Incident Management](https://sre.google/workbook/postmortem-culture/), including “Postmortem: All Satellite Machines Sent to Diskerase” (incident 2014-08-11; postmortem published 2014-08-15; an earlier deliberately bad example is also shown).

The good postmortem supports the report case's factual ingredients: a turndown automation bug sent all satellite machines into disk erase; traffic moved to core; user-facing latency increased for nearly two days; some impact values were redacted; the monitoring data was unreliable and impact figures were estimated; exact revenue impact was unknown. The immediate mitigation and longer recovery are distinguished in the source.

**What a skill demonstration may reasonably conclude:** A concise executive update can distinguish confirmed event sequence from estimated impact, say what remains unknown, summarize mitigation, and identify a bounded follow-up decision. The source explicitly gives caveats that some names and values were fictionalized or replaced with placeholders.

**Claim limits:** Do not use the opening “bad postmortem” block as incident evidence: it is intentionally written as a bad example, including a blameful root-cause statement. Use the later full postmortem. The source does not support inventing exact loss, revenue, individual fault, or saying the mitigation prevented recurrence. This incident record is strong raw material for reporting, but its source purpose is incident learning.

### 5. `management-retro`: recommended case source

**Better source:** Google Cloud, [Postmortems at Loon: a guiding force for rapid development](https://cloud.google.com/blog/products/devops-sre/loon-sre-use-postmortems-to-launch-and-iterate) (2021-12-07).

This is a better source for the *purpose and scope* of a retrospective than the satellite incident alone. The article says Loon standardized postmortems across avionics, manufacturing, flight operations, software, and network teams as it moved from R&D toward commercial service. It describes postmortems as a feedback loop to rectify problems, identify safeguards and alerts, share knowledge across teams, and identify longer-term themes and blind spots. It also describes using incident records and anomaly tracking together, and adapting the postmortem format to cases needing further investigation.

**What it supports:** A retrospective can examine a completed event or body of work, learn from what went well and poorly, inspect cross-team/system interactions, and choose follow-up improvements. A bounded demonstration could present a supplied project/incident record and ask the skill to distinguish observed facts, interpretations, missing context, and a small next-cycle action.

**Claim limits:** This is a first-party narrative about Loon's operational postmortem practice, not a public archive of detailed project-period records. It does not establish that a generic quarterly management retrospective caused Loon's transition to commercial service. For a concrete `management-retro` run, use the existing synthetic cases in `skills/management-retro/evals/evals.json` (for example the 12-item project with two late-identified dependencies) or supply an incident record; use Loon as methodological context only. Do not relabel the satellite incident briefing as a management retrospective simply because both use the same source.

## Implication for a five-skill user-facing demo

The examples can show five distinct outputs, not one generic “engineering decision” report:

1. **Technical planning:** conditional option recommendation plus missing measurements and a decision gate.
2. **Technical review:** evidence-linked findings about a submitted plan, with impact and recommended action; do not invent a defect for every section.
3. **Metric decision:** definition/denominator audit and a calibrated conclusion about what the reported movement supports.
4. **Management retrospective:** bounded learning about completed work and a small next-cycle experiment, not a leadership status summary.
5. **Engineering reporting:** audience-matched summary that preserves fact, estimate, and unknown status and names the decision or next action.

The source cases are useful demonstrations of task fit and evidence handling. They do **not** establish comparative efficacy of the skills. A user-facing showcase should label the prompts as evaluator-authored scenarios, distinguish source facts from scenario-added facts, and avoid claiming that one run proves general effectiveness.

## Sources

- GitHub, [gh-ost: GitHub’s online schema migration tool for MySQL](https://github.blog/news-insights/company-news/gh-ost-github-s-online-migration-tool-for-mysql/), 2016-08-01.
- GitLab, [How we measure engineering productivity at GitLab](https://about.gitlab.com/blog/measuring-engineering-productivity-at-gitlab/), 2020-08-27 / 2020-09-02.
- GitHub, [Automating MySQL schema migrations with GitHub Actions and more](https://github.blog/enterprise-software/automation/automating-mysql-schema-migrations-with-github-actions-and-more/), 2020-02-14, updated 2021-08-12.
- Google SRE, [Postmortem Practices for Incident Management](https://sre.google/workbook/postmortem-culture/), including the satellite incident report.
- Google Cloud, [Postmortems at Loon: a guiding force for rapid development](https://cloud.google.com/blog/products/devops-sre/loon-sre-use-postmortems-to-launch-and-iterate), 2021-12-07.
