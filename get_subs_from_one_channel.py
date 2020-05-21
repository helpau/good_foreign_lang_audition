from youtube_transcript_api import YouTubeTranscriptApi
import urllib3
from collections import Counter
def get_videoids(channel_url):
    #https://stackoverflow.com/questions/15512239/python-get-all-youtube-video-urls-of-a-channel
    r=http.request("GET",channel_url)
    url_data=str(r.data.decode("utf-8")).split()
    item= 'href="/watch?'
    vids = [line.replace('href="', 'youtube.com') for line in url_data if item in line]
    vids=list(set([i[i.find("=")+1:i.find('"')] for i in vids]))
    return vids

def get_subs(video_id):
    text=""
    subs=YouTubeTranscriptApi.get_transcript(video_id)
    for i in subs:
        text+=i["text"]
    return text
user_agent={'user-agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
http=urllib3.PoolManager(num_pools=1,headers=user_agent)
channel_url=input("Введите ссылку на канал: ")
#получаем все VideoID
vids=get_videoids(channel_url)
print(vids)
print("Получили {} ссылок на видео".format(len(vids)))
text=""
for i in vids:
    text=text+get_subs(i)
text=text.encode("ascii", "ignore").decode("utf-8")
text=text.split()
with open("output.txt","w") as f:
    for i,j in Counter(text).most_common():
        print(i,j,file=f)
print("Сохранили в output.txt")