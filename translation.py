import urllib.request
print(urllib.request.urlopen("https://translation.googleapis.com/language/translate/v2?key=AIzaSyDRDkVOoM0lwfFB9Za_Q64RquAbqBrPEiI&q=hello&target=es&source=en").read())
