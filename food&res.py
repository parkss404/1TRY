from flask import Flask,request,jsonify,json
import sys

app = Flask(__name__)

foodURL = [
  [ #장터국밥
    "https://map.naver.com/v5/search/%EC%9E%A5%ED%84%B0%EC%88%9C%EB%8C%80%EA%B5%AD%EB%B0%A5/place/37683659?c=14188800.0964972,4388091.7322557,17,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #육쌈냉면 충북대점
    "https://map.naver.com/v5/entry/place/21290001?c=14188335.3376231,4387961.7934544,17,0,0,0,dh",
    #요리조리쿡쿡
    "https://map.naver.com/v5/search/%EC%9A%94%EB%A6%AC%EC%A1%B0%EB%A6%AC%EC%BF%A1%EC%BF%A1/place/17342940?c=14188462.3197663,4387933.6058072,17,0,0,0,dh&isCorrectAnswer=true",
    #월미당
    "https://map.naver.com/v5/search/%EC%9B%94%EB%AF%B8%EB%8B%B9/place/1226472334?c=14188373.3420973,4387893.6133231,17,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #모퉁이파스타
    "https://map.naver.com/v5/search/%EB%AA%A8%ED%89%81%EC%9D%B4%ED%8C%8C%EC%8A%A4%ED%83%80?c=14188609.5063970,4387901.6034849,17,0,0,0,dh",
    #버거킹
    "https://map.naver.com/v5/search/%EB%B2%84%EA%B1%B0%ED%82%B9?c=14188573.6726529,4388047.3140102,16,0,0,0,dh",
    #한가네짬뽕
    "https://map.naver.com/v5/search/%ED%95%9C%EA%B0%80%EB%84%A4%EC%A7%AC%EB%BD%95/place/37944259?c=14188355.5866385,4387981.4083276,17,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #아웃닭
    "https://map.naver.com/v5/search/%EC%95%84%EC%9B%83%EB%8B%AD/place/36379006?c=14188269.2917692,4388092.2455220,16,0,0,0,dh",
    #싱싱오징어바다
    "https://map.naver.com/v5/search/%EC%8B%B1%EC%8B%B1%EC%98%A4%EC%A7%95%EC%96%B4%EB%B0%94%EB%8B%A4/place/34188345?c=14188642.9356401,4388005.5038752,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #소신보부
    "https://map.naver.com/v5/entry/place/926739775?c=14188547.3901211,4388028.7949023,17,0,0,0,dh",
    #우리집 닭강정:       
    "https://map.naver.com/v5/search/%EC%9A%B0%EB%A6%AC%EC%A7%91%EB%8B%AD%EA%B0%95%EC%A0%95/place/38612298?c=14188382.0138856,4388153.2966377,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #코리아 닭발
    "https://map.naver.com/v5/search/%EC%BD%94%EB%A6%AC%EC%95%84%EB%8B%AD%EB%B0%9C/place/1707433717?c=14188401.1274422,4387937.7396209,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #안녕닭
    "https://map.naver.com/v5/search/%EC%95%88%EB%85%95%EB%8B%AD/place/1460495164?c=14188402.1070537,4387987.4426133,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #일미리금계찜닭
    "https://map.naver.com/v5/search/%EC%9D%BC%EB%AF%B8%EB%A6%AC%EA%B8%88%EA%B3%84%EC%B0%9C%EB%8B%AD/place/1767731763?c=14188279.0878844,4387878.7566319,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #쩔어떡볶이포차
    "https://map.naver.com/v5/entry/place/1956461738?c=14188471.3811728,4388082.3963631,17,0,0,0,dh",
    #피자 웨이브
    "https://map.naver.com/v5/search/%ED%94%BC%EC%9E%90%EC%9B%A8%EC%9D%B4%EB%B8%8C/place/1437077056?c=14188472.1492773,4388006.4194238,17,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #홍스족발
    "https://map.naver.com/v5/search/%ED%99%8D%EC%8A%A4%EC%A1%B1%EB%B0%9C/place/1276617246?c=14188366.1953860,4387982.9481105,17,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #부대통령뚝배기 충북대중문점
    "https://map.naver.com/v5/entry/place/1641995762?c=14188379.9210792,4387913.0893529,17,0,0,0,dh",
    #바다향쭈꾸미낙지볶음
    "https://map.naver.com/v5/entry/place/37758290?c=14188788.9422842,4388012.6479311,17,0,0,0,dh",
    #은화수식당
    "https://map.naver.com/v5/search/%EC%9D%80%ED%95%98%EC%88%98%EC%8B%9D%EB%8B%B9/place/1751526576?c=14188178.6331759,4387932.6347774,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #곱창다방
    "https://map.naver.com/v5/search/%EA%B3%B1%EC%B0%BD%EB%8B%A4%EB%B0%A9/place/1786485744?c=14188371.5943813,4387871.8762292,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #짚신스시&롤
    "https://map.naver.com/v5/entry/place/1438031726?c=14188407.4169934,4387911.2998871,16,0,0,0,dh",
    #이런이궈
    "https://map.naver.com/v5/search/%EC%9D%B4%EB%9F%B0%EC%9D%B4%EA%B6%88/place/1119514041?c=14188489.0475760,4387948.3654715,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #한가네짬뽕
    "https://map.naver.com/v5/search/%ED%95%9C%EA%B0%80%EB%84%A4%EC%A7%AC%EB%BD%95/place/37944259?c=14188203.3127071,4387937.2124902,16,0,0,0,dh&placePath=%3Fentry%253Dpll",
    #누구나홀딱반한닭
    "https://map.naver.com/v5/entry/place/36341085?c=14188363.3456070,4387964.6788083,16,0,0,0,dh",
    #나릿집
    "https://d12zq4w4guyljn.cloudfront.net/pre_20191129062847024_photo_97428385fcd8.jpg"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","쩔어떡볶이포차","청년피자","큰손족발","땅스부대찌개","초사골불타는쭈꾸미낙지""False","False","False","False","False"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","파파돈","대구전봇대막창","짚신스시","탕화쿵푸"],
["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","면세상","가마꿉"]
]

foodimg = [
  [#장터국밥
   "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20211213_33%2F1639324342170BJWJP_JPEG%2Fupload_4f7bc055c047ea83f0e7f198e136a99d.jpeg",
   #육쌈냉면 충북대점
   "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyMjA0MjVfMTQ3%2FMDAxNjUwODgwMDM2NTE5.7SRcimmKwoe7IAer_aFQAe6dzufDso0RQoHbDQ9ILtYg.lnKyBTMDA3JqkJIfPSzl4Wr4zG41C8H4Ge6rt5sxrvIg.JPEG%2Fupload_6d456ce3af79e192ec904c8842475724.jpeg",
   #요리조리쿡쿡        
   "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMjJfMTk3%2FMDAxNjEzOTkyMTE1MTY4.IDAF_RH0t7YWBlDIZWiPKBqMOZQufBSxxI5wJpAF0Ycg.Wpc8lr1iC072nNH_bRAh8AWMSdF03zy8UYJTEVgfbSkg.JPEG.my_jk%2FIMG_5387.jpg",
   #월미당        
   "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20220313_144%2F1647143429177FwHB4_JPEG%2Fupload_0f43e5df4c64d34d2f2e8edbac3507eb.jpeg",
   #모퉁이파스타
   "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA3MDZfMTU0%2FMDAxNTMwODM2NTU3NDYx.I_-hpWuPnNwdXV-XGB5ki1how-E7aPbfMPZGnl50gTQg.lb_8l_YjBuxOGf-wkVM8hkhwYbzUDcg9k0EaC79obsEg.JPEG.azml89%2FIMG_5724.jpg",
    #버거킹:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyMjA0MjdfOTEg%2FMDAxNjUxMDY2NjMyNjk3.Wx0W65HSXErlHff7Oz0RCaLiVmVaWsjRVvo6d0y-I0Eg.E5Ti_ZkcRPSFmlkoOq-D0W8XZZAWse26lpB-6-VVMZEg.JPEG%2Fupload_893d9228811e4c4d0ebaf3ebfc94ea36.jpg",
    #한가네짬뽕:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA4MjBfMTI5%2FMDAxNTk3OTI5MDYzMDU4.s5EFI1Gs7zPWDjtIKEz4PcM1bjwYkgOxd2qtnGQJ4EMg.ga7XslfOPlU7_3qV-NsP29por4Sr8Q7gdRFvpw6aHL4g.JPEG.heykzzang%2FKakaoTalk_20200820_214524819_06.jpg",
    #아웃닭:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20220416_205%2F1650036326644MCGoW_JPEG%2Fupload_17e033ab11c59aa115f9f5b0fb81b43c.jpg",
    #싱싱오징어바다:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTEyMTVfNTIg%2FMDAxNTc2NDA4MzIxNDE0.YjY1sepfxPzA2UZ_1pKGoMMs2YaTLVgStjd-vdlvgI8g.fNyBVUHdXSRXyFzIqbxfNoqaoxOKEVW-6vqybEWlCsgg.JPEG.92__sook%2FIMG_2872.jpg",
           "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20220315_185%2F1647313153278poCw7_JPEG%2Fupload_d3039ad0f8de6590e63f9d0793e15cb3.jpg",
    #우리집 닭강정:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzAyMTVfMjMw%2FMDAxNDg3MDkyNDUxNTE1.8SYqyHGCoe-6NW6EyrwgDsYh60RZyBvEw9Ti5LbQCEAg.3UdNKcYm0XkU0-hvvc1bvVByVPtNljtEKNF0M0g2Olwg.JPEG.dh81193%2FIMG_7874.JPG",
    #코리아닭발:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20220410_289%2F1649592619770WHnzf_JPEG%2Fupload_a891ef586f4b44045f50f23850dc2614.jpeg",
    #안녕닭:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20211109_31%2F1636431113080LrSrz_JPEG%2Fupload_74896edb06c26e2caa4c4b08e8f2a67c.jpg",
    #일미리금계찜닭:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTBfMTAx%2FMDAxNjUyMTQ4OTQ3ODY0.-Wa33DcwNaPBkTKB4x8xZNP3W9Apc9RSo-DGoEiRoRAg.VYSt9g8-ZGvwONr0a2NE9YeVyAEYJwMCrXapfMgDsNYg.JPEG.hh0ops%2FKakaoTalk_20220509_133410053_16.jpg"
    #쩔어떡볶이포차:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA0MDVfMTg4%2FMDAxNjQ5MDg0NTk2MDMz.PPSuNIqNhi_QGWUUDhnsLDT0uBAC4c1Syj3r4OnEgOkg.NenUnKEHL2pZphUBhLnNbfMYPk0LKef6TFzDwhMCzYAg.JPEG.qwp0923%2F20220327%25A3%25DF222702.jpg"
    #피자웨이브:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMDJfNzYg%2FMDAxNjQzNzg1OTcyODY3.qXAFw-awCNeFVcTw7ZlbnNrgpkMeAJoAu0ec5ppi95Ag.9NNRZAa01Kd6yTw2k_13j3dE4G6qsiGjHFd4J_ECk_0g.JPEG.ghkdtjswjd11%2FKakaoTalk_20220129_013858410_16.jpg",
    #홍스족발:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTEwMTlfMjMy%2FMDAxNTcxNDU3NzYzMTI4.oC3ekJEVwkBK3v8THeMDv68UW9IOZ2iejzIHpEWqLr4g.nuqzi1JgL_oWJeC75RWZNkfOP-0O1p-m2NT5XSTVf4Ig.JPEG.kwiyongi%2F1571457762114.JPG",
    #부대통령뚝배기 충북대중문점:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA3MTVfMjky%2FMDAxNTk0NzQ4ODMwOTMz.iChUJRgpmjIKQ3opw6FX1alWCOSFqHGNcO8r3dJicQcg.9QLBeqjNDCc0pGHu_i_7Xl4ylhuGFPHF0UV179kDOp8g.JPEG.instar360%2F1594748830983.jpg",
    #바다향쭈꾸미낙지볶음:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTA1MDlfNCAg%2FMDAxNTU3NDExMzIzNTk3.B5P53qWInd2l3pE9izyqcwOKMVf-yUhydHOIOtt5wHEg.eWhLBCH30D6kqGV9Jyt80JHASrnUg-kfAtitMaq272gg.JPEG.pallorabbit%2F20.JPG",
    #은하수식당:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20220321_245%2F164784083154595B7w_JPEG%2Fupload_e2caeb2872f2b4228c1f73aee4a8cc14.jpg",
    #곱창다방:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTJfMjk3%2FMDAxNjUyMzM1NTM2NDAy.apZToWVXvjX9ZCbUoj0sPw_mNucPrPs2tiZ7n5X7RNog.gHIt-fPkboZo7qP-5zIiIrKpl4jctcTSFrhChl7ZkUYg.JPEG.dlsrlrhdwb%2F20220507%25A3%25DF192353.jpg",
    #짚신스시&롤:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODExMTNfMjY1%2FMDAxNTQyMTE0ODExMzM3.rZDdOkpoKmWg_ztVJOnVopP4OfmJXhv84fUu1WvP_Tkg.q9BMLpM9icx_ySvZ1QtTY2FzF7wFTZ1MwFhyYr32IVEg.JPEG.syh9158%2F1542114621991.jpg",
    #이런이궈:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDExMDNfMjkw%2FMDAxNjA0NDE0NDA5MTk3.UN5u52MOIPkfgQyX4vXTEaqsOMXuPDk_mHBqNz8oH1Qg.cBhwW02KwOnNPCMgVVsJC7G5D37puICiE03V1eJQigsg.JPEG.lsy960423%2FIMG_7298.jpg",
    #한가네짬뽕:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2F20160806_228%2Fsuyony1004_1470415420520zmYM2_JPEG%2FP20160708_144842360_3B51E754-62C5-4FBD-BD23-656B05736FA1.JPG",
    #누구나홀딱반한닭:       
    "https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2F20151115_226%2Fhello_myboo_14475260908460p4Nd_JPEG%2FNaverBlog_20151115_033450_15.jpg",
    #나릿집:       
    "https://map.naver.com/v5/entry/place/748715743?c=14188687.6081518,4388051.7114360,13,0,0,0,dh&entry=plt"
    #나릿집:       
    "https://map.naver.com/v5/entry/place/748715743?c=14188687.6081518,4388051.7114360,13,0,0,0,dh&entry=plt"
  ],
          ["순돌이뚱글이순대:https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA2MTZfMjcg%2FMDAxNTI5MTUzMDcxMjAz.QvQZHuvUcz8xyyxh_KL7mYsyxhOxjJEQj2hmt34wIfAg.DjWnwvlmc6ug_kQAhEjsiGhmwSSsETVBbIIwc-auuPwg.JPEG.since950513%2FIMG_4864.jpg",
                "냉면",
                "덮밥",
                "쌀국수",
                "올엔조이https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200310_184%2F1583829765418l18up_JPEG%2FcNVWryvUWVRjIpS8oZfQWIoG.jpg",
                "햄버거",
                "장군반점https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA0MjdfMTQ2%2FMDAxNTg3OTY2NDMwMjc1.18KrOHxynws_TqoqtyX8d7WiOIDuVsji1ZdPuOH-YGMg.dwMFoKKgGZi0xfe_ux0VqXVKZHYS3N4yjG_VwQ5eTgAg.JPEG.coco1938%2FIMG_6420.jpg",
                "가마꿉 청주충북대점https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MzFfMjI1%2FMDAxNjU0MDAyMzc5ODQx.LO8xJU16SK42PzirrqdiyVVh-yStIDiy1xvBuH3jNBgg.0fu5liS4SWQdGPqiiDmk41Tr2O0lc1_1jO0mtQlOtMsg.JPEG.hej051109%2Foutput_3750848045.jpg",
                "수산시장https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA5MDZfMTE3%2FMDAxNTk5Mzc0MTAyNjYx.xtbS7g51-cTpQLVQPJMA_VW6Ry7UCJGMHSuyhuoZGNAg.msmdCme7K75xEh1Mk1iHNNWK9nyI7i9Jwk60TVj3Ljkg.JPEG.mko0506%2F1599374101603.jpg",
                "장충동뚱뚱이할머니족발보쌈https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODAyMDhfNTIg%2FMDAxNTE4MDk5MzE0Mjc1.HsAHDYbgfj6nx5d1DA3pVD51Bya9PPWZxp8m-htAUMkg.9ADamr9alFOdrpZGyceRa6hIl_V48z1cBGGFr2mnm2Mg.JPEG.qogpwltkfkd1%2FIMG_7885.jpg",
                "닭강정",
                "신날개 복대점https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA3MTVfMTM4%2FMDAxNjI2MzUwNjAxMjE1.BLncvF_ajDse2UGv2MRVUNlF0VWNyDGXb1XuPHud0OUg.xCdXtgFiOUFKelmgdVHsKOAqcqkApI1W3QCFQYgsrp4g.JPEG.dbstjdwls82%2F20210715%25A3%25DF182538.jpg",
                "청주닭갈비&닭떡볶이https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20201108_53%2F1604837417810OcY4H_JPEG%2Fupload_a84a6454d59b392c606f0172de1f1313.jpeg",
                "찜닭",
                "청주닭갈비&닭떡볶이https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=https%3A%2F%2Fmyplace-phinf.pstatic.net%2F20201108_53%2F1604837417810OcY4H_JPEG%2Fupload_a84a6454d59b392c606f0172de1f1313.jpeg",
                "옐로우피자https://search.pstatic.net/common/?autoRotate=true&quality=95&type=w750&src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MDhfMTYx%2FMDAxNjUxOTg2Mzk5NzYx._TBSSOKnYvQ4uCxObQGM6bX7buEBkC1SZIuQpZ47V8Ug.3ZbiOCgfaBBhYsLfb3yHE-hqxQf9cqGLZZpUedl25YIg.JPEG.bgr2829%2FIMG_7077.jpg",
                "큰손족발",
                "땅스부대찌개",
                "초사골불타는쭈꾸미낙지",
                "오유미당 청주개신점",
                "증평은성집",
                "하루초밥",
                "마라탕왕훠궈",
                "비룡각",
                "매운치킨",
                "현고들깨손칼국수",
                "삼겹살"],
           [],
           []
          ]
           


foodlist =[
  ["짜장면6","피자15"],#000
  ["부대찌개17","짬뽕22"],#001
  ["보쌈9","족발16","치킨7","회8","삼겹살25"],#010
  ["닭발11","닭볶음탕12","매운치킨23","찜닭13"],#011
  ["국밥0","냉면1","덮밥2","쌀국수3","파스타4","햄버거5"],#100
  ["마라탕21","떡볶이1"],#101
  ["돈까스19","스시20"],#110
  ["닭강정10","쭈꾸미18"],#111
] 
#0,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22 = 22개 
#1,14,24 
#냉면,맵떡,매운치킨

list = [""]


Restaurant = [
              ["장터순대국밥","육쌈냉면 충북대점","요리조리쿡쿡","월미당","모퉁이파스타","버거킹","한가네짬뽕","아웃닭","싱싱오징어바다","소주신랑 보쌈부인","우리집 닭강정","코리아 닭발","안녕닭","일미리금계찜닭","쩔어떡볶이포차","피자웨이브","홍쓰족발","부대통령뚝배기 충북대중문점","바다향쭈꾸미.낙지볶음","은화수식당","곱창다방","짚신스시&롤","이런이궈","한가네짬뽕","누구나홀딱반한닭","나릿집"],
["순돌이뚱글이순대","냉면","덮밥","쌀국수","올엔조이","햄버거","장군반점","가마꿉 청주충북대점","수산시장","장충동뚱뚱이할머니족발보쌈","닭강정","신날개 복대점","청주닭갈비&닭떡볶이","찜닭","청주닭갈비&닭떡볶이","옐로우피자","큰손족발","땅스부대찌개","초사골불타는쭈꾸미낙지","오유미당 청주개신점","증평은성집","하루초밥","마라탕왕훠궈","비룡각","매운치킨","나릿집"],
["청주직지감자탕뼈찜","강남면옥","덮밥","쌀국수","달꽃다방","바니시버거","짜장면","똥짐참맛있는집","오징어회포차","보쌈당한족발","닭강정","엄마닭발","일미닭갈비파전 본점","찜닭","신전떡볶이","피자파는집 청주흥덕구점","둥지마을왕족발","부대찌개","쭈꾸미","파파돈","대구전봇대막창","삼촌스시","탕화쿵푸","짬뽕","매운치킨","나릿집"],
["병천토종순대 직영점","서민냉면얼큰칼국수","덮밥","쌀국수","파스타","햄버거","짜장면","에꿍이치킨","팔팔어시장","보쌈","닭강정","서울닭발","닭볶음탕","찜닭","떡보라","피자","족발","부대찌개","쭈꾸미","김우동","막창선생","초밥한조각 사직점","마라탕","면세상","가마꿉","나릿집"]
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
      dataSend = {
  "version" : "2.0",
            "template" : {
                "outputs" : [{"simpleText": {"text": "Q2. 고기가 땡기나요? \n2/3" }}], 
                 "quickReplies": [{"label": "고기 괜찮아요", "action": "message", "messageText": "고기 괜찮아요"},
                                  {"label": "고기 별로에요", "action": "message", "messageText": "고기 별로에요"},
                                  ]
            }
}
      
      Q1number = 0
      print(Q1number)
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
    global foodURL
    global foodimg
  
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

    elif content == u"삼겹살":
        dataSend = location
        foodkey = 25

    elif content == u"중문":
        locationkey = 0
        dataSend = {
          "version": "2.0",
                            "template": {"outputs": [{'basicCard': {"title": Restaurant[locationkey][foodkey],
                                                                    "thumbnail": {"imageUrl": foodimg[locationkey][foodkey],
                                                                       },
                                                                            
                                                                    "buttons": [
                                                
                                                                        {
                                                                            "action": "webLink",
                                                                            "label": "가게정보보기",
                                                                            "webLinkUrl": foodURL[locationkey][foodkey]
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
          "version": "2.0",
                            "template": {"outputs": [{'basicCard': {"title": Restaurant[locationkey][foodkey],
                                                                    "thumbnail": {"imageUrl": foodimg[locationkey][foodkey],
                                                                       },
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

    elif content == u"정문":
        locationkey = 2
        dataSend = {
          "version": "2.0",
                            "template": {"outputs": [{'basicCard': {"title": Restaurant[locationkey][foodkey],
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

    elif content == u"후문":
        locationkey = 3
        dataSend = {
          "version": "2.0",
                            "template": {"outputs": [{'basicCard': {"title": Restaurant[locationkey][foodkey],
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