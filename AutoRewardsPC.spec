# -*- mode: python ; coding: utf-8 -*-


from PyInstaller.utils.hooks import collect_data_files

datas = []
datas += collect_data_files('customtkinter')
datas += [('assets', 'assets')]

import sys
import os

# Try to locate VCRUNTIME140_1.dll
# Try to locate VCRUNTIME140.dll and VCRUNTIME140_1.dll
extra_binaries = []
dlls = ['VCRUNTIME140.dll', 'VCRUNTIME140_1.dll']
search_paths = [os.path.dirname(sys.executable), sys.base_prefix, os.path.join(sys.base_prefix, 'Library', 'bin')]

for dll in dlls:
    for path in search_paths:
        dll_path = os.path.join(path, dll)
        if os.path.exists(dll_path):
            extra_binaries.append((dll_path, '.'))
            break

a = Analysis(
    ['src\\main.py'],
    pathex=['src'],
    binaries=extra_binaries,
    datas=datas,
    hiddenimports=['customtkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AutoRewardsPC',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\icon.ico'],
    uac_admin=True,
    version='version_info.txt',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AutoRewardsPC',
)
