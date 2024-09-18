

def converter(t):
    from PIL import Image, ImageFont, ImageDraw, ImageOps
    from alerttext import alert_text


    foto = Image.open('pict/pet.jpg')
    alert = Image.open('pict/alertblank.jpg')


    
    foto1 = ImageOps.contain(foto, (750, 550), method=Image.LANCZOS)

    # Поиск позиции для вставки
    
    x, y = foto1.size
    print(x, y)
    position1 = 375 - x // 2
    print(position1)
    position2 = position1 + 35
    alert.paste(foto1, (position2, 200))
    alert.save('pict/alert.jpg')
    alert.close


    alert = Image.open('pict/alert.jpg')
    font = ImageFont.truetype("pict/arial_unicode_ms_bold.otf", size=80)
    font2 = ImageFont.truetype("pict/arial_unicode_ms_bold.otf", size=60)
    font3 = ImageFont.truetype("pict/arial_unicode_ms_bold.otf", size=40)
    idraw = ImageDraw.Draw(alert)
    d = alert_text(t)
  
    idraw.text((375, 90), f"ПРОПАЛА {d[0]}", anchor="ms", font=font2, fill=(0, 0, 0, 0))
    try:
        idraw.text((375, 160), d[1], anchor="ms", font=font2, fill=(0, 0, 0, 0))
    except:
        pass
    try:
        idraw.text((130, 930), d[2], font=font, fill=(0, 0, 0, 0))
    except:
        pass
    try:
        idraw.text((375, 750), d[3], anchor="ms", font=font3, fill=(0, 0, 0, 0))
    except:
        pass
    try:
        idraw.text((375, 790), d[4], anchor="ms", font=font3, fill=(0, 0, 0, 0))
    except:
        pass
    try:
        idraw.text((375, 830), d[5], anchor="ms", font=font3, fill=(0, 0, 0, 0))
    except:
        pass
    alert.save('pict/textalert.jpg')
    return alert


