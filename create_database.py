import sqlite3
import pandas as pd
import os

# Define the database file
db_file = 'news_articles.db'

# Connect to the SQLite3 database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the Articles table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Articles (
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE NOT NULL,
    title TEXT,
    label TEXT,
    theme TEXT,
    badge TEXT,
    datetime TEXT NOT NULL,
    author TEXT,
    text TEXT NOT NULL
)
''')

# Create the Reports table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_date TEXT UNIQUE NOT NULL,
    content TEXT NOT NULL
)
''')

# Create the Article_Report_Link table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Article_Report_Link (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id INTEGER,
    report_id INTEGER,
    FOREIGN KEY (article_id) REFERENCES Articles(article_id) ON DELETE CASCADE,
    FOREIGN KEY (report_id) REFERENCES Reports(report_id) ON DELETE CASCADE
)
''')

# Commit the changes
conn.commit()

# Read the CSV file
csv_file = os.path.join('Exercise', 'scraped_data.csv')

# Debugging statement to print the constructed file path
print(f"Looking for file at: {csv_file}")

# List the contents of the directory
print("Contents of the 'Exercise' directory:")
print(os.listdir('Exercise'))

# Check if the file exists
if not os.path.isfile(csv_file):
    print(f"File not found: {csv_file}")
else:
    df = pd.read_csv(csv_file)

    # Convert NaN values to None
    df = df.where(pd.notnull(df), None)

    # Insert data into the Articles table
    for index, row in df.iterrows():
        try:
            cursor.execute('''
            INSERT INTO Articles (url, title, label, theme, badge, datetime, author, text)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (row['url'], row['title'], row['label'], row['theme'], row['badge'], row['datetime'], row['author'], row['text']))
        except sqlite3.IntegrityError:
            print(f"Article with URL {row['url']} already exists. Skipping...")

    # Commit the changes and close the connection
    conn.commit()
conn.close()