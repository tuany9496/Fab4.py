import win32com.client
def sendMeeting():
    oOutlook = win32com.client.Dispatch("Outlook.Application")
    appt = outlook.CreateItem(1) # AppointmentItem
    appt.Start = "2018-10-28 10:10" # yyyy-MM-dd hh:mm
    appt.Subject = "Subject of the meeting"
    appt.Duration = 60 # In minutes (60 Minutes)
    appt.Location = "Location Name"
    appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added

    appt.Recipients.Add("test@test.com") # Don't end ; as delimiter

    appt.Save()
    appt.Send()
