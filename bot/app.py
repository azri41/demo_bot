from flask import Flask, jsonsify, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    res = str(english_bot.get_response(userText))
    return jsonsify({"response" : res})

if __name__ == "__main__":
    app.run(host="0.0.0.0",)



# from flask import Flask, jsonify,request
# import time
# app = Flask(__name__);
# @app.route("/bot", methods=["POST"])
# def response():
#     query = dict(request.form)['query']
#     res = query + " " + time.ctime()
#     return jsonify({"response" : res})
# if __name__=="__main__":
#     app.run(host="0.0.0.0",)