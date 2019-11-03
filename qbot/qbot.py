#!/usr/bin/env python3
# qbot.py
# cameronshinn

from cogs.console import ConsoleCog
from cogs.dbl import DblCog
from cogs.help import HelpCog
from cogs.mapdraft import MapDraftCog
from cogs.popflash import PopflashCog
from cogs.queue import QueueCog
from cogs.teamdraft import TeamDraftCog
import discord
from discord.ext import commands

BOT_COLOR = 0xFD881E

def run(discord_token, dbl_token=None):
    """ Create the bot, add the cogs and run it """
    bot = commands.Bot(command_prefix='q!', case_insensitive=True)
    bot.add_cog(ConsoleCog(bot))
    bot.add_cog(HelpCog(bot, BOT_COLOR))
    bot.add_cog(QueueCog(bot, BOT_COLOR))
    bot.add_cog(TeamDraftCog(bot, BOT_COLOR))
    bot.add_cog(MapDraftCog(bot, BOT_COLOR))
    bot.add_cog(PopflashCog(bot, BOT_COLOR))

    if dbl_token:
        bot.add_cog(DblCog(bot, dbl_token))

    bot.run(discord_token)
