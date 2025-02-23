# File Renamer by Bro

A slick, free tool to rename all your files and folders in one go. Built with love—tips appreciated if it saves your ass!

## Features
- Renames files *and* folders (e.g., `cool1.jpg`, `cool2`, `cool3_folder`)
- Dark theme, green glow—looks dope
- Progress bar so you know it’s working
- Tip button: Copy my ETH address with one click

## How to Use
1. Download `FileRenamer-v1.0.zip` from [Releases](#releases) or build it yourself.
2. Unzip, run `renamer.exe`.
3. Pick a folder, type a base name (like `photo`), hit "Rename ‘Em!"
4. Files get renamed: `photo1.jpg`, `photo2.pdf`, etc.

## Build It Yourself
### Requirements
- Python 3 (tested on 3.13, 3.9+ should work)
- `Pillow`: `pip install Pillow`
- `PyInstaller`: `pip install pyinstaller`
- Optional: `UPX` for smaller builds (download from upx.github.io, put in `FileRenamer/`)

### Steps
1. Clone this repo: `git clone https://github.com/FallDown57/FileRenamer.git`
2. `cd FileRenamer`
3. Run `build.bat` (Windows) or `pyinstaller --noconsole --icon=assets/icon.ico --add-data "assets;assets" renamer.py`
4. Find `renamer.exe` in `dist/renamer/` (multi-file) or `dist/` (one-file).
