import os
import subprocess
import time

# A Google Chrome elérési útja (a saját telepítési útvonaladra módosítsd)
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# A megnyitni kívánt weboldal URL-je
url = "https://studio.youtube.com/video/2ohbhwJ2hCA/livestreaming"

# Ellenőrizzük, hogy a Google Chrome telepítve van-e
if os.path.exists(chrome_path):
    try:
        # Indítsuk el a Google Chrome böngészőt a megadott URL-lel
        subprocess.Popen([chrome_path, url])
        print("Google Chrome elindítva és megnyitva a weboldalt.")
    except Exception as e:
        print(f"Hiba történt: {e}")
else:
    print("Google Chrome nem található a megadott elérési úton.")

# Várunk egy rövid ideig (pl. 5 másodperc) a weboldal betöltésére
time.sleep(0)
