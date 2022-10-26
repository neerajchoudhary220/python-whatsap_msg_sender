from tkinter import *
from numpy import number
import time
import os
import pyautogui
from Class import savemsg
from Class import property
from Class import updatejson
from sender import whatsapp
from web import chrome
msg_file = savemsg.message.readfile()  # get msg file with read mode
window = Tk()
window.geometry("1200x500")  # size of window
window.resizable(False, False)
window.iconbitmap(r"image/logo/icon.ico")  # icon of window
window.title("Whatsapp Automation")
# window['bg'] = "aqua"
v = Scrollbar(window, orient='vertical')


def msgsave():
    message = msg.get("1.0", "end-1c")
    if len(message) == 0:
        pyautogui.alert(text='Message box must be required !',
                    title='Message', button='OK')
    else:
        savemsg.message.save(message)
        pyautogui.alert(text='Message saved successfully !',
                        title='Save Message', button='OK')

def sendmsg():
    message = msg.get("1.0", "end-1c")
    if len(message) == 0:
            pyautogui.alert(text='Please write message first\n\r inside the mesasge box!',
                        title='Message', button='OK')
            # pyautogui.hotkey('alt', 'f4')
    else:
        savemsg.message.save(message)
        cnt = len(number_of_msg.get())
        numberOfMsg= int(number_of_msg.get())
        if cnt == 0  or numberOfMsg ==0 or numberOfMsg >100:
            pyautogui.alert(text='Number of msg must be between 1 to 100 \n Maximium limit is 100',
                            title='Message', button='OK')
        else:
        
            #update number of msg
            updatejson.update(number_of_msg.get())
            x1,y1 = pyautogui.locateCenterOnScreen(r"image/logo/chrome.png", grayscale= True, confidence=0.9)
            pyautogui.click(x1,y1)
            time.sleep(3)
            x,y = pyautogui.locateCenterOnScreen(r"image/logo/whatsapplogo.png", grayscale= True, confidence=0.9)
            pyautogui.click(x,y)
        
            path = r"image/contact/amita.png"
            whatsapp.sendmsg(number_of_msg.get(),msg.get("1.0", "end-1c"),path)
            pyautogui.alert(text='Message has been sent successfully !',
                                title='Message', button='OK')
        



# msg box label
Label(window, text="Message Box", font=(
    'Arial', 18), fg='#C0C0C0').pack(padx=10)
# msg box
msg = Text(window, width=65, height=5, yscrollcommand=v.set, font=(
    'Arial', 16), borderwidth=1, relief="sunken", wrap=WORD)
msg.insert(END, msg_file)
v.config(command=msg.yview)
msg.pack(padx=2, pady=0)

#send button
sendbtn = Button(window,text="Send",bg=property.buttonbg(), fg=property.buttonfg(), command=sendmsg)
sendbtn.pack(side=RIGHT,padx=10)

# save msg btn
saveBtn = Button(window, text='Save Msg', command=msgsave,
                 bg=property.buttonbg(), fg=property.buttonfg())
saveBtn.pack(padx=10, side=RIGHT)

# left frame
left_frame = Frame(window)
left_frame.pack(side=LEFT)

# number of msg label
txt = StringVar()
number_of_msglabel = Label(left_frame, font=(
    'Arial', 16), text='Number of msg')
number_of_msglabel.pack(side=LEFT, padx=2, pady=4)
# number of msg input field
number_of_msg = Entry(left_frame, textvariable=StringVar,
                      font=('Arial', 16), width=5)
number_of_msg.pack(padx=10, side=LEFT)
number_of_msg.focus()
number_of_msg.insert(END, property.number_of_msg())

# send msg button
right_frame = Frame(window)
right_frame.pack(side=RIGHT)

window.mainloop()
