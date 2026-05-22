"""
Web Scraper Module

This module contains functions for scraping data from websites.

Concepts demonstrated:
- External library usage (requests, BeautifulSoup)
- HTTP requests
- HTML parsing
- Data extraction
- Error handling

IMPORTANT: Always check robots.txt and terms of service before scraping!
"""

import csv
import json
from datetime import datetime


def scrape_quotes():
    """
    Scrape quotes from quotes.toscrape.com
    
    This website is specifically designed for learning web scraping,
    so it's perfect for beginners!
    
    Returns:
        list: List of dictionaries containing quotes and authors
    
    Example return:
        [
            {"text": "Quote text here", "author": "Author Name"},
            {...}
        ]
    """
    try:
        # Import required libraries
        import requests
        from bs4 import BeautifulSoup
        
        # URL of the website (designed for learning web scraping)
        url = "http://quotes.toscrape.com/"
        
        print(f"🌐 Connecting to {url}...")
        
        # Make HTTP GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error if request fails
        
        print("✅ Connected successfully!")
        print("🔍 Parsing HTML content...")
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all quote containers
        quotes = []
        quote_containers = soup.find_all('div', class_='quote')
        
        print(f"Found {len(quote_containers)} quotes\n")
        
        # Extract data from each quote
        for container in quote_containers:
            # Extract quote text
            text_element = container.find('span', class_='text')
            text = text_element.get_text(strip=True) if text_element else 'N/A'
            
            # Extract author
            author_element = container.find('small', class_='author')
            author = author_element.get_text(strip=True) if author_element else 'Unknown'
            
            # Extract tags
            tags_elements = container.find_all('a', class_='tag')
            tags = [tag.get_text(strip=True) for tag in tags_elements]
            
            # Store quote data
            quotes.append({
                'text': text,
                'author': author,
                'tags': tags
            })
        
        return quotes
    
    except ImportError:
        print("\n❌ Error: Required libraries not installed!")
        print("Please run: pip install requests beautifulsoup4")
        return []
    except Exception as e:
        print(f"\n❌ Error scraping quotes: {e}")
        return []


def scrape_weather():
    """
    Demo function that returns mock weather data
    
    In a real scenario, you would make an HTTP request to a weather API.
    This demonstrates the concept without requiring API keys.
    
    Returns:
        dict: Dictionary with weather information
    
    Example return:
        {
            "New York": {"temperature": 22, "condition": "Sunny", "humidity": 65},
            ...
        }
    """
    # Mock data (in real scenario, this would come from an API)
    weather_data = {
        "New York": {
            "temperature": 22,
            "condition": "Sunny",
            "humidity": 65,
            "wind_speed": "15 km/h"
        },
        "London": {
            "temperature": 18,
            "condition": "Cloudy",
            "humidity": 75,
            "wind_speed": "12 km/h"
        },
        "Tokyo": {
            "temperature": 25,
            "condition": "Rainy",
            "humidity": 80,
            "wind_speed": "18 km/h"
        }
    }
    
    return weather_data


def save_to_csv(data, filename):
    """
    Save scraped data to CSV file
    
    Parameters:
        data (list): List of dictionaries to save
        filename (str): Output filename
    
    Example:
        >>> save_to_csv(quotes, 'quotes.csv')
    """
    try:
        if not data:
            print("No data to save.")
            return
        
        # Get keys from first item
        keys = data[0].keys()
        
        # Write to CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"\n✅ Data saved to {filename}")
    
    except Exception as e:
        print(f"\n❌ Error saving to CSV: {e}")


def save_to_json(data, filename):
    """
    Save data to JSON file
    
    Parameters:
        data (dict or list): Data to save
        filename (str): Output filename
    
    Example:
        >>> save_to_json(weather_data, 'weather.json')
    """
    try:
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Data saved to {filename}")
    
    except Exception as e:
        print(f"\n❌ Error saving to JSON: {e}")


def validate_url(url):
    """
    Check if URL is valid
    
    Parameters:
        url (str): URL to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    return url.startswith(('http://', 'https://'))


def get_data_safely(url, timeout=10):
    """
    Make HTTP request with error handling
    
    Parameters:
        url (str): URL to request
        timeout (int): Request timeout in seconds
    
    Returns:
        requests.Response: Response object or None if error
    """
    try:
        import requests
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response
    except ImportError:
        print("Error: 'requests' library not installed")
        return None
    except Exception as e:
        print(f"Error making request: {e}")
        return None
