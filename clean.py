import pandas as pd
import json

# Read the doc.csv with tab delimiter
doc = pd.read_csv('doc.csv', delimiter='\t')

# Load the dictionaries from the backup JSON files
with open('backup_new.json') as f1:
    dict1 = json.load(f1)

with open('backup_old.json') as f2:
    dict2 = json.load(f2)

# Print the initial stats
print(doc.shape)
print(doc.head())

# Ignore the first 450,000 rows in the doc

# Convert dictionary keys to sets for faster lookup
dict1_keys = set(dict1.keys())
dict2_keys = set(dict2.keys())

# Filter out rows that have URL not present in either of the two dictionaries
doc = doc[~doc['Url'].isin(dict1_keys)]  # Ensure 'Url' matches the actual column name in doc.csv
doc = doc[~doc['Url'].isin(dict2_keys)]  # Ensure 'Url' matches the actual column name in doc.csv

# Print stats after filtering
print(doc.shape)
print(doc.head())

# Write the filtered doc to a new csv saving the iloc index without reseting
doc.to_csv('doc_new.csv', index=True, sep='\t')
