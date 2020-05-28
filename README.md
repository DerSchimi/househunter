# Househunter

## Quick Setup
```
git clone https://github.com/DerSchimi/househunter.git
cd househunter
pip3 install -r requirements.txt
cp config.yaml.dist config.yaml
nano config.yaml
python3 househunter.py
```

## Run forever or run periodically


### Run Forever

To run househunter indefinetly:

```
nohup python3 run_househunter_forever.py &
```

### Run on reboot
Add this to your crontab:
```
@reboot cd <yourpath> && /usr/bin/python3 run_househunter_forever.py&
```

## Run periodically

Edit config.yaml and change loop: active: false
Add something like this to your crontab:
```
@hourly cd <yourpath> && /usr/bin/python3 <yourpath>/househunter.py&
```

## Setup


### Requirements
Install requirements from ```requirements.txt``` to run execute househunter properly.
```
pip3 install -r requirements.txt
```

## Usage
```
usage: househunter.py [-h] [--config CONFIG]

Searches for houses on immowelt, ebay classifieds and immoscout and sends results
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


