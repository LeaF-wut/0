import discord
import random
from discord.ext import commands
from config import settings


bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() 
async def hog(ctx): 
    author = ctx.message.author 
    await ctx.send(f'⠀⠀⠘⡀ HOG RIDAAAAAA ⠀⠀ ⠀⠀⠀  ⡜⠀⠀⠀ ⠀\n⠀  ⠑⡀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀\n⠀⠀⠀⠀⠈⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠀⠀\n⠀⠀⠀ ⠀⠀⠀⢸⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠤⠄⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠘⣀⠄⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠉⢈⠩⢙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠠⠀⠀⠨⠐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢐⠐⠌⡌⢄⢐⢈⠔⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⡏⠉⡀⠐⡀⢁⠈⠐⠱⠑⡑⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⢗⠀⠀⠐⡠⡛⠔⡁⢜⡔⡬⢎⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠡⠀⠀⠀⠀⠂⠁⠀⠄⢂⠈⠂⢂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⡿⢟⠩⠐⡀⠀⠀⠀⠐⠐⠁⠓⠒⠒⢀⠁⢐⢝⢟⢿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⠫⠡⠡⠨⢀⠂⠠⠀⠀⢁⠑⡱⠛⠗⡓⢂⠠⢸⢸⢨⠣⡝⣻⣿⣿⣿⣿⣿⣿\n⣿⢏⢐⢁⠊⢌⠐⡈⠄⠠⠀⠀⠀⠀⠁⠑⠈⠀⢄⢕⠸⡨⠪⡪⡘⣻⣿⡿⣿⣿⣿\n⣿⢂⠂⡂⠅⡂⠅⡐⠨⢐⠐⠠⠠⡀⢄⠠⡠⡡⡱⡐⠕⢌⢊⢆⢣⢒⠽⢿⣿⣿⣿\n⠣⢂⠂⠄⠡⠐⠐⠈⠌⡐⠨⡈⠢⠨⡂⢌⢂⠆⡪⠨⡊⠂⡂⠢⢡⣢⣣⡣⣍⢿⣿\n⠨⢂⢂⠁⡀⠀⠀⠁⠐⠈⠐⠈⢈⠈⠐⡀⠄⠁⠌⠈⠔⣄⡀⠠⡑⡂⠆⠢⢂⠑⠽\n⡨⠐⠀⠀⠀⢠⡎⡀⠀⠀⠄⠈⡀⠌⠐⠠⠈⠄⡁⠂⡀⡫⠑⣑⠀⢂⠌⠄⢕⠀⠨\n⠺⡪⠢⡀⠀⠞⢇⢂⠀⠂⡀⠠⠀⠄⠁⠌⠨⠀⢄⠢⡁⢂⢿⡟⡀⠀⠈⠈⡀⠂⣰\n⢀⢀⠀⠄⠀⠀⡐⠀⡈⠄⡐⠅⡊⠌⢌⠄⡕⡑⡁⢂⠂⢂⠸⣿⡄⠀⠈⣠⣴⣿⣿\n⢐⠔⠠⠀⠀⡐⠠⢈⠢⢑⠄⠑⢈⠊⡂⡱⢁⣂⢌⢔⢌⢄⠀⠹⢀⣺⡿⣟⢿⣿⣿\n⢀⠡⠁⠂⠐⠠⠈⠄⢈⠠⢈⢢⡣⣗⠕⠄⣕⢮⣞⣞⣗⣯⢯⡷⡴⣹⡪⣷⣿⣿⣿\n⠊⠄⠠⠠⠡⠈⠠⢐⠠⡊⡎⣗⢭⢐⠹⡹⣮⡳⡵⣳⣻⢾⣻⣽⣻⣺⣺⣽⣿⣿⣿\n⣨⣾⢐⠰⠐⠅⡂⡂⢕⢜⢜⢵⢹⢑⢔⠨⢘⠸⡹⡵⣯⣻⢽⣳⣻⣺⢞⡿⣿⣿⣿\n⣿⣿⡔⠠⢈⠐⠐⢠⢱⢸⢸⢸⢸⠰⡡⢘⢔⢕⠝⢮⣳⢽⢝⡾⡵⡯⣏⠯⣿⣿⣿\n⣿⣿⣗⢅⢢⠠⠡⠢⡱⡑⡕⡕⢅⠣⡊⢨⢪⡣⡣⡂⡬⡳⢽⢽⢽⢽⣞⣧⠙⣿⣿\n⡻⣿⡯⡪⠢⡡⠡⢑⢌⠪⡪⡊⠆⢌⠪⢐⢕⢱⢱⢱⢱⢱⢙⢮⡫⡟⣞⢮⣳⠙⣿\n⠊⣿⣯⠪⡊⠄⢅⠂⢂⠁⢇⢇⢃⠂⢕⠐⠌⡲⡰⡡⣇⠇⢇⢕⠪⠉⠂⠅⠂⡑⠹\n⣸⢿⣳⢱⠨⡐⡽⡿⡶⡾⡬⡢⢂⠅⡢⢡⣌⠐⠈⢎⢎⢎⢔⠠⠡⠠⠠⠡⡁⡂⠡\n⡯⡯⡇⢅⠕⠠⢱⢹⡙⢮⢹⠨⡂⡂⢇⠌⠮⡳⠅⡂⢕⠡⡑⠠⢁⢁⣡⣡⣢⣶⣿\n⣗⢽⢌⡢⡡⡡⡸⡢⡣⡣⡱⡑⠔⡈⢎⢆⢂⠂⠅⣢⡳⣽⡐⢅⢂⣊⣿⣿⣿⣿⣿\n⣯⢯⢷⢽⢮⢯⣺⣪⢞⡮⣳⢘⠔⢌⢜⣞⣖⣮⣻⢮⣯⢷⣿⣻⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿') 
@bot.command()
async def bitches(ctx): 
    author = ctx.message.author 
    await ctx.send(f'🇳 🇴  🇧 🇮 🇹 🇨 🇭 🇪 🇸 ❓ ❔ \n⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝\n⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇\n⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀ \n ⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀ ⠀\n ⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀ ⠀⠀\n  ⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀ ⠀⠀⠀\n    ⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀\n      ⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀\n      ⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀\n      ⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀\n    ⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀\n    ⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀\n    ⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀') 

#@bot.command()
#async def femboy(ctx):
#    author = ctx.message.author 
#    await ctx.send(f'                  ⣀⣤⣤⣤⣤⣤⣤⣀\n              ⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀\n             ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n           ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n           ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠛⠛⠿⠿⣿⣷⣄\n           ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷\n   ⢀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀ ⠀⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣇\n⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⡿\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\n⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\n ⠙⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n       ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃\n        ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n         ⢻⣿⣿⣿⡿⣟⣯⣿⠟⡉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿\n          ⠻⢿⣽⣿⣿⣿⠿⠿⠟⠒⠉⠉⠉⠉⠉⠉⠉⠙⠋\n            ⠈⠿⠋⠉⢀⣠⣤⣤⡔⣄\n               ⣴⠾⠛⠋⠉⠀⢀⣀⠐⣤⣶⣶⡤⢤⣤\n              ⣤⣰⣶⣾⣿⣿⣿⣆⠀⣀⣀⡀⣀⡀\n               ⠉⠉⠀⢀⢀⣀⠀⣀⣈⡿⠿⠿⠽⠃\n               ⠛⠛⠿⠿⠿⠿⠾⠟⢁⣀⡴⣦⠆\n              ⢦⣤⣀⣀⠀⠀⠀⠀⢘⣿⣍⡷⠆\n             ⢶⣄⠈⠉⠛⠛⠿⠓⠀⠉⠋⠉⣀\n            ⣧⡀⠙⠻⢶⣶⡤⠀⠀⠛⠶⠾⠼⠋\n           ⣆⠈⠻⣶⣤⡀⠀⠀⢸⠿⣶⣦⣤⣠⣾\n           ⢠⠙⢷⣤⣀⠈⠁⠀⠀⢠⣤⣀⠈⠉⠈\n           ⡌⢧⣀⠉⠛⠃⠀⠀⠀⠀⠉⠛⠿⠿⠻⠃\n         ⠰⢳⣄⠙⠛⢋⠁⠀⠀  ⠘⠿⣴⣤⣄⣤⡄\n          ⣄⡙⠛⠋⠀⠀⠀⠀  ⠰⣤⣀⠉⠉⠉\n        ⢀⢠⡈⠉⠉⠀⠀⠀⠀⠀ ⢀⡈⠙⠛⠛⠛⠁\n       ⠈⢦⡉⠛⡁⠀⠀  ⠀   ⠈⠻⠷⣶⣦⡆\n      ⡈⢷⣌⠙⠛⠁ ⠀ ⠀⠀   ⠰⣦⣄⣀⣀⡀\n    ⠈⢷⣄⡉⠛⠛⠀⠀  ⠀⠀⠀   ⢀⠈⠙⠛⠛\n    ⢦⣀⠉⠛⠷⠖⠀⠀⠀⠀⠀⠀    ⠘⠿⣶⣦⡄\n  ⣠⣀⠙⠳⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀    ⢠⣀⣀⣀\n  ⠙⠻⢿⣶⣤⣤⠀⠀⠀⠀⠀⠀     ⢠⠛⠛⠻⠿\n ⣦⣄⠈⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈\n⢹⣿⣿⣶⡆⠀⠀⠀⠀⠀⠀⠀          ⠺⠿⠿⠿⠁\n⠙⠻⠟⠁⠀⠀⠀⠀⠀              ⢀⣤⣤⣤⣤⡄\n                          ⠈⣀⣀⣀⣀⠁')

@bot.command()
async def ok(ctx):
    embed= discord.Embed(color = 0xff9900)
    embed.set_image(url = 'https://leaf-wut.github.io/files/index.jpg')
    await ctx.send(embed = embed)

@bot.command()
async def furry(ctx):
    arts = ['https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/2RQn7d2_0So.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/2bO9UjdWGV4.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/4Wbk29OPMxw.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/5CnjbVIUAfk.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/5M2eZTc7ilw.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/5oHShNBFh20.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/81lt5xnRJUU.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/91u0gZ1eJ8g.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/Cdr2a_v0Xqc.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/GZa-kcmVQvE.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/HXC_ZALwa-M.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/IQN8I96fxfw.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/Kfy0RSjBD5g.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/M0uxIGxjscM.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/PTnsiayqcvg.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/Qc6i678Qhaw.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/VmVN905SeLg.png?raw=true','https://github.com/LeaF-wut/leaf-wut.github.io/blob/master/files/OUT/WEZCxP-6a_Q.png?raw=true'] 
    embed=discord.Embed(color = 0x888888)
    embed.set_image(url = random.choice(arts))
    await ctx.send(embed = embed)


bot.run(settings['token'])