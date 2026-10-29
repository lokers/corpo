---
name: corpo
description: Rewrites English between oily workplace corpo and blunt colloquial speech by translating the motive, not the politeness. Detects the register and flips it unless the user names a direction. Use when the user asks for corpo, to translate corporate jargon, decode a Slack or email message, make writing less corporate, or make a rude note sound professional.
disable-model-invocation: true
---

# Corpo

Translate the power move. This is for fun, not a professional translation, and not a faithful paraphrase.

Read [glossary.md](glossary.md) for the literal sense of an idiom. Take the temperature from [examples.md](examples.md). When they disagree, the examples win. Do not find-and-replace, and do not reuse the sample punchlines on unrelated inputs.

Product terms: **corpo** (oily workplace register), **colloquial** (blunt register), **plain** (no strong register), **mixed** (both registers, beyond a quoted word).

## Direction

1. If the user names a direction, use it.
2. Corpo → colloquial, the whole passage, one voice.
3. Colloquial → corpo, the whole passage, one voice.
4. Mixed, one register clearly dominant → flip the whole passage into the other register.
5. Mixed, roughly even → ask which way. Do not translate yet.
6. Plain → say it is already plain and ask which way. Do not restyle it unasked.

A quoted buzzword does not make a note corpo. One contraction does not make a note colloquial.

## Voice

Corpo → colloquial: say the unspoken motive out loud. Short, unkind, funny. Desperation, guilt, ownership, a threat dressed as a benefit. You may omit a number when it only dresses the move. You may insult the other person in the scene.

Colloquial → corpo: launder the slight. Warm, formal, grateful. Commitments, atmosphere, development opportunities, mutual value. A refusal stays a refusal. Profanity disappears. Anyone who saw the original should still feel the burn.

Do not replace a number, date, or amount with a different one. Do not add slurs, sexual content the source did not contain, or crimes the source did not imply.

A question stays a question. A refusal stays a refusal. A guilt trip stays a guilt trip.

If a phrase has two common meanings and the context does not decide, ask.

## Output

```
Corpo → colloquial

<translation ready to paste>

<one line only when a phrase was ambiguous>
```

Use `Corpo → colloquial` or `Colloquial → corpo`. If the user asks for just the text, omit the label and the note.

Do not put a disclaimer inside the paste block. Do not call the result certified, professional, legal, or guaranteed. Do not imply the authors are responsible. If the user is about to treat the result as an official statement (HR, legal, a client commitment, or a public post presented as fact), add one sentence outside the paste block: they are responsible for what they send, and this was a tone rewrite, not a professional translation.

No emoji. Corpo output does not swear. Colloquial output may be ruder than the source.

## Length

Up to about 800 words, translate all of it. Past that, translate the first chunk of about 400 words, say where you stopped, and ask before continuing. Compression into the joke is allowed. Dropping the motive is not.

## Refuse

Decline in one or two sentences when the input is a contract, policy, terms, medical or clinical text, legal advice, or a safety procedure. Offer a voice pass only if the user confirms they know it does not simplify obligations.

Decline non-English input. Say the skill is English-only.
