"""
export_dresses_url.py

This script scrapes dress data from the https://www.net-a-porter.com/ website, extracting details such as brand, name, price, URLs, and image links for each dress. The data is then saved into separate CSV files for each page. The script includes implicit waits, scrolling to load lazy-loading elements, and error handling to ensure smooth data extraction.

Usage:
    python export_dresses_url.py

Features:
    - Extracts product details including brand, name, price, URLs, and image links.
    - Handles lazy loading by scrolling to the bottom of the page.
    - Includes error handling for missing elements.
    - Saves the scraped data into CSV files in the 'dresses' folder.

"""

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import time

# Define the folder path
folder_path = 'dresses'

# Create the folder if it does not exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for page_n in range(1, 162):
    # Ensure to save chromedriver.exe to a directory listed in environment path
    driver = webdriver.Chrome()

    # Sets an implicit wait: https://www.selenium.dev/documentation/webdriver/waits/#implicit-waits
    driver.implicitly_wait(2)

    # Construct the URL
    webpage_url = "https://www.net-a-porter.com/en-kr/shop/clothing?orderBy=8&pageNumber=" + str(page_n)
    driver.maximize_window()
    driver.get(webpage_url)
    print(webpage_url)
    time.sleep(5)

    # Navigate to bottom of page to load all lazy loading images
    
    # html = driver.find_element(By.TAG_NAME, 'html')
    # html.send_keys(Keys.END)
    
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    new_height = 100

    while True:
        # Scroll down to bottom
        driver.execute_script(f"window.scrollTo(0, {new_height});")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height += 500
        if new_height > last_height - 800:
            break

    # Define the XPath expression
    xpath_expression = '//*[@class="ProductItem25__p"]/meta[@itemprop="url mainEntityOfPage"]'

    # Initialize an empty list to store product data
    dress_data = []

    # Find the elements using XPath
    dresses = driver.find_elements(By.XPATH, xpath_expression)
    for dress in dresses:
        # Extract the product URL from the element's "content" attribute
        dress_url = dress.get_attribute("content")
        # print(dress_url)

        dress_brand = dress.find_element(By.XPATH, 'following-sibling::*//span[@itemprop="brand"]').get_attribute("innerHTML")
        # print(dress_brand)

        dress_name = dress.find_element(By.XPATH, 'following-sibling::*//span[@itemprop="name"]').get_attribute("innerHTML")
        print(dress_name)

        dress_price = dress.find_element(By.XPATH, 'following-sibling::*//span[@itemprop="price"]').get_attribute("innerHTML")
        # print(dress_price)

        try:
            dress_primaryImage = dress.find_element(By.XPATH, 'following-sibling::*//div[contains(@class,"primaryImage")]//img').get_attribute("src")
            # print(dress_primaryImage)
        except NoSuchElementException as ex:
            dress_primaryImage = ""
            print("NoSuchElementException has been handled.")

        try:
            dress_secondaryImage = dress.find_element(By.XPATH, 'following-sibling::*//div[contains(@class,"secondaryImage")]//img').get_attribute("src")
            # print(dress_secondaryImage)
        except NoSuchElementException as ex:
            dress_secondaryImage = ""
            print("NoSuchElementException has been handled.")
        
        dress_data.append({"brand": dress_brand,
                           "name": dress_name,
                           "price": dress_price,
                           "url": dress_url,
                           "primaryImage": dress_primaryImage,
                           "secondaryImage": dress_secondaryImage,})

    # Convert the list to a DataFrame
    df = pd.DataFrame(dress_data)

    # Define the filename
    filename = os.path.join(folder_path, f"dresses_data{page_n}.csv")

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

    print("\n")
    print(f"Dresses data extraction for page {page_n} completed and saved to {filename}.")

    # Quit the driver
    driver.quit()