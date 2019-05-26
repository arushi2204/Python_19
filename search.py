import sys,time
import webbrowser


data=sys.argv[1:]


for i in data:
    print(i)
    time.sleep(2)
    webbrowser.open_new_tab("https://www.google.com/search?q="+i)

time.sleep(10)
