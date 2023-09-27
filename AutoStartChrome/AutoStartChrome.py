import os
import subprocess

def open_chrome_with_website():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    website_url = "https://studio.youtube.com/video/2ohbhwJ2hCA/livestreaming"
    
    # Check if Chrome is already running
    if not is_chrome_running():
        # Launch Chrome with the specified website
        subprocess.Popen([chrome_path, website_url])
    else:
        print("Google Chrome is already running.")

def is_chrome_running():
    # Get the list of running processes
    process_list = os.popen('tasklist').read().lower()
    
    # Check if "chrome.exe" is present in the process list
    if "chrome.exe" in process_list:
        return True
    else:
        return False

# Run the function to open Google Chrome with the specified website
open_chrome_with_website()
