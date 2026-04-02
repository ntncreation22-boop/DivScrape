import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
from pathlib import Path

# Save to docs folder for GitHub Pages
DATA_FILE = Path("docs/data.json")

def parse_date(date_string):
    """Parse date string in various formats"""
    if not date_string:
        return None
    try:
        return datetime.strptime(date_string.strip(), "%d %b %Y").strftime("%Y-%m-%d")
    except:
        return date_string.strip()

def scrape_cse_dividends(start_date=None, end_date=None):
    """
    Scrape CSE dividend announcements
    Args:
        start_date: Format DD/MM/YYYY (defaults to 1st of current month)
        end_date: Format DD/MM/YYYY (defaults to today)
    """
    # Use dynamic dates if not provided
    if not start_date or not end_date:
        today = datetime.now()
        first_day = today.replace(day=1)
        start_date = first_day.strftime("%d/%m/%Y")
        end_date = today.strftime("%d/%m/%Y")
    url = "https://www.cse.lk/general-announcements"
    
    # Build the request with parameters
    params = {
        "id": "36429",
        "type": "CASH+DIVIDEND",
        "category": "CASH+DIVIDEND"
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        print(f"Scraping from {start_date} to {end_date}...")
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all announcement items
        announcements = []
        announcement_items = soup.find_all('div', class_='announcement-item')
        
        if not announcement_items:
            # Try alternative selector
            announcement_items = soup.find_all('div', {'data-announcement-id': True})
        
        for item in announcement_items:
            try:
                # Extract company name
                company_name_elem = item.find(['h3', 'h4', 'span'], class_=lambda x: x and 'title' in x.lower() if x else False)
                if not company_name_elem:
                    company_name_elem = item.find_all('div')[0] if item.find_all('div') else None
                
                company_name = company_name_elem.get_text(strip=True) if company_name_elem else "Unknown"
                
                # Extract dates and dividend info - look for text patterns
                text_content = item.get_text()
                
                xd_date = extract_field_value(text_content, "XD date") or extract_field_value(text_content, "Record Date")
                voting_dividend = extract_field_value(text_content, "Voting dividend") or extract_field_value(text_content, "voting dividend per share")
                payment_date = extract_field_value(text_content, "Payment Date") or extract_field_value(text_content, "payment date")
                announcement_date = extract_field_value(text_content, "Announcement Date") or extract_field_value(text_content, "Date of initial")
                
                if xd_date or voting_dividend or payment_date:
                    announcement = {
                        "company_name": company_name,
                        "xd_date": parse_date(xd_date),
                        "voting_dividend_per_share": voting_dividend,
                        "payment_date": parse_date(payment_date),
                        "announcement_date": parse_date(announcement_date),
                        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    announcements.append(announcement)
            except Exception as e:
                print(f"Error parsing item: {e}")
                continue
        
        if announcements:
            save_dividends(announcements)
            print(f"Scraped {len(announcements)} announcements")
            return announcements
        else:
            print("No announcements found")
            return []
    
    except Exception as e:
        print(f"Error scraping CSE: {e}")
        return []

def extract_field_value(text, field_name):
    """Extract field value from text using regex"""
    # Look for pattern: "field_name: value" or "field_name\nvalue"
    patterns = [
        rf"{field_name}\s*:\s*([^\n]+)",
        rf"{field_name}\s*\n\s*([^\n]+)",
        rf"{field_name}\s+([^\n]+)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).strip()
            if value and value != "-":
                return value
    return None

def save_dividends(announcements):
    """Save announcements to JSON file"""
    # Load existing data
    data = load_dividends()
    
    # Add new announcements (append mode as per user request)
    for announcement in announcements:
        data.append(announcement)
    
    # Save to file
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Data saved to {DATA_FILE}")

def load_dividends():
    """Load dividends from JSON file"""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def get_dividends_by_date(start_date=None, end_date=None):
    """Get dividends filtered by date range"""
    data = load_dividends()
    
    if not start_date and not end_date:
        return data
    
    filtered = []
    for item in data:
        xd_date = item.get('xd_date')
        if xd_date:
            if start_date and xd_date < start_date:
                continue
            if end_date and xd_date > end_date:
                continue
            filtered.append(item)
    
    return filtered

if __name__ == "__main__":
    # Test scraping
    scrape_cse_dividends()
