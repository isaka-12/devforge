// filepath: c:\Users\user\Projects\devforge\release.ps1
# DevForge Release Script
param(
    [Parameter(Mandatory=$true)]
    [string]$Version
)

Write-Host "🚀 Releasing DevForge v$Version" -ForegroundColor Cyan

# Update version in files
(Get-Content setup.py) -replace "version='[\d\.]+'" , "version='$Version'" | Set-Content setup.py
(Get-Content pyproject.toml) -replace 'version = "[\d\.]+"' , "version = `"$Version`"" | Set-Content pyproject.toml

# Commit and push
git add .
git commit -m "Release v$Version"
git push origin main

# Create and push tag
git tag "v$Version"
git push origin "v$Version"

Write-Host "✅ Version $Version tagged and pushed!" -ForegroundColor Green
Write-Host "📦 Now create GitHub Release at:" -ForegroundColor Yellow
Write-Host "   https://github.com/isaka-12/devforge/releases/new" -ForegroundColor Yellow