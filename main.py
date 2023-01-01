import discord

client = discord.Client()

# Could lead to a temporary API limitation if the bot has a bad connection and therefore reconnects more often
@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
    blacklist = ['🤡', '🖕', '💩']

    if payload.emoji.name in blacklist:
        await reaction.remove(payload.member)

client.run(your_bot_token)
