import discord
from discord.ext import commands
import random 
import re
from urllib import parse, request

class ChatDiscord(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx):
	    await ctx.send(f'Latencia: {round(self.bot.latency * 1000)}ms')	

	@commands.command(aliases=['8ball', 'sera'])
	async def _8ball(self, ctx, *, question):
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

	@commands.command()
	async def wikipedia(self, ctx, *, search=None):
		query_String = parse.urlencode({'search_query': search})
		html_Content = request.urlopen('https://es.wikipedia.org/w/index.php?sort=relevance&search=' + query_String +'&title=Especial%3ABuscar&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns100=1&ns104=1')
		search_Result = re.findall('href=\"\\/wiki\\(.{11})', html_Content.read().decode())
		print(search_Result)
		await ctx.send('https://es.wikipedia.org/wiki/' + search_Result[0])

def setup(bot):
	bot.add_cog(ChatDiscord(bot))
	print('chat Discord cargo')
