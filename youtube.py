#! /usr/bin/python

from pytube import YouTube

link = input("Inserici il link: ")
yt = YouTube(link)

print("Titolo: ", yt.title)
print("Views: ",yt.views)
print("Lunghezza del video: ",yt.length,"secondi")

ys = yt.streams.get_highest_resolution()
ys.download()
