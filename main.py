from flask import Flask, json, request, jsonify
import sys

app = Flask(__name__)

location = {
            "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "날짜를 선택해 주세요"}}], 
                 "quickReplies": [{"label": "오늘", "action": "message", "messageText": "오늘"},
                                  {"label": "월", "action": "message", "messageText": "월"},
                                  {"label": "화", "action": "message", "messageText": "화"},
                                  {"label": "수", "action": "message", "messageText": "수"},
                                  {"label": "목", "action": "message", "messageText": "목"},
                                  {"label": "금", "action": "message", "messageText": "금"},
                                  {"label": "토", "action": "message", "messageText": "토"},
                                  {"label": "일", "action": "message", "messageText": "일"}
                                  ]
            }
        }

day = {
            "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "날짜를 선택해 주세요"}}], 
                 "quickReplies": [{"label": "오늘", "action": "message", "messageText": "오늘"},
                                  {"label": "월", "action": "message", "messageText": "월"},
                                  {"label": "화", "action": "message", "messageText": "화"},
                                  {"label": "수", "action": "message", "messageText": "수"},
                                  {"label": "목", "action": "message", "messageText": "목"},
                                  {"label": "금", "action": "message", "messageText": "금"},
                                  {"label": "토", "action": "message", "messageText": "토"},
                                  {"label": "일", "action": "message", "messageText": "일"}
                                  ]
            }
        }

Restaurant = ["안녕","반가워","ㅎㅇ","ㄷㄸ"] 

@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)

    global location
    global day
    global locationkey
    global daykey
  
    if content == u"중문":
        dataSend = location
        locationkey = 0
      
    elif content == u"정문":
        dataSend = location
        locationkey = 1
      
    elif content == u"서문":
        dataSend = location
        locationkey = 2
      
    elif content == u"후문":
        dataSend = location
        locationkey = 3

    elif content == u"일":
        daykey = 3
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "error입니다." + Restaurant[locationkey] + Restaurant[daykey]
                        }
                    }
                ]
            }
        }
    
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "error입니다." 
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)