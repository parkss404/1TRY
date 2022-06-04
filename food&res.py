from flask import Flask,request,jsonify,json
import sys

app = Flask(__name__)

foodimg = [
  ["장터순대국밥","육쌈냉면 충북대점","요리조리쿡쿡","월미당","모퉁이파스타","버거킹","한가네짬뽕","아웃닭","싱싱오징어바다","https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20220315_185%2F1647313153278poCw7_JPEG%2Fupload_d3039ad0f8de6590e63f9d0793e15cb3.jpg","우리집 닭강정","코리아 닭발","안녕닭","일미리금계찜닭","쩔어떡볶이포차","피자웨이브","족발","부대찌개","쭈꾸미","은화수식당","막창","짚신스시&롤","이런이궈","한가네짬뽕","매운치킨","등촌칼국수"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","쩔어떡볶이포차","청년피자","큰손족발","땅스부대찌개","초사골불타는쭈꾸미낙지""False","False","False","False","False"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","파파돈","대구전봇대막창","짚신스시","탕화쿵푸"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","면세상","가마꿉"]
]

foodlist =[
  ["짜장면6","피자15"],#000
  ["부대찌개17","짬뽕22"],#001
  ["보쌈9","족발16","치킨7","회8"],#010
  ["닭발11","닭볶음탕12","매운치킨23","찜닭13"],#011
  ["국밥0","냉면1","덮밥2","쌀국수3","파스타4","햄버거5"],#100
  ["마라탕21","떡볶이1"],#101
  ["돈까스19","삼겹살","스시20"],#110
  ["닭강정10","쭈꾸미18"],#111
] 
#0,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22 = 22개 
#1,14,24 
#냉면,맵떡,매운치킨

list = [""]


Restaurant = [
              ["장터순대국밥","육쌈냉면 충북대점","요리조리쿡쿡","월미당","모퉁이파스타","버거킹","한가네짬뽕","아웃닭","싱싱오징어바다","소주신랑 보쌈부인","우리집 닭강정","코리아 닭발","안녕닭","일미리금계찜닭","쩔어떡볶이포차","피자웨이브","홍쓰족발","부대통령뚝배기 충북대중문점","바다향쭈꾸미.낙지볶음","은화수식당","곱창다방","짚신스시&롤","이런이궈","한가네짬뽕","누구나홀딱반한닭","등촌칼국수"],
["순돌이뚱글이순대","냉면","덮밥","쌀국수","올엔조이","햄버거","장군반점","가마꿉 청주충북대점","수산시장","장충동뚱뚱이할머니족발보쌈","닭강정","신날개 복대점","청주닭갈비&닭떡볶이","찜닭","청주닭갈비&닭떡볶이","옐로우피자","큰손족발","땅스부대찌개","초사골불타는쭈꾸미낙지","오유미당 청주개신점","증평은성집","하루초밥","마라탕왕훠궈","비룡각","매운치킨","현고들깨손칼국수"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","파파돈","대구전봇대막창","짚신스시","탕화쿵푸"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","면세상","가마꿉"]
]


location = {
            "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "위치를 선택해 주세요" }}], 
                 "quickReplies": [{"label": "중문", "action": "message", "messageText": "중문"},
                                  {"label": "정문", "action": "message", "messageText": "정문"},
                                  {"label": "서문", "action": "message", "messageText": "서문"},
                                  {"label": "후문", "action": "message", "messageText": "후문"},
                                  ]
            }
        }

Q2 = {
  "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "Q2. 고기가 땡기나요? \n2/3" }}], 
                 "quickReplies": [{"label": "고기 괜찮아요", "action": "message", "messageText": "고기 괜찮아요"},
                                  {"label": "고기 별로에요", "action": "message", "messageText": "고기 별로에요"},
                                  ]
            }
}

Q3 = {
  "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "Q3. 매운건 어떠세요? \n3/3" }}], 
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
    global list
  
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)

    if content == u"같이 먹어요":
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
      keynumber = int(Q1number) * 4 + int(Q2number) * 2 + int(Q3number)       #이진수 -> 10진수 변환
      int(keynumber)
      for i in foodlist[keynumber]:
        list[0] = list[0] + " " + i
      dataSend = {
            "version" : "2.0",
              "template" : {
                "outputs" : [{"simpleText": {"text": "오늘은 이거 어떠세요? \n이 중 하나 말하시면 충북대학교 주변 맛집을 추천해 드립니다! " }}], 
                 "quickReplies": [{"label": list[0], "action": "message", "messageText": list[0]}, 
                      
                                  ]
            }
        }
      
    elif content == u"매운거 별로에요":
      Q3number = 0
      keynumber = int(Q1number) * 4 + int(Q2number) * 2 + int(Q3number)       #이진수 -> 10진수 변환
      int(keynumber)
      print(keynumber)
      for i in foodlist[keynumber]:
        list[0] = list[0] + " " + i
  
      dataSend = {
            "version" : "2.0",
              "template" : {
               "outputs" : [{"simpleText": {"text": "오늘은 이거 어떠세요? \n이 중 하나 말하시면 충북대학교 주변 맛집을 추천해 드립니다! " }}], 
                 "quickReplies": [{"label": list[0], "action": "message", "messageText": list[0]},
                                  
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

  
@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)

    global location
    global food
    global locationkey
    global foodkey
    global Restaurant
  
    if content == u"국밥":
        dataSend = location
        foodkey = 0
      
    elif content == u"냉면":
        dataSend = location
        foodkey = 1
      
    elif content == u"덮밥":
        dataSend = location
        foodkey = 2
      
    elif content == u"쌀국수":
        dataSend = location
        foodkey = 3

    elif content == u"파스타":
        dataSend = location
        foodkey = 4
      
    elif content == u"햄버거":
        dataSend = location
        foodkey = 5
      
    elif content == u"짜장면":
        dataSend = location
        foodkey = 6
      
    elif content == u"치킨":
        dataSend = location
        foodkey = 7

    elif content == u"회":
        dataSend = location
        foodkey = 8
      
    elif content == u"보쌈":
        dataSend = location
        foodkey = 9
      
    elif content == u"닭강정":
        dataSend = location
        foodkey = 10
      
    elif content == u"닭발":
        dataSend = location
        foodkey = 11

    elif content == u"닭볶음탕":
        dataSend = location
        foodkey = 12
      
    elif content == u"찜닭":
        dataSend = location
        foodkey = 13

    elif content == u"떡볶이":
        dataSend = location
        foodkey = 14
      
    elif content == u"피자":
        dataSend = location
        foodkey = 15
      
    elif content == u"족발":
        dataSend = location
        foodkey = 16
      
    elif content == u"부대찌개":
        dataSend = location
        foodkey = 17
        print(foodkey)

    elif content == u"쭈꾸미":
        dataSend = location
        foodkey = 18

    elif content == u"돈까스":
        dataSend = location
        foodkey = 19
      
    elif content == u"막창":
        dataSend = location
        foodkey = 20
      
    elif content == u"스시":
        dataSend = location
        foodkey = 21
      
    elif content == u"마라탕":
        dataSend = location
        foodkey = 22

    elif content == u"짬뽕":
        dataSend = location
        foodkey = 23
      
    elif content == u"매운치킨":
        dataSend = location
        foodkey = 24

    elif content == u"중문":
        locationkey = 0
        dataSend = {
          "version": "2.0",
                            "template": {"outputs": [{'basicCard': {"title": Restaurant[locationkey][foodkey],
                                                                    "description": "가성비 맛집 소.신.보.부",
                                                                    "thumbnail": {"imageUrl": foodimg[locationkey][foodkey],
                                                                                  "link": {"web": "https://map.naver.com/v5/entry/place/926739775?c=14188687.6081518,4388051.7114360,13,0,0,0,dh&placePath=%2Fhome&entry=plt"
                                                                                           }},
                                                                    "buttons": [
                                                
                                                                        {
                                                                            "action": "webLink",
                                                                            "label": "가게정보보기",
                                                                            "webLinkUrl": "https://map.naver.com/v5/entry/place/926739775?c=14188687.6081518,4388051.7114360,13,0,0,0,dh&placePath=%2Fhome&entry=plt"
                                                                        },
                                                                        {
                                                                            "action": "share",
                                                                            "label": "공유하기",
                                                                        }
                                                                    ]
                                                                    }
                                                      }
                                                     ]
                                         }
                            }

    elif content == u"서문":
        locationkey = 1
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : Restaurant[locationkey][foodkey]
                        }
                    }
                ]
            }
        }

    elif content == u"정문":
        locationkey = 2
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : Restaurant[locationkey][foodkey]
                        }
                    }
                ]
            }
        }

    elif content == u"후문":
        locationkey = 3
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : Restaurant[locationkey][foodkey]
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