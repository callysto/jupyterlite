def get_badge(name):
    """
    Returns a badge image with the name of the person who completed the labyrinth.
    """

    import requests
    from PIL import Image, ImageDraw, ImageFont
    import datetime
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    line1_text = name
    line2_text = 'completed the'
    line3_text = 'Music'
    line4_text = 'Data Labyrinth'
    font_size = 46

    try:
        logo = '../resources/callysto-logo.jpg'
    except:
        from io import BytesIO
        logo_url = 'https://github.com/callysto/data-labyrinth/blob/main/resources/callysto-logo.jpg?raw=true'
        logo = BytesIO(requests.get(logo_url, allow_redirects=True).content)

    width, height = 400, 450
    background_color = (255, 255, 255)
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # draw the border
    draw.line((10, 10, 390, 10), fill=(0, 0, 0), width=3)
    draw.line((10, 10, 10, 440), fill=(0, 0, 0), width=3)
    draw.line((390, 10, 390, 440), fill=(0, 0, 0), width=3)
    draw.line((10, 440, 390, 440), fill=(0, 0, 0), width=3)

    # get the image
    image_to_embed = Image.open(logo).resize((200, 200))
    image.paste(image_to_embed, (100, 20+font_size*2+20))

    # get the font
    import requests
    import io
    r = requests.get('https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/RobotoCondensed-Regular.ttf', allow_redirects=True)
    font = ImageFont.truetype(io.BytesIO(r.content), size=font_size)

    # text positions
    line1_size = draw.textlength(line1_text, font=font)
    line2_size = draw.textlength(line2_text, font=font)
    line3_size = draw.textlength(line3_text, font=font)
    line4_size = draw.textlength(line4_text, font=font)
    line1_position = ((width - line1_size) // 2, 20)
    line2_position = ((width - line2_size) // 2, 20+font_size)
    line3_position = ((width - line3_size) // 2, 20+font_size*2+10+200)
    line4_position = ((width - line4_size) // 2, 20+font_size*3+10+200)

    # draw the text on the image
    draw.text(line1_position, line1_text, fill=(111, 74, 158), font=font)
    draw.text(line2_position, line2_text, fill=(111, 74, 158), font=font)
    draw.text(line3_position, line3_text, fill=(142, 162, 161), font=font)
    draw.text(line4_position, line4_text, fill=(142, 162, 161), font=font)
    # add date
    draw.text((21, 20+font_size*4+12+200+2), date, fill=(242, 103, 34), font=ImageFont.truetype(io.BytesIO(r.content), size=14))
    # add hashtag
    draw.text((330, 20+font_size*4+12+200+2), '#callysto', fill=(242, 103, 34), font=ImageFont.truetype(io.BytesIO(r.content), size=14))

    #return(image.resize((200, 225)))
    return(image)