@echo off
@rem Automate commit and push
cd /d %~dp0
git add -A
git commit -a -m "auto-commited"
git push origin master
pause
