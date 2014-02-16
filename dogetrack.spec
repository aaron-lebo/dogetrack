# -*- mode: python -*-
a = Analysis(['dogetrack.py'],
             pathex=['C:\\dogetrack'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='dogetrack.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='dogetrack.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               [('dogetrack.png', 'dogetrack.png', 'DATA'),
                ('settings.json', 'settings.json', 'DATA')],
               strip=None,
               upx=True,
               name='dogetrack')
