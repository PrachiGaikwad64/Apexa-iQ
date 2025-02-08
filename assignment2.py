"""versions of.net Scrapper"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://versionsof.net/core/8.0/8.0.0/")

# Find all tables
tables = driver.find_elements(By.TAG_NAME, "table")

# List to store all table data
dataframes = []

# Extract data from each table
for index, table in enumerate(tables):
    headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    data = []
    for row in rows[1:]:  # Skip header row
        cells = row.find_elements(By.TAG_NAME, "td")
        data.append([cell.text for cell in cells])
    
    # Convert to DataFrame and append to list
    df = pd.DataFrame(data, columns=headers if headers else None)
    dataframes.append(df)

# Concatenate all tables into one DataFrame
final_df = pd.concat(dataframes, ignore_index=True)

# Define the folder path where the CSV file will be saved
save_folder = r"C:\Users\gaikw\OneDrive\Desktop\ApexaiQ\csv.csv"
os.makedirs(save_folder, exist_ok=True)
csv_filename = os.path.join(save_folder, "all_tables.csv")

# Save to a single CSV file
final_df.to_csv(csv_filename, index=False)

print(f"All tables saved in {csv_filename}")

# Close the driver
driver.quit()
