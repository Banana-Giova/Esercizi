import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

def send_email(real_email, fake_sender_email, header, receiver_email, receiver_name, subject, body, password):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email
    """
    msg = MIMEMultipart('alternative')
    msg['From'] = formataddr((str(Header(header, 'utf-8')), fake_sender_email))
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    """
    msg = f"From: {header} <{fake_sender_email}>\nTo: {receiver_name} <{receiver_email}>\nSubject: {subject}\n\n{body}>"
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(real_email, password)
        #text = msg.as_string()
        server.sendmail(real_email, receiver_email, msg.encode())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
real_email = "giovannidgad@gmail.com"
password = "gdjj ictp guxi mgpf"
fake_sender_email = "principe-nigeriano@not-a-scam.com"
receiver_name = "Giovanni"
receiver_email = "giovannidigiuseppe@protonmail.com"
header = "Nigeriani felici"
subject = "Amore Libero in Nigeria"
body = """
Imperdibile!

Risponda subito a questa mail mandando 47 BTC al seguente indirizzo BitCoin:
782D82JDQ02UDJ29KWS0
Per ricevere un principe nigeriano tutto per voi!

Scade il 13 settembre, affrettatevi!
"""

send_email(real_email, fake_sender_email, header, receiver_email, receiver_name, subject, body, password)