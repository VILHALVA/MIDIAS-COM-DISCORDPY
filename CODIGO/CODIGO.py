import discord
from discord.ext import commands
from TOKEN import TOKEN

media_files = {
    'foto': './MIDIAS/FOTO.png',
    'musica': './MIDIAS/AUDIO.mp3',
    'video': './MIDIAS/VIDEO.mp4',
    'documento': './MIDIAS/LIVRO.pdf'
}

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot de Mídia (Tipos) está rodando como {bot.user}')

@bot.command()
async def start(ctx):
    await ctx.send('Bem-vindo ao bot MIDIAS:\n'
                   '/foto - Envia uma foto\n'
                   '/musica - Envia uma música\n'
                   '/video - Envia um vídeo\n'
                   '/documento - Envia um livro')

@bot.command()
async def foto(ctx):
    try:
        file = discord.File(media_files['foto'])
        await ctx.send(file=file)
    except Exception as e:
        print(f'Erro ao enviar foto: {e}')
        await ctx.send('Desculpe, ocorreu um erro ao enviar a foto.')

@bot.command()
async def musica(ctx):
    try:
        file = discord.File(media_files['musica'])
        await ctx.send(file=file)
    except Exception as e:
        print(f'Erro ao enviar música: {e}')
        await ctx.send('Desculpe, ocorreu um erro ao enviar a música.')

@bot.command()
async def video(ctx):
    try:
        file = discord.File(media_files['video'])
        await ctx.send(file=file)
    except Exception as e:
        print(f'Erro ao enviar vídeo: {e}')
        await ctx.send('Desculpe, ocorreu um erro ao enviar o vídeo.')

@bot.command()
async def documento(ctx):
    try:
        file = discord.File(media_files['documento'])
        await ctx.send(file=file)
    except Exception as e:
        print(f'Erro ao enviar documento: {e}')
        await ctx.send('Desculpe, ocorreu um erro ao enviar o documento.')

bot.run(TOKEN)
