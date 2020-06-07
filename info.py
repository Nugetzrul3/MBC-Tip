from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import discord
from discord.ext import commands

import user_db
import config

# connect to coind
rpc_connection = 'http://{0}:{1}@{2}:{3}'.format(config.rpc_user, config.rpc_password, config.ip, config.rpc_port)

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        client = AuthServiceProxy(rpc_connection)
        user_id = str(ctx.author.id)

        if not user_db.check_user(user_id):
            embed = discord.Embed(
                title="**For first-use-user**",
                color=0x0043ff)
            embed.set_author(
                name=ctx.author.display_name,
                icon_url=ctx.author.avatar_url_as(format='png', size=256))
            embed.add_field(
                name="First of all, please type `//help`",
                value="Welcome to world of Tip Magi !")
            embed.set_thumbnail(url=self.bot.user.avatar_url_as(format='png', size=1024))
            embed.set_footer(text="Tip Magi {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                             icon_url=self.bot.user.avatar_url_as(format='png', size=256))

            await ctx.channel.send(embed=embed)
        else:
            pass

            block = client.getinfo()['blocks']
            hash_rate = round(client.getnetworkhashps() / 1000, 4)
            difficulty_pow = client.getinfo()['difficulty']['proof-of-work']
            difficulty_pos = client.getinfo()['difficulty']['proof-of-stake']
            connection = client.getinfo()['connections']
            client_version = client.getinfo()['version']

            embed = discord.Embed(
                title="**Magichain info**",
                color=0x0043ff)
            embed.set_author(
                name=ctx.author.display_name,
                icon_url=ctx.author.avatar_url_as(format='png', size=256))
            embed.add_field(
                name="__Current block height__",
                value="`{0}`".format(block),
                inline=True)
            embed.add_field(
                name="__Network hash rate__",
                value="`{0} KH/s`".format(hash_rate),
                inline=True)
            embed.add_field(
                name="__Difficulty (POW)__",
                value="`{0}`".format(difficulty_pow),
                inline=True)
            embed.add_field(
                name="__Difficulty (POS)__",
                value="`{0}`".format(difficulty_pos),
                inline=True)
            embed.add_field(
                name="__Connection__",
                value="`{0}`".format(connection),
                inline=True)
            embed.add_field(
                name="__Client Version__",
                value="`{0}`".format(client_version),
                inline=True)
            embed.set_footer(text="Tip Magi {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                             icon_url=self.bot.user.avatar_url_as(format='png', size=256))

            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
