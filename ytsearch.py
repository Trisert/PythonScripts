import dmenu
import urllib.request
import re

search_keyword = input("Inserisci cosa vuoi cercare: ")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword.replace(" ", "%"))
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

dmenu.show(video_ids, lines=10)

#video_ids_len = len(video_ids)

#for i in range(video_ids_len):
    #print("https://www.youtube.com/watch?v=" + video_ids[i])
