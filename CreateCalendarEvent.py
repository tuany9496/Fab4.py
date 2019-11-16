 def addevent(start, subject):
    import win32com.client
    oOutlook = win32com.client.Dispatch("Outlook.Application")
    appointment = oOutlook.CreateItem(1) # 1=outlook appointment item
    appointment.Start = start
    appointment.Subject = subject
    appointment.Duration = 20
    appointment.Location = 'Sprortground'
    appointment.ReminderSet = True
    appointment.ReminderMinutesBeforeStart = 1
    appointment.Save()
    return

table = {"11-16":20, "12-1":30, "12-16":40, "12-31":50}

for item in table.keys():
    start = '2012-' + item + ' 18:35'
    subject = 'P-bars. To do:' + str(table[item])
    addevent(start, subject)