# ShadowFox Python Development Internship

This repository contains my completed Python internship tasks based on the supplied ShadowFox task list.

## Completed scope

### Task 1 — Beginner (5 of 9)
The internship asks for **5 out of 9** beginner sections. I completed:
1. Variables
2. Numbers
3. Lists
4. If Condition
5. For Loop

Files are in `task1_beginner/`.

### Task 2 — Intermediate (both required)
1. Web Scraper — `task2_intermediate/web_scraper.py`
2. Hangman — `task2_intermediate/hangman.py`

### Task 3 — Advanced (1 of 3)
I selected **Cricket Fielding Analysis Data Collection**.
- Source sample: `data/IPL_sample_data.xlsx`
- Clean event data: `data/ipl_fielding_events.csv`
- Performance matrix: `data/ipl_performance_matrix.csv`
- Analysis notebook: `task3_cricket_fielding/cricket_fielding_analysis.ipynb`

The notebook analyzes three selected players from the supplied sample:
- Rilee russouw
- Phil Salt
- Yash Dhull

## Setup

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run Task 1

```bash
python task1_beginner/01_variables.py
python task1_beginner/02_numbers.py
python task1_beginner/03_lists.py
python task1_beginner/04_if_condition.py
python task1_beginner/05_for_loop.py
```

`04_if_condition.py` and `05_for_loop.py` are interactive.

## Run Task 2

```bash
python task2_intermediate/hangman.py
python task2_intermediate/web_scraper.py
```

The web scraper uses a public practice page by default and saves results to `scraped_quotes.csv`.

## Open Task 3 notebook

```bash
jupyter notebook
```

Then open:
`task3_cricket_fielding/cricket_fielding_analysis.ipynb`

## GitHub

After creating a GitHub repository, run:

```bash
git init
git add .
git commit -m "Complete ShadowFox Python internship tasks"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/shadowfox-python-internship.git
git push -u origin main
```

Replace `YOUR_USERNAME` and the repository name with your actual GitHub repository details.
