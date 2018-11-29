# -*- mode: python -*-

block_cipher = None

a = Analysis(['likeyoubot_main.py'],
             pathex=['C:\\workspace\\dogfooter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [ ('miracle.lyb', '.\\miracle.lyb', 'DATA')]
a.datas += [ ('kaiser.lyb', '.\\kaiser.lyb', 'DATA')]
a.datas += [ ('blade2.lyb', '.\\blade2.lyb', 'DATA')]
a.datas += [ ('tera.lyb', '.\\tera.lyb', 'DATA')]
a.datas += [ ('blackdesert.lyb', '.\\blackdesert.lyb', 'DATA')]
a.datas += [ ('l2r.lyb', '.\\l2r.lyb', 'DATA')]
a.datas += [ ('icarus.lyb', '.\\icarus.lyb', 'DATA')]
a.datas += [ ('coc.lyb', '.\\coc.lyb', 'DATA')]
a.datas += [ ('talion.lyb', '.\\talion.lyb', 'DATA')]
a.datas += [ ('linm.lyb', '.\\linm.lyb', 'DATA')]
a.datas += [ ('license_key.dat', '.\\license_key.dat', 'DATA')]
a.datas += [ ('license.dat', '.\\license.dat', 'DATA')]
a.datas += [ ('t_logo.png', '.\\t_logo.png', 'DATA')]
a.datas += [ ('.\\image\\dogfooterbot_icon.ico', '.\\dogfooterbot_icon.ico', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='dogfooterbot',
          debug=False,
          strip=False,
          upx=True,
          console=False, icon='dogfooterbot_icon.ico' )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='dogfooterbot2')
