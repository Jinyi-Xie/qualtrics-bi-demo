# Qualtrics to BI Demo Pipeline

This is a simple Python demo project for **Scenario 2** of the Lassonde assessment — showing how to build a basic, local data pipeline from Qualtrics surveys to a BI-ready output.

It reads mock survey data in JSON format (simulating a response from Qualtrics API), does light cleaning and formatting using **pandas**, and exports a final CSV file that can be used in a BI platform.

---

##  Files Included

- `qualtrics_pipeline_demo.py` – The main script that loads, cleans, and exports the data
- `mock_qualtrics_data.json` – Sample input data (you can edit this)
- `engagement_output.csv` – Output file generated after running the script

---

##  How to Run

### 1. Make sure Python 3 and pandas are installed
```bash
pip3 install pandas
```

### 2. Place both files in the same folder:
- `qualtrics_pipeline_demo.py`
- `mock_qualtrics_data.json`

### 3. Run the script:
```bash
python3 qualtrics_pipeline_demo.py
```

### 4. Output:
A file called `engagement_output.csv` will be created with cleaned, BI-friendly data.

---

##  What the Script Does

- Loads mock survey data from JSON
- Keeps only the fields we care about (student ID, engagement status, score, timestamp)
- Cleans up text (removes spaces, lowercases statuses)
- Converts timestamps into datetime format
- Removes incomplete rows
- Drops duplicates and keeps the latest response per student
- Exports final cleaned table to CSV

---

##  Why This Matters
This pipeline avoids relying on slow central systems and gives Lassonde a fast, reliable, and flexible way to update student engagement dashboards.

---

Feel free to tweak the mock data or script to simulate other use cases!