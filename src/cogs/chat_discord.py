import discord
from discord.ext import commands
import random 
import re
from urllib import parse, request
import argparse
import translators as ts
import wikipedia
import datetime

class ChatDiscord(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx):
	    await ctx.send(f'Latencia: {round(self.bot.latency * 1000)}ms')	

	@commands.command(aliases=['ask'])
	async def pregunta(self, ctx, question = None):
		if question is None:
			responses = ['en la India hay una piedra de 7 metros colocada en una pendiente bajo un ángulo de 45º que es imposible de mover.',
			'la velocidad de 100 kilómetros por hora se alcanzó por primera vez en 1899.',
			'el papel moneda fue inventado por los chinos en el siglo 8, pero su uso no se introdujo en Europa hasta el año 1661.',
			'hay más potencia de procesamiento en una calculadora TI-83 que en el equipo que hizo aterrizar el Apolo XI en la Luna.',
			'antes de que existieran los relojes de alarma, los métodos para despertar eran tan variados como extraños. Hombres y mujeres conocidos como Knocker-Uppers recorrían las calles de las principales ciudades de Inglaterra e Irlanda armados con palos largos.',
			'la palabra «bancarrota» viene del renacimiento italiano. Cuando un banquero quebraba o cometía algún tipo de fraude, las autoridades del lugar le rompían el banco sobre el que se sentaba para trabajar. Aunque simbolizaba que ya no podía continuar con su actividad, literalmente lo dejaban con la «banca rota»',
			'una de las guerras más largas de la historia abarca el conflicto entre los Países Bajos y las islas Sorlingas, que forman parte de Gran Bretaña. Duró más de 3 siglos sin un solo disparo. De hecho, la guerra terminó al pasar un par de meses después de su comienzo, en 1651.']
			await ctx.send(f"Hey, tú {ctx.author}, si algo me quieres preguntar, entonces algo deberías preguntar. **Oye**, por cierto sabías que {random.choice(responses)}")
		else:
			responses = ['En mi opinión, sí Es cierto',
					'Es decididamente así',
					'Probablemente',
					'Buen pronóstico',
					'Todo apunta a que sí',
					'Sin duda',
					'Sí',
					'Sí - definitivamente',
					'Debes confiar en ello',
					'Respuesta vaga, vuelve a intentarlo',
					'Pregunta en otro momento',
					'Será mejor que no te lo diga ahora',
					'No puedo predecirlo ahora',
					'Concéntrate y vuelve a preguntar',
					'Puede ser',
					'No cuentes con ello',
					'Mi respuesta es no',
					'Mis fuentes me dicen que no',
					'Las perspectivas no son buenas',
					'Muy dudoso']
			await ctx.send(f'**Pregunta:** {question}\n**Respuesta:** {random.choice(responses)}')	

	@commands.command()
	async def abrazar(self, ctx, member: discord.Member = None):
	    if member is None:
	        embed = discord.Embed()
	        embed.add_field(name="Felipe VI", value=f"{ctx.author} se está abrazando a si mismo 😔")
	        responses = ['https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500',
	        'https://media1.tenor.com/images/f2805f274471676c96aff2bc9fbedd70/tenor.gif?itemid=7552077',
	        'https://media1.tenor.com/images/f9c540c2b5cdb52f22ed835478b0a36f/tenor.gif?itemid=10751424',
	        'https://media1.tenor.com/images/af76e9a0652575b414251b6490509a36/tenor.gif?itemid=5640885',
	        'https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075',
	        'https://media1.tenor.com/images/40aed63f5bc795ed7a980d0ad5c387f2/tenor.gif?itemid=11098589']
	        embed.set_image(url=random.choice(responses))
	        await ctx.send(embed=embed)
	    else: 
	        embed = discord.Embed()
	        embed.add_field(name="Felipe IV", value=f"{ctx.author} está abrazando a {member.mention}, que bonito♥")
	        responses = ['https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500',
	        'https://media1.tenor.com/images/f2805f274471676c96aff2bc9fbedd70/tenor.gif?itemid=7552077',
	        'https://media1.tenor.com/images/f9c540c2b5cdb52f22ed835478b0a36f/tenor.gif?itemid=10751424',
	        'https://media1.tenor.com/images/af76e9a0652575b414251b6490509a36/tenor.gif?itemid=5640885',
	        'https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075',
	        'https://media1.tenor.com/images/40aed63f5bc795ed7a980d0ad5c387f2/tenor.gif?itemid=11098589']
	        embed.set_image(url=random.choice(responses))
	        await ctx.send(embed=embed)

	@commands.command()
	async def besar(self, ctx, member: discord.Member = None):
	    if member is None:
	        embed = discord.Embed()
	        embed.add_field(name="Felipe VI", value=f"{ctx.author} se está besando a si mismo, que cosa tan... ¿rara? 😳")
	        responses = ['https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515',
	        'https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865',
	        'https://media1.tenor.com/images/2f23c53755a5c3494a7f54bbcf04d1cc/tenor.gif?itemid=13970544',
	        'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657',
	        'https://media1.tenor.com/images/22856bcdae011c480af1b500f2b526f5/tenor.gif?itemid=7301675',
	        'https://media1.tenor.com/images/40e72d8a56db62aa6e0acc993656eb33/tenor.gif?itemid=7363594',
	        'https://media1.tenor.com/images/783be11e4b3fcf56753444022247c9f6/tenor.gif?itemid=14497632',
	        'https://media1.tenor.com/images/4cfbebd9af3d054f73a9e79f704f9fbb/tenor.gif?itemid=9782353',
	        'https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409']
	        embed.set_image(url=random.choice(responses))
	        await ctx.send(embed=embed)
	    else: 
	        embed = discord.Embed()
	        embed.add_field(name="Felipe VI", value=f"{ctx.author} está besando a {member.mention}, estoy sin palabras😳")
	        responses = ['https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515',
	        'https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865',
	        'https://media1.tenor.com/images/2f23c53755a5c3494a7f54bbcf04d1cc/tenor.gif?itemid=13970544',
	        'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657',
	        'https://media1.tenor.com/images/22856bcdae011c480af1b500f2b526f5/tenor.gif?itemid=7301675',
	        'https://media1.tenor.com/images/40e72d8a56db62aa6e0acc993656eb33/tenor.gif?itemid=7363594',
	        'https://media1.tenor.com/images/783be11e4b3fcf56753444022247c9f6/tenor.gif?itemid=14497632',
	        'https://media1.tenor.com/images/4cfbebd9af3d054f73a9e79f704f9fbb/tenor.gif?itemid=9782353',
	        'https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409']
	        embed.set_image(url=random.choice(responses))
	        await ctx.send(embed=embed)

	@commands.command(aliases=['cry'])
	async def llorar(self, ctx, member: discord.Member = None):
	    if member is None:
	        respuestas = [f'{ctx.author} está triste😔, ouf.',
	        f'Ugh, creo que {ctx.author} necesita un abrazo :(',
	        f'😔✌',]		
	        embed = discord.Embed()
	        embed.add_field(name="Felipe VI", value=f"{random.choice(respuestas)}")
	        responses = ['https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314',
	        'https://media1.tenor.com/images/09b085a6b0b33a9a9c8529a3d2ee1914/tenor.gif?itemid=5648908',
	        'https://media1.tenor.com/images/4b5e9867209d7b1712607958e01a80f1/tenor.gif?itemid=5298257',
	        'https://media1.tenor.com/images/f7fde4b118501c8fa5cb1a5dd171beab/tenor.gif?itemid=5652242',
			'https://media1.tenor.com/images/de730b51400ed4dfb66d04141ea79a2d/tenor.gif?itemid=7353410',
			'https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296']
	        embed.set_image(url=random.choice(responses))
	        await ctx.send(embed=embed)
	    else: 
	        embed = discord.Embed(aliases=['translate'])
	        embed.add_field(name="Felipe VI", value=f"{ctx.author} está llorando {member.mention} 😔")
	        responses = ['https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314',
	        'https://media1.tenor.com/images/09b085a6b0b33a9a9c8529a3d2ee1914/tenor.gif?itemid=5648908',
	        'https://media1.tenor.com/images/4b5e9867209d7b1712607958e01a80f1/tenor.gif?itemid=5298257',
	        'https://media1.tenor.com/images/f7fde4b118501c8fa5cb1a5dd171beab/tenor.gif?itemid=5652242',
			'https://media1.tenor.com/images/de730b51400ed4dfb66d04141ea79a2d/tenor.gif?itemid=7353410',
			'https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296']
	        await ctx.send(embed=embed)
	        #para borrar 5 mensajes 
	#    YOUTUBE
	@commands.command()
	async def youtube(self, ctx, *, search= None):
		if search is None:
			embed = discord.Embed(title="Escribe algo que quieras buscar el youtube.", color=discord.Color.red())
			await ctx.send(embed=embed)
		else:
			#convertirlo para que pueda ser leido por la url 
			query_string = parse.urlencode({'search_query': search})
			#aqui hacemos la peticion a youtube y nos devuelve html
			html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
			#con esta expresión regular extraemos los id en una especie de lista
			search_result = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
			print(search_result)
			await ctx.send('https://www.youtube.com/watch?v=' + search_result[0])

	# TRADUCTOR
	@commands.command()
	async def tr(self, ctx, tar= None, *, txt= None):
		if tar is None:
			embed = discord.Embed(title="**Cómo traducir:** \nUse ``!tr <idioma al que vas a traducir> <texto o palabra>``", color=discord.Color.red())
			embed.add_field(name="**Idiomas:**", value=f"``zh``: Chino\n``en``: Inglés\n``jp``: Japonés\n``fr``: Francés\n``it``: Italiano\n``de``: Alemán\n``tr``: Turco\n``ru``: Ruso\n``pt``: Portugués")
			await ctx.send(embed=embed)
		elif txt is None:
			await ctx.send("Escribe algo para traducir.")	
		else:
			r = ts.tencent(txt, 'es', f'{tar}')
			await ctx.send(f'{txt} **->** {r} |*{ctx.author}*')

	# TRADUCTOR RECEPTOR
	@commands.command()
	async def trg(self, ctx, tar= None, *, txt= None):
		if tar is None:
			embed = discord.Embed(title="**How to translate to Spanish:** \nUse ``!trg <your language> <text>``", color=discord.Color.red())
			embed.add_field(name="**Languages:**", value=f"``zh``: Chinese\n``en``: English\n``jp``: Japanese\n``fr``: French\n``it``: Italian\n``de``: German\n``tr``: Turkish\n``ru``: Russian\n``pt``: Portuguese")
			await ctx.send(embed=embed)
		elif txt is None:
			await ctx.send("You didn't specify any sentence or word to translate.")	
		else:
			r = ts.tencent(txt, f'{tar}', 'es')
			await ctx.send(f'{txt} **->** {r} | *{ctx.author}*')

	@commands.command()
	async def wikipedia(self, ctx, *, search=None):
		wikipedia.set_lang("es")
		page = wikipedia.page(f"{search}")
		data = wikipedia.summary(f"{search}" , sentences = 5 , chars = 0 , auto_suggest = True , redirect = True)
		if search is None:
			embed = discord.Embed(title="Por favor introduce algo que quieras buscar en Wikipedia.", color=discord.Color.red())
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title="Wikipedia", color=discord.Color.green(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="URL del resultado en Wikipedia", value=f"{page.url}")
			embed.add_field(name=f"Resultado encontrado para '{search}'", value=f"{data}")
			embed.set_image(url=f"{page.images[0]}")
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(ChatDiscord(bot))
	print('chat Discord cargo')
