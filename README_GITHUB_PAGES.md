# CSE Dividend Announcements Scraper

## 📊 Live Website

**Your live website will be at:**
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

*(Replace `YOUR_USERNAME` and `YOUR_REPO` with your actual GitHub credentials)*

---

## ✨ Features

✅ **Automatic Scraping** - Runs every day at 8AM, 10AM, 12PM, 3PM, 8PM (Sri Lanka Time)  
✅ **GitHub Pages Dashboard** - Beautiful, responsive web interface  
✅ **Real-time Data** - Fetches latest dividend announcements from CSE  
✅ **Data Filtering** - Filter announcements by date range  
✅ **Zero Cost** - Completely free hosting via GitHub Pages + GitHub Actions  
✅ **Version Controlled** - All data backed up on GitHub  

---

## 🚀 Quick Start

### For Deployment (Recommended)

See [GITHUB_PAGES_DEPLOYMENT.md](GITHUB_PAGES_DEPLOYMENT.md) for step-by-step instructions to:

1. Create GitHub repository
2. Deploy to GitHub Pages
3. Set up automatic scheduling
4. Go live!

### For Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper manually
python scraper.py

# This creates/updates docs/data.json
```

---

## 📁 Project Structure

```
CSE-Dividend-Scraper/
│
├── .github/
│   └── workflows/
│       └── scrape.yml              ← Automated scheduling
│
├── docs/                           ← GitHub Pages folder
│   ├── index.html                  ← Main website
│   ├── style.css                   ← Styling
│   └── data.json                   ← Dividend data (auto-updated)
│
├── scraper.py                      ← Web scraper
├── requirements.txt                ← Dependencies
│
├── GITHUB_PAGES_DEPLOYMENT.md      ← Deployment guide
└── README.md                       ← This file
```

---

## 🗓️ Automatic Schedule

Once deployed, GitHub Actions runs the scraper automatically:

| Time | Day |
|------|-----|
| 08:00 AM | Every day |
| 10:00 AM | Every day |
| 12:00 PM | Every day |
| 03:00 PM | Every day |
| 08:00 PM | Every day |

*(Times shown in Sri Lanka Time - UTC+5:30)*

---

## 📊 Data Display

The website shows a table with:

| Column | Data |
|--------|------|
| Company Name | Listed company name |
| XD Date | Ex-Dividend Date |
| Dividend Per Share | Amount in Rs. |
| Payment Date | When dividend is paid |
| Announcement Date | When announced |
| Data Retrieved | Scrape timestamp |

**Features:**
- ✅ Auto-updates date range to today
- ✅ Filters by date range
- ✅ Shows statistics (total records, last updated)
- ✅ Responsive (works on mobile, tablet, desktop)

---

## 🔄 How It Works

### Architecture

```
┌─────────────────────────────────────────────┐
│        GitHub Actions (Scheduled)           │
│              runs at 5 times/day            │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│           Python Scraper (scraper.py)       │
│  Fetches from: cse.lk/general-announcements │
└──────────────────┬──────────────────────────┘
                   │
                   ▼ (saves to)
┌─────────────────────────────────────────────┐
│          docs/data.json (JSON)              │
│       Updated on GitHub repository          │
└──────────────────┬──────────────────────────┘
                   │
                   ▼ (fetched by)
┌─────────────────────────────────────────────┐
│    GitHub Pages (Static Website)            │
│    https://YOUR_USERNAME.github.io/REPO/    │
│        displays live data to users          │
└─────────────────────────────────────────────┘
```

---

## 📋 Data Format

Each record in `docs/data.json`:

```json
{
  "company_name": "KEGALLE PLANTATIONS PLC",
  "xd_date": "2026-03-30",
  "voting_dividend_per_share": "3.00",
  "payment_date": "2026-04-10",
  "announcement_date": "2026-03-30",
  "scraped_at": "2026-04-02 12:00:00"
}
```

---

## 🔧 Configuration

### Change Scraping Schedule

Edit `.github/workflows/scrape.yml`:

```yaml
on:
  schedule:
    - cron: '30 2 * * *'   # 8:00 AM SLT
    - cron: '30 4 * * *'   # 10:00 AM SLT
    - cron: '30 6 * * *'   # 12:00 PM SLT
    - cron: '30 9 * * *'   # 3:00 PM SLT
    - cron: '30 14 * * *'  # 8:00 PM SLT
```

**Convert times to UTC** (Sri Lanka is UTC+5:30):
- Desired time - 5 hours 30 minutes = UTC time
- Then use cron format: `MM HH * * *`

### Change Date Range Display

Edit `docs/index.html`, find:

```javascript
const thirtyDaysAgo = new Date(Date.now() - 30*24*60*60*1000)
```

Change `30` to desired number of days.

---

## 🌐 API Endpoints

The `docs/data.json` file can be accessed via API:

```bash
# Get all dividend data
curl https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/docs/data.json
```

Use this to integrate with other applications!

---

## 👀 Monitoring

### GitHub Actions Runs

1. Go to your repository
2. Click **Actions** tab
3. Click **"CSE Dividend Scraper"** workflow
4. See all past runs with status (✅ success or ❌ failure)

### Website Availability

Your website is always available at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

No server to maintain, GitHub handles everything!

---

## 🛠️ Local Development

If you want to modify the scraper or website:

```bash
# Test scraper locally
pip install -r requirements.txt
python scraper.py

# This creates docs/data.json with latest data
# Then push to GitHub
git add .
git commit -m "Updated scraper logic"
git push
```

Changes deploy automatically!

---

## ❓ FAQ

**Q: Will this keep running if I close my computer?**  
A: Yes! GitHub Actions runs on GitHub's servers, not your computer.

**Q: Is there a cost?**  
A: No, completely free. GitHub Pages and GitHub Actions have free tiers.

**Q: Can I modify scraping times?**  
A: Yes, edit `.github/workflows/scrape.yml` and update the cron schedule.

**Q: What if CSE website structure changes?**  
A: Update the scraping logic in `scraper.py` and push changes.

**Q: Can I add more companies?**  
A: Modify the scraper parameters in `scraper.py` (currently focuses on CASH+DIVIDEND type).

**Q: How long is data kept?**  
A: All data is saved to GitHub repository indefinitely (as version history).

---

## 📞 Troubleshooting

### Website not loading
- Check if you updated the data URL in `docs/index.html`
- Verify GitHub Pages is enabled in repository settings

### Data not updating
- Check GitHub Actions runs in repository Actions tab
- Look for red ❌ marks indicating failures
- Click failed run to see error logs

### GitHub Actions failing
- Verify Python dependencies in `requirements.txt`
- Check if GitHub Actions has write permissions (Settings → Actions)
- Review workflow logs for error messages

---

## 📚 Resources

- [GitHub Pages Docs](https://pages.github.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [CSE Announcements](https://www.cse.lk/general-announcements)
- [Cron Schedule Format](https://crontab.guru/)

---

## 📄 License

Free to use for personal and educational purposes.

---

## ✅ Deployment Checklist

- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Updated DATA_FILE path in scraper.py (already done ✓)
- [ ] Updated GitHub URL in docs/index.html
- [ ] Enabled GitHub Pages (docs folder, main branch)
- [ ] Set GitHub Actions permissions to read/write
- [ ] Tested manual scraper run
- [ ] Manually triggered GitHub Actions workflow
- [ ] Verified website loads at GitHub Pages URL
- [ ] Website shows sample data
- [ ] Ready for automatic scheduling!

---

## 🚀 Next Steps

1. Follow [GITHUB_PAGES_DEPLOYMENT.md](GITHUB_PAGES_DEPLOYMENT.md)
2. Deploy to GitHub
3. Share your live URL!

**Live Site:**
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

Enjoy your live CSE Dividend Scraper! 🎉
