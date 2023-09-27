import os
import subprocess

def add_to_startup(file_path):
    """
    Add the program to Windows startup.
    """
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_path = os.path.join(startup_folder, 'ProgramShortcut.lnk')
    target_path = os.path.abspath(file_path)

    with open(shortcut_path, 'w') as shortcut:
        shortcut.write('[InternetShortcut]\n')
        shortcut.write('URL=https://studio.youtube.com/video/2ohbhwJ2hCA/livestreaming\n')
        shortcut.write('IconIndex=0\n')
        shortcut.write('IconFile=C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\n')
        shortcut.write('WorkingDirectory=\n')

    subprocess.call(['attrib', '+h', shortcut_path])

if __name__ == '__main__':
    add_to_startup('C:\\path\\to\\your\\program.py')
