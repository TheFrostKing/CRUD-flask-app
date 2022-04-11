# Windows Event Log Viewer

import time 
import datetime
import win32evtlog # requires pywin32 pre-installed
import win32con


def print_events(event):
    print ('Source Name:', event.SourceName)
    print ('Time Generated:', event.TimeGenerated)
    print ('Event Category:', event.EventCategory)
    print ('Event Type:', evt_type)
    print('reserverd flags', event.ReservedFlags)
    print('event id', event.EventID)
    
    print("end \n")
    

def date2sec(evt_date):
    '''
    This function converts dates with format
    'Thu Jul 13 08:22:34 2017' to seconds since 1970.
    '''
    dt = datetime.datetime.strptime(evt_date, "%a %b %d %H:%M:%S %Y")
    return dt.timestamp()

while True:

    number_of_hours_to_look_back = 24

    begin_sec = time.time()
    begin_time = time.strftime('%H:%M:%S  ', time.localtime(begin_sec))
    seconds_per_hour = 60 * 60
    how_many_seconds_back_to_search = seconds_per_hour * number_of_hours_to_look_back

    server = 'localhost' # name of the target computer to get event logs
    logtype = 'Application' # 'Application' # 'Security'
    #open event log 
    hand = win32evtlog.OpenEventLog(server,logtype)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)


    evt_dict={win32con.EVENTLOG_AUDIT_FAILURE:'EVENTLOG_AUDIT_FAILURE',  # storing all levels of errors and problems
                win32con.EVENTLOG_AUDIT_SUCCESS:'EVENTLOG_AUDIT_SUCCESS',
                win32con.EVENTLOG_INFORMATION_TYPE:'EVENTLOG_INFORMATION_TYPE',
                win32con.EVENTLOG_WARNING_TYPE:'EVENTLOG_WARNING_TYPE',
                win32con.EVENTLOG_ERROR_TYPE:'EVENTLOG_ERROR_TYPE'}


    error_types_to_filter = [win32con.EVENTLOG_WARNING_TYPE, win32con.EVENTLOG_ERROR_TYPE]

    count_logs = 0


    while True:
        events = win32evtlog.ReadEventLog(hand, flags,0)
        if events:
            for event in events:
                the_time = event.TimeGenerated.Format()
                seconds = date2sec(the_time)
                if seconds < begin_sec - how_many_seconds_back_to_search: break


                if event.EventType in error_types_to_filter:
                    count_logs += 1
                    evt_type = str(evt_dict[event.EventType])

                    print_events(event)
                    
            if seconds < begin_sec - how_many_seconds_back_to_search: break  # get out of while loop as well
        
    print('total: ', count_logs)

    break
    
                
