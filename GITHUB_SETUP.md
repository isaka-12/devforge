# 🚀 Quick GitHub Setup Guide

Follow these steps to publish DevForge to GitHub and PyPI.

## Step 1: Initialize Git (if not done)

```powershell
cd C:\Users\user\Projects\devforge
git init
git add .
git commit -m "Initial commit: DevForge v1.0.0"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `devforge`
3. Description: "Universal project scaffolder for React, FastAPI, and Flutter"
4. Public repository
5. **Don't** initialize with README (we already have one)
6. Click **Create repository**

## Step 3: Push to GitHub

```powershell
# Add remote (replace 'isakamtweve' with your username)
git remote add origin https://github.com/isakamtweve/devforge.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Set Up PyPI (One-Time)

1. **Create PyPI account**: https://pypi.org/account/register/
2. **Create API token**: https://pypi.org/manage/account/token/
   - Name: "DevForge"
   - Scope: "Entire account"
   - **Copy the token** (starts with `pypi-`)

3. **Add to GitHub Secrets**:
   - Go to your repo → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI token
   - Save

## Step 5: Publish to PyPI

### Option A: Via GitHub Release (Automated)

```powershell
# Tag and push
git tag v1.0.0
git push origin v1.0.0
```

Then on GitHub:
- Go to Releases → Draft a new release
- Choose tag: v1.0.0
- Title: "v1.0.0 - Initial Release"
- Description: Features and changes
- Publish release

GitHub Actions will automatically publish to PyPI!

### Option B: Manual Publishing

```powershell
# Install tools
pip install build twine

# Build
python -m build

# Upload to PyPI
twine upload dist/*
```

Enter your PyPI username and password when prompted.

## Step 6: Test Installation

```powershell
# Install from PyPI
pipx install devforge

# Test
devforge --help
devforge list
```

## 🎉 Done!

Users can now install your tool with:
```powershell
pipx install devforge
```

## Updating Later

1. Update version in `setup.py` and `pyproject.toml`
2. Commit changes
3. Create new tag: `git tag v1.0.1`
4. Push: `git push origin v1.0.1`
5. Create GitHub release

GitHub Actions will auto-publish!

---

See [PUBLISHING.md](PUBLISHING.md) for detailed instructions.
