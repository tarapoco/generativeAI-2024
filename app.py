from flask import Flask,render_template,request
import google.generativeai as palm
import replicate
import os

os.environ['REPLICATE_API_TOKEN'] = "787f515cb0624813736c11e7fefec66473394f02"
palm.configure(api_key="AIzaSyBanf1tuv5CAcvzv02Il7ImDRGBSmEnOuk")
model = {
    "model":"models/chat-bison-001",
}

name=""
flag=1

app = Flask(name)

@app.route("/",methods=["GET", "POST"])
def index():
    global flag
    flag=1
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    global flag,name
    if flag==1:
        name = request.form.get("name")
        flag=0
    return(render_template("main.html", r=name))

@app.route("/palm_request", methods=["GET", "POST"])
def palm_request():
    return(render_template("palm.html"))

@app.route("/palm_reply", methods=["GET", "POST"])
def palm_reply():
    q = request.form.get("q")
    r = palm.chat(
    **model,
    messages=q
    )
    return(render_template("palm_reply.html", r=r.last))

@app.route("/image_request", methods=["GET", "POST"])
def image_request():
    return(render_template("image_request.html"))

@app.route("/image_reply", methods=["GET", "POST"])
def image_reply():
    q = request.form.get("q")
    r = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input={
        "prompt": q,
    },
)
    return(render_template("image_reply.html", r=r[0]))

@app.route("/music_request",methods=["GET","POST"])
def music_request():
    return(render_template("music_request.html"))

@app.route("/music_reply",methods=["GET","POST"])
def music_reply():
    q = request.form.get("q")
    r = replicate.run(
        "meta/musicgen:7be0f12c54a8d033a0fbd14418c9af98962da9a86f5ff7811f9b3423a1f0b7d7",
        input={
            "prompt": q,
            "duration:": 5
        }
    )
    return(render_template("music_reply.html",r=r))

@app.route("/video_request",methods=["GET","POST"])
def video_request():
    return(render_template("video_request.html"))

@app.route("/video_reply",methods=["GET","POST"])
def video_reply():
    q = request.form.get("q")
    r = replicate.run(
        "anotherjesse/zeroscope-v2-xl:9f747673945c62801b13b84701c783929c0ee784e4748ec062204894dda1a351",
        input={
            "prompt": q,
            "num_frames": 5
        }
    )
    time.sleep(60)
    return(render_template("video_reply.html",r=r[0]))

if __name__=="__main__":
    app.run()
