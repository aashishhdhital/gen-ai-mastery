# 🌐 Project 3: Web Scraper

## 📌 Overview
Scrape data from websites and save it to a file. This project demonstrates working with external libraries and HTTP requests.

## 🎯 Learning Objectives
- ✅ Modules and packages (importing libraries)
- ✅ HTTP requests (requests library)
- ✅ HTML parsing (BeautifulSoup)
- ✅ Data extraction and processing
- ✅ File writing (saving data)
- ✅ Error handling for network requests

## 📂 Project Structure
```
03-web-scraper/
├── main.py          # Main web scraper program
├── scraper.py       # Scraping functions
└── README.md        # This file
```

## 🚀 How to Run

### Step 1: Install required libraries
```bash
pip install requests beautifulsoup4
```

### Step 2: Run the scraper
```bash
cd 03-web-scraper
python main.py
```

### Step 3: Follow the prompts
```
🌐 Web Scraper - Phase 1 Project
================================

Choose what to scrape:
1. Quotes (from quotes.toscrape.com)
2. Weather (basic example)
3. Exit

Enter your choice (1-3): 1

✅ Scraping quotes from website...
Saving to quotes.csv...

🎉 Scraping complete! Data saved to quotes.csv
```

## 💡 Code Explanation

### Key Concepts

1. **Importing Libraries**: Use external packages
   ```python
   import requests
   from bs4 import BeautifulSoup
   ```

2. **HTTP Requests**: Fetch web pages
   ```python
   response = requests.get('https://example.com')
   html_content = response.text
   ```

3. **HTML Parsing**: Extract data from HTML
   ```python
   soup = BeautifulSoup(html_content, 'html.parser')
   titles = soup.find_all('h1')
   ```

4. **Data Processing**: Clean and format data
   ```python
   data = []
   for item in items:
       data.append(item.text.strip())
   ```

5. **File Writing**: Save scraped data
   ```python
   with open('output.csv', 'w') as file:
       file.write(data)
   ```

## ⚠️ Important: Web Scraping Ethics

**Before scraping any website:**
1. Check the website's `robots.txt` file
2. Read their Terms of Service
3. Don't overload servers with requests
4. Use delays between requests
5. Respect the website's resources

**Example of ethical scraping:**
```python
import time

for page in pages:
    scrape_page(page)
    time.sleep(2)  # Wait 2 seconds between requests
```

## 🎓 Practice Challenges

### Level 1 (Easy)
- [ ] Scrape article titles from a news site
- [ ] Extract product names from an e-commerce site
- [ ] Save data to a text file instead of CSV

### Level 2 (Medium)
- [ ] Add pagination (scrape multiple pages)
- [ ] Extract multiple fields (title, price, rating)
- [ ] Save to JSON format
- [ ] Add delays between requests

### Level 3 (Hard)
- [ ] Scrape JavaScript-rendered content (Selenium)
- [ ] Create a database with sqlite3
- [ ] Build a schedule to scrape periodically
- [ ] Handle and log errors

## 📚 Key Takeaways

✨ **What You'll Learn:**
- How to use external libraries
- How to make HTTP requests
- How to parse and extract data from HTML
- How to save data to files
- How to handle errors gracefully

## ⚙️ Installation Troubleshooting

**If pip install fails:**
```bash
# On Windows
python -m pip install requests beautifulsoup4

# On macOS/Linux
python3 -m pip install requests beautifulsoup4
```

**Verify installation:**
```bash
python -c "import requests; import bs4; print('✅ Success!')"
```

---

**Congratulations! You've completed Phase 1 Projects!** 🎉

Next: Move on to Phase 2 - NumPy & Pandas!
