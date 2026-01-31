- [ ] merge donations and about us page in _includes
- [ ] allow TCPIndia draft in eleventy ignore 
# 🗳️ Mock EVM + VVPAT Simulator (Browser-based)

This project is a **browser-based simulation of an Electronic Voting Machine (EVM) with VVPAT**, built using **HTML, SVG, CSS, and Vanilla JavaScript**.

The goal is **not UI polish**, but to model **correct voting logic, state transitions, and VVPAT behavior** as realistically as possible.

---

## 🚀 Features

### ✅ EVM + Ballot Unit
- Two candidates (🍎 Apple, 🍌 Banana)
- Button press with LED feedback
- Vote locking to prevent rapid double voting

### ✅ VVPAT Slip Simulation
- Slip preview window
- Slip movement into storage slots
- SVG-based slip rendering (no canvas, no images)

---

## 🧠 Core Logic Design

This project is intentionally designed as a **state machine**, not a simple animation demo.

### 🔹 Phase 1 – Movement (Completed)
- Slips move **only** when finalized
- Preview position is explicit
- Storage positions are fixed
- No time-based movement hacks

### 🔹 Phase 2 – Visibility (Completed)
Slip visibility depends on **two independent light sources**:

| Condition | Visible Slips |
|---------|--------------|
Lid open | All slips |
Lid closed + artificial light (≤7s) | Preview slip only |
Lid closed + no light | No slips |

> Artificial light lasts **7 seconds after a vote**

---

### 🔹 Phase 3 – Voting Logic (Completed)
- Only **one preview slip** exists at any time
- Votes are grouped into **runs**
- Repeated votes trigger special behavior
- Winner emission happens **once per run**
- Explicit run reset prevents phantom slips

---

## 🏆 Winner Logic (Experimental)

- A fixed `winner` symbol (currently 🍌) is used for testing
- On the **second same vote in a run**, the winner is emitted
- Further identical votes start a **new run**

This logic is intentionally explicit to explore edge cases.

---

## 🛑 Voting Limit

- Maximum **4 finalized votes**
- After 4 votes:
  - Voting is locked
  - Voters are alerted
  - Results can be viewed by opening the lid

---

## 🧩 Important State Variables

```js
previewSlip           // unresolved slip at preview
voteLog               // finalized slips only
lastVoteSymbol        // tracks vote runs
winnerEmittedForRun   // prevents duplicate winner slips
artificialLightOn     // 7-second VVPAT light
vvpatOpen             // lid state (natural light)

⚠️ Preview slips are never stored in voteLog

Perfect 👍
Here is a GitHub-ready README.md, tailored specifically for GitHub Pages hosting and public viewing.
You can copy–paste this directly into README.md.
Copy code
Md
# 🗳️ Mock EVM + VVPAT Simulator

A **browser-based simulation of an Electronic Voting Machine (EVM) with VVPAT**, built using **HTML, SVG, CSS, and Vanilla JavaScript**.

🔗 **Live Demo (GitHub Pages):**  
➡️ https://<your-username>.github.io/<your-repo-name>/

> This project focuses on **correct logic, state transitions, and VVPAT behavior**, not UI polish.

---

## 📸 Preview

Open the live demo and:
- Cast votes using the Ballot Unit
- Watch slips appear in the VVPAT preview
- Toggle the lid to inspect stored slips
- Observe correct behavior after voting ends

---

## 🚀 Features

### ✅ Ballot Unit
- Two candidates (🍎 Apple, 🍌 Banana)
- Button press animation
- LED feedback
- Vote lock to prevent rapid re-votes

### ✅ VVPAT Slip Simulation
- SVG-based slips (no images, no canvas)
- Preview window


- Slip storage slots
- Smooth animated movement

---

## 🧠 Architecture Overview

This project is designed as a **finite-state system**, not a simple animation demo.

---

## 🔹 Phase 1 — Movement (Completed)
- Slips move **only** when finalized
- Preview position is explicit
- Storage positions are fixed
- No time-based movement hacks

---

## 🔹 Phase 2 — Visibility (Completed)

Slip visibility depends on **two light sources**:

| Condition | Visible Slips |
|--------|---------------|
Lid open | All slips |
Lid closed + artificial light (≤7s) | Preview slip only |
Lid closed + no light | No slips |

> Artificial light stays ON for **7 seconds after each vote**

---

## 🔹 Phase 3 — Voting Logic (Completed)

- Only **one preview slip** exists at any time
- Votes are grouped into **runs**
- Repeated votes trigger special behavior
- Winner emission happens **once per run**
- Explicit run reset prevents phantom slips

---

## 🏆 Winner Logic (Experimental)

- A fixed `winner` symbol (🍌) is used for testing
- On the **second identical vote in a run**, the winner is emitted
- Further identical votes start a **new run**

This logic exists to explore **edge cases and state correctness**.

---

## 🛑 Voting Limit

- Maximum **4 finalized votes**
- After voting ends:
  - Buttons are ignored
  - Voter is alerted
  - Results can be viewed by opening the VVPAT lid

---

## 🧩 Key State Variables

```js
previewSlip           // unresolved slip at preview
voteLog               // finalized slips only
lastVoteSymbol        // tracks vote runs
winnerEmittedForRun   // prevents duplicate winners
artificialLightOn     // 7-second VVPAT light
vvpatOpen             // lid state (natural light)
⚠️ Preview slips are never stored in voteLog
🔒 Core Invariants
Preview slip is never inferred from storage
Storage layout never touches preview
Time never moves slips — only state transitions do
Winner is emitted at most once per run
All resets are explicit
🛠️ Tech Stack
HTML5
SVG (inline)
CSS
Vanilla JavaScript
No frameworks. No libraries. No build tools.
▶️ Running Locally
Clone the repository
Open index.html in any modern browser
Works fully offline
🌍 Deploying to GitHub Pages
Push index.html to the main branch
Go to Settings → Pages
Select:
Source: main
Folder: /root
Save — GitHub will provide the live URL
🎯 Purpose
This project is:
A logic & state-machine exercise
A visual reasoning tool
A learning experiment
It is not intended for real-world elections.
⚠️ Disclaimer
This is a simulation only.
It does not represent any real EVM implementation.
👤 Author
Built independently as an engineering and reasoning exercise.

