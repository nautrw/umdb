import disnake
from disnake.ext import commands


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """
        Returns the bot's ping
        """
        await inter.send(
            f"# :ping_pong: Pong!\nPing: `{round(self.bot.latency * 1000, 1)}ms`"
        )


def setup(bot):
    bot.add_cog(Tools(bot))
