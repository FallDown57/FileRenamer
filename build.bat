@echo off
echo Building your faster app...
pyinstaller --noconsole --clean --icon=assets/icon.ico --add-data "assets;assets" --upx-dir . --exclude-module PyQt5 --exclude-module PyQt6 --exclude-module matplotlib renamer.py
echo Done! Check dist/renamer/ for renamer.exe
pause