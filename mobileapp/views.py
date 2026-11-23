from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText

def send_mail(request):
  sender_email = "nehruraja9485@gmail.com"
  sender_password = "rxcz ldvl wnmf xksm"
  receiver_email = "sce19ec057@sairamtap.edu.in"
  
  subject = "Data Engineer Role"
  body = "Apply for Data Engineer Role"
  
  # Message Format
  message = MIMEText(body)
  message["Subject"] = subject
  message["Sender"] = sender_email
  message["To"] = receiver_email
  
  try:
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,sender_password)
    server.send_message(message)
    return HttpResponse("Message sent.....")
  except Exception as e:
    return HttpResponse(e)
  