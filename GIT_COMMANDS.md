# 🎯 GitHub Deployment Commands (Copy & Paste)

## ⚠️ Prerequisites

- GitHub account created at [github.com](https://github.com)
- GitHub repository created (name: `cse-dividend-scraper`)
- Git installed on your computer

---

## 🔧 Step 1: Initial Setup (Run Once)

Open PowerShell in your project folder (`D:\DivScrape`) and run:

```powershell
cd D:\DivScrape

git init

git config user.name "Your Name"
git config user.email "your-email@gmail.com"

git remote add origin https://github.com/YOUR_USERNAME/cse-dividend-scraper.git

git add .

git commit -m "Initial commit: CSE Dividend Scraper with GitHub Pages"

git branch -M main

git push -u origin main
```

**Replace:**
- `Your Name` with your name
- `your-email@gmail.com` with your email
- `YOUR_USERNAME` with your GitHub username

**First time pushing?** You'll be prompted to authenticate:
- Use your GitHub username
- For password, use a Personal Access Token (see below if needed)

---

## 🔑 If Authentication Fails

Create a Personal Access Token:

1. Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token"
3. Check these boxes:
   - `repo`
   - `workflow`
4. Copy the token
5. When PowerShell asks for password, paste the token

Then retry the push command above.

---

## 📝 Step 2: Update Website URL

```powershell
# Open the file and edit line ~76
# Change this line:
# const url = 'https://raw.githubusercontent.com/YOUR_USERNAME/cse-dividend-scraper/main/docs/data.json';
# 
# Replace YOUR_USERNAME with your actual GitHub username

git add docs/index.html

git commit -m "Update data URL for GitHub"

git push
```

---

## ✅ Step 3: Enable GitHub Pages

**Do this on GitHub website** (not in PowerShell):

1. Go to repository → Settings
2. Click Pages (left sidebar)
3. Under "Source":
   - Select `Deploy from a branch`
   - Select branch: `main`
   - Select folder: `/docs`
4. Click Save

Then wait 1-2 minutes for GitHub to build your site.

---

## 🔐 Step 4: Allow GitHub Actions

**Do this on GitHub website**:

1. Go to repository → Settings
2. Click Actions → General (left sidebar)
3. Under "Workflow permissions":
   - Select `Read and write permissions`
   - Check `Allow GitHub Actions to create and approve pull requests`
4. Click Save

---

## 🧪 Step 5: Test GitHub Actions

**Do this on GitHub website**:

1. Go to your repository
2. Click Actions tab
3. Click "CSE Dividend Scraper"
4. Click "Run workflow" button
5. Click "Run workflow" again to confirm

Wait 30 seconds, then refresh. You should see a ✅ green checkmark.

---

## 🌐 Step 6: Visit Your Site

Open in browser:

```
https://YOUR_USERNAME.github.io/cse-dividend-scraper/
```

Replace `YOUR_USERNAME` with your actual GitHub username.

You should see:
- ✅ Beautiful dashboard
- ✅ Dividend data table
- ✅ Sample data showing

---

## 📝 Updating Code Later

If you make changes to your project:

```powershell
cd D:\DivScrape

git add .

git commit -m "Describe what changed"

git push
```

Changes deploy automatically!

---

## 🧹 Optional: Clean Up Old Files

These aren't needed for GitHub Pages, but kept for reference:

```powershell
git rm --cached app.py scheduler.py
git rm -r --cached templates/
git rm -r --cached static/
git rm --cached run.bat run.sh test_scraper.py

git commit -m "Remove local-only files"
git push
```

---

## 🔄 Daily Operations

### Check if scraper ran:

Go to repository → Actions tab → "CSE Dividend Scraper" → See all runs

### Manually trigger scraper:

1. Actions tab
2. "CSE Dividend Scraper" workflow
3. "Run workflow"
4. "Run workflow" (confirm)

### Update scraper:

```powershell
# Edit scraper.py
# Then:
git add scraper.py
git commit -m "Updated scraping logic"
git push
```

---

## 🆘 Troubleshooting Commands

### Check git status:
```powershell
git status
```

### See recent commits:
```powershell
git log --oneline -5
```

### View remote URL:
```powershell
git remote -v
```

### Force push (use only if needed):
```powershell
git push -u origin main --force
```

### Reset to last commit:
```powershell
git reset --hard HEAD
```

---

## 📋 Success Checklist

Run these commands to verify:

```powershell
# Check git is initialized
git status

# Check remote is GitHub
git remote -v

# Check branch is main
git branch

# Check files are committed
git log --oneline -1
```

You should see:
- ✅ Status: "On branch main"
- ✅ Remote: "origin https://github.com/YOUR_USERNAME/cse-dividend-scraper.git"
- ✅ Branch: `* main`
- ✅ Latest commit message visible

---

## 🎉 All Done!

Your site is now live at:
```
https://YOUR_USERNAME.github.io/cse-dividend-scraper/
```

Data updates automatically every day! 🚀

---

## 📚 Quick Reference

| Command | What It Does |
|---------|------------|
| `git status` | Show what's changed |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit changes locally |
| `git push` | Push to GitHub |
| `git pull` | Get latest from GitHub |
| `git log --oneline` | See commit history |
| `git diff` | See what changed |

---

## 💡 Pro Tips

1. **Commit often** - Small commits are easier to debug
2. **Clear messages** - "Fixed bug" is better than "update"
3. **Pull before pushing** - Avoid conflicts: `git pull` then `git push`
4. **Check Actions logs** - If scraper fails, Actions tab shows why

---

Need help? Check: [DEPLOY_5MIN.md](DEPLOY_5MIN.md)
