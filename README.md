# Flipkart Mobile Web Scraping

Welcome to the Flipkart Mobile Web Scraping project! 🚀 This project demonstrates how to scrape detailed mobile phone information from Flipkart using Python, BeautifulSoup, and Requests. The focus is on gathering real-time data for Realme mobile phones, which includes their names, prices, ratings, memory specifications (RAM/ROM), images, and product links. All the collected data is neatly stored in a CSV file, ready for further analysis or research.

Whether you're into data analysis, product comparison, or just love working with real-world data, this project will show you how to automate the process of scraping valuable information from e-commerce websites like Flipkart.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [How to Run](#how-to-run)
- [Sample Output](#sample-output)
- [Data Structure](#data-structure)
- [Future Enhancements](#future-enhancements))

## Overview

In this project, we use BeautifulSoup and Requests to scrape detailed mobile phone listings from Flipkart's website. The goal is to pull out important product details for Realme mobile phones such as:

- **Product Name** 🏷️
- **Price** 💰
- **Ratings** ⭐
- **Memory (RAM/ROM)** 🧠
- **Image URLs** 📸
- **Product Links** 🔗

This project showcases the power of web scraping in collecting structured data and storing it in a CSV file for further analysis, comparison, and visualization. If you’ve ever wondered how to extract data from e-commerce platforms programmatically, this project is for you!

## Technologies Used

This project uses a combination of powerful Python libraries to perform the web scraping and data manipulation:

- **Python**: The main programming language used to write the script and handle all logic.
- **BeautifulSoup**: A powerful library used to parse HTML and extract useful data from Flipkart's product listings.
- **Requests**: A simple HTTP library to send requests and get the HTML content of the Flipkart page.
- **Pandas**: For organizing and manipulating the scraped data efficiently.
- **CSV**: For saving and exporting the data into a structured CSV file that’s ready for further analysis or visual representation.

## Features

- **Real-Time Scraping of Mobile Details**: Scrapes detailed data for Realme mobile phones including names, prices, ratings, memory specifications, images, and more.
- **CSV Export**: Saves all collected data into a CSV file, which can easily be imported into tools like Excel, Google Sheets, or Python for analysis.
- **Customizable Data**: You can adjust the number of items scraped, or target different mobile brands or categories on Flipkart.
- **Error Handling**: Gracefully handles missing or incomplete data, ensuring the script runs smoothly even when some information is unavailable.
- **CSV**: For saving and exporting the data into a structured CSV file that’s ready for further analysis or visual representation.

## How to Run

To run the web scraper and start collecting mobile data from Flipkart, follow these simple steps:

1. **Clone the Repository**: Start by cloning this repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/flipkart-mobile-web-scraping.git
Install Required Libraries: Make sure you have all the necessary libraries installed. You can do this with pip:

bash
Copy
Edit
pip install requests beautifulsoup4 pandas
Run the Script: Once the setup is complete, run the script:

bash
Copy
Edit
python scraper.py
Check the Output: After running the script, a mobiles_info.csv file will be generated, containing the extracted data.

## Sample Output
Here's a preview of how the data looks in the CSV format:
<img width="960" alt="Screenshot of csv data" src="https://github.com/user-attachments/assets/7d0bcf79-515c-466a-ba70-fddf9497264b" />


## Data Structure
The data is structured in a CSV format with the following columns:
- Name: Name of the mobile phone.
-Price: Price of the mobile phone.
-Rating: Rating of the product based on user reviews.
-Memory: RAM and ROM details of the mobile.
-Link: The URL to the Flipkart product page.

## Future Enhancements
-Advanced Filtering: Add filters to scrape only mobile phones within a specific price range or from specific brands.
-Multiple Pages Scraping: Scrape data from multiple pages of mobile listings for more extensive results.
-Error Logging: Implement better error logging and exception handling for better troubleshooting.
-Data Visualization: Integrate data visualization libraries like Matplotlib or Seaborn to plot graphs based on the scraped data (e.g., price distribution, rating averages).




