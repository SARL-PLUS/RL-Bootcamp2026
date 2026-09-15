# 3rd International RL Bootcamp 2026: Master Reference

> **This is the single source of truth** for all RL Bootcamp 2026 information.
> Local path: `Synced_Projects\Lectures_and_Talks\RL_bootcamp_2026\`
> Remote: https://github.com/SARL-PLUS/RL_bootcamp_2026

---

## 🌐 Event Overview
| Field | Detail |
|:------|:-------|
| **Name** | 3rd International Reinforcement Learning Bootcamp |
| **Dates** | September 16–18, 2026 |
| **Venue** | HS Agnes Muthspiel, Unipark Nonntal, Erzabt-Klotz-Straße 1, 5020 Salzburg |
| **Homepage** | https://sarl-plus.github.io/RL-Bootcamp2026/ |
| **Registration** | Free (86 confirmed participants, 3 waiting list, 93 total in Indico) |
| **Indico** | [Category](https://indico.cern.ch/category/21735/) / [Event](https://indico.cern.ch/event/1705983/) |

---

## 💻 Git Repositories

### 1. Master Project (this repo): Code, Tutorials, Planning, Docs
| | |
|:--|:--|
| **Remote** | https://github.com/SARL-PLUS/RL_bootcamp_2026 |
| **Local** | `Synced_Projects\Lectures_and_Talks\RL_bootcamp_2026\` |
| **Purpose** | Central hub: tutorial code, planning docs, budget, keynote tracking, meeting notes |
| **Key Folders** | `tutorial/`: hands-on session code · `docs/`: planning, funding, keynotes · `website/`: legacy landing page source |

### 2. Website: GitHub Pages Source
| | |
|:--|:--|
| **Remote** | https://github.com/SARL-PLUS/RL-Bootcamp2026 |
| **Local** | `Synced_Projects\Lectures_and_Talks\RL_bootcamp_2026\RL-Bootcamp2026-website\` |
| **Purpose** | Public-facing event website (served via GitHub Pages) |
| **Live URL** | https://sarl-plus.github.io/RL-Bootcamp2026/ |

### 3. Tutorial Code (separate branch)
| | |
|:--|:--|
| **Remote** | https://github.com/SARL-PLUS/RL_bootcamp_2026 (branch: `tutorial-code`) |
| **Purpose** | Participant-facing Colab notebooks and environments |
| **Key Content** | Maze environment notebooks (Q-Learning, SARSA) in `/Tutorial Hands-On Session: Tabular RL & Discrete MDPs` |

---

## 📅 Canonical 3-Day Program Schedule (Aligned with Website)

### Day 1: Wednesday, September 16 (Foundations & Accelerator Physics)
| Time | Session | Details / Speakers |
| :--- | :--- | :--- |
| **11:00 – 12:00** | Arrival, Registration & Coffee | Welcome desk, badge pickup |
| **12:00 – 13:00** | Opening Lunch (ARGE Beisl) | Self-paid lunch |
| **13:00 – 13:15** | Opening and Introduction | Simon Hirländer & LOC |
| **13:15 – 14:00** | Lecture 1: Introduction to RL (No Math, No Panic) | Olga Mironova |
| **14:00 – 15:00** | Lecture 2: Reinforcement Learning Fundamentals | Simon Hirländer |
| **15:00 – 15:30** | Coffee Break | Foyer / Courtyard catering |
| **15:30 – 17:30** | Tutorial Hands-On: Tabular RL & Discrete MDPs | Léa Keller & Tutors (Colab Maze) |
| **17:30 – 18:15** | Keynote: Designing for Intelligence: Particle Accelerators in the AI Era | Dr. Verena Kain (CERN, remote) |
| **18:15 – 21:00** | Welcome Dinner (ARGE Beisl) | Self-paid social dinner |

### Day 2: Thursday, September 17 (Algorithms, Keynotes & Continuous Control)
| Time | Session | Details / Speakers |
| :--- | :--- | :--- |
| **09:00 – 09:45** | Lecture 3: Policy Gradients and Actor Critics | Thomas Gallien (JOANNEUM / AI Austria) |
| **09:45 – 10:30** | Keynote: What Should Models Model in Model-Based RL? | Prof. Michael Bowling (Univ. of Alberta / Amii) |
| **10:30 – 11:00** | Coffee Break | Foyer / Courtyard catering |
| **11:00 – 11:45** | Keynote: The benefits of satisficing in reinforcement learning | Prof. Ronald Ortner (MU Leoben) |
| **11:45 – 12:30** | Keynote: Learning Humanoid Robot Policies for Industrial Tasks | Prof. Elmar Rückert (MU Leoben) |
| **12:30 – 12:45** | Official Group Photo | Pia Fronia (Photographer) |
| **12:45 – 14:00** | Lunch (ARGE Beisl) | Self-paid lunch |
| **14:00 – 15:30** | Tutorial Hands-On 2: Continuous Control & The Reality Gap | MuJoCo Ant to Crippled Ant |
| **15:30 – 16:00** | Coffee Break | Foyer / Courtyard catering |
| **16:00 – 18:00** | Tutorial Hands-On 3: Custom MDP Design & Competition | Air Traffic Control Tournament |
| **19:00 – 21:00** | Official Conference Social Dinner (Dai Pai) | Asian street food, self-paid |

### Day 3: Friday, September 18 (Agentic AI, Closing & City Tour)
| Time | Session | Details / Speakers |
| :--- | :--- | :--- |
| **09:00 – 10:30** | Interactive Wrap-Up Tutorial: Findings & Expert Panel | Organizers & Keynote Panel |
| **10:30 – 11:00** | Coffee Break | Foyer / Courtyard catering |
| **11:00 – 12:00** | Lecture: Agentic AI in the Context of Reinforcement Learning | Marius-Constantin Dinu (ExtensityAI / AI Austria) |
| **12:00 – 13:00** | Tournament Final, Awards Ceremony & Closing Remarks | Awards Ceremony (Sutton & Barto textbooks) |
| **13:00 – 14:00** | Farewell Lunch (ARGE Beisl) | Self-paid lunch |
| **15:00 – 16:00** | Salzburg City Visit | Guided cultural walk |

---

## 📅 Workshop Projects & Environments

### Session 1: Tabular RL & Discrete MDPs
* **Environment:** Interactive `Maze` (Google Colab notebook)
* **Algorithms:** Q-Learning, SARSA
* **Files:** `Maze environment.ipynb` (starter) · `Maze solutions.ipynb` (solutions)
* **Branch:** `tutorial-code`

### Session 2: Continuous Control & The Reality Gap
* **Environment:** `MuJoCo Ant` → `Crippled Ant`
* **Goal:** Train continuous control policies, evaluate sim-to-sim transfer

### Session 3: Custom MDP Design & Competition
* **Environment:** `UMFlightEnv` (Air Traffic Control Tournament)
* **Goal:** Design reward functions, observation spaces, transition dynamics; group tournament

---

## 🎤 Confirmed Keynote Speakers
| Speaker | Affiliation | Topic |
|:--------|:------------|:------|
| Prof. Ronald Ortner | Montanuniversität Leoben | "Mathematical Foundations of RL & Satisficing" |
| Dr. Verena Kain | CERN | "RL for Real-Time Beam Steering & Accelerator Control" |
| Prof. Elmar Rückert | Montanuniversität Leoben (CPS) | "Theory & Humanoid Robot Training for Industrial Tasks" |
| Prof. Michael Bowling | University of Alberta / Amii | "Continual Learning, Game Theory & Model-Based RL" |

---

## 📍 Locations

### Venue & Transport
* **Lecture Hall:** HS Agnes Muthspiel, Unipark Nonntal, Erzabt-Klotz-Str. 1
* **Nearest Stop:** Justizgebäude (Obus Lines 3, 5, 10 from Hauptbahnhof/Airport)

### Meals & Social Events
| Event | Location | Address |
|:------|:---------|:--------|
| Lunches + Welcome Dinner (Sept 16) | **ARGE Beisl** | Ulrike-Gschwandtner-Str. 5 (adjacent to venue) |
| Social Dinner (Sept 17, 19:00) | **Dai Pai** | ~60 pax, decided 26.08.2026 (office@daipai.at) |

### Recommended Hotels
| Hotel | Address | Distance |
|:------|:--------|:---------|
| JUFA Hotel Salzburg City | Josef-Preis-Allee 18 | 5–10 min walk |
| Hotel Via Roma | Nonntaler Hauptstr. 47 | 5–10 min walk |
| Altstadthotel Kasererbräu | Kaigasse 33 | 10 min (Old Town) |
| Altstadthotel Weisse Taube | Kaigasse 9 | 10 min (Old Town) |
| Wyndham Grand Salzburg | Fanny-von-Lehnert-Str. 7 | Public transport |
| Hotel zum Hirschen | Elisabethstr. 5 | Public transport |
| MEININGER Hotel | Fürbergstr. 18-20 | Budget option |

---

## 📂 Other Local Folders (reference copies, not primary)
| Folder | Path | Purpose |
|:-------|:-----|:--------|
| Flyers & print materials | `Workshops_and_Schools\RL_Bootcamp_2026\` | PDFs of flyers |
| Shared lecture resources | `RL_Lectures_Master\07_Shared_Resources\RL_Bootcamp_2026\` | Cross-linked from RL lectures |
| Research-Projects website | `Research-Projects\Bootcamp\` | MathPhysSim/Bootcamp.git (legacy website) |
| Legacy tutorial (2024) | `RL_Bootcamp_Legacy\RL_bootcamp_tutorial-master\` | 1st bootcamp tutorial code |

---

## 📋 Key Planning Documents (in this repo)
* [Running Notes (Google Doc)](https://docs.google.com/document/d/1-ZOAOV1fCHykHFCYFKa3GLEFL_DuG3ewRYauKvb5DzA/edit?usp=sharing)
* [Meeting Notes 2026-06-08](./docs/RL_Bootcamp_2026_Meeting_Notes_2026-06-08.md)
* [Program Ground Truth (15.09.2026)](./docs/planning/Program_Ground_Truth_2026-09-15.md): Canonical 3-day schedule, speaker lineup & curriculum
* [Program Schedule (Historical 2026-06-08)](./docs/program_schedule_2026-06-08.md)
* [Keynote Communication Log](./docs/keynote_communication_log.md)
* [Keynote Contact List](./docs/keynote_contact_list_2026-06-08.md)
* [Helpers & Support Team](./docs/helpers_and_support_team_2026-06-08.md)
* [Budget Estimate](./docs/planning/budget_estimate.md)
* [Funding Strategy](./docs/planning/funding_strategy.md)
* [FFG Dissemination Docs](./docs/funding/ffg_dissemination/)
