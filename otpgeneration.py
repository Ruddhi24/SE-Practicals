#Implement a program in Java/Python to generate One Time Password
# and send it to the registered email ID or mobile number.
#smptlib = Simple Mail Transfer Protocol client
import random
#to gernerate random otp using random module.
import smtplib
#to send otp to users by their respective email address

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sender_emailid','password')
otp = ''.join([str(random.randint(0,9)) for i in range(4)])
msg="HELLO, YOUR GENERATED OTP IS "+str(otp)
server.sendmail('sender_emailid','reciever_emailid',msg)
server.quit()

