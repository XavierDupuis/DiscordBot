# Kirbo DiscordBot
<p align="center">
    <img align="center" src="assets/kirbo.png"></img>
</p>

## Prerequisites
1. Python (3.9.1 or higher recommended)


## Installation
1. Clone the repo.

```bash
$ git clone https://github.com/XavierDupuis/DiscordBot.git
```

2. Obtain a [Discord Bot Token](https://discord.com/developers/applications) for your bot instance

<p align="center">
    <img align="center" src="assets/discorddeveloperportalmenu.png"></img>
</p>
<p align="center">
    <img align="center" src="assets/discorddeveloperportalkey.png"></img>
</p>

3. Run

    Installs python requirements located in requirements.txt
    (will automatically close)

```bash
$ run.bat
```

4. Copy your Discord Bot Token in "keys/DiscordToken.txt

5. Download a ffmpeg instance and store it in "ffmpeg/ffmpeg.exe"

6. Start the bot instance

```bash
$ main.py
```

## Services
The following services require a key in order to properly access data

apod : store key in "keys/APODKey.txt" (A [limited demo key](https://api.nasa.gov/) is available on the NASA API website)

weather : store key in "keys/OpenWeatherKey.txt" (An account is required for a [free limited key](https://openweathermap.org/price) )
    
ocr : store key in "keys/RapidAPIKey.txt" (An account is required for a [free limited key](https://rapidapi.com/microsoft-azure-org-microsoft-cognitive-services/api/microsoft-computer-vision3/endpoints) )

translate : store key in "keys/RapidAPIKey.txt" (An account is required for a [free limited key](https://rapidapi.com/googlecloud/api/google-translate1/endpoints) )
