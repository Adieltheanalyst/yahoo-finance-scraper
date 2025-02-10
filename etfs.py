import random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")

# Set up WebDriver
service = Service("C:\\Users\\gacha\\Downloads\\chromedriver-win64 (3)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://finance.yahoo.com/research-hub/screener/etf/")

# Wait for the page to load
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".fin-size-small.rounded.rightAlign"))
).click()
time.sleep(15)

# Click to start extraction
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.yf-1hdw734~ .yf-1hdw734+ .yf-1hdw734'))
).click()
time.sleep(20)

# Desired data structure
extracted_data = []

# Function to extract data from the current page
# Function to extract data from the current page
def extract_data():
    try:
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for row in rows:
            try:
                etf = {}
                etf['Symbol'] = row.find_element(By.CSS_SELECTOR, ".symbol.yf-1m808gl").text
                etf['Name'] = row.find_element(By.CSS_SELECTOR, ".yf-eg2gbv").text
                etf['Link'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(4) a").get_attribute("href")
                etf['Price_intraday'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
                etf['Change'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text
                etf['Change_pct'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(7)").text
                etf['Volume'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(8)").text
                etf['YTD_Return'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(9)").text
                etf['Three_Months_Return'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(10)").text
                etf['One_Year_Return'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(11)").text
                etf['Three_Year_Return'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(12)").text
                etf['Five_Year_Return'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(13)").text
                etf['Net_Expense_Ratio'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(14)").text
                etf['Gross_Expense_Ratio'] = row.find_element(By.CSS_SELECTOR, "td:nth-child(15)").text

                # Extract ratings
                try:
                    rating_element = row.find_element(By.CSS_SELECTOR, "div.star-rating")
                    filled_stars = 0
                    stars = rating_element.find_elements(By.CSS_SELECTOR, "div.icon > svg > path")
                    for star in stars:
                        path = star.get_attribute("d")
                        if 'M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z' in path:
                            filled_stars += 1
                    etf['Rating'] = f"{filled_stars} star{'s' if filled_stars > 1 else ''}"
                except:
                    etf['Rating'] = "No rating"  # In case the rating is not available

                # Append the extracted ETF data to the list
                extracted_data.append(etf)

            except Exception as e:
                print(f"Error extracting data for a row: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Pagination logic
page_number = 1
while True:
    print(f"Scraping data from page {page_number}...")
    extract_data()

    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='next-page-button']"))
        )
        time.sleep(random.uniform(5, 10))
        next_button.click()
        time.sleep(10)  # Allow time for the next page to load
        page_number += 1
    except Exception as e:
        print(f"Stopping pagination at page {page_number} due to error: {e}")
        break

# Save the extracted data to JSON
json_filename = 'refined_etf_data.json'
with open(json_filename, 'w', encoding='utf-8') as json_file:
    json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)

print(f"Data has been successfully written to {json_filename}")
driver.quit()
