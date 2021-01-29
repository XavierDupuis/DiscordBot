@echo off
mode con:cols=36 lines=11
if not exist "keys" (mkdir keys && echo. 2>keys/DiscordToken.txt)
pip install -r requirements.txt
python main.py
