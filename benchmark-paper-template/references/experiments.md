# Experiment & Insight Design

Design experiments that go beyond leaderboard numbers to reveal deep insights about model capabilities. In a Benchmark paper, the experiment section is NOT about "proving our method is best", it is about **revealing where and why models fail, and what this means for future research.**

## 1. Baseline Model Selection

Cover multiple axes for comprehensive comparison. Minimum 10-15 models:

| Axis | Categories | Purpose |
|------|-----------|---------|
| **Open vs. Closed** | GPT-4o, Claude, Gemini vs. LLaMA, Qwen, Mistral, DeepSeek | Capability gap between proprietary and accessible models |
| **Model Scale** | 7B → 13B → 70B → 100B+ | How capability scales with parameters |
| **Architecture** | Decoder-only vs. Encoder-Decoder; text-only vs. multimodal | Architecture-specific strengths/weaknesses |
| **Specialization** | General vs. domain-specific (code, math, vision, etc.) | Whether specialized training transfers |

Ask the user: "Which models will be evaluated? Do they cover all four axes above?"

## 2. Evaluation Protocol

### 2.1 Evaluation Settings

Define how models interact with the benchmark:

| Element | Key Questions | Guidance |
|---------|-------------|----------|
| **Input format** | How does the model receive input? What context is provided? | Specify prompt template, input structure, and any special formatting |
| **Output extraction** | How is model output parsed and scored? | Define extraction rules, parsing logic, and edge case handling |
| **Prompting strategies** | Zero-shot, Few-shot (1/3/5), CoT, Domain knowledge prompting, Tool-use | Test multiple; report which helps/hurts |
| **Evaluation method** | Auto metrics, LLM-as-Judge, Human eval | Use ≥2 methods; validate LLM-judge against human |
| **Metrics selection** | What metrics and why? (e.g., Accuracy, F1@K, MAE, Correlation) | Justify metric choices; prefer ONE headline metric for main ranking, with breakdowns as secondary |
| **Repetitions** | 1-5 runs per model | Report mean ± std for non-deterministic setups; report intra-model variance |
| **Temperature** | 0 for reproducibility, >0 for diversity analysis | Document the choice |

### 2.2 Human Baseline Experiment

If conducting human evaluation, specify:

| Element | Details |
|---------|---------|
| **Participant profile** | How many? Background/expertise? Recruitment criteria? |
| **Experiment protocol** | Task instructions, time limit, annotation interface |
| **Inter-rater reliability** | Agreement metric (Cohen's κ, Fleiss' κ, ICC) and threshold |
| **Comparison design** | Same samples evaluated by both humans and models |

### 2.3 Baseline Fairness

Document the optimization effort for each baseline equally. Reviewers are increasingly aware of "baseline nerfing", under-optimizing competitor hyperparameters. Each baseline should use the best known configuration.

## 3. RQ-driven Experiment Structure

Organize ALL experiments around your Research Questions. Each RQ drives one analysis subsection:

### RQ Analysis Template

For each RQ, specify:

```
RQ[N]: [The question]
├── Hypothesis: [What you expect to find]
├── Experiment: [Specific comparison or analysis]
├── Variables: [What you vary vs. control]
├── Metrics: [What you measure]
├── Visualization: [Figure or Table type]
└── Expected Finding: [What insight this yields]
```

### Common Analysis Types

| Analysis | What It Reveals | Visualization | Priority |
|----------|----------------|---------------|----------|
| **Overall Performance** | General capability landscape | Large table: all models × all metrics | MUST |
| **Category Breakdown** | Per-taxonomy performance | Grouped bar chart or heatmap | MUST |
| **Difficulty Gradient** | How performance degrades with difficulty | Line chart (x=difficulty, y=score) | MUST |
| **Error Taxonomy** | WHAT types of mistakes models make | Stacked bar chart, pie chart + error examples | HIGH |
| **Model Behavioral Bias** | Whether models have systematic tendencies (e.g., score inflation, over-conservatism, preference for certain answer types) | Distribution density curves, calibration plots | HIGH |
| **Human vs. Model** | Where AI matches/exceeds/falls behind | Radar chart or paired comparison bars | HIGH |
| **Prompting Impact** | How strategy affects performance | Ablation table (rows=models, cols=strategies) | MEDIUM |
| **Scale Effect** | How model size affects capability | Line chart (x=params, y=score) | MEDIUM |
| **Cross-dim Correlation** | Which capabilities are linked | Correlation heatmap | OPTIONAL |

## 4. The Overall Performance Table

The largest and most important table in the paper (typically Table 2 or 3):

```
| Model | Size | Overall | [Dim1] | [Dim2] | [Dim3] | [SubDim1.1] | [SubDim1.2] | ... |
|-------|------|---------|--------|--------|--------|-------------|-------------|-----|
| GPT-4o | - | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
| Claude | - | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
| LLaMA-70B | 70B | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
| ... | | | | | | | | |
| Human | - | XX.X | XX.X | XX.X | XX.X | XX.X | XX.X | |
```

Design guidelines:
- **Bold** the best result per column; **underline** second-best
- Group models by category (closed-source / open-source / specialized)
- Include human performance as upper bound (if applicable)
- Add average and worst-case rows if insightful

## 5. Evidence-led result interpretation

Use the `experiment-data-analysis` skill when raw results or tables are
available. Before writing a finding:

1. define the comparison unit and common evaluation subset;
2. check coverage, duplicates, aggregation axes, and missing cells;
3. report the direction and magnitude of the result;
4. inspect variation across models, datasets, tasks, and seeds;
5. name the important exception or boundary;
6. match the claim strength to the experimental design.

An experiment paragraph should answer one research question. State the
comparison, give the decisive values, and qualify the scope. Do not list every
cell or add a generic statement about importance.

Use numbered findings only when the paper's format benefits from them. A result
does not need to be surprising or framed as a future-research agenda to be
worth reporting. Negative and mixed results should remain visible.

Do not infer a mechanism from an uncontrolled comparison. Do not claim
statistical significance without a specified test. Do not call a result
consistent or robust without stating the datasets, tasks, perturbations, or
seeds over which that property was assessed.

## 6. Case Study Design

Include 2-4 case studies for qualitative depth:

| Type | Purpose | Format |
|------|---------|--------|
| **Success case** | Show benchmark discriminates capability | Strong model vs. weak model on same input |
| **Failure case** | Reveal specific model limitation | Model output + annotation of where/why it fails |
| **Surprising case** | Highlight counter-intuitive behavior | Setup expectation → show unexpected result |
| **Edge case** | Test capability boundary | Minimal change that flips correct → incorrect |

## 7. Companion Method Experiments (If Applicable)

If proposing a companion method (from bench-design):

- Comparison with baselines on the new benchmark
- Ablation study of method components
- Per-category improvement analysis (WHERE does the method help most?)
- Generalization test (does improvement transfer to other benchmarks?)
- **Downstream application validation** (can the benchmark/method be used to improve real-world performance? e.g., VisJudge-Bench validated through downstream visualization quality improvement)

## 8. Research Opportunities

Derive 3-5 future directions from your Findings. Typical directions:

- How to enhance model capability on [the gap area]
- Human-AI collaboration patterns for [the task]
- Benchmark extension (new modalities, languages, domains, difficulty levels)
- Training methodology improvements inspired by the findings
- Theoretical understanding of why [specific Finding] occurs
