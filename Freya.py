import discord, os, random, time

token = open('token.txt', 'r').read()  # Open the file and read the token

intents = discord.Intents.default()  # Create an Intents object with default intents
intents.message_content = True  # Enable the message content intent

freya = discord.Client(intents=intents)  # Creates the client with intents

@freya.event  # Decorator to register an event in the client
async def on_ready():  # async def is a function that can be paused and resumed
    print('Freya standing by!')  # Print a message in the console when the bot is ready

@freya.event
async def on_message(message):
    specific_channel_id = 1297090957661175818
    if message.channel.id == specific_channel_id:
        if message.author == freya.user:
            return
        else:
            await message.add_reaction('🟤')  # reacts to the message so the user knows it's been received
            await message.channel.send("Hiya, I'm Freya")  # Send a message to the channel where the message was sent

freya.run(token)  # Run the bot with the token

time.sleep(5)  # Sleep for 5 seconds