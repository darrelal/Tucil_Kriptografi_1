from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

alphabet = 'abcdefghijklmnopqrstuvwxyz'

huruf_ke_index = dict(zip(alphabet, range(len(alphabet))))
index_ke_huruf = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, key):
    encrypted = ''
    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]
    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (huruf_ke_index[letter] + huruf_ke_index[key[i]]) % len(alphabet)
            encrypted += index_ke_huruf[number]
            i += 1

    return encrypted

def decrypt(cipher, key):
    decrypted = ''
    split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]
    for each_split in split_cipher:
        i = 0
        for letter in each_split:
            number = (huruf_ke_index[letter] - huruf_ke_index[key[i]]) % len(alphabet)
            decrypted += index_ke_huruf[number]
            i += 1

    return decrypted

window = Tk()
window.title("Tugas Kriptografi")
window.geometry('350x160')
myFont = Font(family="Fixedsys", size = 9)

message_label = Label(window, text = "Message:", font=myFont)
message_label.grid(column=0, row=0)

message = Entry(window, width=30, font=myFont)
message.grid(column=1, row=0)

key_label = Label(window, text="Key:", font=myFont)
key_label.grid(column=0, row=1)

key = Entry(window, width=30, font=myFont)
key.grid(column=1, row=1)

result_label = Label(window, text="Your Result Will Appear Here", font=myFont)
result_label.grid(column=1, row=4)

def begin_encoding():
    given_message = message.get()
    given_key = key.get()

    if len(given_key) == 0:
        messagebox.showerror("Key Error", "Please Enter a Key")
        return
    
    given_message = encrypt(given_message, given_key)
    encoded_message = '"' + given_message
    encoded_message = given_message + '"'
    result_label.configure(text=encoded_message)

def begin_decoding():
    given_message = message.get()
    given_key = key.get()
    if len(given_key) == 0:
        messagebox.showerror("Key Error", "Please Enter a Key")
        return
    
    given_message = decrypt(given_message, given_key)
    decoded_message = '"' + given_message + '"'
    result_label.configure(text=decoded_message)

to_encode = Button(window,text = "Encode",command=begin_encoding,font = myFont)
to_encode.grid(column=1, row=2)

to_decode = Button(window, text="Decode", command=begin_decoding, font=myFont)
to_decode.grid(column=1, row=3)



window.mainloop()

