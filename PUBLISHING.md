# 📦 Publishing DevForge to PyPI

Complete guide to publish DevForge so users can install it with `pipx install devforge`.

## 🎯 One-Time Setup

### 1. Create PyPI Account

1. Go to https://pypi.org/account/register/
2. Create an account
3. Verify your email

### 2. Create PyPI API Token

1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Give it a name: "DevForge GitHub Actions"
4. Scope: "Entire account" (or specific to devforge later)
5. **Copy the token** (starts with `pypi-...`)

### 3. Add Token to GitHub Secrets

1. Go to your GitHub repo: https://github.com/isakamtweve/devforge
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `PYPI_API_TOKEN`
5. Value: Paste your PyPI token
6. Click **Add secret**

## 🚀 Publishing Process

### Option 1: Automatic (via GitHub Release) - Recommended

1. **Update version** in both files:
   - `setup.py`: Change `version='1.0.0'` to `version='1.0.1'`
   - `pyproject.toml`: Change `version = "1.0.0"` to `version = "1.0.1"`

2. **Commit and push**:
   ```bash
   git add .
   git commit -m "Bump version to 1.0.1"
   git push origin main
   ```

3. **Create a GitHub Release**:
   ```bash
   # Tag the release
   git tag v1.0.1
   git push origin v1.0.1
   ```
   
   Or use GitHub UI:
   - Go to https://github.com/isakamtweve/devforge/releases
   - Click **Draft a new release**
   - Tag: `v1.0.1`
   - Title: `v1.0.1 - Description of changes`
   - Description: List of changes/features
   - Click **Publish release**

4. **Wait for GitHub Actions**:
   - Go to **Actions** tab
   - Watch the "Publish to PyPI" workflow run
   - It will automatically build and publish to PyPI

5. **Verify on PyPI**:
   - Check https://pypi.org/project/devforge/
   - Your new version should appear

### Option 2: Manual (Local Publishing)

1. **Install build tools**:
   ```bash
   pip install build twine
   ```

2. **Update version** in `setup.py` and `pyproject.toml`

3. **Clean previous builds**:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

4. **Build the package**:
   ```bash
   python -m build
   ```

5. **Check the build**:
   ```bash
   twine check dist/*
   ```

6. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```
   
   Enter your PyPI credentials when prompted.

## 📋 Pre-Publishing Checklist

Before each release, verify:

- [ ] Version updated in `setup.py`
- [ ] Version updated in `pyproject.toml`
- [ ] README.md is up to date
- [ ] All features tested locally
- [ ] Documentation is accurate
- [ ] CHANGELOG updated (if you have one)
- [ ] No debug/test code in main files
- [ ] All imports work correctly

## 🧪 Test Your Package Locally

Before publishing, test the build:

```bash
# Build the package
python -m build

# Install locally
pip install dist/devforge-1.0.1-py3-none-any.whl

# Test it
devforge --help
devforge list
```

## 🔄 Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **Major (1.0.0)**: Breaking changes
- **Minor (1.1.0)**: New features, backward compatible
- **Patch (1.0.1)**: Bug fixes, backward compatible

Example:
```
1.0.0 → Initial release
1.0.1 → Bug fix
1.1.0 → Added new framework support
2.0.0 → Breaking API changes
```

## 📦 Users Can Install With

Once published, users can install with:

```bash
# Using pipx (recommended for CLI tools)
pipx install devforge

# Using pip
pip install devforge

# Upgrade to latest
pipx upgrade devforge
# or
pip install --upgrade devforge
```

## 🔍 Verify Publication

After publishing, verify:

1. **PyPI page**: https://pypi.org/project/devforge/
2. **Install test**:
   ```bash
   pipx install devforge
   devforge --version
   ```
3. **Uninstall test**:
   ```bash
   pipx uninstall devforge
   ```

## 🐛 Troubleshooting

### "Package already exists"
- You can't re-upload the same version
- Increment version number and try again

### "Invalid token"
- Check GitHub secret is correct
- Generate new PyPI token if needed

### "Forbidden"
- Verify PyPI account email is confirmed
- Check API token has correct permissions

### Build fails
- Check all files are included in MANIFEST.in
- Verify setup.py and pyproject.toml are correct

## 📝 Continuous Deployment

Your GitHub Actions workflow automatically:
1. Triggers on new GitHub releases
2. Builds the package
3. Checks for errors
4. Publishes to PyPI

No manual steps needed! Just create a release.

## 🎓 First Time Publishing Checklist

- [ ] PyPI account created
- [ ] PyPI API token generated
- [ ] Token added to GitHub secrets
- [ ] GitHub Actions workflow configured
- [ ] README.md complete
- [ ] LICENSE file present
- [ ] Version numbers set correctly
- [ ] Test locally with `python -m build`
- [ ] Create GitHub release or run manual upload

## 🚀 You're Ready!

Your package is now ready to be published. Users worldwide can install it with:

```bash
pipx install devforge
```

Happy publishing! 🔥
