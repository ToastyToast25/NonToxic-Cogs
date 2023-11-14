import discord
from redbot.core import commands

class TempRoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remove_temporary_member_role(self, ctx):
        member = ctx.author
        temporary_member_role_id = 1173307263570677880  # Replace with the actual ID of your "Temporary Member" role
        member_role_id = 1173304546668322866  # Replace with the actual ID of your "Member" role

        if discord.utils.get(member.roles, id=temporary_member_role_id):
            try:
                await member.remove_roles(discord.Object(id=temporary_member_role_id))

                member_role = discord.utils.get(ctx.guild.roles, id=member_role_id)
                if member_role:
                    await member.add_roles(member_role)
                    await ctx.send(f"Removed Temporary Member role and assigned Member role to {member.mention}")
                else:
                    await ctx.send("Error: Member role not found.")
            except Exception as e:
                await ctx.send(f"Error: {e}")
        else:
            await ctx.send(f"{member.mention} does not have the Temporary Member role.")

def setup(bot):
    bot.add_cog(TempRoleCog(bot))
