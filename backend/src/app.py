from flask import Flask, jsonify, request, render_template, Markup, send_file
from PIL import Image, ImageFont, ImageDraw
from flask_cors import CORS
from FancyQuotePoster import FancyQuotePoster as FQP #template creator
import io
import base64

app = Flask(__name__)
CORS(app)

@app.route("/download-img/test", methods=["GET", "POST"])
def test():
    clientData = request.json
    text = clientData['test']
    b64 = clientData['b64']
    b64_png = Image.open(io.BytesIO(base64.b64decode(b64))).resize((600,600))
    im_io = io.BytesIO()
    im_bg = ImageDraw.ImageDraw(b64_png)
    im_bg.text((10,0), text, fill='black')
    b64_png.save(im_io, 'png', quality=70)
    im_io.seek(0)
    im_io_png = base64.b64encode(im_io.getvalue())
    context = im_io_png.decode('UTF-8')
    return jsonify({'imgData':context, 'test':text})


@app.route("/download-img/model-1", methods=["GET", "POST"])
def templateModel1():
    clientData = request.json
    bgImgData = clientData['uploadedImgData']
    quote = clientData['quoteText']
    quoteSource = clientData['quoteSource']
    quoteOwner = clientData['quoteOwner']
    logoImg  = clientData['logoImg']
    website = clientData['websiteDomain']

    bgImg = io.BytesIO(base64.b64decode(bgImgData))
    logo = io.BytesIO(base64.b64decode(logoImg))

    imgTemp2 = FQP(bg=bgImg)
    imgTemp2.add_bg_filter((145,123,190), opacity=100)
    imgTemp2.add_bg_text_model(size=(800, 850), position=(-110,0),opacity=180) 
    imgTemp2.add_text_quote(quote, position_reset=True, position=(180, 360), align='left')
    imgTemp2.add_text_quote_owner(quoteOwner, position_reset=True, position=(180,870)) 
    imgTemp2.add_website(website, text_position=(0,-560))
    imgTemp2.add_logo(logo, position=(-100, -340))

    im_io = io.BytesIO()
    imgTemp2.bg.save(im_io, 'png', quality=70)
    
    im_io.seek(0)
    im_io_png = base64.b64encode(im_io.getvalue())
    context = im_io_png.decode('UTF-8')
    return jsonify({'imgData':context, 'quote':quote, 'quoteOwner':quoteOwner, 'quoteSource':quoteSource, 'logoImg':logoImg})


@app.route("/download-img/model-2", methods=["GET", "POST"])
def templateModel2():
    clientData = request.json
    bgImgData = clientData['uploadedImgData']
    quote = clientData['quoteText']
    quoteSource = clientData['quoteSource']
    quoteOwner = clientData['quoteOwner']
    logoImg  = clientData['logoImg']
    website = clientData['websiteDomain']

    bgImg = io.BytesIO(base64.b64decode(bgImgData))
    logo = io.BytesIO(base64.b64decode(logoImg))

    imgPost = FQP(bg=bgImg)
    imgPost.add_bg_filter((255, 214, 107)) 
    imgPost.add_bg_text_model(frame=True)
    imgPost.add_text_quote(quote, position=(0,-30), base_text_size=80, max_text_width=650)
    imgPost.add_text_quote_owner(quoteOwner, position=(0,480))
    imgPost.add_text_quote_source(quoteSource, position=(0, 315))

    imgPost.add_logo(logo, position=(0, -300))
    imgPost.add_website(website, text_position=(0, 560))
    im_io = io.BytesIO()
    
    imgPost.bg.save(im_io, 'png', quality=70)
    
    im_io.seek(0)
    im_io_png = base64.b64encode(im_io.getvalue())
    context = im_io_png.decode('UTF-8')
    return jsonify({'imgData':context, 'quote':quote, 'quoteOwner':quoteOwner, 'quoteSource':quoteSource, 'logoImg':logoImg})

@app.route("/download-img/model-3", methods=["GET", "POST"])
def templateModel3():
    clientData = request.json
    bgImgData = clientData['uploadedImgData']
    quote = clientData['quoteText']
    quoteSource = clientData['quoteSource']
    quoteOwner = clientData['quoteOwner']
    logoImg  = clientData['logoImg']
    website = clientData['websiteDomain']

    bgImg = io.BytesIO(base64.b64decode(bgImgData))
    logo = io.BytesIO(base64.b64decode(logoImg))

    imgTemp3 = FQP(bg=bgImg)
    imgTemp3.add_bg_text_model(size=(600, 1200), opacity=180) 
    imgTemp3.add_bg_text_model(size=(120, 8), opacity=300, rgb=(0,0,0), position=(0, -300)) 
    imgTemp3.add_bg_text_model(size=(120, 8), opacity=300, rgb=(0,0,0), position=(0, 250)) 
    imgTemp3.add_text_quote(quote, max_text_width=410,position=(0,-50)) 
    imgTemp3.add_logo(logo, position=(0, -450), resize=(200,200))
    imgTemp3.add_text_quote_owner(quoteOwner, position=(0,480))

    im_io = io.BytesIO()
    imgTemp3.bg.save(im_io, 'png', quality=70)
    
    im_io.seek(0)
    im_io_png = base64.b64encode(im_io.getvalue())
    context = im_io_png.decode('UTF-8')
    return jsonify({'imgData':context, 'quote':quote, 'quoteOwner':quoteOwner, 'quoteSource':quoteSource, 'logoImg':logoImg})


if __name__ == '__main__':
    app.run()
