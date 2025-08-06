# Web-Scraping
#  Web Scraping for Mobile Market Analysis

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Last Updated](https://img.shields.io/badge/last%20updated-July%202025-orange.svg)]()
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red.svg)]()

A Python-based web scraping solution that extracts product data for **Mi smartphones** listed on Flipkart. This script fetches product **names, prices, ratings, images**, and **direct links**, and saves them into a structured CSV file for easy analysis, automation, or integration.

---

##  Features

-  Scrapes **Mi brand** smartphones from Flipkart
-  Extracts:
  - Product Name
  - Price
  - Rating
  - Image URL
  - Product Link
-  Outputs a clean, structured `webscraping.csv`
-  Lightweight, fast, and easy to run

---

##  Tech Stack

| Tool            | Purpose                      |
|-----------------|------------------------------|
| Python          | Programming Language         |
| BeautifulSoup4  | HTML Parsing (Web Scraping)  |
| Requests        | Sending HTTP Requests        |
| Pandas          | Data Structuring & CSV Output|

---

##  Output Sample

| Name               | Price    | Rating | Image URL           | Product Link             |
|--------------------|----------|--------|----------------------|---------------------------|
| Redmi Note 13 Pro  | ₹19,999  | 4.3    | https://...image.jpg | https://flipkart.com/...  |
| Mi 11X 5G          | ₹27,999  | 4.4    | https://...image2.jpg| https://flipkart.com/...  |

>  Scrapes top 20 listings by default.

---

##  Installation

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/flipkart-mobile-scraper.git
cd flipkart-mobile-scraper
