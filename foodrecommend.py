from flask import Flask,request,jsonify,json
import sys

app = Flask(__name__)


foodlist =[
  ["짜장면","피자"],#000
  ["부대찌개","짬뽕"],#001
  ["내장류","보쌈","족발","치킨","회"],#010
  ["닭발","닭볶음탕","등갈비","매운치킨","불족발","아구찜","찜닭"],#011
  ["국밥","김밥","냉면","덮밥","만두","샌드위치","쌀국수","파스타","햄버거"],#100
  ["마라탕","맵떡"],#101
  ["돈가스","삼겹살","스시"],#110
  ["내장볶음","닭강정","쭈꾸미"],#111
] 

Q2 = {
  "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "Q2. 고기가 땡기나요? " }}], 
                 "quickReplies": [{"label": "고기 괜찮아요", "action": "message", "messageText": "고기 괜찮아요"},
                                  {"label": "고기 별로에요", "action": "message", "messageText": "고기 별로에요"},
                                  ]
            }
}

Q3 = {
  "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "Q3. 매운건 어떠세요? " }}], 
                 "quickReplies": [{"label": "매운거 괜찮아요", "action": "message", "messageText": "매운거 괜찮아요"},
                                  {"label": "매운거 별로에요", "action": "message", "messageText": "매운거 별로에요"},
                                  ]
            }
}

A = {
      "version" : "2.0",
                 "template" : {
                   "outputs" : [{"simpleText": {"text": "안녕하세요 "}}]
                              }
    }
    

@app.route('/food', methods=['POST'])
def index():

    global Q1
    global Q2
    global Q3
    global Q1number
    global Q2number
    global Q3number
    global keynumber
    global foodlist
    global dataSend
    global A
  
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)

    if content == u"같이먹어요":
      dataSend = Q2
      Q1number = 1
    
    elif content == u"혼밥입니다":
      dataSend = Q2
      Q1number = 0
    elif content == u"고기 괜찮아요": 
      dataSend = Q3
      Q2number = 1
    elif content == u"고기 별로에요": 
      dataSend = Q3
      Q2number = 0
    elif content == u"매운거 괜찮아요":
      Q3number = 1
      dataSend = A
      
    elif content == u"매운거 별로에요":
      Q3number = 0
      keynumber = int(Q1number) * 4 + int(Q2number) * 2 + int(Q3number)       #이진수 -> 10진수 변환
      int(keynumber)
      print(keynumber)
      dataSend = {
            "version" : "2.0",
              "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : foodlist[keynumber][0]
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

app.run(host='0.0.0.0', port=81)