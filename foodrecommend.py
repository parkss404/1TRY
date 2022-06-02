from flask import Flask,request,jsonify,json
import sys

app = Flask(__name__)

@app.route('/food', methods=['POST'])
def index():

    global Q1number
    global Q2number
    global Q3number
  
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)

    if content == u"같이먹어요":
      Q1number = 1
    elif content == u"혼밥입니다":
      Q1number = 0
    elif content == u"고기 괜찮아요": 
      Q2number = 0
    
    
    return jsonify(dataSend)

app.run(host='0.0.0.0', port=81)