# Daily Expense Tracker 💸📊

A clean, fast, and user-friendly way to log your daily expenses and instantly see where your money goes. Built with a sharp, responsive UI and simple flows so anyone—from students to busy professionals—can track spending in seconds.

[Repo](https://github.com/AshmitThakur23/Daily-Expense-Tracker) • Default branch: `main`

![Made with Python](https://img.shields.io/badge/Python-18%25-3776AB?logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-37.4%25-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-44.6%25-1572B6?logo=css3&logoColor=white)

---

## ✨ Highlights (Why it stands out)

- 🧭 Zero-friction UX: add an expense in just a few clicks.
- 📱 Fully responsive: looks great on mobile and desktop.
- 🔍 Filter & search: quickly find expenses by category/date.
- 📈 At-a-glance insights: daily/monthly totals to guide better decisions.
- 🧩 Simple architecture: HTML/CSS UI powered by lightweight Python where needed.

---

## 👀 Screenshots (Front-end Preview)

Place your three PNG screenshots inside a folder like `screenshots/` and ensure the paths below match your filenames.

<p align="center">
  <img src="screenshots/overview.png" alt="Dashboard Overview" width="85%" />
  <br/>
  <em>Overview — clean dashboard summarizing your spending.</em>
</p>

<p align="center">
  <img src="screenshots/add-expense.png" alt="Add Expense Form" width="85%" />
  <br/>
  <em>Add Expense — quick form with category, amount, date, and notes.</em>
</p>

<p align="center">
  <img src="screenshots/history.png" alt="Expense History and Filters" width="85%" />
  <br/>
  <em>History — filterable, searchable list of previous expenses.</em>
</p>

Tip: Rename your images to meaningful names (e.g., `overview.png`, `add-expense.png`, `history.png`) so HR/reviewers understand what they’re seeing at a glance.

---

## 🧠 Problem & Solution

- The problem: keeping track of small, daily expenses is tedious, and complex apps add friction.
- The solution: a minimal, beautiful expense tracker you can start using instantly—no logins, no setup hurdles.

Impact:
- Encourages consistent tracking habits.
- Offers clear monthly insights for smarter budgeting.
- Fast onboarding—ideal for personal or academic portfolios.

---

## ⚙️ Tech Stack

- Frontend: HTML + CSS (responsive, accessible, clean layout)
- Logic/Data: Python (for data handling/APIs if present)
- Version Control: Git + GitHub

Language composition:
- CSS: 44.6%
- HTML: 37.4%
- Python: 18%

---

## 🚀 Getting Started

Choose the path that matches your setup.

### Option A — Static frontend (no backend)
1. Clone the repo:
   ```
   git clone https://github.com/AshmitThakur23/Daily-Expense-Tracker.git
   cd Daily-Expense-Tracker
   ```
2. Open `index.html` in your browser.  
   Optional: serve locally for better dev experience:
   ```
   # Python 3
   python -m http.server 8000
   # Visit http://localhost:8000
   ```

### Option B — Python backend (if `app.py` / `requirements.txt` are present)
1. Clone the repo:
   ```
   git clone https://github.com/AshmitThakur23/Daily-Expense-Tracker.git
   cd Daily-Expense-Tracker
   ```
2. Create and activate a virtual environment:
   - Windows:
     ```
     py -3 -m venv .venv
     .\.venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   python app.py
   ```
5. Open the URL from the terminal (commonly `http://127.0.0.1:5000/`).

---

## 🗂️ Suggested Project Structure

Adjust to match your actual files:

```
Daily-Expense-Tracker/
├─ index.html
├─ styles/            # CSS files
│  └─ style.css
├─ scripts/           # JS (if any, for UI interactivity)
│  └─ main.js
├─ app.py             # Python backend (if present)
├─ requirements.txt   # Python deps (if present)
└─ screenshots/       # Add your 3 PNG images here
   ├─ overview.png
   ├─ add-expense.png
   └─ history.png
```

---

## 🧾 Core Data Model (simple and extensible)

- Expense
  - id: string/number
  - date: ISO date (YYYY-MM-DD)
  - category: string (e.g., Food, Travel, Bills)
  - amount: number
  - note: string (optional)

Easy to extend with:
- currency, tags, vendor, payment method, receipts, recurring flags, etc.

---

## 🧩 Design & UX Principles

- Accessibility first: readable contrast, semantic HTML, form labels, keyboard-friendly controls. ♿
- Visual clarity: consistent spacing, legible typography, and clean hierarchy.
- Performance: minimal assets, no heavy frameworks for the core flow. ⚡
- Maintainability: separation of concerns (HTML structure, CSS styling, Python logic).

---

## ✅ What I Built & Learned

- Designed a responsive UI that reduces the time to add an expense.
- Implemented filters and summaries for quick insights.
- Practiced clean CSS architecture and semantic HTML.
- Integrated a light Python layer (if present) for data handling.

---

## 🔮 Roadmap

- [ ] CSV/Excel export
- [ ] Charts for category breakdowns and monthly trends
- [ ] Recurring expenses and reminders
- [ ] PWA for offline-first usage
- [ ] Optional authentication and cloud sync

---

## 🤝 Contributing

Issues and PRs are welcome!  
- Create an issue for feature requests or bugs.
- Keep PRs focused with clear descriptions and testing notes.

---

## 📫 Contact

- Author: [Ashmit Thakur](https://github.com/AshmitThakur23)
- Project: [Daily Expense Tracker](https://github.com/AshmitThakur23/Daily-Expense-Tracker)

If you like this project, please give it a ⭐ — it helps others discover it!

---

Notes for maintainers:
- Update the three screenshot paths to your actual PNG filenames.
- Keep only the relevant Getting Started option (A or B) based on your repo’s setup.
- If using a Python backend, ensure `requirements.txt` and the `app.py` run command match your framework (e.g., Flask/FastAPI).
