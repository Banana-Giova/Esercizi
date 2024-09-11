import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(real_email, sender_email, receiver_email, subject, body, password):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(real_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
real_email = "private@mail.com"
password = "password"
sender_email = "principe-nigeriano@not-a-scam.com"
receiver_email = "private@mail.com"
subject = "Amore Libero in Nigeria"
body = """
Imperdibile!

Risponda subito a questa mail mandando 47 BTC al seguente indirizzo BitCoin:
782D82JDQ02UDJ29KWS0
Per ricevere un principe nigeriano tutto per voi!

Scade il 13 settembre, affrettatevi!
"""

send_email(real_email, sender_email, receiver_email, subject, body, password)