# Codex research skills

Reusable Codex skills for research planning, technical-paper writing,
experimental analysis, figure design, and pre-submission review.

## Included skills

- `benchmark-paper-template`
- `experiment-data-analysis`
- `figure-designer`
- `humanizer`
- `idea-evaluator`
- `intro-drafter`
- `pre-submission-reviewer`
- `tech-paper-template`
- `vibe-research-workflow`

These are user-created skills. OpenAI system skills and plugin-provided skills
are not included.

## Install

Clone the repository and copy the skill directories into the Codex skill
directory.

```bash
git clone https://github.com/ZhaoZiyu1998/codex-research-skills.git
cd codex-research-skills
for skill in */SKILL.md; do
  directory=${skill%/SKILL.md}
  cp -a "$directory" ~/.codex/skills/
done
```

Restart Codex after installation.

Codex can also install the repository when asked:

```text
Install all skills from https://github.com/ZhaoZiyu1998/codex-research-skills
```

Each directory is self-contained. Copy the whole directory rather than only
`SKILL.md`, since some skills include references, scripts, interface metadata,
or license files.

## Updating

Pull the latest repository version and copy the directories again.

```bash
git pull
for skill in */SKILL.md; do
  directory=${skill%/SKILL.md}
  cp -a "$directory" ~/.codex/skills/
done
```

## Attribution

The `humanizer` skill adapts part of the AI-writing pattern taxonomy from
[`blader/humanizer`](https://github.com/blader/humanizer) by Siqi Chen, which
is distributed under the MIT License. The upstream license is preserved in
`humanizer/LICENSE.blader-humanizer`. See [NOTICE.md](NOTICE.md) for the full
statement.
