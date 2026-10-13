---
name: autoresearch-to-human-paper
description: Turn a paper produced by an automated or agent-driven research pipeline ("autoresearch") into one that reads as written by a careful human author for a top venue. Use when a LaTeX paper reads like a lab notebook or repository dump, when the user asks to make an AI-written paper read human, to revise a draft section by section against published papers, to remove AI tone, defensive hedging, number dumps or process narration, to rebuild the appendix, or to fit the body to a page limit. Works section by section, compares every section with 3-4 accepted papers in the same area, verifies every claim against the paper's own data, recompiles after each change, and pushes when asked.
---

# Autoresearch paper to human paper

Automated research pipelines produce papers with a recognizable shape:
registration jargon and branch names, process narration ("a follow-up
campaign fired"), number dumps that repeat the figures, defensive caveats on
every claim, results scattered between body and appendix, and an appendix
that retells the repository. The science may be sound. The writing is not
what a reviewer expects. This skill rewrites the paper section by section
until it reads like a paper by a careful human author, without changing any
result.

## Ground rules

1. **Never change data.** Every number, sign and disclosed negative result
   stays as recorded. Rewording may drop a number from prose, but the value
   must remain in a table, figure or appendix.
2. **Verify every sentence you write** against the source tables, appendix
   or data files. After each rewrite, reread the source and check scope:
   endpoint-to-endpoint trends are not monotone trends, "99%" is not "all",
   "most cells" is not "every cell". Wording drift is the most common error.
3. **Recompile after every change** and check: no undefined references or
   citations, the body ends on the last allowed page, nothing spills over.
4. **Work section by section with the user.** Before each section, show how
   the comparison papers write it, list the problems in the current text,
   propose a plan, and wait for approval unless the user said "改" or
   equivalent. Report in the user's language.
5. **Commit and push when the user asks**, with a message that says what
   changed and why. Fetch first. If the remote moved (e.g. Overleaf sync),
   inspect the incoming change and rebase rather than overwrite it.

## Step 0: Build the comparison set

Find 3-4 papers that are (a) the closest in topic and (b) accepted at top
venues (verify the venue on the official proceedings or OpenReview page, not
on aggregators). Download them into a folder outside the paper repository and
convert to text (`pdftotext`). For every section you revise, extract the same
section from each comparison paper and summarize how they write it before
proposing changes. The user will ask "看看别人怎么写的"; have the answer ready.

## Step 1: Section-by-section rewrite

### Abstract
- Background in one sentence, then the tension with current practice, then
  the thesis as one quotable sentence, then findings, then a practical
  takeaway.
- No result numbers and no model-size numbers. State results qualitatively.
- Past tense for measured results.

### Introduction
- Order: why it matters (with a citation), what current practice does and
  what goes wrong, what we isolate and the headline finding with Figure 1,
  a short experimental-design paragraph, then findings as bold claims each
  pointing to a section.
- State openly the result that reviewers would otherwise find and use
  against the paper (e.g. a simple baseline beats both studied variants),
  framed as part of the argument.
- No detailed numbers.

### Related work
- Labeled paragraphs. Closest work first, each with one sentence on how it
  differs. A paragraph that confronts contrary or adjacent evidence. Do not
  restate the introduction's thesis at the end.
- Check every cited paper for venue status and add the closest accepted
  papers that are missing.

### Method vs. experiments
- The method section defines the object of study, the estimand and the
  notation. Run conditions (models, data, budgets, grids, seeds, evaluation,
  tolerances, implementation differences) go in an experimental-setup
  subsection at the start of the experiments section, which groups setup
  and all result subsections together.

### Experiment subsections
Follow the `experiment-data-analysis` skill:
- One question per paragraph: why the experiment is needed, what is
  compared and held fixed, the result, what it supports, its scope.
- **Prose carries no numbers that a reader can read off a figure or table.**
  In the results prose keep at most one magnitude anchor for the whole
  section; move every other value to the appendix and describe it in words.
- Controls grouped by the threat each rules out, not narrated row by row.
- Every claim in the abstract or introduction needs a figure in the body,
  as the comparison papers do for robustness claims. Per-seed tables belong
  in the appendix.

### Captions
Say only what is plotted and how to read it: axes, sign convention, markers,
bands, which panel is which. No bold takeaway titles and no findings. The
analysis lives in the text.

### Discussion and conclusion
Present perfect for the summary, then practical recommendations with their
cost, then connections to the closest prior work, then one concrete next
measurement. The ACL-style Limitations section is mandatory but short:
three items stated as scope, each pointing to where the evidence is.

### Appendix
An appendix is supporting material, not a retelling of the repository. Use
the comparison papers' structure: derivations, implementation and training
details, then additional results for each body section in body order, then
surveys.
- Remove registration branch names, verdict labels, evidence-status and
  claim-to-registration tables, device-placement stories, follow-up and
  stop-rule narration, and "which is why the body..." closers.
- Keep one paragraph stating that protocols, grids, seeds and analysis
  scripts were fixed before each experiment, and that experiments were
  designed in sequence.
- Remove claims and side analyses that the body never uses, especially
  ones that carry self-invalidated statistics or internal contradictions.
- Keep, in plain words, every disclosure the body relies on (opposite-sign
  results, post-hoc extensions and their order, cohort disagreements,
  instability near the effect). Deleting these looks like concealment once
  the code is public.

## Step 2: Style rules (apply everywhere, including headings)

- No question sentences, and no headings that read as questions
  ("Why...", "What...").
- No defensive negations: rewrite "does not establish / cannot / not X /
  need not / never / no" as a positive statement of what the data show
  ("leaves open", "seed-inconsistent", "kept separate", "fell faster than").
  This includes the title and section titles.
- No "X, not Y" or "rather than" contrasts as paragraph closers.
- No semicolons or em/en dashes in prose.
- Past tense for procedures and measured results, present for definitions.
- No formulaic openers ("To test this, we...", "We first ask whether...")
  and no "therefore/thus" closers that restate the paragraph.
- No blocked vocabulary from the `humanizer` skill (robust, notably,
  crucial, leverage, underscore, highlight, reveal, yet as filler...).
- One name per quantity (e.g. "contrast", "crossing", "tokens per
  parameter"), used consistently.
- Every abbreviation and symbol defined at first use in reading order,
  including inside captions and table headers (NLL, LR, WSD, method
  acronyms, subscripts, plot labels).

## Step 3: Repetition

Compare with the comparison papers before cutting. Their core message
appears in the abstract, introduction, results and conclusion (often 5-10
times); that is intended. Remove only:
- a point repeated inside one section or one paragraph,
- body text that copies the appendix,
- the same recommendation twice within the conclusion,
- a sentence that restates the one before it.

## Step 4: Page budget

Top-venue papers fill the page limit exactly. Measure the last page after
every change (`pdftotext -layout` line numbers per column). To cut: move
per-seed tables and illustrative figures to the appendix, drop repeats. To
fill: add a body figure for any claim that only the appendix supports,
answer a likely reviewer question with existing appendix evidence, or make
the next-step paragraph concrete. Never fill with filler sentences.

## Step 5: Audits with subagents

Run audits as background agents and verify their output yourself:
- AI-tone audit, split into two halves of the paper plus the appendix,
  using the `humanizer` and `pre-submission-reviewer` rule files.
- Repetition audit across body, captions and appendix, with lines freed
  per fix.

Agents often reintroduce what the rules forbid (numbers from tables,
semicolons in rewrites, merged disclosures). Check every suggested rewrite
against Steps 1-3 and the data before applying it.

## Step 6: Bibliography

- Every cited key defined, no duplicates, BibTeX warnings zero.
- Venue of every preprint rechecked; replace arXiv with the published venue
  when one exists (verify on proceedings or OpenReview).
- Authors checked against arXiv metadata for new entries.
- Proper nouns protected with braces ({Shampoo}, {Kronecker}, {FineWeb}),
  with the colon outside the braces ({SOAP}: Title) so the word after it
  keeps its capital.
- Uniform fields across entries of the same venue.
- Read the rendered reference list, not only the .bib file.

## Mechanics

- LaTeX source mixes line breaks unpredictably and shells mangle
  backslashes. Make prose edits with `scripts/latex_replace.py`, which takes
  a JSON list of [old, new] pairs and matches across any whitespace, and
  write the JSON with a file-writing tool rather than a heredoc.
- Build in a scratch copy of the repository (`pdflatex`, `bibtex`,
  `pdflatex`, `pdflatex`) so the repository never receives build products.
- New figures: reuse the repository's style module, store the plotted
  values in a data file that names its source table, commit script, data
  and PDF together.
