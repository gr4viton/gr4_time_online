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

def set_online_time():
    url = 'http://just-the-time.appspot.com/'
    print('Getting current online time from [', url, ']')
    str_tim = str( urllib.request.urlopen(url).read() )
    print('Got time [',str_tim,']')
    _win_set_time( time.strptime(str_tim, "b'%Y-%m-%d %H:%M:%S '") )

def _win_set_time(struct_time):
    print('struct_time = "',struct_time,'"')
    import win32api
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # win32api.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    win32api.SetSystemTime(struct_time.tm_year,
                          struct_time.tm_mon,
                          struct_time.tm_wday,
                          struct_time.tm_mday,
                          struct_time.tm_hour,
                          struct_time.tm_min,
                          struct_time.tm_sec,
                          0
                          )

if __name__ == '__main__':
    set_online_time()
