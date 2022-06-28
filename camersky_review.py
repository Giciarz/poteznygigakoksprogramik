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
        if Path.isfile(Path.joinpath(DIR_PATH, path)):
            count += 1
# Starting fuction

def jd():

   # Make catalog
    if not Path.exists(DIR_PATH):
        try:
            Path.mkdir("Fotki")
        except FileExistsError:
            print(FileExistsError)

    # Make a Photo

    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.contrast = 10
    sleep(2) #from time import sleep


    camera.capture(f"./Fotki/Twoje_Foto{count + 1}.jpg") 
    print("Done.")
    camera.stop_preview()
    camera.close()

# show photo function
def show_photo(): #don't start name of function with up letter - only small

    img = Image.open(f"./Fotki/Twoje_Foto{count + 1}.jpg") #So...I can show only one picture? The last? Why not all?
    img.show()

# Del function

def delete_img():
    for f in Path.iterdir(DIR_PATH):
        Path.unlink(Path.joinpath(DIR_PATH,f))

# photo label

root = tk.Tk()

screen_width = 600
screen_height = 300

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# center_x = int(screen_width/2 - screen_width / 2)
# center_y = int(screen_height/2 - screen_height / 2)

root.geometry(f'{screen_width}x{screen_height}')
root.resizable(True, True)
root.title('Do a photo')
root.configure(bg="snow1")
# root.attributes('-alpha',1)

# photo button
img_button = tk.Button(
    root,
    text='Do a photo',
    bg='LightCyan3',
    activebackground='LightCyan2',
    borderwidth='3',
    command=jd
)
img_button.pack(
    ipadx=screen_width/35,
    ipady=screen_height / 35,
    expand=True
)

# Show me photo

show_button = tk.Button(
    root,
    text='Show me a photo',
    bg='LightCyan3',
    activebackground='LightCyan2',
    borderwidth='3',
    command=show_photo

)
show_button.pack(
    ipadx=screen_width/35,
    ipady=screen_height / 35,
    expand=True
)
# Delete button
del_button = tk.Button(
    root,
    text='Delete all photos',
    bg='LightCyan3',
    activebackground='LightCyan2',
    borderwidth='3',
    command=delete
)
del_button.pack(
    ipadx=screen_width / 35,
    ipady=screen_height / 35,
    expand=True
)

# quit button
exit_button = tk.Button(
    root,
    text='Exit',
    bg='LightCyan3',
    activebackground='LightCyan2',
    borderwidth='3',
    command=root.destroy
)

exit_button.pack(
    ipadx=screen_width / 35,
    ipady=screen_height / 35,
    expand=True
)

if __name__ == "__main__":
    root.mainloop()


# this is very simple script - please move all of this to class object - it will be more friendly :)
# please migrate ALL print to toastease migrate ALL print to toast
