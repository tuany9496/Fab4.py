import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")

def sendEmail():
  Msg = outlook.CreateItem(0) # Email
  Msg.To = "test@test.com" # you can add multiple emails with the ; as delimiter. E.g. test@test.com; test2@test.com;
  Msg.CC = "test@test.com"
  Msg.Subject = "Subject"
  Msg.Body = "Your text (not html)"
  Msg.Send()