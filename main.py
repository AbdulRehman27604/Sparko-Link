import Send_email
import Speech_Input
import Email_ai

if __name__ == "__main__":
    receiver_email = input("Please enter the email to send to: ")
    sender_email = input("Please enter your email address: ")
    password = input("Please enter your password: ")
    subject = input("Please enter the subject of the email: ")

    print("Tell the AI the topic of the email: ")
    email_topic = Speech_Input.speech_detection()

    print("Generating email content using AI...")
    email_body = Email_ai.generate_email_content(email_topic)

    Send_email.send_email(receiver_email, sender_email, subject, email_body, password)

