import discord
from discord.ext import commands
import random


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """All commands that require a prefix have the following decorator:
    @commands.command()
    async def some_command (self, ctx)
    etc
    """

    @commands.command()
    async def avatar(self, ctx, target: discord.User = None):
        """Shows a Users avatar. Defaults to the Author"""
        if target is None:
            target = ctx.author
        await ctx.send(target.avatar_url)

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        """Kenobi Gif"""
        await ctx.send('https://tenor.com/view/hello-there-hi-there-greetings-gif-9442662')

    @commands.command()
    async def zodiac(self, ctx, *, UserID):
        """Calls the user a Babylonian Racist"""
        await ctx.send(
            'Hey there, <@{}>, you ancient Babylonian racist. https://vm.tiktok.com/ZMeUcjhSB/ . Have fun!'.format(
                UserID)
        )

    @commands.command()
    async def goldstar(self, ctx):
        """You tried (TM)"""
        await ctx.reply('https://tenor.com/view/ahtf-gif-5633413')

    # need to readd dong, probably can just copy from flop or do it yourself
    @commands.command()
    async def dong(self, ctx, target: discord.User = None):
        if target is None:
            target = ctx.author
        embedDong = discord.Embed(title='{}\'s dong size is:'.format(target),
                                  description='8{}D'.format('=' * random.randint(0, 30)),
                                  color=discord.Colour.dark_green())
        await ctx.send(embed=embedDong)
    # less go, did self


def setup(bot):
    bot.add_cog(FunCog(bot))
