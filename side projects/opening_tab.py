import sched
import time
import webbrowser

url_lst = ['https://www.youtube.com/watch?v=d9zSKHrE7aQ&ab_channel=asmrzeitgeist', 'https://moodle.dawsoncollege.qc.ca/my/', 'https://dawsoncollege.omnivox.ca/Login/Account/Login?ReturnUrl=%2fintr%2f', 'https://www.youtube.com/']


for website in url_lst:
    webbrowser.open_new_tab(website)

    time.sleep(0.5)

