from lbcapi3 import api
from discord.ext import commands
import discord
import datetime

hmac_key = 	'fa004f787583c7960a6228de73c9fd26'
hmac_secret = '7e6fcb15b9732fb2156faf267a6401cdcdacde15d460f582e3a9ec0f30ea542f'

conn = api.hmac(hmac_key, hmac_secret)

precio_dolar = conn.call('GET', '/api/equation/USD_in_VES').json()
btc_in_bs = conn.call('GET', '/api/equation/btc_in_usd*USD_in_VES').json()
btc_in_usd = conn.call('GET', '/api/equation/btc_in_usd').json()

a = precio_dolar['data']
b = btc_in_bs['data']
c = btc_in_usd['data']


class LbCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	# DOLARTODAY

	#precio el general del dolar aca usamos la api de local bitcoin para dar un resume de los precios actuales(localbitcoin)
	@commands.command()
	async def mercado(self, ctx):
		embed = discord.Embed(title="Precio en tiempo real gracias a:", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
		embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/3753877149/ca76b3799963bec0c34879a429ff5f3a_400x400.png")
		embed.add_field(name="Precio actual en Bs :dollar:", value=f'{a} Bs')
		embed.add_field(name="Precio de 1 BTC en Bs :dollar:", value=f'{b} Bs')
		embed.add_field(name="Precio del BTC :dollar:", value=f'{c} $')
		await ctx.send(embed=embed)


	#multiplicador de precio del dolar(localbitcoin)
	@commands.command()
	async def usd(self, ctx, *,numero: int = None):
	    if numero is None:
	    	embed = discord.Embed(title="Precio del dólar en bolívares", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
	    	await ctx.send(embed=embed)
	    else:
	        usd_json = conn.call('GET', '/api/equation/USD_in_VES*'+f'{numero}').json()
	        r = usd_json['data']
	        embed = discord.Embed(title=f'El monto de **{numero}USD** en bolivares son **{r} Bs**', color=discord.Color.green())
	        await ctx.send(embed=embed)

	#funcion para cambiar de ves a dolares
	@commands.command()
	async def ves(self, ctx, *, n= None):
		if n is None:
			embed = discord.Embed(title=f"Especifica el monto de bolívares para convertirlos a dólares (USD), ejemplo ``!ves 70000``.\nUtiliza ``!mercado`` para conocer el mercado de hoy.",color=discord.Color.green())
			await ctx.send(embed=embed)
		else:
			usd_json = conn.call('GET', '/api/equation/USD_in_VES*1').json()
			r = usd_json['data']
			rf = float(r)
			nf = float(n)
			rm = nf / rf
			rm1 = round(rm,2)
			embed = discord.Embed(title=f"El monto de **{n} VES** es igual a **{rm1} USD**",color=discord.Color.green())
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(LbCog(bot))
	print('localbitcoin cargo')

