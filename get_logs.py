# Windows Event Log Viewer
# FB - 201012116
import time 
import datetime
import win32evtlog # requires pywin32 pre-installed
import win32con

def print_event_data(events):
    for event in events:
        evt_type = str(evt_dict[event.EventType])

        print ('Source Name:', event.SourceName)
        print ('Time Generated:', event.TimeGenerated)
        print ('Event Category:', event.EventCategory)
        print ('Event Type:', evt_type)
        print('reserverd flags', event.ReservedFlags)
        print('event id', event.EventID)
        
        print("end \n")
    print('total: ', len(events))


def date2sec(evt_date):
    '''
    This function converts dates with format
    'Thu Jul 13 08:22:34 2017' to seconds since 1970.
    '''
    dt = datetime.datetime.strptime(evt_date, "%a %b %d %H:%M:%S %Y")
    return dt.timestamp()

# while True:

number_of_hours_to_look_back = 24
datetime_back = datetime.datetime.now() - datetime.timedelta(hours=number_of_hours_to_look_back)
event_types_to_filter_on = [win32con.EVENTLOG_WARNING_TYPE, win32con.EVENTLOG_ERROR_TYPE]

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

count_logs = 0


# my_time_var = begin_sec - how_many_seconds_back_to_search
all_events = win32evtlog.ReadEventLog(hand, flags,0)
print(len(all_events), "< -- all events")
time_filtered_events = [event for event in all_events if event.TimeGenerated > datetime_back]
type_filtered_events = [event for event in time_filtered_events if event.EventType in event_types_to_filter_on]


print_event_data(type_filtered_events)


# time.sleep(5)


                
