# AESC Telegram Bot - @aesc_bot
[![Build Status](https://travis-ci.org/FranceX/aesc_bot.svg?branch=master)](https://travis-ci.org/FranceX/aesc_bot)

Telegram bot pour les etudiants de l'ESC à Université de Lausanne.

# Installation
The bot can be installed in two ways, either using docker, or run directly via python

## Clone
```
git clone https://github.com/FranceX/aesc_bot.git
cd aesc_bot
```

## Set environment variables
To run the bot looks for the API Key under the ```API_KEY``` environment variable.
Store your API Key in a file named ```.env```, a sample file ```.env-example``` is provided.

Source and export the variable to the environment (not needed if using Docker-Compose)
```
source .env
export API_KEY
```

## Python
Ensure you have python 3.6 installed, no other version has been tested.

Install the dependencies
```
pip install -r requirements.txt
```

Run the bot
```
python run_bot.py
```

## Docker
Run either the latest version by building the image yourself, or use the included compose file to run the latest image from Docker Hub (Or edit the compose file to build from the local Dockerfile)


### Plain Docker
Build the image
```
docker build -t aesc_bot .
```

Create and run a container in background
```
docker run -d -e API_KEY --name aesc_bot aesc_bot
```

### Docker Compose
```
docker-compose up -d
```