#Welcome to E-mail Bot
#This program takes the subject, receiver, and body of an email.
#Multiple attachment options including image and pdf attachments are also available.
#The sender's email address is "anshsaraiya10@gmail.com"


#Importing the necessary libraries
import os
import smtplib
import imghdr
from email.message import EmailMessage


#Getting sender login details from environment variables
email_address = os.environ.get('DB_USER')
email_password = os.environ.get('DB_PASS')


#Taking email details from user
sub = input("Enter E-mail Subject here \n")
body = input("Enter e-mail content here \n")
print("To how many receivers do you want to send this email? Please enter a number")
contact_no = int(input())
contacts = []
for i in range (contact_no):                             #Getting receivers' email addresses
    x = input("Enter receiver's E-mail address here \n")
    contacts.append(x)


#Creating email
msg = EmailMessage()     
msg['Subject'] = sub
msg['From'] = email_address
msg['To'] = contacts
msg.set_content(body)


#Adding image attachments to email
print("Do you want to add image attachments? Enter Y for yes, N for no")
yes_no = input()

if yes_no == 'Y' or yes_no == 'y':
    print("How many images do you want to attach to your email? Please enter a number")
    img_no = int(input())

    for i in range (img_no):
        file = input('Paste image location here \n')                                               #Takes file location
        with open(file, 'rb') as f:
            file_data = f.read()                                                                   #Reads file location
            file_type = imghdr.what(f.name)                                                        #Finds image type
            file_name = f.name                                                                     #Gives name to image
            
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name) #Attaches image to email


#Adding PDF attachments to email
print("Do you want to add PDF attachments? Enter Y for yes, N for no")
yes_no = input()

if yes_no == 'Y' or yes_no == 'y':
    print("How many attachments do you want to add to your email? Please enter a number")
    pdf_no = int(input())

    for i in range (pdf_no):
        file = input('Paste pdf location here \n')                                                            
        with open(file, 'rb') as f:
            file_data = f.read()                                                                              
            file_name = f.name
            
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


#Sends email here
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)          #Logging in to the server

    smtp.send_message(msg)                             #Sending message
    print("Your email has been sent!")