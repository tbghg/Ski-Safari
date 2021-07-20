# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
py_files = [
    'game.py',
    'escmenu.py',
    'Mainmenu.py',
    'medal_Wall.py',
    'My_class.py'
]
add_files = [
    ('Fonts\\*.ttf','Fonts'),
    ('Menu_UI\\*.png', 'Menu_UI'),
    ('audios\\*.wav', 'audios'),
    ('UI\\*.png', 'UI'),
    ('UI\\*.ico', 'UI'),
    ('medal_data\\*.txt','medal_data')
]
a = Analysis(py_files,
             pathex=['D:\\个人学习\\滑雪大冒险项目\\venv'],
             binaries=[],
             datas=add_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['zmq'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='滑雪大冒险',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='UI\\my_icon.ico'
          )