import webbrowser

link = "https://www.google.com/search?num=20&newwindow=1&site=&source=hp&q="
link2 = "http://www.bing.com/search?q="
link3 = "https://yandex.com/search/?text="
link4 = "https://search.yahoo.com/?p="
link5 = "https://duckduckgo.com/?q="
link6 = "https://en.wikipedia.org/w/index.php?search="

while True:
    new = 2

    q = input("Search: ")

    link += q
    link2 += q
    link3 += q
    link4 += q
    link5 += q
    link6 += q

    webbrowser.open(link,new=new)
    webbrowser.open(link2,new=new)
    webbrowser.open(link3,new=new)
    webbrowser.open(link4,new=new)
    webbrowser.open(link5,new=new)
    webbrowser.open(link6,new=new)

    print("The search operation was conducted. :-)")
