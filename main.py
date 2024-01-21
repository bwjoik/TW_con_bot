from codeop import CommandCompiler
from typing import Final
import os 
from dotenv import load_dotenv
import discord 
from responses import get_response
from discord.ext import commands

load_dotenv()
#print the token
TOKEN: Final = os.getenv('DISCORD_TOKEN')
# JUDGMENT_COUNT: Final = os.getenv('JUDGMENT_COUNT')
# print(JUDGMENT_COUNT)
intents:discord.Intents = discord.Intents.default()
intents.message_content = True
client:discord.Client = discord.Client(intents=intents)
#client = commands.Bot(command_prefix='!!',intents=intents)
async def send_message(message: discord.Message, user_message: str) -> None:
    if not user_message:
        print('message was empty')
        return
        
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response:str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    username: str = message.author.name
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'{username} sent a message in {channel}: {user_message}')
    await send_message(message, message.content)

def main() -> None:
    client.run(TOKEN)

if __name__ == "__main__":
    main()


