import discord
from discord.ext import tasks, commands
from discord.utils import get
import locale
import sys
import textwrap
import os
import sqlite3

class userinfo(commands.Cog):
    def init(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        async with ctx.typing():  #vllt auch ctx.send()

            locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8') #german month names
            
            embed = discord.Embed(title="Userinfo", colour=discord.Colour(0x56c6fc))
            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Name:", value=member)
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name="Nickname:", value=member.nick)
            embed.add_field(name="Created the discord account at:", value=member.created_at.strftime("%d.%B.%Y at %H:%M:%S"))
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name="Joined the server at:", value=member.joined_at.strftime("%d.%B.%Y at %H:%M:%S"))
            embed.add_field(name="ID:", value=member.id)
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name="Roles:", value=" ".join([role.mention for role in member.roles if not role.name == "@everyone"]))
            

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(userinfo(bot))
