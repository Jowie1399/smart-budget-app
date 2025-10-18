# smart-budget-app
Smart Budget — Financial Literacy Dashboard for Low-Income Families
# MoneySkills — Financial Literacy Dashboard (Flask + Dash)

## Quick start (local)

1. Clone or create project folder and paste files.
2. Create virtualenv and activate:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS / Linux:
     ```
     python -m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:

# -------How to set up and run the app.-----

## create venv and activate
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt

# create demo data and user
python create_sample_db.py
python create_demo_user.py

# run app
python app.py

# Developer Kinsley Were
# created: 10/18/2025
# SmartBudget — Financial Literacy Dashboard for Low-Income Families

**Tagline:** Empowering families with simple budgeting skills — "I can save a little, I can plan."

---

## Slide 1 — Title
**SmartBudget**  
*Empowering Families with Financial Skills*

Helping low-income families learn money management, budget wisely, and save for a better future through an interactive dashboard and simple learning tools.

---

## Slide 2 — The Problem
**The Financial Literacy Gap**

- Many low-income families lack basic financial literacy.
- Limited access to easy-to-understand financial education.
- High rates of debt and low savings.
- Existing financial tools are often complex and inaccessible.

---

## Slide 3 — Our Solution
**SmartBudget Dashboard**

- A lightweight, mobile-first web dashboard (Flask + Dash) that teaches practical money skills.  
- Short lessons in plain language, a simple budget builder, and visual spending insights.  
- Designed for low-data and low-literacy users.

---

## Slide 4 — Key Features
**What Makes SmartBudget Unique**

- 📊 Simple, interactive budgeting dashboard  
- 💰 Savings goals and progress tracker  
- 🧠 Bite-sized lessons in plain language  
- 🔐 Secure accounts (Flask-Login) for personal budgets  
- 📥 Export budgets as CSV for local sharing

---

## Slide 5 — How It Works
**User Journey**

1. Register or login (secure auth).  
2. Enter monthly income and expenses per category.  
3. Dashboard visualizes spending and remaining funds.  
4. Set a savings goal and track progress.  
5. Export or print the budget for sharing.

---

## Slide 6 — Market Opportunity
**Why Now**

- Large untapped audience: millions lack access to practical financial education.  
- NGOs and microfinance orgs seek simple tools to deliver financial literacy.  
- Opportunity to partner for social impact and funded pilots.

---

## Slide 7 — Revenue Model
**Sustainable, Socially-Minded Options**

- Freemium: core features free; small-fee premium lessons or tools.  
- NGO / Corporate partnerships for sponsored rollouts.  
- Grants and research partnerships using anonymized aggregate data.

---

## Slide 8 — Technology Stack
**Simple & Scalable**

- Backend: **Flask** (Python) — app logic, auth, DB.  
- Dashboard: **Dash (Plotly)** — interactive charts.  
- DB: **SQLite** for MVP (upgradeable to PostgreSQL).  
- Data & viz: **pandas**, **plotly**.  
- Frontend: Bootstrap for responsive UI.

---

## Slide 9 — Social Impact
**Driving Real Change**

- Builds basic budgeting skills and savings habits.  
- Supports SDGs: poverty reduction and economic empowerment.  
- Easily adapted to local languages and currencies.

---

## Slide 10 — Call to Action
**Join Us**

We’re looking for:
- NGO and microfinance partners for pilots  
- Seed funding for productization and outreach  
- Volunteers for localization and content creation

**Repo:** https://github.com/<yourusername>/financial-dashboard

---

## Demo & How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/<yourusername>/financial-dashboard.git
cd financial-dashboard

2.# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

3.pip install -r requirements.txt

4.# optional
python create_sample_db.py
python create_demo_user.py

5.python app.py
