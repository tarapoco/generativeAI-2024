from flask import Flask,request,render_template
import google.generativeai as palm

palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")
model = {
    "model": "models/chat-bison-001",
}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
    
@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("name")
    return(render_template("main.html",r=name))

@app.route("/palm_request",methods=["GET","POST"])
def palm_request():
    return(render_template("palm.html"))

@app.route("/palm_reply",methods=["GET","POST"])
def palm_reply():
    q = request.form.get("q")
    r = palm.chat(
        **model,
        messages=q
    )
    return(render_template("palm_reply.html",r=r.last))

if __name__ == "__main__":
    app.run()
