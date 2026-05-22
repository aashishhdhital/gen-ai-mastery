"""
🌐 WEB SCRAPER - Phase 1 Project

This program demonstrates web scraping by extracting data from websites
and saving it to a file.

Concepts covered:
- External libraries (requests, BeautifulSoup)
- HTTP requests
- HTML parsing
- Data extraction
- File operations
- Error handling

Author: Gen AI Mastery
Date: 2025

IMPORTANT: Always respect website terms of service and robots.txt!
"""

import time
from scraper import scrape_quotes, scrape_weather, save_to_csv, save_to_json


def display_menu():
    """
    Display the scraper menu
    """
    print("\n" + "="*50)
    print("     🌐 WEB SCRAPER - Phase 1 Project")
    print("="*50)
    print("\nChoose what to scrape:")
    print("  1. Quotes (from quotes.toscrape.com)")
    print("  2. Weather Info (demo example)")
    print("  3. Exit")
    print("="*50)


def get_user_choice():
    """
    Get valid user choice
    
    Returns:
        str: User's choice (1-3)
    """
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("❌ Invalid choice! Please enter 1, 2, or 3.")


def scrape_quotes_menu():
    """
    Handle quotes scraping
    """
    print("\n🔄 Scraping quotes from quotes.toscrape.com...")
    print("This may take a moment...\n")
    
    try:
        quotes_data = scrape_quotes()
        
        if not quotes_data:
            print("❌ No data was scraped.")
            return
        
        print(f"\n✅ Successfully scraped {len(quotes_data)} quotes!")
        
        # Show sample
        print("\n📊 Sample quotes:")
        for i, quote in enumerate(quotes_data[:3], 1):
            print(f"\n{i}. {quote.get('text', 'N/A')[:100]}...")
            print(f"   Author: {quote.get('author', 'Unknown')}")
        
        # Ask user to save
        save = input("\nDo you want to save to file? (yes/no): ").lower().strip()
        if save in ['yes', 'y']:
            save_to_csv(quotes_data, 'quotes.csv')
            print("✅ Data saved to quotes.csv")
    
    except Exception as e:
        print(f"❌ Error scraping quotes: {e}")


def scrape_weather_menu():
    """
    Handle weather scraping (demo)
    """
    print("\n🔄 Fetching weather data...")
    print("Note: This is a demo using mock data.\n")
    
    try:
        weather_data = scrape_weather()
        
        print("✅ Weather data retrieved!")
        print("\n📊 Weather Information:")
        for city, info in weather_data.items():
            print(f"\n{city}:")
            print(f"  Temperature: {info['temperature']}°C")
            print(f"  Condition: {info['condition']}")
            print(f"  Humidity: {info['humidity']}%")
        
        # Ask user to save
        save = input("\nDo you want to save to file? (yes/no): ").lower().strip()
        if save in ['yes', 'y']:
            save_to_json(weather_data, 'weather.json')
            print("✅ Data saved to weather.json")
    
    except Exception as e:
        print(f"❌ Error fetching weather: {e}")


def main():
    """
    Main program loop
    """
    print("\n" + "="*50)
    print("  Welcome to Web Scraper!")
    print("="*50)
    print("\nLearn how to:")
    print("  • Make HTTP requests")
    print("  • Parse HTML")
    print("  • Extract data from websites")
    print("  • Save data to files")
    print("\n⚠️  Always respect website terms of service!\n")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            scrape_quotes_menu()
        elif choice == "2":
            scrape_weather_menu()
        elif choice == "3":
            print("\n👋 Thank you for using Web Scraper! Goodbye!\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program cancelled by user.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
