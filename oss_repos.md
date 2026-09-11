# Open-Source World-Model / VLA / VLN Repository Comparison

Survey date: **2026-09-11**. Every URL below was verified via GitHub page fetch and/or LICENSE/commits.atom; all 31 URLs returned HTTP 200.
**Verified count: 31**.

Stars are approximate snapshots from GitHub pages at survey time. Licenses from LICENSE files when present; otherwise marked not stated.

## Comparison table

| name | org | url | license | stars (approx) | primary modality | last activity hint | related papers (arxiv) | notes |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- |
| dreamerv3 | danijar | https://github.com/danijar/dreamerv3 | MIT | 3767 | latent/video (RSSM categorical latents from pixels) | last commit 2026-05-25 | 2301.04104 | World-model RL (DreamerV3): learn RSSM world model + actor-critic in imagination. Actively maintained JAX reimplementation. |
| dreamerv2 | danijar | https://github.com/danijar/dreamerv2 | MIT | 1056 | latent/video (discrete latents) | last commit 2022-05-04 (mature/stable) | 2010.02193 | World-model RL (DreamerV2): discrete RSSM; Atari with world-model imagination. Predecessor to V3. |
| dreamer | danijar | https://github.com/danijar/dreamer | MIT | 624 | latent/video | last commit 2021-05-03 (historical) | 1912.01603 | Original Dreamer: latent imagination for continuous control. Foundational world-model agent. |
| daydreamer | danijar | https://github.com/danijar/daydreamer | not stated (no LICENSE file found) | 459 | latent/video + proprioception (real robots) | last commit 2022-12-19 (initial release era) | 2206.14176 | World models for physical robot learning (A1/xArm/UR5); Dreamer-style actor-learner on real hardware without sim. |
| iris | eloialonso | https://github.com/eloialonso/iris | GPL-3.0 | 899 | video tokens + Transformer dynamics | last commit 2024-10-14 | 2209.00588 | Transformer world model (discrete autoencoder + autoregressive Transformer) for sample-efficient Atari RL (IRIS). |
| diamond | eloialonso | https://github.com/eloialonso/diamond | MIT | 2104 | video (diffusion world model) | last commit 2024-12-06; CSGO branch | 2405.12399 | DIAMOND: diffusion-as-world-model; RL agent trained in diffusion imagination (Atari + CSGO demo). |
| open-oasis | etched-ai | https://github.com/etched-ai/open-oasis | MIT | 2131 | video (action-conditional DiT) | last commit 2024-11-08 | — | Oasis 500M inference: interactive Minecraft-like world model (Decart/Etched). Weights on HF Etched/oasis-500m. Blog post oasis-model.github.io (no arXiv id found). |
| STORM | weipu-zhang | https://github.com/weipu-zhang/STORM | not stated (no LICENSE file found) | 143 | latent/video (Transformer WM) | last commit 2026-03-18 (readme update; code marked lightly maintained) | 2310.09615 | STORM: Stochastic Transformer-based World Models for RL (NeurIPS 2023). |
| twm | jrobine | https://github.com/jrobine/twm | MIT | 91 | latent/video (Transformer WM) | last commit 2023-04-04 | 2303.07109 | TWM: Transformer-based World Models (ICLR 2023; arXiv:2303.07109). Related to transformer-WM line alongside IRIS/STORM. |
| TWISTER | burchim | https://github.com/burchim/TWISTER | Apache-2.0 | 60 | latent (Transformer + contrastive CPC) | last commit 2025-03-09 | 2503.04416 | TWISTER (ICLR 2025): Transformer world models with action-conditioned Contrastive Predictive Coding. |
| jafar | flairox | https://github.com/flairox/jafar | Apache-2.0 | 107 | video/latent (Genie-style tokenizer+LAM+dynamics) | last commit 2025-01-23 | 2402.15391 | Open Genie reimplementation in JAX (workshop paper Jafar). Not DeepMind official. |
| jasmine | p-doom | https://github.com/p-doom/jasmine | Apache-2.0 | 163 | video/latent (Genie-architecture WM) | last commit 2025-10-31 | 2402.15391 | Production-oriented JAX world-modeling stack implementing Genie-like tokenizer/LAM/dynamics (+ MaskGIT/diffusion/AR baselines). Evolved from jafar. |
| gaia2-pytorch | lucidrains | https://github.com/lucidrains/gaia2-pytorch | MIT | 63 | video (driving WM architecture) | last commit 2025-07-01 (WIP) | 2503.20523 | Community PyTorch reimplementation of Wayve GAIA-2 architecture. Official GAIA-1/2 weights/code from Wayve are NOT open. |
| cosmos | NVIDIA | https://github.com/NVIDIA/cosmos | OpenMDW-1.1 | 11800 | video/omnimodal world foundation models | last commit 2026-09-10 (very active) | — | NVIDIA Cosmos platform hub: world foundation models, datasets, tools for Physical AI. Meta-repo / entrypoint. |
| cosmos-predict1 | nvidia-cosmos | https://github.com/nvidia-cosmos/cosmos-predict1 | Apache-2.0 | 472 | video (world foundation model) | last commit 2026-06-07 | — | Cosmos-Predict1: general-purpose video world foundation models for Physical AI fine-tuning. |
| cosmos-predict2.5 | nvidia-cosmos | https://github.com/nvidia-cosmos/cosmos-predict2.5 | Apache-2.0 | 1366 | video (predictive WFM; action-conditioned robotics paths) | last commit 2026-06-08 | — | Cosmos-Predict2.5: latest predictive world foundation models; text/image/video conditioning; robot workflows. |
| jepa | facebookresearch | https://github.com/facebookresearch/jepa | CC-BY-NC-4.0 | 4133 | video (latent predictive JEPA) | last commit 2025-02-27 | 2404.08471 | V-JEPA: self-supervised video JEPA (predict in representation space). Non-commercial license. |
| vjepa2 | facebookresearch | https://github.com/facebookresearch/vjepa2 | MIT | 4600 | video (latent predictive; action-conditioned AC variant) | last commit 2026-03-23 | 2506.09985 | V-JEPA 2 (+ V-JEPA 2-AC): video world-model-like predictors enabling understanding/prediction/planning; MIT license. |
| 3D-VLA | UMass-Embodied-AGI | https://github.com/UMass-Embodied-AGI/3D-VLA | not stated (no LICENSE file found) | 635 | 3D + language + action (generative WM) | last commit 2024-10-29 | 2403.09631 | 3D-VLA (ICML 2024): 3D vision-language-action generative world model for embodied interaction. |
| robodreamer | UMass-Embodied-AGI | https://github.com/UMass-Embodied-AGI/robodreamer | not stated (no LICENSE file found) | 0 | video (compositional diffusion WM for robots) | last commit 2025-03-20; mirror rainbow979/robodreamer ~102★ last 2024-09 | 2404.12377 | RoboDreamer compositional video world model for robot imagination/planning. Public star count on org page showed 0; same README also on rainbow979/robodreamer (~102★). |
| embodied-generalist | embodied-generalist | https://github.com/embodied-generalist/embodied-generalist | MIT | 489 | 3D + language (embodied generalist) | last commit 2025-04-20 | 2311.12871 | LEO (ICML 2024): embodied generalist agent in 3D world (nav+manipulation); VLA-adjacent, not classic RSSM WM. |
| openvla | openvla | https://github.com/openvla/openvla | MIT | 6992 | vision + language + action (policy) | last commit 2025-03-23 | 2406.09246 | OpenVLA: open VLA policy trained on Open X-Embodiment. Policy stack (not a generative world model), closely related ecosystem. |
| octo | octo-models | https://github.com/octo-models/octo | MIT | 1771 | vision + language + action (transformer policy) | last commit 2024-07-31 | 2405.12213 | Octo: generalist robot policy on ~800k OXE trajectories; diffusion/transformer policy (not a world model). |
| open_x_embodiment | google-deepmind | https://github.com/google-deepmind/open_x_embodiment | Apache-2.0 | 2028 | robot trajectories (multi-embodiment dataset + RT-X refs) | last commit 2025-11-05 | 2310.08864 | Open X-Embodiment dataset + RT-X pointers. Foundation data for OpenVLA/Octo; not a world-model codebase. |
| VLN-CE | jacobkrantz | https://github.com/jacobkrantz/VLN-CE | MIT | 868 | vision + language (navigation, continuous Habitat) | last commit 2025-01-07 | 2004.02857 | VLN-CE baselines/env: Vision-and-Language Navigation in Continuous Environments (Habitat). VLN stack, not generative WM. |
| Recurrent-VLN-BERT | YicongHong | https://github.com/YicongHong/Recurrent-VLN-BERT | MIT | 209 | vision + language (navigation policy) | last commit 2022-06-11 | 2011.13922 | Recurrent VLN-BERT (CVPR 2021 Oral): transformer VLN agent. Classic VLN-BERT line. |
| MapGPT | chen-judge | https://github.com/chen-judge/MapGPT | not stated (no LICENSE file found) | 137 | vision + language (LLM map-guided VLN) | last commit 2025-05-03 | 2401.07314 | MapGPT (ACL 2024): map-guided prompting + adaptive path planning for VLN. |
| NavGPT | GengzeZhou | https://github.com/GengzeZhou/NavGPT | MIT | 350 | vision + language (LLM reasoning VLN) | last commit 2023-11-07 | 2305.16986 | NavGPT (AAAI 2024): explicit LLM reasoning for VLN. |
| MineDojo | MineDojo | https://github.com/MineDojo/MineDojo | MIT | 2255 | video/game + language (Minecraft embodied platform) | last commit 2023-08-29 | 2206.08853 | MineDojo: open-ended Minecraft embodied agent platform with internet-scale knowledge. Adjacent to WM research (DreamerV3 diamond challenge etc.). |
| Voyager | MineDojo | https://github.com/MineDojo/Voyager | MIT | 7193 | language (LLM agent) + Minecraft | last commit 2023-07-27 | 2305.16291 | Voyager: LLM-powered open-ended Minecraft agent (skill library/curriculum). Not a learned world model; adjacent embodied stack. |
| minerl | minerllabs | https://github.com/minerllabs/minerl | CC-BY-NC-SA-4.0 | 974 | video/game (Minecraft RL env + datasets) | last commit 2025-01-22 | — | MineRL: sample-efficient RL competition env/datasets in Minecraft. Common benchmark substrate for world-model agents; NC-SA license. |

## Family coverage notes

| Family | Status in this survey |
| --- | --- |
| Dreamer / DreamerV2 / DreamerV3 / DayDreamer | Included (danijar/*) |
| IRIS / Transformer WMs / DIAMOND / Oasis | Included (iris, STORM, twm, TWISTER, diamond, open-oasis) |
| GAIA-1/2 | Official Wayve code/weights **not open**; community `lucidrains/gaia2-pytorch` included |
| Genie | Official DeepMind Genie **not open**; open reproductions `flairox/jafar`, `p-doom/jasmine` included |
| UniSim | Interactive UniSim world-model code **not found open** (research page only; `google/unisim` is unrelated) |
| GameNGen | Google GameNGen **no verified official OSS** found; Oasis/DIAMOND cover GameNGen-like interactive video WMs |
| NVIDIA Cosmos | Included (`NVIDIA/cosmos`, cosmos-predict1, cosmos-predict2.5) |
| 3D-VLA / RoboDreamer / LEO / DayDreamer | Included |
| OpenVLA / Octo / Open X-Embodiment | Included (VLA/dataset stacks) |
| VLN-BERT / MapGPT / NavGPT / VLN-CE | Included (Recurrent-VLN-BERT + MapGPT + NavGPT + VLN-CE) |
| JEPA / V-JEPA | Included (`facebookresearch/jepa`, `vjepa2`) |
| MineRL / MineDojo / Voyager | Included (adjacent embodied platforms) |

## Exclusions (honest)

- **No invented repos.** Candidates that failed verification or are closed-source were omitted.
- **GAIA-1 official**, **Genie official**, **UniSim interactive simulator code**, **GameNGen official** were not found as open trainable/inference stacks with public weights/code matching the papers.
- Prefer actively maintained / well-known OSS; community WIP Genie servers (e.g. experimental opengenie stacks) omitted to keep the table focused.

## Machine-readable

See `oss_repos.jsonl` — one JSON object per repo with `verified: true`.
