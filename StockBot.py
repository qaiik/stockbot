import discord
import logging
from dotenv import load_dotenv
import os 


def main():
	# program logic goes here
	
	load_dotenv
	TOKEN = os.getenv('DISCORD_TOKEN')

def logging():
	# logging code here
	logger = logging.getLogger('discord')
	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
	# specifically writes to discord.log
	handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)



class StockBot(discord.Client):
	bot = commands.self(command_prefix='?', description=description, intents=intents) 	

	# all event handlers must be coroutines

	# no need for decorator when in class definition

	async def on_ready(self):
		print(f"We've logged on as {self.user}")
		# doesn't need to be awaited - non blocking function

	async def on_message(self, message):
		if message.author == self.user:
			return
		if message.content.startswith('$hello'):
			await message.channel.send('hello!')
	
	async def help_call(message):
		if message.content("help"):
			await message.channel.send('let me give you some help')


	
client = StockBot()

# just for jokes, the token needs to go here in the actual call
client.run(TOKEN)