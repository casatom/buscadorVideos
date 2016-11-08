pip install -r requirements.txt

from pyquery import PyQuery as Pq
from urllib import urlencode


 
def search_youtube_video(title, pages):
    for page in range(pages):
        params = urlencode({'search_query':'intitle:"%s", video, long' % title, 'page':page})
        jq = Pq(url="http://www.youtube.com/results?%s" % params,
                headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20140129 Firefox/24.0"})
        jq.make_links_absolute("http://www.youtube.com")
        for video in jq("ol.item-section").children().items():
            url = video.find("a.yt-uix-tile-link").attr("href")
            title = video.find("a.yt-uix-tile-link").text()
            time = video.find("span.video-time").text()   
            if time:
                tsecs = 0
                items = time.split(':')
                items.reverse()
                for i in range(len(items)):
                    tsecs += int(items[i])*(60**i)          
            description = video.find("div.yt-lockup-description").text()
            thumb = video.find("div.yt-thumb img").attr("data-thumb")
            if not thumb:
                thumb = video.find("div.yt-thumb img").attr("src")
            if thumb:
                thumb = thumb.lstrip("//")     
            published = video.find("ul.yt-lockup-meta-info li").eq(0).html()
            views = video.find("ul.yt-lockup-meta-info li").eq(1).html()
 
            print
            print "url:", url
 



