import discord
from discord.ext import commands
from datetime import datetime
from cogs.api_coingecko import *


bot = commands.Bot(command_prefix='!', description="This a helper bot")

extensions = ['cogs.api_localBit', 'cogs.api_coingecko', 'cogs.chat_discord']

	#info 
@bot.command()
async def info(ctx):
        embed = discord.Embed(title="📝 **Información sobre Rasner**")
        embed.add_field(name=f"**Información:**", value="Rasner fue creado por Chapi & Abiel, para servidores hispanos.")
        embed.add_field(name=f"**Comandos:**", value="Los comandos todavía están en construcción")
        embed.set_footer(text="https://laputamadre.co")
        await ctx.send(embed=embed)

#para verificar usuarios


@bot.event
async def on_ready():
	print('estoy listo')

# ACA CARGAMOS LAS EXTENSIONES
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

    bot.run('NjI3MTc0Njk2NTI1NDk2MzIw.XY41lA.6RogRECBjKe1E5aMkY6uOD0sRV8')

