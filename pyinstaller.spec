#
# rtlsdr_scan
#
# http://eartoearoak.com/software/rtlsdr-scanner
#
# Copyright 2012 - 2014 Al Brown
#
# A frequency scanning GUI for the OsmoSDR rtl-sdr library at
# http://sdr.osmocom.org/trac/wiki/rtl-sdr
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import platform

extension = ''
system = platform.system().lower()
architecture, _null = platform.architecture()

if system == 'windows':
    extension = '.exe'

filename = 'rtlsdr_scan-' + system + '-' + architecture.lower() + extension

a = Analysis(['src/rtlsdr_scan.py'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=None)

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts + [('O', '', 'OPTION')],
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', filename),
          icon='rtlsdr_scan.ico',
          debug=False,
          strip=False,
          upx=True,
          console=True)
