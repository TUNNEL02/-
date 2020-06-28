import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("봇을 구동중임.")


@client.event
async def on_message(message):
    if message.content.startswith("!작성"):
        channel = message.content[4:22]
        msg = message.content[23:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="MUTE")
        await author.add_roles(role)
        await message.channel.send("**뮤트를 성공하였습니다.**")

    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[4:23]))
        role = discord.utils.get(message.guild.roles, name="MUTE")
        await author.remove_roles(role)
        await message.channel.send("**언뮤트를 성공하였습니다.**")



access_token = os.environ["BOT_TOKEN]
client.run(access_token)

