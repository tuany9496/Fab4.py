from requests import *
import pdfkit

url = 'http://127.0.0.1:8000/searched'
#url = input("Please enter the url of the file you want to download:")
path = input("Please enter the file path ex. C:\Jim\Desktop: ")
file_name = input("Please enter file name: ")
if pdfkit.from_url(str(url), str(path + file_name)): # Check if method from_url returned True
    print("Sucessfully created pdf from url")
else:
    print("Something went wrong")
    print("Download starting.")
#r = requests.get(pdf)

#with open(path, 'wb') as f:
 #   f.write(r.content)
