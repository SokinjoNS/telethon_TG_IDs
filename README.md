# Telegram Group and Channel ID Extractor

This Python script utilizes the Telethon library to connect to the Telegram API and list all groups and channels that the bot or user is a part of. It's a handy tool for developers and administrators who need to quickly retrieve IDs for Telegram entities.

## Features

Lists the names and IDs of all groups and channels (including supergroups) associated with the given credentials.
Utilizes the Telethon library for efficient and authenticated communication with the Telegram API.
Prerequisites
Before you begin, ensure you have the following:

- Python 3.6 or newer installed on your system.
- A Telegram account and the API credentials (API ID and Hash) obtained through my.telegram.org.
- A bot token if you intend to use this script with a Telegram bot. Obtain one through BotFather on Telegram.

## Installation

Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://your-repository-url.git
cd your-repository-directory
```

## Install Dependencies

This script requires the Telethon library. Install it using pip:

```bash
pip install telethon
```

## Configure Your Credentials

Rename credentials_tg.json.example to credentials_tg.json and fill in your Telegram API api_id, api_hash, and bot_token (optional, for bot use).

```bash
{
  "api_id": "YOUR_API_ID",
  "api_hash": "YOUR_API_HASH",
}
```

## Usage

After configuring your credentials, you can run the script to list all groups and channels.

The script will authenticate with the Telegram API using the provided credentials and then list the names and IDs of all groups and channels associated with the account or bot.

## Important Notes

This script is meant for legitimate and authorized use cases, such as managing your own groups, channels, or bots. Always respect privacy and Telegram's Terms of Service.

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository. Your feedback and contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
