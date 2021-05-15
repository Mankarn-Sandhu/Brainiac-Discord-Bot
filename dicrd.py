import discord
from discord.ext import commands
from googlesearch import search
import random

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name = '.rules for help'))
    
@bot.command()
async def wiki(ctx,*, query):
    author = ctx.author.mention

    for j in search(str("wikipedia page") + query, tld="com", num = 10, start = 0, stop = 1 , pause = 0, country = 'canada'):
        await ctx.channel.send(f"Here is your result {author}")
        await ctx.send(f"\n:point_right: {j}")

@bot.command()
async def define(ctx,*, query):
    author = ctx.author.mention
   
    for j in search(str("websters definition of") + query, tld="com", num = 10, start = 0, stop = 1 , pause = 0):
        await ctx.channel.send(f"Here is your result {author}")
        await ctx.send(f"\n:point_right: {j}")

@bot.command()
async def research(ctx,*, query):
    author = ctx.author.mention
   
    for j in search(str("google scholar") + query, tld="com", num = 10, start = 0, stop = 1 , pause = 0):
        await ctx.channel.send(f"Here is your result {author}")
        await ctx.send(f"\n:point_right: {j}")

@bot.command()
async def rules(ctx):
    myEmbed = discord.Embed(title = "Help", description = """
       .wiki to search Wikipedia articles
        
        .define to find the Websters definition of a word

        .8ball to answer all of your questions
        
        .rules to bring this up again
    
        """
        , color = 0x00ff00)
    myEmbed.add_field(name = "Version Code", value = "v1.0.1", inline = False)
    myEmbed.add_field(name = "Date Released", value = "May 14th, 2021", inline = False)
    myEmbed.set_footer(text = "Mankarn Sandhu")
    await ctx.channel.send(embed = myEmbed)


@bot.command(aliases = ['8ball', '8Ball', '8BALL', 'eightball'])
async def _8ball(ctx, *, question):
    author = ctx.author.mention

    responses = [ 'It is certain',
                'Without a doubt',
                'You may rely on it',
                'Yes definitely',
                'It is decidedly so',
                'As I see it, yes',
                'Most likely',
                'Yes',
                'Outlook good',
                'Signs point to yes',
                'Reply hazy try again',
                'Better not tell you now',
                'Ask again later',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don’t count on it',
                'Outlook not so good',
                'My sources say no',
                'Very doubtful',
                'My reply is no']
    await ctx.send(f'Question from {author}: {question} \nAnswer: {random.choice(responses)}')


bot.run('#your-token-here')
