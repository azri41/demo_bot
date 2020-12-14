# from flask import Flask, jsonify,request
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# import os

# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# try:
#     os.remove("db.sqlite3")
#     print("Old database removed. Training new database")
# except:
#     print('No database found. Creating new database.')

# english_bot = ChatBot('Bot')
# english_bot.set_trainer(ListTrainer)
# for file in os.listdir('data'):
#     print('Training using ' + file)
#     convData = open('data/' + file).readlines()
#     english_bot.train(convData)
#     print("Training completed for " + file)

# filenumber = int(os.listdir('saved_conversations')[-1])
# filenumber = filenumber + 1
# file = open('saved_conversations/' + str(filenumber), "w+")
# file.write('bot : Hi There! I am a medbot. You can begin conversation by typing in a message and pressing enter.\n')
# file.close()

# app = Flask(__name__)

# english_bot = ChatBot('Bot',
#                       storage_adapter='chatterbot.storage.SQLStorageAdapter',
#                       logic_adapters=[
#                           {
#                               'import_path': 'chatterbot.logic.BestMatch'
#                           },

#                       ],
#                       trainer='chatterbot.trainers.ListTrainer')
# english_bot.set_trainer(ListTrainer)


# app = Flask(__name__)
# @app.route("/bot", methods=["POST"])
# def response():
#     query = dict(request.form)['query']
#     res = str(english_bot.get_response(query))

#     appendfile = os.listdir('saved_conversations')[-1]
#     appendfile = open('saved_conversations/' + str(filenumber), "a")
#     appendfile.write('user : ' + query + '\n')
#     appendfile.write('bot : ' + res + '\n')
#     appendfile.close()

#     return jsonify({"response" : res})


# if __name__=="__main__":
#     app.run(host="0.0.0.0",)

from flask import Flask, jsonify,request
import time
app = Flask(__name__);
@app.route("/bot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    res = query + " " + time.ctime()
    return jsonify({"response" : res})
if __name__=="__main__":
    app.run(host="0.0.0.0",)