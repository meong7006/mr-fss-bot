import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# YOUR FILLED-IN IDS
TARGET_CHANNEL_ID = 1560875521104019587  # destination channel id
YOUR_USER_ID = 1560867888561266789      # your user id

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    # ignore messages sent by mr fss itself
    if message.author == client.user:
        return

    # check if message arrives in your target channel
    if message.channel.id == TARGET_CHANNEL_ID:
        await message.channel.send(f"<@{YOUR_USER_ID}> new update dropped!")

client.run(os.getenv('BOT_TOKEN'))
