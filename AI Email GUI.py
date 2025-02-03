from tkinter import *
from tkinter import messagebox
from Speech_Input import speech_detection
from Email_ai import generate_email_content
from Send_email import send_email
user_response = "Write email but Don't include a subject about"
receiver_email = ""
subject = ""
email_body = ""
sender_email = ""
password_key = ""
u_name = ""

EM = Tk()


def second_window():
    SK = Toplevel(EM)
    layout(SK,"#080117")
    email_details(SK)

def thirdwindow():
    SK_2 = Toplevel()
    n = Frame(SK_2, height=145,bg="black")
    n.pack(fill="x", side="top")
    layout(SK_2, "#696969")
    record_display(SK_2)

def layout(SK,bg_color):
    SK.title("Sparko Link")
    SK.geometry("538x1048")
    SK.configure(bg=bg_color)
    bg = PhotoImage(file="Smail2.png")
    label1 = Label(SK, image=bg)
    label1.place(x=220, y=20)
    label1.image = bg


def email_details(SK):
    global receiver_email
    global subject
    frame = Frame(SK,width="435", height="500", bg="#080117")
    frame.place(x=50, y=160)
    h1 = Label(frame,text="SEND EMAILS",width="15",height="2",bg="black", font=("Helvetica",23,"bold"))
    h1.place(x=120,y=20)

    from1 = Entry(frame, width=28, borderwidth=0, highlightthickness=0, fg="white", bg="grey",font=("Microsoft YaHei UI Light", 14))
    from1.place(x=148, y=160)
    Frame(frame, width=400, height=2, bg="white").place(x=2, y=180)
    Label(frame, text="RECIPIENT:", border=0, width="8", height="0", fg="white", bg="#080117").place(x=63, y=159)
    #receiver_email = from1

    sub = Entry(frame, width=28, borderwidth=0, highlightthickness=0, fg="white", bg="grey",font=("Microsoft YaHei UI Light", 14))
    sub.place(x=148, y=190)
    Frame(frame, width=400, height=2, bg="white").place(x=2, y=210)
    Label(frame, text="SUBJECT:", border=0, width="8", height="0", fg="white", bg="#080117").place(x=66, y=189)
    #subject = sub

    Button(frame,width=20,pady=7,text="NEXT",bg="black",fg="black",border=0,command=lambda: is_login_ok(from1.get(),sub.get(),SK)).place(x=120,y=400)


def is_login_ok(From, sub,SK):
    global receiver_email
    global subject

    receiver_email = From
    subject = sub

    if From == "" or sub == "":
        messagebox.showerror("Invaild","one of the required fields are empty")
    else:
        SK.withdraw()
        thirdwindow()

def record_display(SK_2):
    Label(SK_2,text="Please press the button to record audio", width="40", height="2",fg="white",bg="black").place(x=100, y=200)
    textbox = Text(SK_2, height=13, width=73, font=("Arial", 12), wrap="word")
    textbox.place(x=10, y=300)
    Button(SK_2, text="RECORD", width='5', height='2', bg='white', command=lambda: display_text(textbox)).place(x=230, y=150)
    Button(SK_2, text="Regenerate Response",width='15',height='2',bg='white',command=lambda: chat_reply(textbox)).place(x=360,y=500)
    Button(SK_2, text="Send Email", width='15', height='2', bg='white',command=send_mail).place(x=360, y=600)
    Button(SK_2, text="Send Email", width='15', height='2', bg='white', command=send_mail).place(x=360, y=600)

def display_text(textbox):
    global user_response
    global email_body
    result = "You: "
    user_response = speech_detection()
    result += user_response
    user_response += "from"
    user_response += u_name
    textbox.insert(END, result + '\n')
    textbox.insert(END, " ")

    text_body = generate_email_content(user_response)
    Ai_reply = "AI: "
    Ai_reply += text_body
    email_body = text_body
    textbox.insert(END, Ai_reply + '\n')

    textbox.yview(END)

def chat_reply(textbox):
    global email_body
    regenerate_response = user_response
    print(regenerate_response)
    text_body = generate_email_content(regenerate_response)
    re_Ai_reply = "AI: "
    re_Ai_reply += text_body
    email_body = text_body
    textbox.insert(END, re_Ai_reply + '\n')

    textbox.yview(END)

def send_mail():
        send_email(str(receiver_email), str(sender_email), subject, email_body, str(password_key))

def password_main_layout():
    EM.title("Sparko Link")
    EM.geometry("538x1048")
    bg = PhotoImage(file="splink2.png")
    label1 = Label(EM, image=bg)
    label1.place(x=0, y=0)
    label1.image = bg

    Label(EM, text="Username: ", font=("Arial", 18), fg="white", bg="#0A0A18").place(x=130, y=500)
    username_entry = Entry(EM, font=("Arial", 18))
    username_entry.place(x=240, y=500, height=30, width=180)

    Label(EM, text="Password: ", font=("Arial", 18), fg="white", bg="#0A0A18").place(x=130, y=540)
    password_entry = Entry(EM, font=("Arial", 18), show="*")
    password_entry.place(x=240, y=540, height=30, width=180)

    btn_login = Button(EM, text="Login", font=("Arial", 18), command=lambda: is_password_ok(username_entry.get(), password_entry.get()))
    btn_login.place(x=240, y=600)

    EM.mainloop()

def is_password_ok(username, password):
    global sender_email
    global password_key

    file = open("sparko.txt", "r")

    for line in file:
        line = line.strip()
        array = line.split(',')
        print(array)
        if (array[0] == username and array[1] == password):
            u_name = array[4]
            sender_email = array[3]
            password_key = array[2]
            EM.withdraw()
            second_window()
            file.close()
    messagebox.showerror("Invalid", "Username or password is invalid, PLease try again")


password_main_layout()
thirdwindow()
EM.mainloop()





