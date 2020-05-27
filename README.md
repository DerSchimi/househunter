# Househunter

## Quick Setup
```
sudo apt-get install wget unzip python-pip 
wget https://github.com/derschimi/househunter/archive/master.zip
unzip master.zip
cd househunter-master
pip install -r requirements.txt
mv config.yaml.dist config.yaml
nano config.yaml
python3 househunter.py
```
## Run Forever

To run househunter indefinetly:

```
nohup python3 run_househunter_forever.py &
```
## Run on reboot
Add this to your crontab:
```
@reboot cd <yourpath> && /usr/bin/python3 run_househunter_forever.py&
```

## Setup


### Requirements
Install requirements from ```requirements.txt``` to run execute househunter properly.
```
pip install -r requirements.txt
```

## Usage
```
usage: househunter.py [-h] [--config CONFIG]

Searches for houses on immowelt, ebay kleinanzeigen and immoscount and sends results
to Telegram User

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG
                        Config file to use. If not set, try to use
                        '~git-clone-dir/config.yaml'

```

### Configuration

#### Bot registration
A new bot can registered with the telegram chat with the [BotFather](https://telegram.me/BotFather).

#### Chat-Ids
To get the chat id, the [REST-Api](https://core.telegram.org/bots/api) of telegram can be used to fetch the received messages of the Bot.
```
$ curl https://api.telegram.org/bot[BOT-TOKEN]/getUpdates
```

#### Config File

Rename the config.yaml.dist to config.yaml and fill as described.


## Constributions/Based on
- [@NodyHub](https://github.com/NodyHub)
- [@tschuehly](https://github.com/tschuehly)


