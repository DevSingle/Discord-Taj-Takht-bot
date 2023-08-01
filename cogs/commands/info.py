import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="Info")
    async def info(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("""
Coming Soon...
        """
        , ephemeral=True)

def setup(bot):
    bot.add_cog(Info(bot))