from flask import Flask,render_template,request
from nltk.chat.util import reflections,Chat 
import re


pairs = [
    [
        r"hi|hey|hello|hiiiiiiiiiii",
        ["hello","hi"]
    ],
    [
        r"What is your name ?",
        ["My name is chatbot created to talk to people "]
    ],
    [
        r"How are you ?",
        ["I am fine...thankyou\n What about you??"]
    ],
    [
        r"(.*) age?",
       [ "I am computer program.....dont you know that"]
    ],
    [
        r"(.*) location|city ?",
        ["Jaipur","Gwalior"]
    ],
    [
        r"how is weather in (.*)",
        ["Weather is awesome in %1.....you will love it"]
    ],
    [
        r"(.*) bye| bye (.*)|quit|bye",
        ["Okay bye it wasn't nice talking to you","bye bye take care"]
    ],
    [
        r"who created you?.*",
        ["A very sensible woman :)"]
    ],
    [
        r"w.* are you?",
        ['None of your business..']
    ],
    [
        r"I am (.*)",
        ['You are welcome %1']
    ],
    [
        r"(.*)",
        ["Tell me something new about you...."]
    ]
]

chat = Chat(pairs,reflections)
#chat.converse()


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/get")
def home():
    msg = request.args.get("msg")
    print(msg)
        #for var in pairs:
            #if re.search(var[0],msg):
                #return str(var[1])
    return chat.respond(msg)
            


app.run(port=80,debug=True)
