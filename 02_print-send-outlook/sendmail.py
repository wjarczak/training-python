import subprocess
import time
import win32com.client
subprocess.call([r'C:\pathtogeneratepdf.bat\generatepdf.bat'])
time.sleep (5)
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'email@yourdomain.com'
mail.Subject = 'Email subject'
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = "Email body"
#If you want to add attachments uncomment that and provide path to file
#mail.Attachments.Add('C:\\Program Files\\wkhtmltopdf\\bin\\xxx.pdf')
#mail.CC = ''
mail.Send()
