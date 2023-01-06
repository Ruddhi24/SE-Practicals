#IMPLEMENTATION OF OTP GENERATION CODE AFTER CODE REVIEW:
import random
import senders_data
import smtplib
n=(int(input("Enter your range of otp: ")))
def generate_otp(n):
    OTP=""
    for i in range(n):
        OTP+=str(random.randint(0,9))
    return (OTP)
server =smtplib.SMTP('smtp.gmail.com',587)

Senders_email = senders_data.email
Senders_password= senders_data.password

def sendersemail():
    server.starttls()
    server.login("sender_emaiid",password="")
receivers_name=input("Please enter receiver's name: ")
receivers_email=input("Please enter receiver's email: ")
def recievers_email():
    sendersemail()
    otp_var=generate_otp(n)
    msg=("Hello, "+ receivers_name +"\n"+"Your OTP has been successfully sent, please check it..."+ str(otp_var)+" is your OTP ")
    print(msg)
    server.sendmail(Senders_email,receivers_email,msg)
    server.quit()
    print("email has been sent!")
recievers_email()
