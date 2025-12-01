# qualtrics_pipeline_demo.py

import json
import pandas as pd
from datetime import datetime

# Step 1: Load fake Qualtrics data from a file (we pretend it's from the API)
# The file should be called 'mock_qualtrics_data.json'
with open('mock_qualtrics_data.json') as f:
    data = json.load(f)

# Step 2: Turn the JSON data into a table (pandas DataFrame)
# We grab the list of responses from the JSON
responses = data.get("responses", [])
df = pd.json_normalize(responses)  # Makes it into rows and columns

# Step 3: Keep only the fields we care about
# For example: student ID, engagement status, score, and timestamp
keep_fields = ['values.student_id', 'values.engagement_status', 'values.engagement_score', 'values.last_updated']
df = df[keep_fields]

# Step 4: Rename the columns to something shorter and nicer
df.columns = ['student_id', 'engagement_status', 'engagement_score', 'response_timestamp']

# Step 5: Do some basic cleaning
# Like removing extra spaces, making text lowercase, fixing date format
df['student_id'] = df['student_id'].astype(str).str.strip()
df['engagement_status'] = df['engagement_status'].str.strip().str.lower()
df['response_timestamp'] = pd.to_datetime(df['response_timestamp'], errors='coerce')  # Turn text into datetime

# Step 6: Drop any rows that are missing important info
df = df.dropna(subset=['student_id', 'engagement_status'])

# Step 7: If the same student filled it out twice, keep only the newest one
df = df.sort_values('response_timestamp').drop_duplicates(subset='student_id', keep='last')

# Step 8: Save the cleaned data to a CSV file
df.to_csv('engagement_output.csv', index=False)
print("✅ Cleaned data exported to engagement_output.csv")
