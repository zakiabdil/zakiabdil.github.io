@echo off
cd /d "%~dp0"
python get_data.py

REM Launch GitHub Desktop and open the repository
"C:\Users\Asus\AppData\Local\GitHubDesktop\GitHubDesktop.exe" --restore-previous-path --unity-launch

REM Commit the changes with a message
"C:\Users\Asus\AppData\Local\GitHubDesktop\GitHubDesktop.exe" --commit-all --untracked-files --summary "Updated data.json"

REM Push the committed changes to the remote GitHub repository
"C:\Users\Asus\AppData\Local\GitHubDesktop\GitHubDesktop.exe" --push
