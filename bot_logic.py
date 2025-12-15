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

#Envia um dos memes que está na pasta "images" se o comando $meme for digitado NO SERVIDOR
#Na linha 19 (Desse código) altera qual o nome do comando "async def !meme!(ctx)". Se ele (o nome do comando) for alterado
#Exclua o terminal (deligue o bot) e inicie o bot (ligue o bot)
@bot.command()
async def meme(ctx):
    image_name = random.choice(os.listdir('images'))
    with open (f'images/{image_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

#Escolhe um nome se digitar $choose op1 op2 op3. Se for opções com espaços Ex: "op1 espaço1" "op2 espaço2 " "op3 espaço3"
#Ou Ex: op1_espaço1 op2_espaço2 op3_espaço3
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    if not choices:
        await ctx.send("Você precisa passar pelo menos uma opção. Ex: op1 op2 op3. Ex: (aspas)op1 espaço1(aspas) (a)op2 espaço2(a)  (a)op3 espaço3(a)")
        return
    await ctx.send(random.choice(choices))

#Gera uma senha aleatória usando os dígitos da linha 38
@bot.command()
async def password(ctx, *pass_length: int):
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
