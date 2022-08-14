import os.path
import subprocess
import platform
import sys


def main():
    if platform.system() == 'Linux':
        subprocess.call(['sh', './unix.sh', f'{os.path.abspath(os.path.curdir)}/image.png'])
    elif platform.system() == 'Windows':
        p = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                              '-ExecutionPolicy',
                              'Unrestricted',
                              './windows.ps1', f'{os.path.abspath(os.path.curdir)}\image.png'], cwd=os.getcwd(),
                             stdout=sys.stdout)
        p.communicate()
    elif platform.system() == 'Darwin':
        subprocess.call(['sh', './macos.sh', f'{os.path.abspath(os.path.curdir)}/image.png'])


main()
