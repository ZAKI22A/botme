import datetime
from discord.ext import commands
import discord

from reo.console.logging import logger
from reo.src.checks import checks
import traceback

class on_command(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot

    @commands.Cog.listener()
    async def on_command_completion(self, ctx: commands.Context):
        try:
            embed = discord.Embed(
                title="Command Executed",
                color=0x2f3136
            )
            embed.add_field(name="Command", value=f"`?{ctx.command.name}`", inline=False)
            embed.add_field(name="User", value=f"{ctx.author.mention} (`{ctx.author.id}`)", inline=False)
            embed.add_field(name="Channel", value=f"{ctx.channel.mention}", inline=False)
            embed.set_thumbnail(url=ctx.author.display_avatar.url)
            await self.bot.log.send(guild=ctx.guild, type="guild_update", embed=embed)
        except Exception as e:
            logger.error(f"Error in on_command_completion logging: {e}")