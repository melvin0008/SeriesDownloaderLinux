# -*- mode: python -*-
a = Analysis(['pb.py'],
             pathex=['/home/melvin/development/SeriesDownloaderLinux/SeriesDownloaderLinux'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pb',
          debug=False,
          strip=None,
          upx=True,
          console=False )
