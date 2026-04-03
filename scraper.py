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
        date_string = date_string.strip()
        
        # Try DD-MM-YYYY format first (from API)
        try:
            return datetime.strptime(date_string, "%d-%m-%Y").strftime("%Y-%m-%d")
        except:
            pass
        
        # Try DD/MM/YYYY format
        try:
            return datetime.strptime(date_string, "%d/%m/%Y").strftime("%Y-%m-%d")
        except:
            pass
        
        # Try "D MMM YYYY" format
        try:
            return datetime.strptime(date_string, "%d %b %Y").strftime("%Y-%m-%d")
        except:
            pass
        
        # Return as-is if no format matches
        return date_string.strip()
    except:
        return date_string

def scrape_cse_dividends(start_date=None, end_date=None):
    """
    Scrape CSE dividend announcements from API
    Args:
        start_date: Format DD/MM/YYYY (defaults to 1st of current month)
        end_date: Format DD/MM/YYYY (defaults to today)
    """
    # Not used by the API anymore, but keeping for compatibility
    
    api_url = "https://www.cse.lk/api/smd"
    
    # Build the request body for POST - correct format from network inspection
    payload = {
        "allCategories": False,
        "allCompanies": True,  # Get all companies
        "categories": ["CASH DIVIDEND"]
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Origin': 'https://www.cse.lk',
        'Referer': 'https://www.cse.lk/announcements'
    }
    
    try:
        print(f"Scraping dividend announcements from CSE...")
        response = requests.post(api_url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        announcements = []
        
        # Parse API response
        # Structure: {"Announcement": {"CASH DIVIDEND": [items]}}
        if isinstance(data, dict) and 'Announcement' in data:
            announcement_data = data['Announcement']
            
            # Iterate through categories (typically "CASH DIVIDEND")
            for category_name, category_items in announcement_data.items():
                if isinstance(category_items, list):
                    for item in category_items:
                        try:
                            # Parse dates from DD-MM-YYYY format to YYYY-MM-DD
                            xd_date = item.get('xd')
                            payment_date = item.get('payment')
                            record_date = item.get('recordDate')
                            announcement_date = item.get('dateOfAnnouncement')
                            
                            announcement = {
                                "company_name": item.get('company', 'Unknown'),
                                "company_symbol": item.get('symbol'),
                                "xd_date": parse_date(xd_date),
                                "voting_dividend_per_share": item.get('votingDivPerShare'),
                                "non_voting_dividend_per_share": item.get('nonVotingDivPerShare'),
                                "payment_date": parse_date(payment_date),
                                "record_date": parse_date(record_date),
                                "announcement_date": parse_date(announcement_date),
                                "final_interim": item.get('agm'),
                                "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            }
                            # Only add if we have at least some dividend or date info
                            if announcement['xd_date'] or announcement['payment_date']:
                                announcements.append(announcement)
                        except Exception as e:
                            print(f"Error parsing item: {e}")
                            continue
        
        if announcements:
            save_dividends(announcements)
            print(f"✓ Scraped {len(announcements)} dividend announcements")
            return announcements
        else:
            print("No announcements found")
            return []
    
    except Exception as e:
        print(f"Error scraping CSE API: {e}")
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
