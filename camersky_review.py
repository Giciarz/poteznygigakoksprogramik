import os

from time import sleep
import tkinter as tk
from pathlib import Path
#from PIL import Image


#from picamera import PiCamera

DIR_PATH = "Fotki"

def count_images():
    global count #never use global variable - maybe if you have really, but really need
    count = 0
    for path in Path(DIR_PATH).iterdir(): #use pathlib, not os.path
        if Path.isfile(os.path.join(DIR_PATH, path)):
            count += 1
# Starting fuction

def jd():

    # Make catalog
    if not os.path.exists(DIR_PATH):
        try:
            os.makedirs("Fotki") #os.makedirs(DIR_PATH)
        except FileExistsError: #except FileExistsError as error
            pass #print(error) - something like this: try: except: pass is very unaceptable situation for evry programmer
                # you can not create directory but you don't know that so you thing the directory exist.
                # please print error

    # Make a Photo

    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.contrast = 10
    time.sleep(2) #from time import sleep


    camera.capture(f"./Fotki/Twoje_Foto{count + 1}.jpg") #it will be working on windows/linux? Nope! Because you using
    # wrong path structure. Correct way is: pathlib.Path().curdir.joinpath(DIR_PATH).joinpath(Twoje_Foto{count+1}.jpg)
    # To be honest - you don't need count of files in directory - don't use the count variable, instead of this use
    # current datetime - from datetime import datetime
    # Twoje_Foto{datetime.datetime.now()}.jpg
    # OR
    # Just get the newest picture and get the last number -
    # a =  method_to_get_latest_picture()
    # count = a.split("Twoje_Foto")[1]
    print("Done.") #Done what?
    camera.stop_preview()
    camera.close()

# Show photo function
def Show_photo(): #don't start name of function with up letter - only small

    img = Image.open(f"./Fotki/Twoje_Foto{count + 1}.jpg") #So...I can show only one picture? The last? Why not all?
    img.show()

# Del function

def DEL(): #This function is stupid - I made 100 pictures and I want keep all except one but I lost all pictures. Why?
    for f in os.listdir(DIR_PATH): #os.pathlib
        os.remove(os.path.join(DIR_PATH, f)) #os.pathlib. What happen if user can not remove picture?

# photo label

root = tk.Tk()

window_width = 600
window_height = 300

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') #ugh, why? Use winfo_screenwidth and winfo_screenheight instead using hardcoded value. Or is any reason for this?
root.resizable(True, True)
root.title('Do a photo')
root.configure(bg="blue")
# root.attributes('-alpha',1)

# photo button
img_button = tk.Button(
    root,
    text='Do a photo',
    bg='green',
    activebackground='light green',
    borderwidth='12',
    relief='ridge',
    command=jd
)
img_button.pack(
    ipadx=screen_width/10,
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
    ipady=5,
    expand=True
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

if __name__ == "__main__":
    root.mainloop()


# this is very simple script - please move all of this to class object - it will be more friendly :)
# please migrate ALL print to toast
