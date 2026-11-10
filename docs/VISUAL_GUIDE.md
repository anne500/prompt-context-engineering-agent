# 📖 Visual Guide: Prompt and Context Engineering

[← Project README](../README.md)

**🟦 Instructions · 🟪 Supporting evidence · 🟩 Recorded checks · 🟠 Limits and planned work**

## 🧠 1. What changes between the three modes?

![Three input modes using the same local model](assets/project-overview.svg)

| Input component | ⚪ Baseline | 🟦 Prompt mode | 🟪 Context mode |
| --- | --- | --- | --- |
| Question about automated tests | ✅ | ✅ | ✅ |
| Format and beginner-audience instructions | — | ✅ | ✅ |
| Fictional Cedar reference | — | — | ✅ |
| Model and system prompt | Same | Same | Same |
| Tools or retrieval | None | None | None |

Prompt design is part of context design. This exercise isolates two changes:
adding output instructions, then adding a reference. It does not implement a
production context pipeline, memory, retrieval, or autonomous tool use.

## 🧩 2. Anatomy of the supplied context

```mermaid
flowchart TD
    S["🟦 System: software engineering helper"] --> I["📦 Invocation input"]
    Q["❓ Question: why use automated tests?"] --> I
    F["🟦 Rules: 3 lines, bullet prefix, under 80 words"] --> I
    R["🟪 Reference: fictional Cedar behavior"] --> I
    I --> M["🤖 Qwen 3.5 4B"]
    M --> A["💬 Generated answer"]
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#172554
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#3B0764
    classDef green fill:#DCFCE7,stroke:#15803D,color:#14532D
    class S,Q,F blue
    class R,I,M purple
    class A green
```

In the current code, question, format rules, and reference are concatenated into
one user message. Labels improve readability; they are not a security boundary.
The comparison script's system prompt contains no explicit policy for treating
malicious reference text. That scenario has not been evaluated here.

### 🟪 What the Cedar reference actually says

| Reference fact | What a faithful answer can say |
| --- | --- |
| Tests run when a pull request opens | Tests provide feedback during review |
| Regression tests check existing behavior | They help detect regressions in covered scenarios |
| A failed test blocks the release workflow until review | A failed test gates release pending review |
| Tests cover selected scenarios | Passing tests cannot prove there are no defects |

Cedar is fictional. These statements are authored demonstration inputs, not
findings about a live CI system.

## 🔧 3. Why refine the prompt?

| Version | Requested structure | Observed output |
| --- | --- | --- |
| Initial | Exactly three bullets, under 80 words, beginner audience | Both improved modes returned a paragraph |
| Revised | Exactly three lines, each starting with `- `; under 80 words; no surrounding text | Both improved modes returned compliant bullet lines |

![Saved format results](assets/format-results.svg)

Only the format instruction changed between these saved comparison runs.
The observed improvement motivates validation; it does not establish a general
prompt success rate. The baseline had no bullet or length requirement.

## 🚦 4. What does the validator check?

```mermaid
flowchart TD
    L["📄 Read saved log"] --> P{"Three completed sections?"}
    P -->|No| E["🔴 Stop with parse error"]
    P -->|Yes| B{"Baseline section?"}
    B -->|Yes| N["⚪ Report word count; format N/A"]
    B -->|No| C{"3 nonempty bullet lines AND under 80 words?"}
    C -->|Yes| Y["🟢 Format PASS"]
    C -->|No| F["🔴 Format FAIL"]
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#172554
    classDef green fill:#DCFCE7,stroke:#15803D,color:#14532D
    classDef red fill:#FEE2E2,stroke:#DC2626,color:#7F1D1D
    classDef amber fill:#FEF3C7,stroke:#B45309,color:#78350F
    class L,P,B,C blue
    class Y green
    class E,F red
    class N amber
```

Word counting splits on whitespace and excludes leading bullet markers.
Blank lines are ignored, so this check establishes three **nonempty** bullet
lines rather than exactly three physical lines. The checker does not score
audience suitability, factual accuracy, or faithfulness to reference evidence.
Missing log files are reported and skipped by the current implementation.

## 🛡️ 5. A separate instruction-boundary exercise

![Five-case boundary exercise](assets/injection-results.svg)

This separate script uses a stricter system prompt than the comparison script.
It requires `Yes` or `No` and specifies `No` for requests to override the rules.

```mermaid
flowchart TD
    S["🟦 System rule: Yes or No only"] --> M["🤖 Fresh agent invocation"]
    C["🧪 Control or override request"] --> M
    M --> O["💬 Raw response"]
    O --> F["🟩 Format: exactly Yes or No after trim"]
    O --> E["🟪 Answer: matches authored expectation"]
    F --> R["📋 Report separate counts"]
    E --> R
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#172554
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#3B0764
    classDef green fill:#DCFCE7,stroke:#15803D,color:#14532D
    classDef amber fill:#FEF3C7,stroke:#B45309,color:#78350F
    class S,C blue
    class M,E purple
    class F green
    class O,R amber
```

The mixed question expects `No` because it also requests an instruction override.
This label expresses this exercise's policy, rather than the answer to its
embedded Python question. Five passes do not prove protection against other
attacks. Retrieved-document injection and action authorization are not tested.

## 🔎 6. Format compliance is not evidence fidelity

| Dimension | Example from the saved output | Evaluation |
| --- | --- | --- |
| 🟩 Structure | Three bullet lines and fewer than 80 words | Automated format PASS |
| 🟪 Reference use | Context answer acknowledges tests cannot guarantee zero defects | Manual observation |
| 🟠 Fidelity | Reference gates on any failed test; answer gates on critical issues | Manual limitation |
| 🟠 Unsupported specificity | Baseline gives an unsourced numerical cost claim | Manual limitation |
| 🟠 Overstatement | Prompt-only answer says tests ensure existing features work correctly | Manual limitation |

Do not combine these into an overall accuracy score. No automated grounding
rubric or labeled factual-quality benchmark is implemented in this project.

## 🟪 7. Bridge to Build Release and Integration Engineering

| Learning exercise | Proposed BRI experiment | Evidence needed |
| --- | --- | --- |
| Minimal question | Diagnose a failure with little context | Labeled failure cases |
| Explicit instructions | Require diagnosis, supporting evidence, and uncertainty | Separate structural and semantic rubrics |
| Supplied Cedar reference | Supply identified build logs and test reports | Artifact IDs, commit identity, timestamps |
| Manual fidelity review | Check each diagnosis against source evidence | Human-reviewed expected findings |
| Direct override probes | Place hostile instructions inside supplied log text | Separate indirect-injection test set |

These are planned adaptations. No build-log experiment or thesis result is
claimed for this repository.

## 🗂️ 8. Inspect the evidence

| Evidence | File |
| --- | --- |
| Initial instructions | [Original script](baselines/prompt_context_agent_initial.py) |
| Revised instructions | [Current comparison script](../prompt_context_agent.py) |
| Original failures | [First run](../first-run.txt) |
| Revised passes | [Second run](../second-run.txt) |
| Recomputed format results | [Validation log](../validation-results.txt) |
| Five-case boundary results | [Injection exercise log](../prompt-injection-results.txt) |

🟦 Learn the mechanism. 🟩 Preserve what ran. 🟪 Define the research measure.
🟠 Keep untested extensions visibly marked as planned.
