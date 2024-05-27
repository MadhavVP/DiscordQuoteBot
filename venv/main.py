import copy
import random
import textwrap

import discord
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

token = "{YOUR_TOKEN_HERE}"

client = discord.Client()

img = [Image.open("../gfx/mountainBG.jpg"), Image.open("../gfx/desertBG.jpg"), Image.open("../gfx/roadBG.jpg")]
colors = [(200, 255, 255), (0,0,0)]
numImages = 3
imgWidth = 1200
imgHeight = 675

myFont = ImageFont.truetype('arial.ttf', 65)
padding = 5

quoteFile = "../gfx/quote.png"


@client.event
async def on_ready():
    print(f"{client.user.name} is ready!")


@client.event
async def on_message(mss):
    if mss.author == client.user:
        return
    if mss.content[0] is not '!':
        return
    if mss.author == client.user:
        return
    if mss.content == '!quoteB':
        if mss.reference is not None:
            m = mss.reference.resolved.content
            memeImg = copy.deepcopy(img[random.randint(0, numImages - 1)])
            image = ImageDraw.Draw(memeImg)
            lines = textwrap.wrap(m, width=30)
            l, t, r, b = myFont.getbbox(m)
            lineHeight = (imgHeight - (len(lines) * (b - t))) / 2
            for line in lines:
                image.text((imgWidth / 2, lineHeight), line, font=myFont, fill=colors[1], align="center", anchor="mm")
                lineHeight += (b - t) + padding
            memeImg.save(quoteFile)
            picture = discord.File(open(quoteFile, "rb"))
            await mss.channel.send(file=picture)
            await mss.channel.send(f'"{m}"\n-{mss.reference.resolved.author}')
            del memeImg
        else:
            await mss.channel.send("Not a reply!")
    if mss.content == '!quoteW':
        if mss.reference is not None:
            m = mss.reference.resolved.content
            memeImg = copy.deepcopy(img[random.randint(0, numImages - 1)])
            image = ImageDraw.Draw(memeImg)
            lines = textwrap.wrap(m, width=30)
            l, t, r, b = myFont.getbbox(m)
            lineHeight = (imgHeight - (len(lines) * (b - t))) / 2
            for line in lines:
                image.text((imgWidth / 2, lineHeight), line, font=myFont, fill=colors[0], align="center", anchor="mm")
                lineHeight += (b - t) + padding
            memeImg.save(quoteFile)
            picture = discord.File(open(quoteFile, "rb"))
            await mss.channel.send(file=picture)
            await mss.channel.send(f'"{m}"\n-{mss.reference.resolved.author}')
            del memeImg
        else:
            await mss.channel.send("Not a reply!")
    if mss.content == '!quote':
        if mss.reference is not None:
            m = mss.reference.resolved.content
            memeImg = copy.deepcopy(img[random.randint(0, numImages - 1)])
            image = ImageDraw.Draw(memeImg)
            lines = textwrap.wrap(m, width=30)
            l, t, r, b = myFont.getbbox(m)
            lineHeight = (imgHeight - (len(lines) * (b - t))) / 2
            for line in lines:
                image.text((imgWidth / 2, lineHeight), line, font=myFont, fill=colors[1], align="center", anchor="mm")
                lineHeight += (b - t) + padding
            memeImg.save(quoteFile)
            picture = discord.File(open(quoteFile, "rb"))
            await mss.channel.send(file=picture)
            await mss.channel.send(f'"{m}"\n-{mss.reference.resolved.author}')
            del memeImg
        else:
            await mss.channel.send("Not a reply!")


client.run(token)
