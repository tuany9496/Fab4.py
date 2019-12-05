import win32com.client as win32
from datetime import datetime
import pytz
tz = pytz.timezone("US/Pacific")

start_time = tz.localize(datetime(2019, 12, 27, 00))
subject = 'Scheduled Travel'
duration = 720
location = 'Vacation'

recipient = 'charles.baker@cgu.edu; ali.bazarah@cgu.edu; yian.tuan@cgu.edu'
sender = 'cjbaker@jpl.nasa.gov'

outlook = win32.Dispatch('outlook.application')
# CreateItem: 1 -- Outlook Appointment Item
appt = outlook.CreateItem(1) 

# set the parameters of the meeting
appt.Start = start_time
appt.Duration = duration
appt.Location = location
appt.Subject = subject

appt.MeetingStatus = 1 # this enables adding of recipients
appt.Recipients.Add(recipient)
appt.Organizer = sender
appt.ReminderMinutesBeforeStart = 15
appt.ResponseRequested = True
appt.Save()
#appt.Send()
