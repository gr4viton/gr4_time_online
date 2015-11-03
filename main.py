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
    struct_time_online = time.strptime(string_time_online, "b'%Y-%m-%d %H:%M:%S '")
    if _win_set_time(struct_time_online) == 0:
        print('Succesfully updated system time from the internet page [', url, ']')
        system_datetime = _datetime_from_tuple_time(win32api.GetSystemTime())
        print('Current system time is [', system_datetime, ']')

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
    return 0


def _datetime_from_tuple_time(tuple_time_system):
    tuple_time_system = tuple(chain(*(tuple_time_system[0:2], tuple_time_system[3:])))
    # print('tuple_time_system [', tuple_time_system, ']')
    return datetime.datetime(*tuple_time_system)

def beep_on_difference(struct_time_online, beep_seconds = 5):
    """
    Beep pc speaker if the time is off more than [beep_seconds] seconds
    """
    struct_datetime_system = _datetime_from_tuple_time(win32api.GetSystemTime())
    struct_time_system = struct_datetime_system.timetuple()
    print('struct_time_system [', struct_time_system, ']')

    difference = time.mktime(struct_time_system) - time.mktime(struct_time_online)

    if(abs(difference) > beep_seconds):
        print('System to online time difference is larger than threshold [',
              int(difference), '>', beep_seconds, '] seconds')
        print('Iniciating beep.\7') # functional only when runned from command line ($ python.exe main.py)
    else:
        print('System to online difference [', int(difference), '] seconds')

if __name__ == '__main__':
    set_online_time()

