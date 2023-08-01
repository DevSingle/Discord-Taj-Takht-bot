import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.context import Context
from nextcord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionFailed, ExtensionNotFound, ExtensionNotLoaded, NoEntryPointError

from nextcord.ext.commands import command, Cog, has_role, Bot as _bot



class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx: Context, extension: str):
        try:
            if ".py" in extension:
                extension.replace(".py", "")
        except:
            await ctx.send(":warning: Please provide an extension name")
        try:
            print(self.bot.loaded_extensions[extension])
            self.bot.load_extension(self.bot.loaded_extensions[extension])
        except ExtensionNotFound:
            await ctx.send(f":warning: Extension **{extension}** doesn't exist!")
        except ExtensionAlreadyLoaded:
            await ctx.send(f":warning: Extension **{extension}** is already loaded!")
        except NoEntryPointError:
            await ctx.send(f":warning: Extension **{extension}** doesn't have a setup function")
        except ExtensionFailed as ex:
            await ctx.send(f":warning: Ran to a problem while running **{extension}**\n:x: Cause: **{ex}**")
        except KeyError:
            await ctx.send(f":warning: Extension **{extension}** doesn't exist!")
        except Exception as ex:
            await ctx.send(
                f":interrobang: An unexpected problem occured!\n:x: Cause: **{ex}**\n:small_orange_diamond: You can issues here: https://github.com/Alijkaz/ICC/issues ")
        else:
            await ctx.send(f':white_check_mark: All done! Successfully loaded **{extension}**')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx: Context, extension: str):
        try:
            if ".py" in extension:
                extension.replace(".py", "")
        except:
            await ctx.send(":warning: Please provide an extension name")
        try:
            self.bot.unload_extension(self.bot.loaded_extensions[extension])
        except ExtensionNotFound:
            await ctx.send(f":warning: Extension **{extension}** doesn't exist!")
        except ExtensionNotLoaded:
            await ctx.send(f":warning: Extension **{extension}** is not loaded yet to be unloaded!")
        except KeyError:
            await ctx.send(f":warning: Extension **{extension}** doesn't exist!")
        except Exception as ex:
            await ctx.send(
                f":interrobang: An unexpected problem occured!\n:x: Cause: **{ex}**\n:small_orange_diamond: You can issues here: https://github.com/Alijkaz/ICC/issues ")
        else:
            await ctx.send(f':white_check_mark: All done! Successfully unloaded **{extension}**')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx: Context, extension: str):
        await self.unload(ctx, extension)
        await self.load(ctx, extension)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def shutdown(self, ctx: Context):
        bot: _bot = ctx.bot
        await bot.close()

def setup(bot):
    bot.add_cog(Cog(bot))
