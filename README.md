# Ciência dos Dados - Trabalho 1
Análises de dados para a matéria de Ciências de Dados na UFBA (2026.1)

- Primeira proposta: criação de visualizações estatísticas de **[Assunto a definir]**

## **Estrutura Geral**:

- **data**: arquivos brutos e tratados (CSV, JSON, xlsx)
- **src**: código fonte e seus módulos
- - **loader.py**: Limpeza e carregamento (Pandas)
- - **plotters.py**: Funções de plotagem (Matplotlib/Seaborn/Plotly)
- - **utils.py**: Helpers (formatadores de data, cores, etc.)
- **main.py**: Ponto de entrada (orquestração)
- **notebooks**: Pasta com Jupyter notebooks para Prototipagem e Análise Exploratória de Dados (EDA)

---
## **Pré-requisitos**:
- **Gdown** (Download Base Pública no Google Drive)
- **Pandas** (Tratamento de bases)
- **Matplotlib** (Plotagem de gráficos básica)
- **Seaborn** (Plotagem visual de gráficos)
- **Plotly** (Outra opção de plotagem visual de gráficos)

Para instalar as dependências, use o seguinte comando a partir da pasta raíz do projeto:
```
pip install -r requirements.txt
```

## **Schema dos dados usados**

### Identity (5 columns)
| Column | Type | Description |
|---|---|---|
| `model_name` | string | Canonical model display name (e.g., "Claude Opus 4.6 (Adaptive Reasoning, Max Effort)") |
| `model_slug` | string | URL-safe identifier used by Artificial Analysis |
| `provider` | string | Company or lab that created the model |
| `provider_slug` | string | URL-safe provider identifier |
| `aa_id` | string | Unique Artificial Analysis UUID |

### Intelligence Benchmarks (4 columns)
| Column | Type | Description |
|---|---|---|
| `aa_intelligence_index` | float | Artificial Analysis Intelligence Index v4.0 — composite of 10 evaluations including GPQA Diamond, Humanity's Last Exam, LiveCodeBench, SciCode, AIME, and others. Scale: 0–100. Higher is better. (98.5% fill) |
| `aa_coding_index` | float | Coding-specific benchmark composite. (78.6% fill) |
| `aa_math_index` | float | Math-specific benchmark composite. (59.2% fill) |
| `composite_benchmark` | float | Average of all available raw evaluation scores (see below), normalized to 0–100. (95.6% fill) |

### Raw Evaluation Scores (7 columns, scale 0.0–1.0)
| Column | Type | Description |
|---|---|---|
| `mmlu_pro` | float | MMLU-Pro score — professional-level knowledge |
| `gpqa_diamond` | float | GPQA Diamond — graduate-level science reasoning |
| `humanitys_last_exam` | float | Humanity's Last Exam — extremely difficult cross-discipline questions |
| `livecodebench` | float | LiveCodeBench — real-world competitive coding |
| `scicode` | float | SciCode — scientific code generation |
| `math_500` | float | MATH-500 — mathematical problem-solving |
| `aime_2025` | float | AIME 2025 — American Invitational Mathematics Examination |

### Pricing (4 columns)
| Column | Type | Description |
|---|---|---|
| `input_cost_usd_per_1m` | float | USD per 1 million input tokens. NaN = no pricing data available. |
| `output_cost_usd_per_1m` | float | USD per 1 million output tokens. |
| `blended_cost_usd_per_1m` | float | Blended cost assuming 3:1 input-to-output token ratio. $0.00 = genuinely free tier. NaN = no data. |
| `pricing_tier` | string | Categorical tier: Free ($0), Budget (<$0.50), Mid ($0.50–$5), Premium ($5–$30), Ultra (>$30), Unknown (no data) |

### Speed & Latency (3 columns)
| Column | Type | Description |
|---|---|---|
| `output_tokens_per_second` | float | Median generation speed (P50 over 72 hours). Measured in OpenAI-equivalent tokens. |
| `time_to_first_token_s` | float | Median latency to first token received, in seconds. |
| `time_to_first_answer_s` | float | Median time to first answer token (for reasoning models, this is after the thinking phase). |

### Human Preference (3 columns)
| Column | Type | Description |
|---|---|---|
| `chatbot_arena_elo` | float | LMArena (Chatbot Arena) ELO rating from 5.6M+ blind crowdsourced votes. (10.2% fill — only models present in both sources) |
| `arena_elo_ci95` | float | 95% confidence interval on the ELO rating. |
| `arena_votes` | float | Total number of Arena votes for this model. |

### Model Metadata (3 columns)
| Column | Type | Description |
|---|---|---|
| `parameter_count` | float | Billions of parameters (where publicly disclosed or extractable). (63.1% fill) |
| `release_year` | float | Year of public release (2023–2026). (64.5% fill) |
| `is_open_source` | bool | Whether model weights are publicly available (open-weight). |

### Derived Value Metrics (4 columns)
| Column | Type | Description |
|---|---|---|
| `intelligence_per_dollar` | float | `aa_intelligence_index ÷ blended_cost_usd_per_1m` — higher means more intelligence per dollar spent. Key value metric. |
| `price_performance_ratio` | float | `composite_benchmark ÷ log(blended_cost + 1)` — benchmark-weighted value score. |
| `elo_benchmark_blend` | float | `0.5 × normalized_ELO + 0.5 × normalized_intelligence_index` — blended human+machine ranking. |
| `speed_per_dollar` | float | `output_tokens_per_second ÷ blended_cost_usd_per_1m