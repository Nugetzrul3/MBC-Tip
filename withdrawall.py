from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import Decimal
import discord
from discord.ext import commands

import user_db
import config

# connect to coind
rpc_connection = 'http://{0}:{1}@{2}:{3}'.format(config.rpc_user, config.rpc_password, config.ip, config.rpc_port)

class Withdrawall(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def withdrawall(self, ctx, address=None):
        client = AuthServiceProxy(rpc_connection)
        user_id = str(ctx.author.id)

        if ctx.channel.id == 723496777566781491:

            if not user_db.check_user(user_id):
                embed = discord.Embed(
                    title="**For first-use-user**",
                    color=0x0043ff)
                embed.set_author(
                    name=ctx.author.display_name,
                    icon_url=ctx.author.avatar_url_as(format='png', size=256))
                embed.add_field(
                    name="First of all, please type `//help`",
                    value="Welcome to world of Tip MBC !")
                embed.set_thumbnail(url=self.bot.user.avatar_url_as(format='png', size=1024))
                embed.set_footer(text="Tip MBC {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                 icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                await ctx.channel.send(embed=embed)
            else:
                pass

                account = str(ctx.author.id)
                balance = Decimal(client.getbalance(account, config.CONFIRM))

                if address is None:
                    embed = discord.Embed(color=0xffd800)
                    embed.set_author(
                        name=ctx.author.display_name,
                        icon_url=ctx.author.avatar_url_as(format='png', size=256))
                    embed.add_field(
                        name="Please check `//help` ",
                        value=" :mag: ")
                    embed.set_footer(text="Tip MBC {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                     icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                    await ctx.channel.send(embed=embed)
                else:
                    pass

                    if balance < Decimal('0.5'):
                        embed = discord.Embed(color=0xff0000)
                        embed.set_author(
                            name=ctx.author.display_name,
                            icon_url=ctx.author.avatar_url_as(format='png', size=256))
                        embed.add_field(
                            name="Amount must be at least 0.5 MBC.",
                            value="Your balances : ```{0} MBC```".format(client.getbalance(account, config.CONFIRM)))
                        embed.set_footer(text="Tip MBC {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                         icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                        await ctx.channel.send(embed=embed)
                    else:
                        amount = balance - Decimal(str(config.FEE))
                        validate = client.validateaddress(address)

                        if not validate['isvalid']:
                            embed = discord.Embed(color=0xff0000)
                            embed.set_author(
                                name=ctx.author.display_name,
                                icon_url=ctx.author.avatar_url_as(format='png', size=256))
                            embed.add_field(
                                name="invalid address.",
                                value="`{0}`".format(str(address)))
                            embed.set_footer(text="Tip MBC {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                             icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                            await ctx.channel.send(embed=embed)
                        else:
                            txid = client.sendfrom(account, address, float(amount))
                            tx = client.gettransaction(txid)
                            txfee = tx['fee']

                            client.move(account, "tipmagi_wallet", Decimal(str(config.FEE)))
                            client.move("tipmagi_wallet", account, -txfee)

                            embed = discord.Embed(
                                title="**Block explorer**",
                                url='https://microbitcoinorg.github.io/explorer/#/address/{0}'.format(txid),
                                color=0x0043ff)
                            embed.set_author(
                                name=ctx.author.display_name,
                                icon_url=ctx.author.avatar_url_as(format='png', size=256))
                            embed.add_field(
                                name="Withdrawal complete `{0} MBC`\nwithdraw fee is `{1} MBC`\nPlease check the transaction at the above link.".format(amount, str(config.FEE)),
                                value="Your balances : `{0} MBC`".format(client.getbalance(account, config.CONFIRM)))
                            embed.set_footer(text="Tip MBC {0} [Owner: {1}]".format(config.VERSION, self.bot.get_user(config.OWNER_ID)),
                                             icon_url=self.bot.user.avatar_url_as(format='png', size=256))

                            await ctx.channel.send(embed=embed)

        else:
            embed = discord.Embed(title="Oops", color=0x7152b6)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url_as(format='png', size=256))
            embed.add_field(
                name="Wrong Channel",
                value="Please ur #testrestriction to use this tipbot",
            )
            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Withdrawall(bot))
