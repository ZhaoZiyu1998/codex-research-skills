---
name: research-code-cleanup
description: Simplify a research or paper artifact repository around the experiments, certificates, tables, figures, and reproducibility claims that remain in the current paper. Use when asked to clean a paper codebase, reduce Python file count or line count, merge fragmented experiment pipelines, remove dead experimental branches, factor shared utilities, simplify over-defensive research code, or document which experiment each file runs.
---

# Research Code Cleanup

Reduce the repository to a clear, reproducible implementation of the current
paper. Optimize for traceability and readable research code, not minimum line
count and not a general-purpose framework.

## Preserve the scientific contract

Before changing code, identify what the current paper actually claims. Keep
code that has at least one concrete responsibility:

- runs a current paper experiment or population;
- implements a method or certificate used by those experiments;
- produces a current table or figure;
- aggregates canonical results needed to reproduce a claim;
- preserves an expensive checkpoint or result needed for reuse;
- tests a soundness-critical invariant or a current experiment path.

Do not preserve code merely because it might become useful later. Do not
delete a soundness check, directed-rounding step, denominator guard,
transactional fail-closed decision, seed control, or provenance field required
by the paper.

## Work in two phases

Always finish inter-file cleanup before intra-file cleanup. If the user asks to
review the phases separately, stop after the inter-file report and wait for
confirmation. Otherwise continue after recording the phase boundary.

### Phase 1: Inter-file cleanup

1. Inspect repository instructions, `git status`, the paper, README, and the
   current experiment entry points. Preserve unrelated user changes.
2. Build an inventory with five classes:
   - paper experiment drivers;
   - shared certificate or method modules;
   - genuinely shared utilities;
   - focused tests;
   - unsupported, duplicated, obsolete, or one-off code.
3. Map every retained experiment to its paper claim, table, figure, input,
   output, and command. Treat this map as the source of truth.
4. Trace each experiment's complete call chain with `rg`: driver, helper,
   aggregation, plot, and imported certificate code. Do not infer use from a
   filename alone.
5. Give each paper experiment one discoverable top-level Python driver. Keep
   its run, aggregation, and plotting logic in that module unless the same
   logic is genuinely used by at least two current experiments.
6. Inline single-use wrappers and merge experiment-specific helper files into
   their driver. Remove duplicate CLIs, duplicate aggregation scripts, stale
   figure generators, abandoned variants, internal audit pipelines, and old
   smoke drivers that support no current claim.
7. Factor common code only after the experiment drivers are visible. Move code
   into a utility module only when at least two current call paths use the same
   operation with the same semantics. Do not manufacture a base class,
   registry, plugin system, or configuration layer.
8. Keep certificate modules separate from experiment drivers when they
   implement reusable mathematical semantics. Consolidate duplicate
   implementations rather than copying certificate logic into each experiment.
9. Keep tests separate from experiment count. Compress redundant tests, but
   retain focused adversarial tests for soundness-critical boundaries.

Use total Python-file count as a fragmentation alarm. A healthy paper artifact
usually has roughly one experiment driver per paper experiment and no more
than about one additional Python file per experiment for shared method,
utility, and test responsibilities. This is a heuristic, not a reason to merge
unrelated mathematics into a giant file. Every file beyond it needs a concrete
paper-facing explanation.

Before material deletion, make or identify a recoverable git commit. Do not
delete expensive checkpoints, canonical result records, user data, or external
source snapshots unless the task explicitly includes them. Delete tracked dead
code rather than moving it into an archive folder.

### Inter-file gate

Report:

- the number of paper experiments;
- Python files and source lines before and after;
- the retained experiment-to-driver map;
- retained certificate, utility, and test modules with one-line duties;
- files merged or deleted and why;
- any remaining fragmentation that has a real reason.

Do not start broad function-level cleanup until this structure is stable.

### Phase 2: Intra-file cleanup

Process one Python file at a time, beginning with experiment drivers and then
shared certificate, utility, and test modules.

For each file:

1. State its single paper-facing responsibility and current callers.
2. Remove unreachable code, duplicate calculations, unused imports, unused
   outputs, stale branches, and helpers used once when inlining is clearer.
3. Reduce CLI arguments to choices the current experiment actually varies.
   Keep paper defaults visible in the command or driver rather than building a
   configuration framework.
4. Remove verbose progress logging, redundant JSON fields, per-step debug
   dumps, hashes, manifests, compatibility versions, caches, retries, and
   fallback paths unless a current paper artifact or realistic failure requires
   them.
5. Save only canonical per-run records, summaries used by the paper, and
   checkpoints expensive enough to justify reuse. Do not save the same fact in
   several formats.
6. Replace speculative validation with assertions for documented invariants.
   Let real errors fail visibly. Never convert certificate failure into default
   success.
7. Prefer direct NumPy/PyTorch/pandas code and plain functions. Create a helper
   only when it gives a meaningful name to reused logic or materially shortens
   the main path.
8. Preserve readable variable names and the connection to paper notation. Do
   not code-golf numerical proofs.

After each file, report lines removed, behavior retained, and validation run.
Then continue to the next file unless the user asked for confirmation at each
step.

## Validate scientifically

Run the narrowest relevant checks after every structural edit, then run the
paper-facing suite at phase completion.

- Re-run deterministic smoke cases for changed experiment call chains.
- Compare canonical summaries, table inputs, and figure inputs before and
  after when behavior should be unchanged.
- Use adversarial tests at certificate boundaries: just inside/outside the
  tolerance, failed positive denominators, nonfinite bounds, dtype changes,
  and states that must remain inconclusive.
- Check that no nonconforming output becomes released and that failed
  verification remains fail-closed.
- For timing code, first check for competing jobs and keep setup, update,
  verification, and serialization boundaries explicit.
- Do not rerun expensive experiments merely to prove a mechanical refactor.
  Use existing checkpoints and canonical records when they are sufficient.

If a cleanup changes scientific outputs, stop treating it as cleanup. Diagnose
the difference and report it before proceeding.

## Maintain the README

Keep one concise experiment map containing:

- experiment name and paper purpose;
- primary driver;
- exact run command;
- required environment and inputs;
- canonical outputs;
- table or figure consuming those outputs.

Describe public reproduction, not internal debugging history, failed attempts,
or audit chronology.

## Final report

Lead with the resulting repository shape. Give:

- experiment count;
- Python file and line counts, with before/after deltas;
- experiment, certificate, utility, and test breakdown;
- deleted or consolidated modules;
- tests and artifact comparisons that passed;
- checkpoints or result records deliberately retained;
- any remaining file whose responsibility is not obvious.

Commit only the intended cleanup. Preserve unrelated and untracked user files.
