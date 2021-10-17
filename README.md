# Media-Controller
Control Music playing on your PC using your phone.

Ever played music on your PC while laying in bed and suddenly a song you **hate** comes up? You have to get up, walk all the way to your PC, skip the song, walk all the way back and only then can you go back to procrastinating. Thats too much effort.

After running `main.py`, a website will be hosed on your local network, it will be under `192.168.0.<Your IP>:80`.
<img src="https://raw.githubusercontent.com/hamolicious/Media-Controller/main/screenshots/screenshot.jpg" alt="screenshot of website" width="400">

You can drop a `.bat` file in the startup folder `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` that launches the script on startup (make sure to use pythonw.exe to launch the script to run it without a console window), an example file is in the `scripts/` folder.

## TODO
- [ ] Volume Level Feedback
- [ ] IP/MAC address whitelisting


