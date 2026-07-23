---
name: experiment-data-analysis
description: Analyze experimental data for technical papers, audit result completeness and comparison fairness, derive claims supported by tables or per-run records, identify exceptions and sensitivity, and turn the analysis into precise experiment prose. Use when interpreting experiment logs, JSON or CSV results, tables, figures, ablations, sensitivity studies, baseline comparisons, or when checking whether a paper's experimental claims follow from its data.
---

# Experiment Data Analysis

## Purpose

Move from raw runs or tables to defensible paper claims. Treat data integrity,
comparison design, statistical interpretation, and prose as one chain. Never
write the conclusion first and search for supporting numbers afterward. Make
the author's choices visible instead of producing a fluent summary of rows.

## Workflow

### 1. Establish the comparison unit

Identify:

- the unit of one observation, such as a seed, dataset, task, fold, or query;
- the factors varied and held fixed;
- the metric direction and any chance or reference value;
- the expected and observed coverage for every method;
- whether values are raw runs, aggregates, or copied summaries.

Do not pool unlike units without an explicit aggregation rule. Report missing
cells as missing. Never treat a dash as zero or silently replace raw results
with a hard-coded aggregate.

### 2. Audit data integrity

Check unique run keys, duplicate records, seed counts, checkpoint identity,
metric definitions, aggregation axes, and `ddof`. Trace every reported number
to its source when files are available. Stop and flag the issue when two files
claim the same run key with different values.

### 3. Build fair comparisons

Compare methods on the same datasets, tasks, seeds, checkpoints, budgets, and
evaluation protocol whenever the claim is comparative. If coverage differs,
use the common subset or state the exact scope of each aggregate. Do not call a
method best because it was evaluated on an easier subset.

List all design differences before attributing a performance gap to one
component. A controlled ablation may support component-level attribution. An
uncontrolled comparison supports only an observed difference.

### 4. Read the result at four levels

For each research question, inspect:

1. **Direction:** which method or condition is higher or lower?
2. **Magnitude:** how large is the absolute and, when meaningful, relative
   difference?
3. **Variation:** how does the result vary across seeds, tasks, datasets, or
   models?
4. **Boundary:** where does the pattern weaken, reverse, or remain unknown?

Use uncertainty intervals or statistical tests only when their assumptions and
units are appropriate. Do not call a difference significant without a
specified test. Do not call a method stable from a small standard deviation
over an unspecified aggregation axis.

### 5. Assign the correct claim strength

- **Descriptive:** reports a measured value or ordering.
- **Comparative:** reports a difference under a matched protocol.
- **Associational:** states that two measured quantities vary together.
- **Mechanistic hypothesis:** offers a possible explanation and labels it as
  such.
- **Causal:** requires a controlled intervention that isolates the factor.
- **Generalization:** requires evidence across the populations named in the
  claim.

Downgrade the wording when the evidence does not reach the claimed level.

### 6. Select evidence, not table contents

Organize each subsection around one question. Select the few values that answer
that question, then mention the important exception or range. Do not narrate
every row. Use a table for exhaustive values and prose for the comparison that
matters.

A useful paragraph order is:

1. why the experiment is needed;
2. what is compared;
3. whether the prerequisite or control holds;
4. what is observed;
5. how it may be interpreted;
6. what it cannot establish.

Stop once the supported point is clear. Do not add a generic importance
sentence.

### 7. Run the claim audit

Before returning prose, verify:

- every number matches the supplied evidence;
- every use of “best,” “consistent,” “robust,” or “generalizes” has the stated
  scope needed to support it;
- no causal explanation comes from an uncontrolled comparison;
- ranges include the relevant minimum and maximum;
- tied rounded values are not presented as a strict ranking;
- custom metrics and arrows are explained;
- missing methods or cells are visible;
- conclusions do not depend on cherry-picked seeds or tasks;
- terminology remains fixed across the section.

## Output modes

Match the user's request:

- **Data audit:** coverage, provenance, duplicates, aggregation, and blockers.
- **Analysis:** research-question table with evidence, exceptions, and claim
  strength.
- **Paper prose:** concise LaTeX paragraphs grounded in the analysis.
- **Claim review:** quote each claim and mark it supported, overstated,
  ambiguous, or unsupported.
- **Full workflow:** return all four in that order.

When the user asks for a reusable prompt, read
[`references/general-prompt.md`](references/general-prompt.md) and adapt only
its input and output slots.

## Writing rules

Use past tense for experimental procedures and measured results unless the
venue convention differs. Prefer direct verbs and exact metric names. Avoid
hype, forced “Finding X” labels, method-by-method laundry lists, and synonyms
for established technical terms. Preserve necessary qualifications and
negative results.
