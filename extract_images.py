"""
Originally, this script was designed to extract product images directly from the website. However, I later identified a pattern in the URLs, allowing all image URLs to be generated using `build_image_data.py`.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time

# Define the folder path
folder_path = 'images'

# Create the folder if it does not exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

csvpath = "dresses/combined_file.csv"
df = pd.read_csv(csvpath)
product_data = []

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    print(f"Index: {index}")
    webpage_url = row["url"]
    print(webpage_url)
    product_code = webpage_url.split("/")[-1]

    # Ensure to save chromedriver.exe to a directory listed in environment path
    driver = webdriver.Chrome()

    # Sets an implicit wait: https://www.selenium.dev/documentation/webdriver/waits/#implicit-waits
    driver.implicitly_wait(2)

    # Construct the URL
    driver.maximize_window()
    driver.get(webpage_url)
    print(webpage_url)
    time.sleep(5)

    cross_popup = "//button[contains(@class,'Overlay9__close')]"
    cross_popups = driver.find_elements(By.XPATH, cross_popup)
    for each in cross_popups:
        each.click()
        time.sleep(2)
    
    # Define the XPath expression
    next_button = "//button[contains(@class,'ImageCarousel87__next')]"
    next_buttons = driver.find_elements(By.XPATH, next_button)
    for i in range(6):
        for each in next_buttons:
            each.click()
            time.sleep(1)

    xpath_expression = '//img[contains(@class,"Image18__image")]'

    product_details = {"url": webpage_url}

    print("fetching images")
    elements = driver.find_elements(By.XPATH, xpath_expression)
    for element in elements:
        img_url = element.get_attribute("src")
        if img_url.startswith("data:image/gif;base64") and product_code not in img_url:
            continue
        print(img_url)
        if "bk" in img_url:
            product_details["back_image"] = img_url
        elif "fr" in img_url:
            product_details["front_image"] = img_url
        elif "in" in img_url:
            product_details["main_image"] = img_url
        elif "cu" in img_url:
            product_details["zoom_image"] = img_url

    product_data.append(product_details)
    driver.quit()

# Convert the list to a DataFrame
df = pd.DataFrame(product_data)

# Define the filename
filename = os.path.join(folder_path, "export-" + csvpath.split("/")[-1])

# Save the DataFrame to a CSV file
df.to_csv(filename, index=False)

print("*******")
print(f"Product data extraction completed and saved to {filename}.")
print("*******")