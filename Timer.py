"""
  ____________________________________ 
/ This file has been downloaded from  \
\ https://t.me/HydraLearn ,Join US (: /
 ------------------------------------ 
        \   ^__^
         \  (oo)\_______
           (__)\       )\/\
                ||----w |
                ||     ||
 """

""" Before starting work, read the READ.ME file at the bottom of this project in GitHub. """

import time
def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:20d}:{:02d}'.format(mins, secs)
        print(timer,end='\r')
        time.sleep(1)
        t -= 1
    print('Done')
t = input("Enter the time in seconds :")
countdown(int(t))