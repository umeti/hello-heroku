import requests
import json

def bili_video(id):
    url = "https://api.bilibili.com/x/web-interface/view?"
    t = id[:2]
    if t == "av":
        url += "aid="+id[2:]
    else:
        url += "bvid="+id

    req = requests.get(url)
    body = req.text
    print(url)

    return body

def bili_video_simple(id):
    '''
 "stat": {
      "aid": 3866176,
      "view": 1118,
      "danmaku": 28,
      "reply": 33,
      "favorite": 53,
      "coin": 72,
      "share": 11,
      "now_rank": 0,
      "his_rank": 0,
      "like": 23,
      "dislike": 0,
      "evaluation": "",
      "argue_msg": ""
    }
    '''
    data = json.loads(bili_video(id))["data"]
    s = data["stat"]
    tab = "\t"
    msg = f'''《{data['title']}》
👀 {s["view"]} {tab}💫 {s["danmaku"]}{tab}💬 {s["reply"]}
👍 {s["like"]}{tab}🌑 {s["coin"]}{tab}⭐️ {s["favorite"]}
'''

    return msg


def test():
    info = bili_video_simple("BV1gs41197o8")
    info2 = bili_video_simple("av810872")
    
    print(info)
    print(info2)


if __name__ == '__main__':
    test()
