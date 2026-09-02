# AI Mastery Roadmap — Sep 2026 → Dec 2027

**Goal:** MANGA-tier ML Engineer (GenAI specialization) offer, ≥50 LPA, by end of 2027.
**Commitment:** 6+ hrs/day. Daily briefing + debrief. Mastery gates on every topic. Everything from scratch before libraries.
**Target role:** MLE spine + GenAI specialization → Applied Scientist extension afterward.

---

## Phases

### Phase 0 — Arming Up (Weeks 1–2) — ⏳ IN PROGRESS (started 2026-09-02)
- [x] Workspace + git repo initialized, daily commit habit begins (11 commits day 1)
- [ ] Git from scratch — ch1 basics ✅ (zones, add/commit/log/diff/restore); branches/merge/graph pending (ch2)
- [x] GitHub account audit + keys (private acct, HTTPS+GCM on work network; SSH key generated, parked for VM/home)
- [ ] Linux VM wired up: SSH access ✅, nvidia-smi ✅; repo clone + two-machine workflow pending
- [ ] Linux daily-driver basics: filesystem, navigation, files, permissions, man pages
- [ ] Terminal fluency drills begin (daily, permanent)
- [x] Python + tooling verified (mean.py ran local); GPU verified: Tesla T4 16GB, CUDA 13.0
- [x] Anki installed, first deck created (10 cards), first review cleared
- [x] Employer IP/moonlighting clause check (user confirmed allowed — on record)
- [ ] GATE 0: environment + git + Linux basics exam

### Phase 1 — Bedrock (Months 1–3): Math foundations + Python core
- Math: arithmetic → algebra → functions → trig → precalculus → differential calculus
- Python: syntax, control flow, data structures, functions, comprehensions, files, errors, regex
- Daily: ~2h math, ~2.5h Python, ~1h Linux/git drills, ~0.5h Anki
- Gates per topic; monthly retention re-exams begin

### Phase 2 — The Engine (Months 3–6): DSA + Prob/Stats + Linear Algebra + SQL
- DSA daily forever: complexity from first principles → arrays → hashing → two pointers →
  stack/queue → linked lists → trees → heaps → graphs → backtracking → DP (~700+ problems by interview day)
- Probability from counting → distributions → CLT → hypothesis testing → Bayesian (all from scratch: mean, std, sampling, tests)
- Linear algebra: vectors → matrices → eigen → SVD (from scratch → then NumPy + vectorization internals)
- Information theory: entropy, cross-entropy, KL
- SQL from zero → joins → window functions → schema design → NoSQL concepts

### Phase 3 — The Craftsman (Months 6–8): SWE mastery + Classical ML from scratch
- Python OOP, modules/packages, typing, pytest, pdb/debugging, clean code, project structure, concurrency (GIL, asyncio)
- Software design craft: requirements → UML/C4 → design docs/ADRs → design patterns → API design (FastAPI)
- Classical ML derived + from scratch: linear/logistic regression, regularization, trees, ensembles,
  SVM, k-means, PCA, gradient descent variants → then scikit-learn
- Validation & metrics: CV variants, leakage, bias-variance, calibration, ROC/PR, ranking metrics (NDCG/MRR)
- Also: time-series forecasting, recommender systems, classical NLP (TF-IDF, naive Bayes), search/IR (BM25)
- Docker from zero. Optimization theory. Problem discovery & scoping skill begins.
- Brand track starts: GitHub quality repos, first posts, Kaggle begins

### Phase 4 — Deep Learning (Months 8–11)
- Perceptron → MLP → backprop derived on paper → own autograd engine + mini-framework → then PyTorch
- CNNs, RNN/LSTM, embeddings, init/norm/regularization — from scratch first
- Tabular, image, video, audio, GNNs (from scratch)
- Generative: VAEs, GANs, diffusion from scratch. Multimodal: CLIP, VLMs, Whisper. RL fundamentals: MDPs, policy gradients, PPO
- Paper implementations: AlexNet, ResNet, BatchNorm, Adam, Word2Vec, ...
- Training optimization: mixed precision, grad accumulation/clipping, distributed basics. CUDA programming begins.
- Parallel: CI/CD (GitHub Actions), Kubernetes fundamentals, FastAPI serving, distributed systems fundamentals

### Phase 5 — The LLM Era (Months 11–14)
- Historical line: n-grams → word2vec → seq2seq → attention → Transformer implemented line-by-line from the paper
- Own tokenizer (BPE), own embedding model, own GPT trained from scratch on the VM GPU
- Scaling laws, pretraining data engineering, synthetic data
- Fine-tuning: full, LoRA (math derived), QLoRA. RLHF/DPO/GRPO on RL foundations. Reasoning models.
- Inference optimization: quantization, distillation, pruning, KV cache, batching, vLLM, Ollama
- RAG from scratch (incl. HNSW from scratch) → vector DBs → then frameworks. Agents from scratch → LangGraph etc.
- LLM evals: harnesses, LLM-as-judge, RAG/agent evals, online A/B. AI security: prompt injection, red-teaming. Responsible AI.
- Azure: DevOps, AML, AI Foundry, real deployments. MLOps end-to-end: MLflow, DVC, Airflow, monitoring/drift.
- Real-world track: own curated dataset published on HF Hub; CAPSTONE — production-grade deployed measured GenAI system
- Open-source contribution push

### Phase 6 — The Gauntlet (Months 14–16)
- System design + ML system design + LLM system design frameworks
- DSA at interview intensity, timed mocks (I play the interviewer)
- Behavioral story bank (STAR), resume/LinkedIn overhaul, referrals, warm-up interviews → target loops
- Negotiation training. AS-readiness extension after offers.

---

## Rules of Engagement
0. **First-principles teaching law:** every concept starts with intuition in plain language
   (physical/real-world analogy), then the formula is built element by element — every symbol
   named, every operation justified ("why divide? why square?") — then worked by hand on paper,
   and only then coded. Notation is never dropped on the learner unexplained.
1. **From-scratch law:** no library until its core is built by hand and gated.
2. **Mastery gates:** 3-tier exam (easy/med/hard), ≥80% incl. hard tier. Fail → remediate → new exam.
3. **Daily loop:** briefing (plan with definitions of done) → work → debrief (scorecard, honest assessment, tomorrow's seeds).
4. **Everything committed to git daily.** Sunday weekly retro.
5. **Sustainability:** 1 light day/week, 1 full rest day per 3 weeks, sleep non-negotiable, buffer weeks per phase.
6. **Failure protocol:** miss a day → resume, no spiral. Miss 3+ → re-plan week. Fail gate twice → diagnose method.
7. **Monthly retention re-exams** of all past material.
8. **IP hygiene:** nothing from employer work in public artifacts.

## Infrastructure
- Authoring: this folder (Windows), git repo
- Compute: Linux VM, 16GB VRAM GPU — training, Docker, K8s, serving, CUDA
- Overflow: Colab/Kaggle free GPUs

## Progress Log
| Date | Milestone |
|------|-----------|
| 2026-09-02 | Program approved. Workspace created. Phase 0 begins. |
| 2026-09-02 | Day 1: 7/7 items. Repo live on private GitHub (HTTPS/GCM; corp firewall blocks SSH 22+443). T4 GPU verified. Bonus: Vol-02 ch1 (mean) — 6 paper exercises + first algebraic proof + mean.py from scratch (gated). Midnight quiz #1: 6.5/10 — re-drill: 1/n & pot translation, n·x̄ identity, add-dot sin. |
