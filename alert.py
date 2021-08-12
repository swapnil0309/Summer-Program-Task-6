def mail():
#To set up a Gmail address for testing your code, do the following:
#  Create a new Google account.
#  Turn Allow less secure apps to ON. Be aware that this makes it easier for others to gain access to your account.
    
    import smtplib
    sender_email = "Enter senders Email "
    receiver_email = "Enter receivers email"
    password = "Enter password for senders email"
    message = "Hello this was sent by using Python"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,password)
    print("Login Success")
    server.sendmail(sender_email,receiver_email,message)
    print("Email has been seen to ", receiver_email)

def whatsapp():
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly("WhatsApp No" , 'One face has been recognised')
    print("Whatsapp message has been sent")

def launch_ec2():
    import os
    os.system("aws ec2 run-instances  --image-id  ami-0ad704c126371a549 --instance-type t2.micro --key-name awsdef --count 1 ")

def creating_EBS_volume():
    import os
    os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 5 --volume-type gp2")
