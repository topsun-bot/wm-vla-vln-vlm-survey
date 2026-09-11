# CROSSWALK — World Model × VLM × VLA × VLN

Short survey points for a robotics / ODM stack. No fabricated citations.

## Definitions

- **World Model (WM)**: learned (often latent) dynamics that predict future states / observations / rewards conditioned on actions — used for imagination, planning, or policy training without always rolling the real env.
- **VLM (Vision-Language Model)**: multimodal foundation model mapping images/video ↔ language (caption, VQA, grounding). Perception + semantic interface; typically *not* an action policy by itself.
- **VLA (Vision-Language-Action)**: policy / foundation model that maps vision + language instructions → robot actions (often continuous control or action tokens). Examples in OSS: OpenVLA, Octo.
- **VLN (Vision-and-Language Navigation)**: agents that follow natural-language route instructions in visual environments (discrete graph or continuous Habitat-style). Examples: VLN-CE, NavGPT, MapGPT.
- **Intersection papers**: works that explicitly couple WM imagination with VLA/VLN, or use WM-style prediction inside language-conditioned control / nav (tagged `intersection` or multi-tagged in this pack).

## How they compose

- **Perception → latent**: VLM / vision encoder compresses RGB(D) into tokens or latents that a WM or policy consumes.
- **Latent dynamics**: WM predicts next latents (or pixels / occupancy / 3D) given actions — Dreamer-style RSSM, transformer WMs, diffusion/video WMs, JEPA predictors, occupancy WMs (e.g. OccWorld line).
- **Language grounding**: instructions or goals enter via VLM embeddings, LLM planners, or language-conditioned WM actions (e.g. Pandora-style language actions; LUMOS-style language-conditioned imitation + WM).
- **Action / navigation head**:
  - Manipulation → VLA policy (direct) *or* WM imagination + planner / actor-critic.
  - Navigation → VLN policy / LLM tool-calling over maps *or* WM-based predictive nav (e.g. X-MOBILITY-style).
- **Typical stack sketch**: sensors → VLM/encoder → (optional WM rollouts for what-if) → VLA/VLN policy or MPC → low-level controller.
- **Data path**: large trajectory corpora (Open X-Embodiment) train VLA; video/interaction data train WMs; VLN uses instruction-path datasets (R2R / RxR / VLN-CE).

## Open-source landscape gaps (from `oss_repos.md` honesty notes)

- **GAIA-1/2 (Wayve)**: official code/weights **not open**; community `lucidrains/gaia2-pytorch` is architecture WIP only.
- **Genie (DeepMind)**: official **not open**; open reproductions `flairox/jafar`, `p-doom/jasmine` approximate Genie-style tokenizer/LAM/dynamics.
- **UniSim**: interactive UniSim world-model code **not found open** (research page; `google/unisim` unrelated).
- **GameNGen**: **no verified official OSS**; closest interactive video-WM OSS in this survey: Oasis / DIAMOND.
- **What *is* open and useful**: DreamerV3 / DayDreamer, IRIS / DIAMOND / Oasis, NVIDIA Cosmos predict stacks, V-JEPA 2, 3D-VLA / RoboDreamer, OpenVLA / Octo / Open X-Embodiment, VLN-CE / NavGPT / MapGPT.
- Prefer verified LICENSE + recent commits; several useful repos still lack a LICENSE file (noted in OSS table).

## Practical integration notes (robotics / ODM)

- **Start with policy vs model**: if you need deployable language→action now → OpenVLA/Octo path; if you need imagination / offline sim / sample efficiency → DreamerV3 / Cosmos-predict / diffusion WM path.
- **Do not assume paper ≡ runnable stack**: Genie / GAIA / UniSim / GameNGen papers are landmarks, not drop-in deps — plan for reimplementation cost or closed APIs.
- **Latent vs pixel WM**: latent RSSM/JEPA is cheaper for control loops; pixel/video diffusion WMs are richer for visualization & data gen but heavier for onboard ODM.
- **3D / occupancy WMs** (OccWorld, Gaussian WM, 3D-VLA): better fit for mapping-heavy ODM than pure Atari-style video WMs.
- **Language interface**: keep VLM for grounding/instruction parsing; avoid stuffing full LLM into the 100 Hz loop — cache goals, run WM/VLA at mid rate, low-level tracking underneath.
- **Eval honesty**: report real-robot or continuous VLN-CE metrics separately from sim Atari/Minecraft WM scores; they do not transfer as numbers.
- **Licensing**: V-JEPA (original) was CC-BY-NC; V-JEPA 2 is MIT — check before commercial ODM use. MineRL is NC-SA.
- **Data**: Open X-Embodiment is the shared substrate for many VLAs; WMs often need action-conditioned video you may have to collect on-robot (DayDreamer lesson).
- **Safety**: WM imagination can propose physically invalid futures — gate with constraints / residual real-world fine-tuning before trusting open-loop rollouts.
- **ODM mapping tip**: treat WM occupancy / Gaussian predictions as *priors* for the map filter, not as ground truth; fuse with real sensors.

## Pack pointers

- Full paper table: `PAPERS.md` / `papers_merged.jsonl`
- Per-paper Chinese summaries: `PAPERS_DETAIL.md` / `papers_detailed.jsonl`
- Chinese companion: `CROSSWALK.zh.md` (this file stays English)
- OSS comparison: `oss_repos.md` / `oss_repos.jsonl`
- Forks under `topsun-bot`: `forks_created.md`
- Methodology & gaps: `README.md` (Chinese)
