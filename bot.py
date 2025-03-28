import os
from dotenv import load_dotenv

import nextcord
from nextcord.ext import commands

from utils import generate_puzzel_embed, is_game_over, is_vaild_word, random_puzzel_id, update_embed

load_dotenv()

bot = commands.Bot(command_prefix=commands.when_mentioned)

GUILD_IDS= (
    [int(guild_id) for guild_id in os.getenv("GUILD_IDS").split(",")]
    if os.getenv("GUILD_IDS", None)
    else nextcord.utils.MISSING
)


@bot.slash_command(description="Play a game of wordle", guild_ids=GUILD_IDS)
async def play(interaction: nextcord.Interaction):
    # generate a puzzel
    puzzel_id = random_puzzel_id()
    # create the puzzel to display
    embed = generate_puzzel_embed(interaction.user, puzzel_id)
    # send the puzzel as an interaction response
    await interaction.send(embed=embed)

@bot.event
async def on_message(message: nextcord.Message):
    # get the message replied to
    ref = message.reference
    if not ref or not isinstance(ref.resolved, nextcord.Message):
        return
    parent = ref.resolved

    # if the parent message ist not the bot's message, ignore it
    if parent.author.id != bot.user.id:
        return

    # check that the message has embeds
    if not parent.embeds:
        return
    
    embed = parent.embeds[0]

    # check that the user is the one playing
    if embed.author.name != message.author.name:
        await message.reply(
            f"This game was started by {embed.author.name}. Start a new game with /play", 
            delete_after=5
            )
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return


    # check that the game is not over
    if is_game_over(embed):
        await message.reply("The game is already over. Start a new game with /play", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return

    # check that a singel word is in the message
    if len(message.content.split()) > 1:
        await message.reply("Please respond with a single 5-letter word", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return

    # check that the word is vaild
    if not is_vaild_word(message.content):
        await message.reply("That is not a vaild word or try it with lowercases", delete_after=5)
        try:
            await message.delete(delay=5)
        except Exception:
            pass
        return

    # update the embed
    embed = update_embed(embed, message.content)
    await parent.edit(embed=embed)

    # attempt to delete the message
    try:
        await message.delete()
    except Exception:
        pass

bot.run(os.getenv("TOKEN"))