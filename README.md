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

OpenAI system skills and plugin-provided skills are not included. This
collection combines one locally authored skill with skills adapted or copied
from two third-party projects. See [Sources and licenses](#sources-and-licenses)
before redistributing or modifying it.

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

## Sources and licenses

The repository uses multiple licenses.

- `experiment-data-analysis` is locally authored and distributed under the
  [MIT License](LICENSE.MIT).
- `benchmark-paper-template`, `figure-designer`, `idea-evaluator`,
  `intro-drafter`, `pre-submission-reviewer`, `tech-paper-template`, and
  `vibe-research-workflow` originate from
  [`HKUSTDial/Supervisor-Skills`](https://github.com/HKUSTDial/Supervisor-Skills).
  They remain under
  [CC BY-NC-SA 4.0](LICENSE.supervisor-skills), including the non-commercial
  and share-alike conditions. Some copies have been modified.
- `humanizer` adapts part of the AI-writing pattern taxonomy from
  [`blader/humanizer`](https://github.com/blader/humanizer) by Siqi Chen,
  which is distributed under the MIT License. The upstream license is
  preserved in `humanizer/LICENSE.blader-humanizer`.

See [NOTICE.md](NOTICE.md) for the detailed attribution and modification
statement. No attribution in this repository implies endorsement by an
upstream author.
