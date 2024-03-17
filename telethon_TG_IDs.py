from telethon.sync import TelegramClient
import json
import asyncio

def load_credentials(filename='credentials_tg.json'):
    with open(filename) as f:
        return json.load(f)

credentials = load_credentials()

client = TelegramClient('my_telethon_session', credentials['api_id'], credentials['api_hash'])

async def list_groups():
    await client.start(bot_token=credentials['bot_token'])  # Use the bot token to start the client

    # List all groups
    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:  # This will include supergroups (channels) as well
            print(dialog.name, dialog.id)

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(list_groups())
