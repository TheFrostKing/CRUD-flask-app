# Windows Event Log Viewer

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

evt_dict={win32con.EVENTLOG_AUDIT_FAILURE:'EVENTLOG_AUDIT_FAILURE',  # storing all levels of errors and problems
            win32con.EVENTLOG_AUDIT_SUCCESS:'EVENTLOG_AUDIT_SUCCESS',
            win32con.EVENTLOG_INFORMATION_TYPE:'EVENTLOG_INFORMATION_TYPE',
            win32con.EVENTLOG_WARNING_TYPE:'EVENTLOG_WARNING_TYPE',
            win32con.EVENTLOG_ERROR_TYPE:'EVENTLOG_ERROR_TYPE'}

error_types_to_filter = [win32con.EVENTLOG_AUDIT_FAILURE, win32con.EVENTLOG_ERROR_TYPE] # filter by critical and error levels


number_of_hours_to_look_back = 24
datetime_back = datetime.datetime.now() - datetime.timedelta(hours=number_of_hours_to_look_back)


while True:
    server = 'localhost' # name of the target computer to get event logs
    log_types = ["System", "Application", "Security"]
    for log_type in log_types:
        handle = win32evtlog.OpenEventLog(server,log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total = win32evtlog.GetNumberOfEventLogRecords(handle)

        count_logs = 0
        gathered_events = []
        while True:
            events = win32evtlog.ReadEventLog(handle, flags,0)
            if events:
                for event in events:

                    if event.EventType in error_types_to_filter and event.TimeGenerated >= datetime_back:
                        count_logs += 1
                        evt_type = str(evt_dict[event.EventType])

                        gathered_events.append(event)
                    
                        
                if event.TimeGenerated < datetime_back:
                    print('log type: ' +'total: ',log_type ,count_logs)
                    break

    if log_type == log_types[len(log_types)-1]:
        break






   


    
    

    


    


    
                
