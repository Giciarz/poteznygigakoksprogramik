import tkinter as tk
from tkinter import *
from picamera import PiCamera
import os, os.path
import time
from PIL import Image

dir_path = "Fotki"

# Starting fuction

def JD():
    
    # Cout files
    
    global count
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print(count)
    
    # Make catalog
    if not os.path.exists(dir_path):
        try: 
            os.makedirs("Fotki")
        except FileExistsError:
            pass
    
    # Make a Photo
    
    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.contrast = 10
    time.sleep(2)
    
        
    camera.capture(f"./Fotki/Twoje_Foto{count + 1}.jpg")
    print("Done.")
    camera.stop_preview()
    camera.close()

# Show photo function
def Show_photo():

    img = Image.open(f"./Fotki/Twoje_Foto{count + 1}.jpg")
    img.show()

# Del function

def DEL():
    for f in os.listdir(dir_path):
        os.remove(os.path.join(dir_path,f))

# photo label

root = tk.Tk()
root.geometry('600x400')
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
# Delete button
del_button = tk.Button(
    root,
    text='Delete all photos',
    bg='purple3',
    activebackground='purple1',
    borderwidth='12',
    relief='ridge',
    command=DEL
)
del_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
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
