# NET-A-PORTER Dresses Web Scraper

This project is a web scraping tool designed to collect information about dresses from a popular brand's website using Selenium. The aim of this project is to stay updated with the latest dress collections and to provide a challenging learning experience in web scraping and data handling.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mayankv03/web_scraping_net_a_porter.git
   cd web_scraping_net_a_porter
   ```

2. **Install the required packages:**
   
   Make sure you have Python and pip installed. Then, run:
   ```bash
   pip install selenium pandas
   ```

3. **Download ChromeDriver:**
   
   Download ChromeDriver from [here](https://getwebdriver.com/chromedriver) and ensure it is in your system's PATH or in the same directory as your script.

## Usage

1. **Run the script:**
   ```bash
   python export_dresses_url.py
   ```
   
   The script will start scraping dress data from the specified website and save the data into CSV files located in the `dresses` folder.

2. **Parameters:**
   
   The script is currently configured to scrape pages 1 through 161. Adjust the `for page_n in range(1, 162)` line if you need to change the page range.

## Features

- **Implicit Waits:** Ensures that elements are loaded before attempting to interact with them.
- **Scrolling:** Automatically scrolls to the bottom of the page to load all lazy-loading elements.
- **Error Handling:** Handles cases where elements may not be present.
- **Data Storage:** Stores scraped data in CSV files for easy access and analysis.

## Project Structure

```
web_scraping_net_a_porter/
│
├── dresses/               # Folder where the scraped data will be saved
│   ├── dresses_data1.csv
│   ├── dresses_data2.csv
│   └── ... 
│
├── export_dresses_url.py        # Main script for web scraping
├── build_image_data.py          # Script for generating image data
├── combine_dresses_data.py      # Script for combining multiple csv files
├── extract_images.py            # Old script for scraping images information
├── README.md                    # Project readme file
├── LICENSE                      # Project readme file
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the existing style and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
