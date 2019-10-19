from discord.ext import commands
import discord
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

#esta funcion es saber el valor de una cripto moneda e cualquier moneda(coingecko)
class Cgecko(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def conv(self, ctx, arg1= None, arg2= None, n: int= None, *args):
		if arg1 is None:
			embed = discord.Embed(title="Por favor especifica las monedas a convertir.", color=discord.Color.red())
			embed.add_field(name="**Utilización:**", value="!conv [a] [b] [cantidad]\n **Ejemplo:** !conv bitcoin-cash usd 10")
			await ctx.send(embed=embed)
		else:
			if arg2 is None:
				valornuevo = cg.get_price(ids=f'{arg1.lower()}', vs_currencies='usd')
				vresult = valornuevo[f'{arg1.lower()}']['usd']
				embed = discord.Embed(title=f"Un **{arg1.lower()}** es igual a {vresult} en **USD**")
				embed.set_footer(text="Resultado automático en USD, ejemplo de uso: !conv bitcoin ltc")
				await ctx.send(embed=embed)
			else:
				if n >= 0:
					valornuevo = cg.get_price(ids=f'{arg1.lower()}', vs_currencies=f'{arg2.lower()}')
					vresult = valornuevo[f'{arg1.lower()}'][f'{arg2.lower()}']
					vr = float(vresult)
					m = vr * n
					embed = discord.Embed(title=f'{m}', color=discord.Color.green())
					await ctx.send(embed=embed)                 
				else:	
					valornuevo = cg.get_price(ids=f'{arg1.lower()}', vs_currencies=f'{arg2.lower()}')
					vresult = valornuevo[f'{arg1.lower()}'][f'{arg2.lower()}']
					embed = discord.Embed(title=f'Un **{arg1.lower()}** es igual {vresult} **{arg2.lower()}**.', color=discord.Color.green())
					await ctx.send(embed=embed)

	@commands.command()
	async def lista(self, ctx):
		embed = discord.Embed(title="Listado de monedas disponibles.", color=discord.Color.red())
		embed.add_field(name="**Utilización:**", value="``!cv [a] [b]`` = ``[a] es igual a [b].``")
		embed.add_field(name="**[a]:**", value="``bitcoin, litecoin, dogecoin, bitcoin-cash, ethereum, ripple, eos``")
		embed.add_field(name="**[b]:**", value="``btc, ltc, dogecoin, bitcoin-cash, eth, xrp, eos, usd, ars, cop, brl, cad, eur, mxn``")
		await ctx.send(embed=embed)



def setup(bot):
	bot.add_cog(Cgecko(bot))
	print('Coingecko cargo')



""" 
@conv.error
async def on_command_error(self, ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title='Estas monedas no corresponden a ninguna moneda disponible en la base de datos, intenta con otra.', color=discord.Color.red())
		await ctx.send(embed=embed)
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title='Especifique a moneda en texto, ejemplo: usd', color=discord.Color.red())
		await ctx.send(embed=embed)

	raise error
"""
"""
@conv.error
async def conv_error(ctx, error):
	embed = discord.Embed(title=f'Estas monedas no corresponden a ninguna moneda disponible en la base de datos, intenta con otra.', color=discord.Color.red())
	await ctx.send(embed=embed)
"""