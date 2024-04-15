@echo off
cd /d "%~dp0"
python get_data.py
"C:\Users\Asus\AppData\Local\GitHubDesktop\GitHubDesktop.exe" --restore-previous-path --unity-launch
"C:\Users\Asus\AppData\Local\GitHubDesktop\GitHubDesktop.exe" --commit-all --untracked-files --summary "Updated data.json"
"C:\Users\Asus\AppData\Local\GitHubDesktop\GitHubDesktop.exe" --push