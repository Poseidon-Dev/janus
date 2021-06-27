# Janus | Converter Bot


Janus is a simple converter bot. He converts imperial/metric data listening 
to conversations that may have the need for the conversion

## Authors

* **[Johnny Whitworth (@Poseidon-dev)](https://github.com/poseidon-dev)** 

## Support

If you need some help for something, please reach out to me directly or submit an issue and I'll get to it as soon as I can

## How to use

The local convert.db file has two tables
One with the conversation rates and the other with string posibilities
with a foreign reference on the first. Add conversions as you will. 

Create a .env with the following variables:

BOT_TOKEN=YOURTOKEN
APPLICATION_ID=YOURAPPID

DB_LOCATION=convert.db
VERSION=1.0.0

He's an event listener. So after setup, he should function

