import urllib.request
import urllib.parse
import re

def searchOnYoutube(query):
    query_string = urllib.parse.urlencode({"search_query" : query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return "https://www.youtube.com/watch?v=" + search_results[0]