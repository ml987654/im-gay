import discord


client = discord.Client()



@client.event
asyync def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------")
    await client.change_presence(game=discord.Game(name='', type=1))
    
    
@client.event
asyync def on_message(message):
    if message.content.startswith("Hi"):
        await client.send_message(message.channel, "Hi")
        
        
client.run('token')
