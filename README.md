# sports-data-project

⚽ Sports Data Pipeline: Football Match Analysis

This project builds a complete end-to-end data pipeline in Python to fetch, clean, and analyze football match data across multiple leagues and seasons using the Football-Data.org API.

> ✅ Designed to demonstrate strong code structure, data cleaning, and exploratory data analysis (EDA) with 1,000+ match records.
>
> 🎥Video Presentation Link: https://youtu.be/beLK5muC70s

---

🔧 Project Structure

`
sports-data-project/
├── data/                  # Raw + cleaned CSV data
│   ├── raw_matches.csv
│   └── cleaned_matches.csv
├── eda/                   # EDA notebook with plots and findings
│   └── eda_report.ipynb
├── scripts/               # Python scripts for automation
│   ├── fetch_data.py
│   └── clean_data.py
├── .env                   # (ignored) contains API token
├── .gitignore
├── requirements.txt
└── README.md
`

---

💡 Features

- 🔄 Fetches match data from Premier League, Serie A, and other leagues
- 📆 Supports multiple seasons (2021–2023)
- 🧹 Cleans data: removes duplicates, handles missing values
- 📊 Performs EDA using matplotlib & seaborn
- ✅ Includes 1000+ cleaned match records

---

🚀 How to Run

1. Install Requirements

`bash
pip install -r requirements.txt
`

2. Create .env File

Create a file named .env at the root with:
`
APITOKEN=yourtoken_here
`

> Get your token from: https://www.football-data.org/client/register

3. Fetch Match Data

`bash
python scripts/fetch_data.py
`

4. Clean the Raw Data

`bash
python scripts/clean_data.py
`

5. Run Exploratory Data Analysis

`bash
jupyter notebook eda/eda_report.ipynb
`

---

📈 Example EDA Insights

- Total goals per match (distribution)
- Top scoring teams at home


---

📁 Submission Checklist

- ✅ data/cleaned_matches.csv with 1000+ records
- ✅ Modular, commented code
- ✅ EDA notebook with findings
- ✅ README with setup and usage
- ✅ Video presentation explaining the system
- ✅ GitHub repo submitted

---

🔐 Notes

- .env is listed in .gitignore to protect sensitive credentials
- If .env was accidentally committed, revoke your token and generate a new one

