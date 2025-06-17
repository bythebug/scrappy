"""
linkedin_scraper.py

Author: Suraj Van Verma
Created: June 2025
Description:
    Scrapes all email addresses from comments on a LinkedIn post.
    Outputs a CSV file with unique emails and associated comment text.

Usage:
    - Requires ChromeDriver installed and in PATH
    - Requires Selenium and Pandas:
        pip install selenium pandas
"""

import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os

# ==== CONFIGURATION ====
POST_URL = 'https://www.linkedin.com/feed/update/urn:li:activity:7339295701866082304/'  # ✅ Your LinkedIn post
SCROLL_TIMES = 10  # Increase if many comments
WAIT_LOGIN = 20    # Time to manually log in

# ==== CHROME SETUP ====
options = Options()
options.add_argument("--user-data-dir=/tmp/selenium_profile")  # Temp profile to avoid session conflicts
options.add_argument("--remote-debugging-port=9222")  # Needed to avoid "DevToolsActivePort" error

print("🚀 Launching Chrome...")
driver = webdriver.Chrome(options=options)

print("🌐 Opening LinkedIn post...")
driver.get(POST_URL)
print(f"⏳ Waiting {WAIT_LOGIN}s for login or page load...")
time.sleep(WAIT_LOGIN)  # You log in manually in this time if needed

# ==== FUNCTION TO LOAD MORE COMMENTS ====
def click_load_more():
    try:
        load_more = driver.find_element(By.XPATH, '//button[contains(@aria-label, "more comments")]')
        load_more.click()
        print("🔁 Clicked 'Load more comments'")
        return True
    except NoSuchElementException:
        return False
    except ElementClickInterceptedException:
        time.sleep(1)
        return click_load_more()

# Keep trying to load more until it's done
print("🔄 Loading all comments...")
for _ in range(SCROLL_TIMES):
    clicked = click_load_more()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    if not clicked:
        break

# ==== SCROLL TO LOAD COMMENTS ====
# print("🔄 Scrolling through comments...")
for _ in range(SCROLL_TIMES):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# ==== EXTRACT EMAILS FROM COMMENTS ====
print("🔍 Extracting emails from comments...")
comments_elements = driver.find_elements(By.CLASS_NAME, 'comments-comment-item__main-content')

data = []
for c in comments_elements:
    text = c.text
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    for email in emails:
        data.append({"Email": email, "Comment": text})

df = pd.DataFrame(data).drop_duplicates(subset=["Email"])

# ==== SAVE AS CSV FILE ====
# Base filename
base_filename = "linkedin_emails_with_comments"
filename = f"{base_filename}.csv"
i = 1

# Check for existing files and create a new one if needed
while os.path.exists(filename):
    filename = f"{base_filename}_{i}.csv"
    i += 1

df.to_csv(filename, index=False)
print(f"✅ Done! Saved {len(df)} cleaned emails to {filename}")

driver.quit()