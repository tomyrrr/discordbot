
from binhex import REASONABLY_LARGE
from cgitb import text
from smtplib import _Reply
from turtle import title
import discord
from discord.ext import commands 

bot = commands.Bot(command_prefix="!") 

@bot.event
async def on_ready():
    print("je sui la")
    channel = bot.get_channel(957244742373109803)
    await channel.send("TomBot Est Dersomais en Ligne")

@bot.command()
async def jeux(ctx):
    await ctx.send("https://www.roblox.com/games/6141543464/IDA-RP-FR")

@bot.command()
async def invite(ctx):
    await ctx.send("https://discord.com/invite/CAHnVcuGJc")


@bot.command()
async def vote(ctx):
    await ctx.send("https://top-serveurs.net/roblox/ida-rp")


@bot.command()
async def  hhelp(ctx):
    await ctx.send("Voicie Mes Comandes")
    _Reply(vote)



bot.run("OTU3MjQ1Mjc2OTg3NDgyMTkz.Yj7-Ig.fc7sVB7cHVk_1Nte8KQgB70F09o")