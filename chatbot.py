import tkinter as tk
from tkinter import scrolledtext

def response(user_input):
    user_input=user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return 'Hi! How can I help you'
    elif 'your name' in user_input:
        return "I'm Chatbot"
    elif 'help' in user_input:
        return "You can ask me Question like What's your name ? , How are you ? or Bye"
    elif 'how are you' in user_input:
        return "I'm fine"
    elif 'bye' in user_input:
        return 'Bye'
    else:
        return "Sorry, I didn't understand. Please ask me something"

def send_message():
    user_message=entry.get()
    chat.insert(tk.END,"You: "+user_message+"\n")
    bot=response(user_message)
    chat.insert(tk.END,"Bot: "+bot+"\n")

root=tk.Tk()
root.title("Simple chatbot")
chat=scrolledtext.ScrolledText(root, width=50,height=15)
chat.pack(padx=10,pady=10)

entry=tk.Entry(root, width=40)
entry.pack(padx=10,pady=5)

send_btn=tk.Button(root,text="Send", command=send_message)
send_btn.pack(pady=5)
