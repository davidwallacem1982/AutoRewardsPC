import os

import customtkinter
import PyInstaller.__main__
from PyInstaller.utils.hooks import collect_all

# Get customtkinter path to include its data
customtkinter_path = os.path.dirname(customtkinter.__file__)

# Collect all resources for customtkinter and other key libs
# This returns (datas, binaries, hiddenimports)
ctk_datas, ctk_binaries, ctk_hiddenimports = collect_all("customtkinter")
pil_datas, pil_binaries, pil_hiddenimports = collect_all("PIL")
pystray_datas, pystray_binaries, pystray_hiddenimports = collect_all("pystray")

# Define assets to include
# Format: (source, destination)
assets = [("assets", "assets"), ("src", "src")]

# Merge datas
all_datas = ctk_datas + pil_datas + pystray_datas
for source, dest in assets:
    # PyInstaller expects "source;dest" on Windows
    all_datas.append((source, dest))

# Merge binaries
all_binaries = ctk_binaries + pil_binaries + pystray_binaries

# Merge hidden imports
all_hiddenimports = (
    ctk_hiddenimports
    + pil_hiddenimports
    + pystray_hiddenimports
    + [
        "ui",
        "core",
        "domain",
        "babel",
        "win32timezone",
        "pystray",
        "pystray._win32",
        "pkg_resources.extern",
        "PIL",
        "PIL.Image",
        "PIL.ImageDraw",
    ]
)

# Define PyInstaller arguments
args = [
    "src/main.py",  # Script to build
    "--name=AutoRewardsPC",  # Name of the executable
    "--noconfirm",  # Replace output directory
    "--onedir",  # Generate a directory (easier for debugging assets)
    "--windowed",  # No console window
    "--icon=assets/icon.ico",  # Icon
    "--clean",  # Clean cache
    "--paths=src",  # Add src to search path
]

# Append compiled args
for src, dest in all_datas:
    args.append(f"--add-data={src};{dest}")

for src, dest in all_binaries:
    args.append(f"--add-binary={src};{dest}")

for hidden in all_hiddenimports:
    args.append(f"--hidden-import={hidden}")

# Run PyInstaller
print("Starting build process with robust dependency collection...")
try:
    PyInstaller.__main__.run(args)
    print("Build finished. Check 'dist/AutoRewardsPC'.")
except Exception as e:
    print(f"Build failed: {e}")
