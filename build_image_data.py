"""
This script extracts product codes from product URLs, then merges and organizes them based on their properties and resolutions.
"""

import pandas as pd
import os

folder_path = "dresses"
csvpath = "combined_file.csv"
df = pd.read_csv(os.path.join(folder_path,csvpath))
product_data = []

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    url = row["url"]
    product_code = url.split("/")[-1]

    product_details = {
        "url": url,
        "product_code": product_code,
        
        "main_image_230"    : f"https://www.net-a-porter.com/variants/images/{product_code}/in/w230_a3-4_q60.jpg",
        "main_image_390"    : f"https://www.net-a-porter.com/variants/images/{product_code}/in/w390_a3-4_q60.jpg",
        "main_image_920"    : f"https://www.net-a-porter.com/variants/images/{product_code}/in/w920_a3-4_q60.jpg",
        "main_image_2000"   : f"https://www.net-a-porter.com/variants/images/{product_code}/in/w2000_a3-4_q60.jpg",
        "back_image_230"    : f"https://www.net-a-porter.com/variants/images/{product_code}/bk/w230_a3-4_q60.jpg",
        "back_image_390"    : f"https://www.net-a-porter.com/variants/images/{product_code}/bk/w390_a3-4_q60.jpg",
        "back_image_920"    : f"https://www.net-a-porter.com/variants/images/{product_code}/bk/w920_a3-4_q60.jpg",
        "back_image_2000"   : f"https://www.net-a-porter.com/variants/images/{product_code}/bk/w2000_a3-4_q60.jpg",
        "front_image_230"   : f"https://www.net-a-porter.com/variants/images/{product_code}/fr/w230_a3-4_q60.jpg",
        "front_image_390"   : f"https://www.net-a-porter.com/variants/images/{product_code}/fr/w390_a3-4_q60.jpg",
        "front_image_920"   : f"https://www.net-a-porter.com/variants/images/{product_code}/fr/w920_a3-4_q60.jpg",
        "front_image_2000"  : f"https://www.net-a-porter.com/variants/images/{product_code}/fr/w2000_a3-4_q60.jpg",
        "zoom_image_230"    : f"https://www.net-a-porter.com/variants/images/{product_code}/cu/w230_a3-4_q60.jpg",
        "zoom_image_390"    : f"https://www.net-a-porter.com/variants/images/{product_code}/cu/w390_a3-4_q60.jpg",
        "zoom_image_920"    : f"https://www.net-a-porter.com/variants/images/{product_code}/cu/w920_a3-4_q60.jpg",
        "zoom_image_2000"   : f"https://www.net-a-porter.com/variants/images/{product_code}/cu/w2000_a3-4_q60.jpg",
        }

    product_data.append(product_details)

# Convert the list to a DataFrame
df = pd.DataFrame(product_data)

# Define the filename
filename = os.path.join(folder_path, "all_image_" + csvpath.split("/")[-1])

# Save the DataFrame to a CSV file
df.to_csv(filename, index=False)

print("*******")
print(f"Product data compilation completed and saved to {filename}.")
print("*******")