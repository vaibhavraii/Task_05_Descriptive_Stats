# Task_05_Descriptive_Stats

## 1. Project Overview
This repository documents **Research Task 05 – Descriptive Statistics & Large-Language-Models**.  
The goal is to:

1. Extract structured tables from the *2025 Syracuse Women’s Lacrosse* PDF stat sheet.  
2. Generate clean `.csv` files that an LLM can query.  
3. Craft natural-language prompts, record how well the LLM answered, and analyse the results.

> **Important:** *Per assignment guidance, the raw dataset **must not** be committed to GitHub.*  
> Place the PDF locally under `data/raw/` (or have the script download it) and keep it git-ignored.

---


---

## 3. Quick-start
```bash
# 1 – clone repo & move into it
git clone https://github.com/<your-handle>/Task_05_Descriptive_Stats.git
cd Task_05_Descriptive_Stats

# 2 – create & activate a virtual-env
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 3 – install dependencies
pip install -r requirements.txt

# 4 – add the PDF (NOT tracked by Git)
mkdir -p data/raw && cp /path/to/2025SUStats.pdf data/raw/

# 5 – run the extractor
python scripts/pdf_to_csv.py

# 6 – inspect outputs
ls data/outputs/2025_su_tables_full/*.csv


