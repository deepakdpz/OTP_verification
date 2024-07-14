# importing random module for random number and smtplib module for sending mail to a valid email through internet
import random
import smtplib

# generating a random OTP number
OTP = random.randint(100000,999999)

# OTP is converted to string and stored in a message variable
message = str(OTP)


# program to send email using smtplib and for security reasons the below code only have demo email account and password
server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("xxxx@gmail.com","app password to account")

emailid = input("Enter your email:")

server.sendmail("From email",emailid,message)

otp_msg = input("Enter your otp: ")


if otp_msg==message:

    print("OTP verified successfully")

else:

    print("OTP not verified.Please check your OTP again")    
