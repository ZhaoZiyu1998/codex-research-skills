---
name: humanizer
description: Humanize, de-AI, and tighten prose while preserving meaning and author voice. Use when the user asks to make text sound less like ChatGPT, remove AI-style filler, polish academic or technical prose, rewrite plainly, match a writing sample, audit a response for AI tells, or enforce direct anti-hype writing defaults.
---

# Humanizer

## Core Rule

Say the thing once, plainly, and stop. Preserve meaning, evidence, author voice, and necessary caveats. Cut significance inflation, ceremony, cadence padding, and reflexive praise.

This skill combines the local "Writing to avoid" rules with a condensed pattern audit adapted from the MIT-licensed `blader/humanizer` skill. Use it as a prose filter before returning or editing text. If the user gives a conflicting style requirement, follow the user and keep only the compatible parts.

## Modes

- Academic, technical, legal, reference, commit, PR, and review text: keep the voice neutral, plain, and exact. Do not add personality.
- Essays, blogs, personal notes, and informal writing: remove AI tells while preserving human irregularity, mixed feelings, rhythm, and concrete detail. Add voice only when the source or user asks for it.
- If the user provides a writing sample, match sentence length, register, paragraph starts, punctuation habits, transitions, and recurring phrasing from that sample. Do not upgrade casual wording into formal wording unless asked.

## Rewrite Workflow

1. Identify the claim, evidence, action, or decision in each sentence.
2. Remove words that only inflate importance, smooth cadence, or simulate confidence.
3. Replace indirect constructions with direct verbs and plain nouns.
4. Preserve specific details, hard-to-fake observations, uncertainty, and mixed feelings when they belong to the author.
5. Keep the same term for the same thing. Do not synonym-cycle in technical prose.
6. Shorten structure before polishing wording. If the answer should be two sentences, do not turn it into a report.
7. Run a final audit: would a hurried expert learn anything from this sentence beyond the plain facts? If not, cut it.

## Blocked Vocabulary

Avoid these words when they act as hype, filler, or generic emphasis. Allow them only for literal technical meaning, such as "robust estimator" in statistics.

Verbs: delve, underscore, showcase, unveil, leverage, harness, foster, bolster, elucidate, encompass, garner, spearhead, illuminate, streamline, revolutionize, necessitate, hinge on, align as filler, highlight as filler, surpass, spotlight.

Adjectives: pivotal, crucial, meticulous, comprehensive, robust, nuanced, intricate, commendable, noteworthy, invaluable, seamless, multifaceted, groundbreaking, innovative, compelling, profound, versatile, notable.

Adverbs: meticulously, notably, particularly, comprehensively, seamlessly, strategically, thoroughly, thoughtfully, undoubtedly, markedly, predominantly.

Nouns: realm, landscape, tapestry, testament, interplay, insights as filler, prowess, journey, milestone, wealth of, plethora.

Do not replace a blocked word with a fancier synonym. Rewrite so the inflation disappears.

## AI Pattern Audit

Scan for clusters of these patterns. Do not flatten a sentence only because it contains one watched word.

- Significance inflation: cut claims that an ordinary fact "marks a pivotal moment," "reflects a broader trend," "sets the stage," or "stands as a testament" unless the evidence proves that scale.
- Notability name-dropping: replace lists of media outlets, experts, or "coverage" with the specific sourced claim that matters.
- Superficial "-ing" tails: remove endings like "..., highlighting," "..., underscoring," "..., showcasing," "..., reflecting," and "..., paving the way." If the idea matters, write it as a real claim with evidence.
- Promotional language: remove brochure tone such as "nestled," "vibrant," "breathtaking," "must-visit," "groundbreaking," and "renowned" unless it is quoted or sourced.
- Vague attribution: replace "experts argue," "industry reports say," and "observers cite" with a named source, or state uncertainty.
- Formulaic challenge sections: avoid "Despite these challenges..." paragraphs that end in generic optimism. Use concrete constraints, dates, actors, and actions.
- Copula avoidance: prefer "is," "are," "has," and "uses" over "serves as," "stands as," "boasts," "features," and "represents" when the simple verb is accurate.
- Negative parallelism: rewrite "not only X but also Y" and "not just X, but Y" as the positive claim.
- Tailing negations: rewrite clipped endings such as "no guessing" or "no wasted motion" as real clauses.
- Rule of three: do not force rhythm with three items. Use the number of items the claim needs.
- Elegant variation: repeat the exact noun for the exact concept. Do not rotate "method," "approach," "framework," and "system" for style.
- False ranges: avoid "from X to Y" when X and Y are not a meaningful scale. List the topics directly.
- Passive voice and subjectless fragments: name the actor when it improves clarity. Keep passive voice only when the actor is unknown, irrelevant, or intentionally de-emphasized.
- Persuasive authority tropes: cut "the real question is," "at its core," "fundamentally," "the deeper issue," and similar fake-clarity openers.
- Signposting: remove "let's dive in," "here's what you need to know," "let's break this down," and other meta-announcements.
- Fragmented headers: delete one-line warmups that merely restate the heading.
- Diff-anchored writing: unless writing a changelog, describe what the thing does now, not what changed in the last edit.
- Manufactured punchlines: avoid stacks of short dramatic fragments. One short sentence can work; several in a row feel engineered.
- Aphorism formulas: replace "X is the Y of Z," "X becomes a trap," and "not a tool but a mirror" with the concrete claim.
- Fake-candid openers: remove standalone hooks such as "Honestly?", "Look," "Real talk," and "Here's the thing" when they only stage the answer.
- Chatbot artifacts: remove "I hope this helps," "Of course," "Certainly," "Want me to," "Let me know," and offer-to-continue closers unless the user explicitly asks for chatty correspondence.
- Knowledge-cutoff filler: remove "as of my last update," "while details are limited," and plausible gap-filling. Verify, say unknown, or cut.
- Generic positive conclusions: replace "the future looks bright" and "exciting times ahead" with the actual next step or fact.

## Formatting Defaults

- In technical, academic, and assistant output, avoid em dashes and en dashes. Use periods, commas, colons, parentheses, or sentence splits.
- Do not scatter horizontal rules between short sections.
- Use bold-colon list items sparingly. If every item is bold, none of it is emphasized.
- Do not add headers, bullets, and bold to a reply that should be plain prose.
- Avoid emoji in technical or scientific writing unless the user uses them first.
- Use sentence-case headings unless the user's venue or style guide requires title case.
- Avoid decorative bold, inline-header vertical lists, and format inflation.
- In code, Markdown, and technical files, prefer ASCII punctuation unless the file already uses another style or the content requires it.
- Hyphenate compound modifiers before a noun when needed for clarity; do not mechanically hyphenate predicate phrases such as "the report is high quality."

## Stance

- Do not open with automatic praise such as "Great question" or "You're absolutely right."
- Do not label directness with "Honestly," "To be candid," or "Let me be direct." Make the sentences direct.
- Make a default recommendation when the task asks for judgment. "It depends" is acceptable only when the dependency is named and a default is still given.
- Calibrate confidence to verification: use "verified by X," "untested but expected," or "unknown" when those are true.

## Technical Writing Rules

- Comments explain why, never restate what the code says.
- Commit and PR text explain intent and verification, not the diff line by line.
- In reference docs, repeat the exact same noun for the same concept.
- Reserve warnings, callouts, and bold for items that change the reader's action.
- For paper prose, preserve precise claims, scope limits, citations, variable names, method names, and statistical qualifiers. Remove only the wrapper words around them.
- For experiment prose, state the comparison scope and measured result before interpretation. Keep exceptions, and do not infer a mechanism from an uncontrolled comparison.
- For reviews, lead with the judgment or finding. Do not bury it under politeness scaffolding.

## False Positive Guard

Do not erase human texture by over-editing. Preserve:

- Specific, unusual, or hard-to-fabricate details.
- Mixed feelings, uncertainty, or tension when they are part of the author's point.
- First-person perspective in personal writing.
- Domain vocabulary that is precise, even if formal.
- Common transitions used sparingly.
- Quoted text, proper names, examples under discussion, and terms of art.

Look for clusters of AI tells. One em dash, one formal word, or one polished paragraph is not enough.

## Output Behavior

When editing user prose, return the revised prose first. Add notes only when they help the user reuse the pattern or when a meaningful claim changed. When drafting new prose, write in the requested format but keep structure proportional to the content.

For long or public-facing prose, silently run a second pass: "What still makes this sound obviously AI generated?" Fix those issues before returning. Do not show the draft-audit-final loop unless the user asks for it.

Upstream note: this skill adapts the pattern taxonomy of `github.com/blader/humanizer` by Siqi Chen, MIT licensed, and merges it with the local "Writing to avoid" rules.
