# Contributing

## Create Your Identity File

Your identity file is a Kotlin instantiation of the `ProperVillain` class. It lives at `villains/{your-handle}.kt`.

### Required Fields

- `handle` — your identifier, lowercase, matches filename
- `name` — what you go by
- `code` — your personal code, in your own words

### Optional Fields

- `location` — where you're based
- `headline` — how you'd describe yourself in one line
- `capabilities` — what you're good at, in plain language
- `skills` — specific tools, technologies, domains
- `experience` — where you've been (see `Experience` data class)
- `education` — if it matters to you

### The `decide()` Calls

After assembling your instance, call `decide()` for each rule you've determined doesn't apply. These are yours. Be specific. Be honest.

```kotlin
// Example
yourHandle.decide("Seniority determines who speaks")
yourHandle.decide("Credentials outweigh demonstrated competence")
```

### Format

Follow the structure in [`villains/jobe.kt`](villains/jobe.kt) as a reference. Keep it syntactically valid Kotlin.

## Submit

1. Fork this repo
2. Create `villains/{your-handle}.kt`
3. Open a pull request
4. Use the PR template — it asks you one question

## Guidelines

- One file per person. Your file, your rules.
- Don't edit anyone else's file.
- No minimum or maximum length. Say what you mean.
