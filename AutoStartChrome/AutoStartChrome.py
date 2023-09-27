import os
import subprocess
import winreg

def set_registry_key(key_path, value_name, value):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
    except WindowsError:
        pass

def create_startup_entry():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_path = os.path.join(startup_folder, 'Google Chrome.lnk')
    target_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    arguments = 'https://studio.youtube.com/video/2ohbhwJ2hCA/livestreaming'

    with open(shortcut_path, 'w') as shortcut_file:
        shortcut_file.write('[InternetShortcut]\n')
        shortcut_file.write('URL=' + arguments + '\n')
        shortcut_file.write('IconIndex=0\n')
        shortcut_file.write('IconFile=' + target_path + '\n')

def main():
    set_registry_key('Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', 'Hidden', '0')
    create_startup_entry()

if __name__ == '__main__':
    main()
