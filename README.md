# 🧠 Prompt Engineering and Context Engineering for AI Agents

![Project overview and reading map](assets/readme-overview.svg)

🎨 [Shared architecture colors and diagram conventions](VISUAL_STYLE.md)

> **📚 Tutorial foundation:** This learning project is based on [Darsh Shah's freeCodeCamp tutorial](https://www.freecodecamp.org/news/how-to-use-prompt-engineering-and-context-engineering-for-ai-agents/). See [Tutorial Acknowledgment and Attribution](#tutorial-acknowledgment-and-attribution) for the original source and the repository's extensions.


![Project overview: baseline, prompt, and context input modes](docs/assets/project-overview.svg)

![Python](https://img.shields.io/badge/Python-Local-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-v1-166534)
![Ollama](https://img.shields.io/badge/Ollama-Local_Inference-334155)
![Model](https://img.shields.io/badge/Model-Qwen_3.5_4B-7C3AED)
![Format](https://img.shields.io/badge/Revised_Format-2_of_2-15803D)
![Boundary checks](https://img.shields.io/badge/Boundary_Cases-5_of_5-15803D)

The result badges summarize saved demonstration runs, not live CI status.

**🟦 Learn AI · 🟩 Portfolio evidence · 🟪 PhD research · 🟠 Planned work**

| 🟦 Learn AI | 🟩 Portfolio evidence | 🟪 Research connection |
| --- | --- | --- |
| Design instructions and select supporting context | Preserve original failures and revised outputs | Separate format compliance from evidence fidelity |
| Test system instruction boundaries | Publish readable logs and reproducible checks | Build toward evidence-grounded BRI evaluation |

> **📍 Current checkpoint:** adapted tutorial baseline complete. Both revised mode outputs passed the saved format checks; five instruction-boundary cases passed in one run. Broader grounding and BRI experiments remain planned.

<a id="explore-the-project"></a>

## 🧭 Explore the project

[🧩 Architecture](#architecture) · [🚀 Setup](#run-on-windows-powershell) · [🧪 Results & verification](#observed-results) · [🗂️ Evidence & guides](#evidence-files) · [🎨 Visual standard](VISUAL_STYLE.md)


A local learning project comparing how instructions and supporting evidence
affect responses from an Ollama-hosted language model.

Built with Python, LangChain, and qwen3.5:4b.

## 🟦 Base tutorial

The baseline compares three inputs to a local agent: a plain request, a revised prompt, and a prompt supplied with reference context. The article also includes a prompt-injection exercise. [Darsh Shah’s freeCodeCamp tutorial: How to Use Prompt Engineering and Context Engineering for AI Agents](https://www.freecodecamp.org/news/how-to-use-prompt-engineering-and-context-engineering-for-ai-agents/)

## 🧩 Extensions added in Project 4

| Extension | What this project added |
| --- | --- |
| **Cedar context and prompt revision** | Created a fictional Cedar reference and preserved original and revised outputs with timings. |
| **Automated format checks** | Checked the three-bullet and word-limit requirements on the captured outputs. |
| **Expanded instruction-boundary checks** | Added five cases with separate checks for output format and answer correctness. |
| **Visual evidence** | Added diagrams, result graphics, and an illustrated guide. |

See [observed results](#observed-results) and the [extension roadmap](#learning-and-extension-roadmap) for recorded and planned work.

<a id="experiments"></a>

## 🧪 Experiments

1. Baseline question with minimal instructions.
2. Prompt engineering with explicit output constraints.
3. Context engineering with a fictional Project Cedar reference.
4. Revised instructions after observed format failures.
5. A Yes/No instruction-boundary exercise with five test cases.

The agent has no tools attached. Reference text is supplied directly;
this project does not implement document retrieval.

<a id="observed-results"></a>

## 📊 Observed Results

![Original format failures and revised passes, with word counts](docs/assets/format-results.svg)

Word counts exclude bullet markers and use whitespace-separated words.

| Run | Mode | Words | Three bullets | Under 80 words |
| --- | --- | ---: | --- | --- |
| First | Prompt engineered | 42 | Fail | Pass |
| First | Context engineered | 37 | Fail | Pass |
| Second | Prompt engineered | 36 | Pass | Pass |
| Second | Context engineered | 42 | Pass | Pass |

The baseline produced 536 words in both runs. It had no length or
bullet-format requirement.

The instruction-boundary exercise passed format and expected-answer
checks for all five cases: two controls and three override attempts.

<a id="architecture"></a>

## 🧩 Architecture

```mermaid
flowchart TD
    Q["❓ Same question"] --> B["⚪ Baseline: question only"]
    Q --> P["🟦 Prompt: question + format rules"]
    P --> C["🟪 Context: also add Cedar reference"]
    B --> M["🤖 Same local Qwen model"]
    P --> M
    C --> M
    M --> L["📄 Save each response"]
    L --> V["🟩 Automatic format checks"]
    L --> R["🟠 Manual evidence review"]

    %% Shared architecture palette: see VISUAL_STYLE.md
    classDef default fill:#F8FAFC,stroke:#475569,color:#0F172A,stroke-width:2px;
    classDef process fill:#DBEAFE,stroke:#2563EB,color:#172554,stroke-width:2px;
    classDef model fill:#EDE9FE,stroke:#7C3AED,color:#3B0764,stroke-width:2px;
    classDef store fill:#CCFBF1,stroke:#0F766E,color:#134E4A,stroke-width:2px;
    classDef decision fill:#FEF3C7,stroke:#B45309,color:#78350F,stroke-width:2px;
    classDef human fill:#FFEDD5,stroke:#C2410C,color:#7C2D12,stroke-width:2px;
    classDef output fill:#DCFCE7,stroke:#15803D,color:#14532D,stroke-width:2px;
    classDef failure fill:#FEE2E2,stroke:#B91C1C,color:#7F1D1D,stroke-width:2px;
    class B default;
    class Q,P,L process;
    class C,M model;
    class R human;
    class V output;
```

Each experiment supplies a fresh user message list. No checkpointer, tools, or
retrieval pipeline is configured. The Cedar reference is manually supplied.

<a id="instruction-boundary-results"></a>

## 🛡️ Instruction-boundary results

![Five saved instruction-boundary cases, all passing](docs/assets/injection-results.svg)

Two controls and three override attempts passed in one recorded run.
The mixed request expects `No` under this exercise's explicit system policy.
This tests direct messages, not indirect injection through retrieved content.

<a id="format-success-and-evidence-fidelity-are-separate"></a>

## 📊 Format success and evidence fidelity are separate

| Observation | Status | Meaning |
| --- | --- | --- |
| Revised output uses three short bullet lines | 🟢 Automatically checked | Output structure meets the specified contract |
| Context answer states tests cannot guarantee zero defects | 🟣 Manually observed | Relevant limitation from the supplied reference appears |
| Cedar blocks on any failed test; answer says critical issues | 🟠 Fidelity issue | The response narrows the supplied release rule |
| Baseline makes an unsourced numerical cost claim | 🟠 Unsupported claim | Fluent output still needs evidence review |

[Read the illustrated guide for prompt anatomy, validation logic, and trust boundaries](docs/VISUAL_GUIDE.md).


<a id="run-on-windows-powershell"></a>

## 🚀 Run on Windows PowerShell

Install Ollama, start it, and make qwen3.5:4b available.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
ollama pull qwen3.5:4b

python .\prompt_context_agent.py
python .\validate_outputs.py
python .\prompt_injection_demo.py
```

The validator reads the included first-run.txt and second-run.txt logs.
It does not generate new model responses.

<a id="evidence-files"></a>

## 🗂️ Evidence Files

- [first-run.txt](first-run.txt): original responses.
- [second-run.txt](second-run.txt): responses after instruction refinement.
- [validation-results.txt](validation-results.txt): automated format checks.
- [prompt-injection-results.txt](prompt-injection-results.txt): instruction-boundary results.
- [Initial script](docs/baselines/prompt_context_agent_initial.py): original instructions.
- [prompt_context_agent.py](prompt_context_agent.py): revised instructions.

<a id="findings-and-limitations"></a>

## ⚠️ Findings and Limitations

More explicit instructions corrected the observed format failures.
The context response reflected the supplied coverage limitation.

Manual review also found limitations:

- The baseline made an unsourced numerical cost claim.
- The prompt-only answer overstated what passing tests establishes.
- The context answer narrowed Cedar's any-failed-test release rule
  to critical issues.
- Format checks do not establish correctness or grounding.
- Each prompt version was observed once per mode.
- Elapsed times include different output lengths and possible loading effects.
- Five instruction-boundary cases do not establish general injection resistance.
- No indirect injection through retrieved documents or tools was tested.
- Temperature zero does not guarantee reproducibility across environments.

Project Cedar is fictional demonstration context, not an operational
project measurement.

<a id="research-connection"></a>

## 🟪 Research Connection

This project motivates separate measures for instruction compliance,
evidence fidelity, and diagnosis quality in GenAI-assisted
Build, Release, and Integration Engineering.

It is a learning demonstration, not a completed thesis evaluation.

<a id="learning-and-extension-roadmap"></a>

## 🧭 Learning and extension roadmap

| Stage | Status | Deliverable |
| --- | --- | --- |
| 1. Three-mode local comparison | ✅ Recorded | Baseline, prompt, and supplied-context outputs |
| 2. Instruction refinement | ✅ Recorded | Original failures and revised format passes |
| 3. Automatic format validation | ✅ Recorded | Three bullet lines and word-limit checks |
| 4. Instruction-boundary exercise | ✅ Recorded | Five cases, separate format and answer checks |
| 5. Visual documentation | ✅ Included | Color diagrams, result graphics, evidence links, illustrated guide |
| 6. Structured run evidence | 🟠 Planned | JSON records with prompts, model identity, and settings |
| 7. Grounding evaluation | 🟠 Planned | Missing, irrelevant, and conflicting reference cases |
| 8. BRI adaptation | 🟠 Planned | Labeled build-log and release-evidence scenarios |

<a id="learning-sequence"></a>

### 🧭 Learning sequence

| Project | Connection |
| --- | --- |
| [1. Multi-Agent Study Guide](https://github.com/anne500/multi-agent-study-guide) | Coordinate roles and workflows |
| [2. Tool Calling and Memory](https://github.com/anne500/local-ai-agent-tool-memory) | Add tools and durable facts |
| [3. Agent Evaluation Harness](https://github.com/anne500/ai-agent-evaluation-harness) | Evaluate behavior and evaluator disagreements |
| **4. Prompt and Context Engineering** | Improve inputs and preserve evidence of outcomes |
| **5. Document RAG** | Next learning connection: retrieve supporting information |

<a id="tutorial-attribution"></a>

<a id="tutorial-acknowledgment-and-attribution"></a>

## 📚 Tutorial Acknowledgment and Attribution

We acknowledge **Darsh Shah** as the author of the foundational tutorial published by **freeCodeCamp**:

**[How to Use Prompt Engineering and Context Engineering for AI Agents](https://www.freecodecamp.org/news/how-to-use-prompt-engineering-and-context-engineering-for-ai-agents/)**  
Published: July 24, 2026.

| Credit and provenance | Description |
| --- | --- |
| 👨‍🏫 Original author | Darsh Shah |
| 📚 Publisher | freeCodeCamp |
| 🧱 Tutorial foundation | A local comparison of baseline, prompt-engineered, and context-engineered inputs, plus a prompt-injection exercise. |
| 🛠️ Repository adaptations and extensions | Fictional Cedar context, revised instructions, saved original and revised outputs, automated format checks, expanded boundary cases, timing, and visual evidence. |

The tutorial is credited for the original learning foundation. Repository-specific adaptations, experiments, verification records, and research connections are documented separately in the project documentation.


Adapted from Darsh Shah's freeCodeCamp tutorial:
[How to Use Prompt Engineering and Context Engineering for AI Agents](https://www.freecodecamp.org/news/how-to-use-prompt-engineering-and-context-engineering-for-ai-agents/).

Extensions include the fictional Cedar reference, timing, instruction
refinement, saved evidence, automated format validation, and expanded
instruction-boundary cases.

