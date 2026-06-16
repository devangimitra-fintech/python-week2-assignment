# Expense Tracker Application

## Overview

The Expense Tracker is a Python-based application that helps users record, manage, and analyze their daily expenses. All expense records are stored in a CSV file, making the data easy to access and maintain.

## Features

* Add new expenses
* View all recorded expenses
* Filter expenses by category
* Filter expenses by date range
* Generate monthly expense summaries
* Display category-wise spending breakdown
* Store data in CSV format
* User-friendly menu-driven interface

## Technologies Used

* Python 3
* CSV Module
* Datetime Module
* Collections Module

## Project Structure

ExpenseTracker/

│

├── main.py

├── file_handler.py

├── expenses.csv

└── README.md

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run the following command:

python main.py

## Sample Features

1. Add Expense
2. View Expenses
3. Filter by Category
4. Filter by Date Range
5. Monthly Summary
6. Category Breakdown
7. Exit

## Learning Outcomes

* File handling using CSV files
* Data processing and filtering
* Working with dictionaries and lists
* Building menu-driven applications
* Exception handling in Python

## Author

Devangi Mitra

# Web Scraper Using Python

## Overview

This project is a Python-based web scraper that extracts book information from the Books to Scrape website and stores the collected data in a CSV file for further analysis.

## Website Used

https://books.toscrape.com/

## Features

* Scrapes data from multiple pages
* Extracts book title
* Extracts price information
* Extracts rating information
* Extracts product URLs
* Handles pagination automatically
* Saves data into CSV format
* Includes error handling
* Implements request delays for responsible scraping

## Technologies Used

* Python 3
* Requests Library
* BeautifulSoup4
* CSV Module

## Project Structure

WebScraper/
│
├── scraper.py
├── books.csv
├── requirements.txt
└── README.md

## Installation

Install the required libraries:

pip install requests beautifulsoup4

## How to Run

python scraper.py

## Output

The program generates a CSV file named:

books.csv

The file contains:

* Title
* Price
* Rating
* Product URL

## Learning Outcomes

* Web scraping fundamentals
* HTML parsing using BeautifulSoup
* Working with APIs and HTTP requests
* Data extraction techniques
* CSV file generation
* Exception handling

## Author

Devangi Mitra
