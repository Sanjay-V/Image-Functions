import os
from flask import Flask, request, render_template, send_from_directory, request, redirect, url_for, abort
from wand.image import Image
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    for upload in request.files.getlist("file"):
        filename = upload.filename
        destination = "/".join([target, filename])
        upload.save(destination)
    return render_template("index.html", image_name=filename)

@app.route('/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route("/<photo>/info")
def open_an_image_file(photo):
    target = os.path.join(APP_ROOT, 'images/')
    image = os.listdir(target)
    if photo in image:
      with Image(filename = target + "/"+ photo) as img: 
        b = img.width
        c = img.height
        e = img.format
        f = img.size 
        d = str("Image Width : " + str(b) + "  " + "Image Height : " + str(c) + "  " + "Image Format : " + str(e) + " " + "Image Size : " + str(f))
    return render_template("index.html", output = d)

@app.route("/convert")
def convert_images():
    input = "images"
    image = os.listdir(input)
    target = os.path.join(APP_ROOT, 'result/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    output = "result"
    for file in image:
        with Image(filename = input+"/"+file) as img: 
            with img.convert('jpg') as converted:
                if "." in file:
                    a = file.split('.')
                    a = a[0] + ".jpg"
                    outpath = os.path.join(output+"/"+a)
                    converted.save(filename = outpath) 
                else:
                    a = file + ".jpg"
                    outpath = os.path.join(output+"/"+a)
                    converted.save(filename = outpath) 
    return render_template("index.html", output = "Images Successfully Converted")

@app.route('/<filename>/converted')
def send_converted_image(filename):
    return send_from_directory("result", filename)

@app.route('/resize')
def resize():
    input = "result"
    image = os.listdir(input)
    target = os.path.join(APP_ROOT, 'resize/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    output = "resize"
    for file in image:
        with Image(filename = input+"/"+file) as img: 
            img.resize(50,60)
            outpath = os.path.join(output+"/"+file)
            img.save(filename = outpath) 
    return render_template("index.html", output = "Images Successfully resized")

@app.route('/<filename>/resized')
def send_resized_image(filename):
    return send_from_directory("resize", filename)

@app.route('/crop')
def crop():
    input = "result"
    image = os.listdir(input)
    target = os.path.join(APP_ROOT, 'crop/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    output = "crop"
    for file in image:
        with Image(filename = input+"/"+file) as img: 
            img.crop(width=100, height=150, gravity='center')
            outpath = os.path.join(output+"/"+file)
            img.save(filename = outpath) 
    return render_template("index.html", output = "Images Successfully cropped")

@app.route('/<filename>/cropped')
def send_cropped_image(filename):
    return send_from_directory("crop", filename)

@app.route('/blur')
def blur():
    input = "result"
    image = os.listdir(input)
    target = os.path.join(APP_ROOT, 'blur/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    output = "blur"
    for file in image:
        with Image(filename = input+"/"+file) as img: 
            img.blur(radius=0 ,sigma=3)
            outpath = os.path.join(output+"/"+file)
            img.save(filename = outpath) 
    return render_template("index.html", output = "Images Successfully blurred")

@app.route('/<filename>/blurred')
def send_blurred_image(filename):
    return send_from_directory("blur", filename)

@app.route('/edge')
def edge():
    input = "result"
    image = os.listdir(input)
    target = os.path.join(APP_ROOT, 'edge/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    output = "edge"
    for file in image:
        with Image(filename = input+"/"+file) as img: 
            img.transform_colorspace('gray')
            img.edge()
            outpath = os.path.join(output+"/"+file)
            img.save(filename = outpath) 
    return render_template("index.html", output = "Images Successfully Edged")

@app.route('/<filename>/edged')
def send_edged_image(filename):
    return send_from_directory("edge", filename)

@app.route('/emboss')
def emboss():
    input = "result"
    image = os.listdir(input)
    target = os.path.join(APP_ROOT, 'emboss/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    output = "emboss"
    for file in image:
        with Image(filename = input+"/"+file) as img: 
            img.transform_colorspace('gray')
            img.emboss()
            outpath = os.path.join(output+"/"+file)
            img.save(filename = outpath) 
    return render_template("index.html", output = "Images Successfully Embossed")

@app.route('/<filename>/embossed')
def send_embossed_image(filename):
    return send_from_directory("emboss", filename)

@app.route('/sepia_tone')
def sepia_tone():
    input = "result"
    image = os.listdir(input)
    target = os.path.join(APP_ROOT, 'sepia_tone/')
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    output = "sepia_tone"
    for file in image:
        with Image(filename = input+"/"+file) as img: 
            img.sepia_tone()
            outpath = os.path.join(output+"/"+file)
            img.save(filename = outpath) 
    return render_template("index.html", output = "Images Successfully Sepia Toned")

@app.route('/<filename>/sepia_toned')
def send_sepia_toned_image(filename):
    return send_from_directory("sepia_tone", filename)

if __name__ == "__main__":
    app.run(port=5555, debug=True)