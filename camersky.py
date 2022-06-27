import tkinter as tk
from tkinter import *
from picamera import PiCamera
import time
from PIL import Image
# Do photo function
def JD():
    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.contrast = 10
    time.sleep(2)
    camera.capture("/home/adam/Desktop/Twoje_Foto.jpg")
    print("Done.")

# Show photo function
def Show_photo():

    img = Image.open("/home/adam/Desktop/Twoje_Foto.jpg")
    img.show()


# photo label

root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Do a photo')
root.configure(bg="blue")

# photo button
img_button = tk.Button(
    root,
    text='Do a photo',
    bg='green',
    activebackground='light green',
    borderwidth='12',
    relief='ridge',
    command=JD
)
img_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# Show me photo

show_button = tk.Button(
    root,
    text='Show me a photo',
    borderwidth='11',
    relief='ridge',
    bg='dark orange',
    activebackground='orange',
    command=Show_photo

)
show_button.pack(
    ipadx=5,
    ipady=5
)

# quit button
exit_button = tk.Button(
    root,
    text='Exit',
    borderwidth='10',
    relief='ridge',
    bg='red3',
    activebackground='red2',
    command=root.destroy
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()