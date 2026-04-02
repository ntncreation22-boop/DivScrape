# 🚀 GitHub Pages Deployment - 5 Minutes Setup

## ✅ What You Have

Your CSE Dividend Scraper is **ready to deploy** with:
- ✓ Web scraper (`scraper.py`)
- ✓ Static website (`docs/index.html`)
- ✓ Automatic scheduler (`.github/workflows/scrape.yml`)
- ✓ Sample data (`docs/data.json`)

---

## 📋 Step-by-Step Deployment

### **STEP 1: Create GitHub Account** (if you don't have one)
Go to [github.com](https://github.com) and sign up - it's free!

---

### **STEP 2: Create Repository**

1. Click "+" icon → **New repository**
2. Enter name: `cse-dividend-scraper`
3. **IMPORTANT: Select "Public"** (required for free GitHub Pages)
4. Click **Create repository**

---

### **STEP 3: Get Your Repository URL**

After creating, you'll see a URL like:
```
https://github.com/YOUR_USERNAME/cse-dividend-scraper
```

Save this! Replace in commands below:
- `YOUR_USERNAME` = your GitHub username
- `YOUR_REPO` = `cse-dividend-scraper`

---

### **STEP 4: Push Code to GitHub**

In PowerShell, go to your project:

```powershell
cd D:\DivScrape

# Initialize and configure git
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"

# Add GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/cse-dividend-scraper.git

# Add all files and commit
git add .
git commit -m "Initial commit: CSE Dividend Scraper"

# Push to GitHub
git branch -M main
git push -u origin main
```

*If you get auth errors, use Personal Access Token instead of password*

---

### **STEP 5: Update Website URL**

1. Open: `docs/index.html`
2. Find line 76:
   ```javascript
   const url = 'https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/docs/data.json';
   ```
3. Replace `YOUR_USERNAME` and `YOUR_REPO`
4. Save file
5. Push to GitHub:
   ```powershell
   git add docs/index.html
   git commit -m "Update data URL"
   git push
   ```

---

### **STEP 6: Enable GitHub Pages**

1. Go to your GitHub repository
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Source":
   - Select `Deploy from a branch`
   - Select branch: `main`
   - Select folder: `/docs`
5. Click **Save**

**You'll see your site URL:**
```
https://YOUR_USERNAME.github.io/cse-dividend-scraper/
```

---

### **STEP 7: Allow GitHub Actions to Push**

1. Go to **Settings** → **Actions** → **General**
2. Scroll to "Workflow permissions"
3. Select: **"Read and write permissions"**
4. Check: **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

---

### **STEP 8: Test Everything**

1. Go to your repository
2. Click **Actions** tab
3. Click **"CSE Dividend Scraper"** workflow
4. Click **"Run workflow"** → **"Run workflow"**
5. Wait 30 seconds, then refresh

You should see ✅ **green checkmark** = Success!

---

### **STEP 9: Visit Your Live Website**

Open in browser:
```
https://YOUR_USERNAME.github.io/cse-dividend-scraper/
```

You should see:
- ✓ Beautiful dashboard
- ✓ Dividend data table
- ✓ Date filters
- ✓ Statistics

**🎉 You're live!**

---

## 🎯 Daily Automatic Updates

Your scraper runs **every day** at:
- 8:00 AM (Sri Lanka Time)
- 10:00 AM
- 12:00 PM
- 3:00 PM
- 8:00 PM

Data automatically updates on your website!

---

## 📝 Common Commands

```powershell
# Check what will be pushed
git status

# See recent commits
git log --oneline

# Update and push after making changes
git add .
git commit -m "Your message"
git push
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Website shows "Loading data..." | Update URL in `docs/index.html` line 76 & push |
| GitHub Actions not running | Check permissions set to "Read and write" (Step 7) |
| Want to disable scheduling | Disable workflow in Actions tab |
| Want to change times | Edit `.github/workflows/scrape.yml` and push |

---

## 🔐 Keep Your Credentials Safe

Never put passwords or API keys in your code!  
If you need them, use GitHub Secrets (Settings → Secrets and variables)

---

## 📊 Monitor Your Scraper

Check if it's working:

1. Go to repository → **Actions** tab
2. Click **"CSE Dividend Scraper"**
3. See all runs with ✅ or ❌ status
4. Click a run to see detailed logs

---

## ✨ Share Your Website

Give this URL to anyone:
```
https://YOUR_USERNAME.github.io/cse-dividend-scraper/
```

They can view live dividend data without any setup!

---

## 🎓 Learn More

- [GitHub Pages Help](https://pages.github.com/)
- [GitHub Actions Help](https://docs.github.com/en/actions)
- [Git Basics](https://git-scm.com/book/en/v2)

---

## ✅ You're Done!

Your CSE Dividend Scraper is:
- ✅ Live on GitHub Pages
- ✅ Automatically scraping data
- ✅ Free forever
- ✅ Ready to share!

**Next:** Share your website URL with others! 🚀

---

**Questions?** Check the detailed guide: [GITHUB_PAGES_DEPLOYMENT.md](GITHUB_PAGES_DEPLOYMENT.md)
