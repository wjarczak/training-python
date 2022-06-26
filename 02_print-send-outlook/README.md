# Print & Send

Print & Send is simple script to print .pdf using batch script and after that send it via Outlook client using python script

## Installation
Intall wkhtmltopdf by downloading it [from website](https://wkhtmltopdf.org/)


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install pywin32
```
## Configuration
In [sendmail.py](sendmail.py) edit few lines of code
```python
import subprocess
import time
import win32com.client
subprocess.call([r'C:\pathtogeneratepdf.bat\generatepdf.bat']) #provide path to generatepdf.bat
time.sleep (5)
outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'email@yourdomain.com' #enter the recipient of the message
mail.Subject = 'Email subject' #enter subject of the message
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = "Email body" #enter body of the message
#if you want to add attachments uncomment that and provide path to file
#mail.Attachments.Add('C:\\Program Files\\wkhtmltopdf\\bin\\xxx.pdf')
#mail.CC = ''
mail.Send()
```
In [generatepdf.bat](generatepdf.bat) edit paths to use program
```bash
cd C:\Program Files\wkhtmltopdf\bin #location of wkhtmltopdf.exe
wkhtmltopdf "website link" G:\path\pdfname.pdf #what website will be printed to pdf and path to save file.
```

## Usage

Just run [sendmail.py](sendmail.py) and you are good to go.
