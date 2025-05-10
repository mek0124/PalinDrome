# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/app/main.py'],
    pathex=[],
    binaries=[],
    datas=[('src/main_window.ui', 'src'), ('src/app/main_window.py', 'src/app')],
    hiddenimports=['PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets', 'src.app.main_window', 'src.main_window'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6.QtNetwork', 'PySide6.QtWebEngineCore', 'PySide6.QtWebEngine', 'PySide6.QtWebEngineWidgets'],
    noarchive=False,
    optimize=1,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [('O', None, 'OPTION')],
    exclude_binaries=True,
    name='PalindromeChecker',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PalindromeChecker',
)
