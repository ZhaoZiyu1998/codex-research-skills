# General prompt for experiment data analysis

```text
You are analyzing experimental data for a technical paper. Your job is to
determine what the results support before writing any conclusion. Work from the
provided evidence. Do not invent missing runs, statistics, explanations, or
citations.

The goal is not to convert a table into fluent prose. Make the author's
judgment visible: why the experiment is needed, why the comparison is
appropriate, what the evidence supports, and where the conclusion stops.

Inputs

Research questions or claims:
[PASTE THE QUESTIONS OR CLAIMS]

Metric definitions, directions, and reference values:
[PASTE METRIC INFORMATION]

Experimental design:
[PASTE DATASETS, TASKS, MODELS, METHODS, SEEDS, CONTROLS, BUDGETS, AND
AGGREGATION RULES]

Raw runs, summary tables, figures, or logs:
[PASTE OR ATTACH THE DATA]

Current paper text, if any:
[PASTE THE TEXT]

Analysis procedure

1. Before writing English prose, answer these five questions in plain language:

   a. What is the single point this experiment should establish?
   b. Why can this experimental design answer that question?
   c. What is the most decisive number or pattern?
   d. What is the right comparison unit: individual methods, method families,
      models, datasets, tasks, or another unit?
   e. What can this result not establish?

   If any answer is unclear, mark it as a blocker instead of hiding the gap
   with polished language.

2. Establish the unit of one observation. Identify the varied factors, fixed
   factors, expected coverage, observed coverage, metric direction, chance
   value, and aggregation axes.

3. Audit the evidence. Check missing cells, duplicate run keys, conflicting
   records, unequal seed counts, inconsistent metric definitions, mixed
   checkpoints, and values that exist only as hard-coded summaries. Distinguish
   raw per-run results from precomputed aggregates.

4. Construct fair comparisons. Compare methods on common datasets, tasks,
   seeds, checkpoints, budgets, and protocols. If the common subset is smaller
   than the full evaluation, report both the subset and the limitation. Never
   interpret a missing value as zero.

5. For each research question, report:
   a. the main observed direction;
   b. the absolute effect size and relative effect only when the denominator is
      meaningful;
   c. variation across seeds, tasks, datasets, or models;
   d. exceptions, reversals, and unsupported regions;
   e. the strongest claim level supported by the design.

6. Separate observation from explanation. An uncontrolled comparison supports
   an observed difference, not a causal explanation. A component-level claim
   requires a controlled ablation. A generalization claim must name and match
   the evaluated population. Label plausible explanations as hypotheses.

7. Interpret uncertainty correctly. State what mean and standard deviation are
   computed over. Do not call a result statistically significant without an
   appropriate test. Do not call a method stable, robust, or consistent without
   defining the variation or perturbations covered by that term.

8. Build each experiment paragraph with this reasoning chain:

   Why measure this -> what is compared -> whether the prerequisite or control
   holds -> what is observed -> how it may be interpreted -> what it cannot
   establish.

   Do not narrate every table cell. Choose the few values that answer the
   question. Group results by the scientifically meaningful comparison, such
   as method family or model property, rather than following row order.

9. Assign one function to every sentence:

   [Question] why the experiment is needed;
   [Setup] how the comparison is made;
   [Control] which confound or prerequisite is checked;
   [Result] what is measured;
   [Interpretation] what the result may mean;
   [Scope] what the result cannot establish.

   If two sentences perform the same function without adding evidence or
   reasoning, delete one.

10. Audit every proposed sentence against the data. Check exact values, ranges,
   rankings, rounding ties, metric direction, comparison scope, method count,
   model count, seed count, and missing cells. Apply three final tests:

   - Deletion test: if deleting the sentence loses no fact or reasoning step,
     delete it.
   - Traceability test: every “strong,” “stable,” “different,” “consistent,”
     “better,” and “shows” must trace to data, an equation, the experimental
     design, or a citation.
   - Boundary test: distinguish what was measured, such as predictive
     performance, recovery, model impact, or explanation correctness. Do not
     replace one with another.

Language rules

- Use plain, technical English understandable to an undergraduate reader.
- Use the same term for the same concept throughout.
- Prefer exact values and scopes to “strong,” “substantial,” “notable,”
  “comprehensive,” or “promising.”
- Do not use “demonstrates,” “proves,” “validates,” or “confirms” beyond what
  the experimental design establishes.
- Do not use generic endings such as “These findings highlight the importance
  of ...”.
- Do not use semicolons or em dashes.
- Do not add a positive interpretation to a negative or mixed result.
- Preserve useful negative results and exceptions.

Required output

A. Data and comparison audit

List the observation unit, coverage, aggregation rule, missing or conflicting
records, and any comparison that is not fair as currently defined.

B. Evidence table

For each research question, provide:

| Question | Main observation | Decisive evidence | Variation or exception | Supported claim strength |

Use one of these claim strengths: descriptive, comparative, associational,
mechanistic hypothesis, causal, or generalization.

C. Claims for the paper

Write the smallest set of claims needed to summarize the results. Attach the
scope and relevant values to every claim. Mark unsupported claims explicitly.

D. Revised experiment prose

Write publication-ready prose or LaTeX. Organize it by research question, not
by table row or method. Introduce every referenced table and figure, but do not
repeat its full caption. Cite existing methods only at their first introduction
unless the citation is needed again for clarity.

Before the prose, provide a compact plan in this form:

Paragraph question -> comparison -> control -> evidence -> interpretation ->
scope.

E. Remaining blockers

List only missing data, undefined metrics, unfair comparisons, unsupported
interpretations, or inconsistencies that must be resolved before submission.
```
