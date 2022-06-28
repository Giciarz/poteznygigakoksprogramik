import os

from time import sleep
from pathlib import Path
# from PIL import Image
# from picamera import PiCamera

import tkinter as tk

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
    sleep(2)


    camera.capture(f"./Fotki/Twoje_Foto{count + 1}.jpg") #it will be working on windows/linux? Nope! Because you using
    # wrong path structure. Correct way is: pathlib.Path().curdir.joinpath(DIR_PATH).joinpath(Twoje_Foto{count+1}.jpg)
    print("Done.") #Done what?
    camera.stop_preview()
    camera.close()

# Show photo function
def show_photo(): #don't start name of function with up letter - only small

    img = Image.open(f"./Fotki/Twoje_Foto{count + 1}.jpg") #So...I can show only one picture? The last? Why not all?
    img.show()

# Del function

def delete_img(): #This function is stupid - I made 100 pictures and I want keep all except one but I lost all pictures. Why?
    for f in os.listdir(DIR_PATH): #os.pathlib
        os.remove(os.path.join(DIR_PATH,f)) #os.pathlib. What happen if user can not remove picture?

# photo label

root = tk.Tk()
root.geometry('600x400') #ugh, why? Use winfo_screenwidth and winfo_screenheight instead using hardcoded value. Or is any reason for this?
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
    command=jd
)
img_button.pack(
    ipadx=5, #ugh, why not winfo_screenwidth and divide by any value? You create very small button
    ipady=5, # the same
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
    command=show_photo

)
show_button.pack(
    ipadx=5, #the same like earlier
    ipady=5 #the same like earlier
)
# Delete button
del_button = tk.Button(
    root,
    text='Delete all photos',
    bg='purple3',
    activebackground='purple1',
    borderwidth='12',
    relief='ridge',
    command=delete_img
)
del_button.pack(
    ipadx=5, #the same like earlier
    ipady=5, #the same like earlier
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
    ipadx=5, #the same like earlier
    ipady=5, #the same like earlier
    expand=True
)

if __name__ == "__main__":
    root.mainloop()


# this is very simple script - please move all of this to class object - it will be more friendly :)
# please migrate ALL print to toast
