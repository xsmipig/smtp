import smtplib
import argparse
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def prompt(prompt):
    return raw_input(prompt).strip()

def connect_server(server_ip):

    return smtplib.SMTP(server_ip)

def do_authentication(server):

    print "Authenticate to gmail"
    user_name = prompt("User Name: ")
    password = prompt("Password: ")
    #user_name = "panwipstest@gmail.com"
    #password = "panwipssxu1"
    server.set_debuglevel(1)
    server.starttls()
    server.login(user_name,password)
    return user_name

def construct_message(fromaddr, toaddrs, subject):
    
    print "Enter message, end with ^D (Unix) or ^Z (Windows):"
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
            % (fromaddr, ", ".join(toaddrs), subject))

    while 1:
        try:
	    line = raw_input()
	except EOFError:
	    break;
        if not line:
	    break;    
        msg = msg + line

    print "Message length is " + repr(len(msg))
    return msg

def construct_mime_message(fromaddr, toaddrs, subject, files):

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = COMMASPACE.join(toaddrs)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    email_body = ""
    print "Enter message, end with ^D (Unix) or ^Z (Windows):"
     
    while 1:
        try:
	    line = raw_input()
	except EOFError:
	    break;
        if not line:
	    break;    
        email_body = email_body + line

    msg.attach(MIMEText(email_body))
    
    for f in files or []:
        with open(f, "rb") as n_file:
            part = MIMEApplication(
		    n_file.read(),
		    Name = os.path.basename(f)
	    )

            part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(f)
            msg.attach(part)

    return msg.as_string()

def send_to_local_server():
    server = smtplib.SMTP("localhost")
    send_from = prompt("From: ")
    send_to_s = prompt("To: ").split()
    subject = prompt("Subject: ")

    msg = construct_message(send_from, send_to_s, subject)
    
    server.sendmail(send_from, send_to_s, msg)
    server.quit()


def send_email(server_ip, attachments=None):
 
    server = connect_server(server_ip)

    if server_ip == "localhost":
        send_from = prompt("From: ")
    else:
        send_from = do_authentication(server)

    send_to_s = prompt("To: ").split()
    subject = prompt("Subject: ")
    
    if attachments is None:

        msg = construct_message(send_from, send_to_s, subject)
        
    else:

	    msg = construct_mime_message(send_from, send_to_s, subject, attachments)

    server.sendmail(send_from, send_to_s, msg)
    server.close()

def main():
    argparser = argparse.ArgumentParser (
        prog = "smtp_client.py",
	description = "simple smtp client")

    argparser.add_argument (
        "-o", "--option",
	dest = "option",
	type = int,
	default = 1,
	help = "option, 1: do not need authentication 2: need authentication")

    argparser.add_argument (
        "-s", "--server_ip",
	dest = "server_ip",
	default = "localhost",
	help = "server ip, default is local host")

    argparser.add_argument (
        "-a", "--attachments",
	dest = "attachments",
	nargs = "+",
	help = "attachments you want to send")

    args = argparser.parse_args()
 

    if args.option == 1:
        send_email(args.server_ip,args.attachments)
    elif args.option == 2:
        send_email("smtp.gmail.com",args.attachments)

if __name__ == "__main__":
    main()
