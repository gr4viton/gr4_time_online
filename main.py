# gr4_time_online
# gr4viton
# sources:
# https://code.google.com/p/just-the-time/
# http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
# http://stackoverflow.com/questions/12081310/python-module-to-change-system-date-and-time
# https://docs.python.org/2/library/time.html

import time
import datetime
import urllib.request
import win32api
from itertools import chain

def set_online_time():
    url = 'http://just-the-time.appspot.com/'
    print('Getting current online time from [', url, ']')
    string_time_online = str( urllib.request.urlopen(url).read() )
    print('Got time [', string_time_online, ']')
    _win_set_time( time.strptime(string_time_online, "b'%Y-%m-%d %H:%M:%S '") )

def _win_set_time(struct_time_online):
    print('struct_time_online [', struct_time_online, ']')
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # win32api.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    beep_on_difference(struct_time_online)
    win32api.SetSystemTime(struct_time_online.tm_year,
                          struct_time_online.tm_mon,
                          struct_time_online.tm_wday,
                          struct_time_online.tm_mday,
                          struct_time_online.tm_hour,
                          struct_time_online.tm_min,
                          struct_time_online.tm_sec,
                          0
                          )
    
def beep_on_difference(struct_time_online, beep_seconds = 5.0):


    # beep pc speaker if the time is off more than X seconds
    tuple_time_system = win32api.GetSystemTime()
    tuple_time_system = tuple(chain(*(tuple_time_system[0:2], tuple_time_system[3:])))
    print('tuple_time_system [', tuple_time_system, ']')
    # print(sum(tuple_time_system))
    struct_time_system = datetime.datetime(*tuple_time_system)
    # struct_time_system = time.mktime(tuple_time_system)
    # struct_time_system = time.mktime(
    print('struct_time_system [', struct_time_system, ']')

    print(type(struct_time_system), type(struct_time_online))
    difference = datetime.timedelta(struct_time_online, struct_time_system)
    print('system to online difference [', difference, ']')
    if(difference > time.second(beep_seconds)):
        print
        print('\7') # functional only when runned through command line ($ python.exe main.py)
if __name__ == '__main__':
    set_online_time()
