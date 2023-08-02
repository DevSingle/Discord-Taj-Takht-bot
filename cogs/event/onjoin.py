import nextcord
from nextcord.ext import commands, tasks


class Onjoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #     self.memberstats.start()

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     embed=nextcord.Embed(title=f"Hi {member.name} 💙",description="Also see these channels:\n<#1135593808583721140>\n<#1135892866032468100>\nEnjoy 😉", color=nextcord.Color.blue()) #Welcome Text
    #     embed.set_thumbnail(url=member.avatar)

    #     guild= self.bot.get_guild(850662966646931456) #Guild ID
    #     channel=guild.get_channel(1135892819110805544) #Channel ID
    #     await channel.send(f"{member.mention} Welcome To {guild.name}",embed=embed) #mention User


    # @tasks.loop(minutes=15)
    # async def memberstats(self):
    #     await self.bot.wait_until_ready()
    #     guild = self.bot.get_guild(850662966646931456) #Guild ID
    #     member_channel = self.bot.get_channel(1135596411707215985) #Channel ID

    #     member_count = guild.member_count

    #     member_count_str = str(member_count).zfill(4)
    #     updated_string = " ".join(member_count_str)

    #     await member_channel.edit(name="⦿ 𝐔 𝐒 𝐄 𝐑 𝐒 = " + f"{updated_string}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed=nextcord.Embed(title=f"Hi {member.name} 💙",description="Also see these channels:\n<#1135593808583721140>\n<#1135892866032468100>\nEnjoy 😉", color=nextcord.Color.blue()) #Welcome Text
        embed.set_thumbnail(url=member.avatar)

        guild= self.bot.get_guild(850662966646931456) #Guild ID
        channel=guild.get_channel(1135892819110805544) #Channel ID
        await channel.send(f"{member.mention} Welcome To {guild.name}",embed=embed) #mention User)
        try:
            # Attempt to send a welcome message to the user via DM
            await member.send("""
💙  بسم الله الرحمن الرحیم 💙 

سلام دوست عزیزم، سرور در حال کانفیگ و دیزاین هست ... 
برای جلوگیری از برخی سواستفاده های احتمالی امکان عضویت دوستان تا زمان بازگشایی سرور وجود نداره 

مرسی از صبر و شکیبایی شما

https://discord.gg/google

برای پشتیبانی می‌توانید با آیدی‌های زیر تماس بگیرید 👑
<@672846574019280896>
<@1052663801448771766>
            """)
        except nextcord.errors.Forbidden as e:
            # Handle the Forbidden error here, e.g., log it or inform the server owner.
            await channel.send(f"{member.mention}\n{e}") #mention User)

        # You might want to remove this line if you don't intend to kick the user.
        await guild.kick(member)

def setup(bot):
    bot.add_cog(Onjoin(bot))
