# CSE Dividend Announcements Scraper

A Python-based web scraper that automatically fetches dividend announcements from the Colombo Stock Exchange (CSE) and displays them in an interactive web dashboard.

## Features

✅ **Automated Scraping** - Runs automatically at scheduled times: 08:00 AM, 10:00 AM, 12:00 PM, 3:00 PM, and 8:00 PM  
✅ **Web Dashboard** - Beautiful, responsive HTML/CSS interface  
✅ **Data Filtering** - Filter dividend data by date range  
✅ **Real-time Updates** - Appends new data as it's scraped  
✅ **Statistics** - Shows total records and last scrape time  
✅ **JSON Storage** - Data stored in JSON format for easy access  

## Project Structure

```
DivScrape/
│
├── app.py                  # Flask web server with integrated scheduler
├── scraper.py             # Web scraper for CSE announcements
├── scheduler.py           # APScheduler configuration (optional standalone)
├── requirements.txt       # Python dependencies
│
├── templates/
│   └── index.html         # Web page template
│
├── static/
│   └── style.css          # Styling for web interface
│
├── dividends_data.json    # Data storage file (auto-created)
├── scheduler.log          # Scheduler logs
│
├── run.bat                # Windows startup script
└── run.sh                 # Linux/Mac startup script
```

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- Flask 2.3.2
- requests 2.31.0
- beautifulsoup4 4.11.1
- APScheduler 3.10.1
- python-dotenv 1.0.0

### 2. Run the Application

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
bash run.sh
```

Or manually:
```bash
python app.py
```

## Usage

### Web Interface

Once running, open your browser and navigate to:
```
http://localhost:5000
```

### Web Dashboard Features

1. **Date Range Filtering**
   - Select start and end dates
   - Click "Filter" to see data for that range
   - Click "Reset" to return to default date range

2. **Data Table**
   - Displays company names
   - XD Date (Ex-Dividend Date)
   - Dividend Per Share amount (in Rs.)
   - Payment Date
   - Announcement Date
   - Data retrieval timestamp

3. **Statistics**
   - Total records scraped
   - Last scrape timestamp

### API Endpoints

Get filtered dividend data:
```
GET /api/dividends?start_date=2026-01-01&end_date=2026-03-31
```

Get all dividend data:
```
GET /api/dividends/all
```

Get statistics:
```
GET /api/stats
```

## Automatic Scheduling

The application runs scraping jobs at these times every day:
- 08:00 AM
- 10:00 AM
- 12:00 PM
- 03:00 PM
- 08:00 PM

New data is automatically appended to the JSON file. Check `scheduler.log` for detailed logs.

## Data Storage

Scraped data is stored in `dividends_data.json` with the following structure:

```json
[
  {
    "company_name": "KEGALLE PLANTATIONS PLC",
    "xd_date": "2026-03-30",
    "voting_dividend_per_share": "3.00",
    "payment_date": "2026-04-10",
    "announcement_date": "2026-03-30",
    "scraped_at": "2026-03-30 09:12:18"
  }
]
```

## Configuration

### Change Scraping Schedule

Edit `app.py` and modify the `job_times` list in the `start_scheduler()` function:

```python
job_times = [
    ('08', '00', '8:00 AM'),
    ('10', '00', '10:00 AM'),
    # Add/modify times as needed
]
```

### Change Port

In `app.py`, modify the last line:
```python
app.run(debug=False, host='0.0.0.0', port=5000)  # Change 5000 to desired port
```

### Change Default Date Range

In `templates/index.html`, update:
```html
<input type="date" id="start_date" value="2026-01-01">
<input type="date" id="end_date" value="2026-03-31">
```

## Troubleshooting

### "Cannot connect to server"
- Ensure Flask app is running on the correct port
- Check firewall settings
- Try `http://127.0.0.1:5000` instead of `localhost`

### "No data found"
- Run manual scrape: `python scraper.py`
- Check internet connection
- Review `scheduler.log` for errors

### Scheduler not running jobs
- Check `scheduler.log`
- Ensure system time is correct
- Verify APScheduler is installed: `pip install APScheduler`

## Performance Notes

- Initial scraping may take 10-30 seconds depending on internet speed
- JSON file size grows with each scrape (~1-5 KB per announcement)
- Multiple scheduler runs append all data (no duplicates processing by default)

## Notes

- Data is appended to the JSON file on each scrape (duplicates are not removed)
- The date range selector **automatically updates to today** when you open the page
- Display range: Last 30 days to today (auto-updated each day)
- All dates are stored in YYYY-MM-DD format for consistency
- Scraper pulls data from 1st of current month to today automatically

## Support

For issues with the CSE website structure or scraping, the HTML parsing may need adjustment in `scraper.py` based on CSE website updates.

## License

Free to use for personal and educational purposes.
