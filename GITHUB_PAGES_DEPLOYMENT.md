# GitHub Pages + GitHub Actions Deployment Guide

## 📋 Prerequisites

- GitHub account (free)
- Git installed on your computer
- Your CSE scraper project ready

---

## 🚀 Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **"New repository"** button
3. Enter repository name: `cse-dividend-scraper` (or any name)
4. **IMPORTANT: Make it PUBLIC** for GitHub Pages free tier
5. Click **"Create repository"**

---

## 📤 Step 2: Initialize Git Locally

In your project folder (`D:\DivScrape`), open PowerShell:

```powershell
# Initialize git repository
git init

# Add remote (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: CSE Dividend Scraper"

# Push to main branch
git branch -M main
git push -u origin main
```

---

## 🔧 Step 3: Configure GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top right)
3. Scroll to **"Pages"** section (left sidebar)
4. Under "Build and deployment":
   - **Source**: Select `Deploy from a branch`
   - **Branch**: Select `main`
   - **Folder**: Select `/docs`
5. Click **"Save"**

GitHub will show your site URL: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

---

## 🔑 Step 4: Give GitHub Actions Permission

1. Go to **Settings** → **Actions** → **General** (left sidebar)
2. Scroll to **"Workflow permissions"**
3. Select: **"Read and write permissions"**
4. Check: **"Allow GitHub Actions to create and approve pull requests"**
5. Click **"Save"**

This lets GitHub Actions push the scraped data back to your repo.

---

## 🎯 Step 5: Update index.html with Your URL

1. Edit `docs/index.html`
2. Find this line (around line 76):
   ```javascript
   const url = 'https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/docs/data.json';
   ```
3. Replace `YOUR_USERNAME` and `YOUR_REPO` with your actual values
4. Save and commit:
   ```powershell
   git add docs/index.html
   git commit -m "Update data URL for GitHub"
   git push
   ```

---

## ✅ Step 6: Test Everything

### Test Scraper Manually (Optional)

```powershell
pip install -r requirements.txt
python scraper.py
```

This creates `docs/data.json` locally. Check if it has data.

### Test GitHub Actions

1. Go to your GitHub repository
2. Click **Actions** tab
3. Click **"CSE Dividend Scraper"** workflow
4. Click **"Run workflow"** → **"Run workflow"**

Wait 30 seconds, then refresh. You should see:
- ✅ Green checkmark = Success
- Check **"Commits"** to see the automated commit
- Check `docs/data.json` to verify data was updated

---

## 🌐 Access Your Website

Your website is now live at:

```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

**Example:**
```
https://john-doe.github.io/cse-dividend-scraper/
```

Share this URL with anyone!

---

## 📅 Automatic Schedule

GitHub Actions will run the scraper at these times **every day** (Sri Lanka Time):

- ⏰ 08:00 AM
- ⏰ 10:00 AM
- ⏰ 12:00 PM
- ⏰ 03:00 PM
- ⏰ 08:00 PM

Data automatically updates in `docs/data.json` and pushes to your repo.

---

## 🔍 Monitor Scheduled Runs

1. Go to **Actions** tab in your repository
2. Click **"CSE Dividend Scraper"**
3. See all past runs with timestamps
4. Click a run to see logs/details

---

## 🛠️ Troubleshooting

### Website shows "Loading data..." forever
- **Problem**: URL not updated in `docs/index.html`
- **Solution**: Update the GitHub URL in the JavaScript code (Step 5)

### GitHub Actions not running at scheduled times
- **Problem**: Workflow disabled or permissions not set
- **Solution**: Check Actions tab, re-enable workflow, verify permissions (Step 4)

### Data not updating
- **Problem**: Scraper failed or no new data available
- **Solution**: Check Actions workflow logs for errors

### "Cannot find GitHub repository"
- **Problem**: Repository not public
- **Solution**: Go Settings → Visibility → Make it Public

---

## 📝 Making Changes Later

If you want to modify the project:

```powershell
# Make changes to files
# ...

# Commit and push
git add .
git commit -m "Your change description"
git push
```

Changes take effect immediately!

---

## 🎉 You're Done!

Your CSE Dividend Scraper is now:

✅ Automatically scraping data at scheduled times  
✅ Saving data to GitHub  
✅ Displaying on a live website  
✅ Completely free (GitHub Pages + GitHub Actions)  

**Share your live URL:**
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

---

## 📚 Additional Commands

```powershell
# Check git status
git status

# View commit history
git log --oneline

# Pull latest changes from GitHub
git pull origin main

# Force push (careful!)
git push -u origin main --force
```

---

## 💡 Tips

1. **Update README**: Add your live website URL to your repository README
2. **Monitor Data**: Check website regularly to see new dividend announcements
3. **Backup**: Your data is version controlled on GitHub - safe from loss!
4. **Share**: Send your live URL to others to view dividend data

---

## 🔗 Useful Links

- [GitHub Pages Documentation](https://pages.github.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Your Repository](https://github.com/YOUR_USERNAME/YOUR_REPO)
- [Your Live Website](https://YOUR_USERNAME.github.io/YOUR_REPO/)

---

Need help? Check the Actions logs on GitHub for detailed error messages!
