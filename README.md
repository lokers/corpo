# Corpo Translator

![A manager says "I trust you. You own this." Then leaves, saying "Don't ask me. If it fails, it's yours."](header.jpeg)

"I trust you. You own this." → "Don't ask me. If it fails, it's yours."

Corpo says the quiet part out loud, and turns the rude reply back into something you could read in a meeting.

## For fun, not for the record

Corpo Translator rewrites tone for fun. It is not a professional translation, not advice, and not a promise that the result means what you think it means.

You are responsible for anything you copy, send, or publish. The authors and contributors are not responsible for translations made with this skill, including missed meaning, shifted tone, or what happens after you send it.

Do not use it for contracts, policies, medical, legal, financial, employment, or safety wording. If a sentence creates an obligation, write it yourself.

## What it does

It reads the register and flips it. Oily corpo becomes the rude motive. A rude line becomes gracious corporate prose. If you name a direction, that wins.

A mixed note with one clear voice is rewritten into the other voice. A roughly even mix, or a note that is already plain, gets a question instead of a rewrite.

The joke is the power move. A number may disappear when it is only there to dress the offer. It is never swapped for a different number.

## What it will not change

- A number or a date into a different number or date.
- A refusal into a yes.
- Plain text. It says so and asks which way you want.
- An even mix of both registers. It asks before it translates.
- Contracts, policies, terms, medical or clinical text, legal advice, and safety procedures. It declines.
- Anything that is not English.

## Install

One command for Cursor, Claude Code, Codex, and the other agents the [skills CLI](https://github.com/vercel-labs/skills) knows. It asks which ones:

```
npx skills add lokers/corpo --skill corpo
```

This machine, every project, no prompt:

```
npx skills add lokers/corpo --skill corpo -g -y
```

One agent:

```
npx skills add lokers/corpo --skill corpo -a cursor
npx skills add lokers/corpo --skill corpo -a claude-code
npx skills add lokers/corpo --skill corpo -a codex
```

Claude Code can also install it as a plugin. In a terminal:

```
claude plugin marketplace add lokers/corpo
claude plugin install corpo@corpo
```

Inside a Claude Code session, the same two steps are `/plugin marketplace add lokers/corpo` and `/plugin install corpo@corpo`. The skill then shows up as `corpo:corpo`.

Or copy `skills/corpo` yourself. The folder must be named `corpo` and must contain `SKILL.md`.

| Agent | This machine | This repo |
|---|---|---|
| Cursor | `~/.cursor/skills/corpo/` | `.cursor/skills/corpo/` |
| Cursor, also read | `~/.agents/skills/corpo/` | `.agents/skills/corpo/` |
| Claude Code | `~/.claude/skills/corpo/` | `.claude/skills/corpo/` |

Paths checked against the [Cursor skills docs](https://cursor.com/docs/skills), the [Claude Code skills docs](https://code.claude.com/docs/en/skills), and the [Claude Code plugin install docs](https://code.claude.com/docs/en/plugins/install).

Other agents: copy that same folder into the skills directory your agent uses for a folder that contains `SKILL.md`.

## Invoke

This skill does not restyle your writing on its own. Name it: `corpo`. After the Claude plugin install, the name is `corpo:corpo`.

Then say what you want, for example "translate this out of corporate jargon", "decode this Slack message", or "make this sound more professional".

## Add a glossary entry

Glossary lines are the literal sense. The joke is looser than the entry. Add a note only when the phrase has two common meanings.

```markdown
### Revisit later
- Corpo: circle back once we have a clearer picture
- Colloquial: I'll come back to this once I know more
```

## License

MIT. See [LICENSE](LICENSE).

---

Lukasz Gosławski [`@lokers`](https://github.com/lokers)
