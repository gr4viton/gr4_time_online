# gr4_time_online
# gr4viton
# sources:
# https://code.google.com/p/just-the-time/
# http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
# http://stackoverflow.com/questions/12081310/python-module-to-change-system-date-and-time
# https://docs.python.org/2/library/time.html

import time
import urllib.request

def set_online_time():
    url = 'http://just-the-time.appspot.com/'
    print('Getting current online time from [', url, ']')
    str_tim = str( urllib.request.urlopen(url).read() )
    print('Got time [',str_tim,']')
    _win_set_time( time.strptime(str_tim, "b'%Y-%m-%d %H:%M:%S '") )

def _win_set_time(time_tuple):
    print(time_tuple)
    import pywin32
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    dayOfWeek = datetime.datetime(time_tuple).isocalendar()[2]
    pywin32.SetSystemTime( time_tuple[:2] + (dayOfWeek,) + time_tuple[2:])

if __name__ == '__main__':
    set_online_time()
