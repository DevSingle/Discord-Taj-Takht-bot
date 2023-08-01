import nextcord
from nextcord.ext import commands, tasks


class Onjoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.memberstats.start()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed=nextcord.Embed(title=f"Hi {member.name} 💙",description="Also see these channels:\n<#1135593808583721140>\n<#1135892866032468100>\nEnjoy 😉", color=nextcord.Color.blue()) #Welcome Text
        embed.set_thumbnail(url=member.avatar)

        guild= self.bot.get_guild(850662966646931456) #Guild ID
        channel=guild.get_channel(1135892819110805544) #Channel ID
        await channel.send(f"{member.mention} Welcome To {guild.name}",embed=embed)


    @tasks.loop(minutes=15)
    async def memberstats(self):
        await self.bot.wait_until_ready()
        guild = self.bot.get_guild(850662966646931456) #Guild ID
        member_channel = self.bot.get_channel(1135596411707215985) #Channel ID

        member_count = guild.member_count

        member_count_str = str(member_count).zfill(4)
        updated_string = " ".join(member_count_str)

        await member_channel.edit(name="⦿ 𝐔 𝐒 𝐄 𝐑 𝐒 = " + f"{updated_string}")

def setup(bot):
    bot.add_cog(Onjoin(bot))
