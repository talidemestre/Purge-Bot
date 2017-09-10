import discord
import asyncio
import copy

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
        #Omninous Delay
        await asyncio.sleep(1)
        #Delete all channels.
        server = message.server
        channelList =[]
        for i in server.channels:
            channelList.append(i)
        for i in channelList:
            await client.delete_channel(i)
        #Delete all roles.
        roleList =[]
        for i in server.role_hierarchy:
            roleList.append(i)
            print (roleList)
        for i in range(1,len(roleList)-1):
            await client.delete_role(server, roleList[i])
        #Confirmation Message
        await client.send_message(message.channel, purge_success)
        
       
client.run('MzU1OTgxMzUzNDUzNjE3MTUy.DJU7Kw.G595TciWLwbQRgGd25S5MXBoAPA')
