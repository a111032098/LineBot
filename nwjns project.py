# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 19:43:46 2024

@author: shu
"""

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, ImageSendMessage,  BubbleContainer,PostbackEvent, TextSendMessage, ImagemapSendMessage, BaseSize, MessageImagemapAction, URIImagemapAction, ImagemapArea, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction, LocationSendMessage, MessageTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from linebot.models import MessageEvent, TextMessage, TextSendMessage, BubbleContainer, ImageComponent, BoxComponent, TextComponent, IconComponent, ButtonComponent, SeparatorComponent, FlexSendMessage, URIAction

import random

line_bot_api = LineBotApi('1F/2d2b2L/kK5A7eG3ArVE2UCxu/i4JowxAXbBbr4KhTDmDxOM5XfnKO7cHKyJIt2HMvmG65Afr1Qh0Jl5KTlp+YiOv8ZjWJ57OQHrT+NrHv0QI6/wNYTK9OdcriHTvyFl5dSr96yNXSjbfZEvJ67wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('27f1258e0f6d04823087314d4fa84acc')

jean = ['Sweet like bubble gum.','You little demon in my stotyline.','Oh my baby sweet like bubble gum.','Your my favourite flavor bubble gum'] #定義一個想要隨機回覆的list

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@成員介紹':
        sendMember(event)
    elif mtext == 'MINJI':  # 如果消息內容為特定命令 
        try: 
            message = TextSendMessage(   
                text = "金玟池 / 김민지 / Kim Min-ji / 2004.05.07（20歲）/ Chanel"  # 創建文字消息內容 
                ) 
            line_bot_api.reply_message(event.reply_token, message)  # 回覆
        except: 
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))  # 發生錯誤時回覆錯誤訊息
    elif mtext == 'HANNI':  # 如果消息內容為特定命令 
        try: 
            message = TextSendMessage(   
                text = "范玉欣 / 하니 / Phạm Ngọc Hân / 2004/10/06（19歲）/ Gucci"  # 創建文字消息內容 
                ) 
            line_bot_api.reply_message(event.reply_token, message)  # 回覆
        except: 
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))  # 發生錯誤時回覆錯誤訊息
    elif mtext == 'DANIELLE':  # 如果消息內容為特定命令 
        try: 
            message = TextSendMessage(   
                text = "牟智慧 / 모지혜 / Mo Ji Hye / 2005/04/11（19歲）/ Celine"  # 創建文字消息內容 
                ) 
            line_bot_api.reply_message(event.reply_token, message)  # 回覆
        except: 
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))  # 發生錯誤時回覆錯誤訊息
    elif mtext == 'HAERIN':  # 如果消息內容為特定命令 
        try: 
            message = TextSendMessage(   
                text = "姜諧潾 / 강해린 / Kang Hae Rin / 2006/05/15（18歲）/ Dior "  # 創建文字消息內容 
                ) 
            line_bot_api.reply_message(event.reply_token, message)  # 回覆
        except: 
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))  # 發生錯誤時回覆錯誤訊息
    elif mtext == 'HYEIN':  # 如果消息內容為特定命令 
        try: 
            message = TextSendMessage(   
                text = "李惠仁 / 이혜인 / Lee Hye In / 2008/04/21（16歲）/ Louis Vuitton"  # 創建文字消息內容 
                ) 
            line_bot_api.reply_message(event.reply_token, message)  # 回覆
        except: 
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))  # 發生錯誤時回覆錯誤訊息
    elif mtext == '@專輯介紹':
        sendCarousel(event)
    elif mtext == '@拍攝地點':
            sendFlex(event)
    elif mtext == '@彩蛋':
        randomRespond(event)


@handler.add(PostbackEvent)  #PostbackTemplateAction觸發此事件

def sendMember(event):  #圖片地圖
    try:
        image_url = 'https://imgur.com/mGMzz7Y.jpg'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 277
        message = ImagemapSendMessage(
            base_url=image_url,
            alt_text="NewJeans成員",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                MessageImagemapAction(  #顯示文字訊息
                    text='MINJI',
                    area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                        x=0, 
                        y=0, 
                        width=imgwidth*0.2, 
                        height=imgheight  
                    )
                ),
             MessageImagemapAction(  #顯示文字訊息
                 text='HANNI',
                 area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                     x=imgwidth*0.2, 
                     y=0, 
                     width=imgwidth*0.2, 
                     height=imgheight  
                 )
             ),
             MessageImagemapAction(  #顯示文字訊息
                 text='DANIELLE',
                 area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                     x=imgwidth*0.4, 
                     y=0, 
                     width=imgwidth*0.2, 
                     height=imgheight  
                 )
             ),
             MessageImagemapAction(  #顯示文字訊息
                 text='HAERIN',
                 area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                     x=imgwidth*0.6, 
                     y=0, 
                     width=imgwidth*0.2, 
                     height=imgheight  
                 )
             ),
             MessageImagemapAction(  #顯示文字訊息
                 text='HYEIN',
                 area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                     x=imgwidth*0.8, 
                     y=0, 
                     width=imgwidth*0.2, 
                     height=imgheight  
                 )
             ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        


def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='How Sweet',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/Ep9Q8fw.jpg',
                        title='How Sweet',
                        text='Tittle Track',
                        actions=[
                            URITemplateAction(
                                label='Official M/V',
                                uri='https://www.youtube.com/watch?v=Q3K0TOvTOno&pp=ygUJSE9XIFNXRUVU'
                            ),
                            MessageTemplateAction(
                                label='🐇🍭',
                                text="Don't you know how sweet it taste?"
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/5cShWaT.jpg',
                        title='Bubble Gum',
                        text='B-Side',
                        actions=[
                            URITemplateAction(
                                label='Official M/V',
                                uri='https://www.youtube.com/watch?v=ft70sAYrFyY&pp=ygUKQlVCQkxFIEdVTQ%3D%3D'
                            ),
                            MessageTemplateAction(
                                label='🐇🫧',
                                text='Sweet like bubble gum.'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendFlex(event):  #彈性配置
    try:
        message = FlexSendMessage(alt_text="彈性配置範例", contents=
{
"type": "carousel",
"contents": [
{
"type": "bubble",
"hero": {
"type": "image",
"url": "https://imgur.com/Y8aXLHf.png",
"size": "full",
"aspectRatio": "20:15",
"aspectMode": "cover"
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "玉田路",
"size": "xl",
"weight": "bold",
"color": "#B06500",
"style": "normal"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": "📍",
"size": "sm",
"flex": 1,
"color": "#000000"
},
{
"type": "text",
"text": "新北市萬里區玉田路",
"flex": 10,
"size": "sm",
"color": "#000000"
}
]
}

]
}
]
},
"footer": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "button",
"action": {
"type": "uri",
"label": "地點",
"uri": "https://maps.app.goo.gl/pkR6GKKvXwfUbwgV9"
},
"color": "#B06500",
"margin": "none",
"height": "sm"
}
]
}
},
{
"type": "bubble",
"hero": {
"type": "image",
"url": "https://imgur.com/WGrzQMc.png",
"size": "full",
"aspectRatio": "20:15",
"aspectMode": "cover"
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "宜蘭礁溪:鄉間道路",
"weight": "bold",
"style": "normal",
"size": "xl",
"color": "#B06500"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{

"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": "📍",
"color": "#000000",
"size": "sm",
"flex": 1
},
{
"type": "text",
"text": "宜蘭縣礁溪鄉奇立丹路3巷",
"flex": 10,
"size": "sm",
"color": "#000000"
}
]
}
]
}
]
},
"footer": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "button",
"action": {
"type": "uri",
"label": "地點",
"uri": "https://maps.app.goo.gl/gTRwaQ2GN7pmGTVo8"
},
"color": "#B06500",
"height": "sm",
"margin": "none"
}
]
}
},
{
"type": "bubble",
"hero": {
"type": "image",
"url": "https://imgur.com/9aPXAyR.png",
"aspectMode": "cover",
"aspectRatio": "20:15",

"size": "full"
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "德陽街平交道",
"weight": "bold",
"style": "normal",
"color": "#B06500",
"size": "xl"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": "📍",
"flex": 1,
"size": "sm"
},
{
"type": "text",
"text": "宜蘭縣礁溪鄉德陽街",
"color": "#000000",
"size": "sm",
"flex": 10
}
]
}
]
}
]
},
"footer": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "button",
"action": {

"type": "uri",
"label": "地點",
"uri": "https://maps.app.goo.gl/s6xmeejpzPnbabxLA"
},
"color": "#B06500",
"margin": "none",
"height": "sm"
}
]
}
},
{
"type": "bubble",
"hero": {
"type": "image",
"url": "https://imgur.com/0RgdRdZ.png",
"size": "full",
"aspectRatio": "20:15",
"aspectMode": "cover"
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "台北萬華:慶豐便利商店",
"size": "xl",
"color": "#B06500",
"weight": "bold",
"style": "normal"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": "📍",
"size": "sm",
"flex": 1
},
{
"type": "text",

"text": "台北市萬華區桂林路244巷61號",
"flex": 10,
"color": "#000000",
"size": "sm"
}
]
}
]
}
]
},
"footer": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "button",
"action": {
"type": "uri",
"label": "地點",
"uri": "https://maps.app.goo.gl/HzDBDDF8Ayhn4avf8"
},
"height": "sm",
"margin": "none",
"color": "#B06500"
}
]
}
},
{
"type": "bubble",
"hero": {
"type": "image",
"url": "https://imgur.com/zXKRE5f.png",
"aspectRatio": "20:15",
"size": "full",
"aspectMode": "cover"
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "台北萬華:華江橋下天橋",
"color": "#B06500",
"size": "xl",
"weight": "bold",

"style": "normal"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": "📍",
"flex": 1,
"size": "sm"
},
{
"type": "text",
"text": "台北市萬華區和平西路三段294號",
"flex": 10,
"size": "sm",
"color": "#000000"
}
]
}
]
}
]
},
"footer": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "button",
"action": {
"type": "uri",
"label": "地點",
"uri": "https://maps.app.goo.gl/wLemNQstUAfNQQa97"
},
"color": "#B06500",
"height": "sm",
"margin": "none"
}
]
}
},
{

"type": "bubble",
"hero": {
"type": "image",
"url": "https://imgur.com/IZxRKmO.png",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "20:15"
},
"body": {
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "台北松山:民生社區",
"color": "#B06500",
"size": "xl",
"weight": "bold",
"style": "normal"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "text",
"text": "📍",
"flex": 1,
"size": "sm"
},
{
"type": "text",
"text": "台北市松山區富錦街429巷",
"color": "#000000",
"size": "sm",
"flex": 10
}
]
}
]
}
]
},
"footer": {

"type": "box",
"layout": "vertical",
"contents": [
{
"type": "button",
"action": {
"type": "uri",
"label": "地點",
"uri": "https://maps.app.goo.gl/9JuKQz1ew3H6RKPp8"
},
"color": "#B06500",
"height": "sm",
"margin": "none"
}
]
}
}
]
}
)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        


def randomRespond(event):
    try:
        message = TextSendMessage(
            text=random.choice(jean)
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

if __name__ == '__main__':
    app.run()
