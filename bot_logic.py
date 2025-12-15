import discord, random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

#Configura qual que vai ser o prefixo (!@#$%¨¨&*) que vai ser usado antes do comando "/meme", "$meme","@meme"
bot = commands.Bot(command_prefix = "$", intents=intents)

#Diz se quando o bot está ligado (o discord precisa estar aberto)
@bot.event
async def on_ready():
    print(f"O{bot.user}acabou de ser ligado(Digite algum comando pro comando ser executado. Ex: $meme)")

    channel_id = 1447698629799186542 # ID do canal
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send("Digite <$help> para ver os comandos")

#Envia um dos memes que está na pasta "images" se o comando $meme for digitado NO SERVIDOR
#Na linha 19 (Desse código) altera qual o nome do comando "async def !meme!(ctx)". Se ele (o nome do comando) for alterado
#Exclua o terminal (deligue o bot) e inicie o bot (ligue o bot)
@bot.command(description="Te mostra 1 de 2 memes sobre programação")
async def meme(ctx):
    """Mostra memes sobre programação."""
    image_name = random.choice(os.listdir('images'))
    with open (f'images/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

#Escolhe um nome se digitar $choose op1 op2 op3. Se for opções com espaços Ex: "op1 espaço1" "op2 espaço2 " "op3 espaço3"
#Ou Ex: op1_espaço1 op2_espaço2 op3_espaço3
@bot.command(description="Escolhe uma das opções que foram dadas. Ex: $choose op1 op2 op3. Ex: 'op1 op' 'op2 op' 'op3 op'") 
async def choose(ctx, *choices: str):
    """Escolhe entre múltiplas escolhas."""
    if len(choices) <= 2:
        await ctx.send("Você precisa passar pelo menos 2 opções. Para mais detalhes digite $help choose")
        return
    await ctx.send(random.choice(choices))

#Gera uma senha aleatória usando os dígitos da linha 38
@bot.command(description="Cria uma senha (escolhendo os caracteres disponíveis) com o número de dígitos que foi digitado (mas tendo que ser maior que 2)")
async def password(ctx, *pass_length: int):
    """Cria uma senha com no mínimo 3 dígitos."""
    elements = "+-/*!&$#?=@<>"
    password = ""
    if not pass_length:
        await ctx.send("Você precisa colocar o número de caracteres que sua senha terá")
        return
    if pass_length:
        pass_length = int(pass_length[0])
        if pass_length >= 2:
            for i in range(pass_length):
                password += random.choice(elements)
        else:
            await ctx.send("A senha precisa ter mais de 2 caracteres")
            return
    await ctx.send(password)

bot.run("Your Token")


