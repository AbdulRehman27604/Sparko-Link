import smtplib

def send_email(receiver_email, sender_email, subject, body, password):
    text = f"Subject: {subject}\n\n{body}"
    try:
        # Create the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade to a secure connection
        server.login(sender_email, password)  # Login to your email account
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
