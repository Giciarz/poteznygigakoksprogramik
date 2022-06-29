from time import sleep
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

# from picamera import PiCamera

DIR_PATH = Path('./Fotki')

# Starting fuction

def jd():

   # Make catalog
    if not DIR_PATH.exists():
        try:
            DIR_PATH.mkdir()
        except FileExistsError:
            print(FileExistsError)
            
            
    global count #never use global variable - maybe if you have really, but really need
    count = 0
    for path in DIR_PATH.iterdir():
        # if DIR_PATH.is_file():
        count += 1

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
def show_photo(): 

    # img = Image.open(f"./Fotki/Twoje_Foto{count + 1}.jpg")
    # img.show()

    image = Image.open(f"./Fotki/Twoje_Foto{count + 1}.jpg")
    resize_img = image.resize((600,600))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img

    # Checkbutton

    CheckVar1 = IntVar()

    C1 = Checkbutton(
        root,
        text="Cos1",
        activebackground="black",
        activeforeground="white",
        variable=CheckVar1,
        onvalue=1,
        offvalue=0
        # command=
    )
    C1.pack()

# Del function

def delete_img():
    path_list = DIR_PATH.glob("*")
    for f in path_list:
        f.unlink()

def sure():

    # Are_u_Sure label

    root = tk.Tk()
    root.geometry('300x150')
    root.resizable(True, True)
    root.configure(bg="ghost white")
    root.title('Are u sure ?')

    w = tk.Label(root, text="Are u sure?")
    w.configure(bg="ghost white")
    w.pack()

    cancel_button = tk.Button(
        root,
        text="Cancel",
        fg='white',
        bd=0,
        bg='#1B8697',
        activebackground='#3192a1',
        command=root.destroy
    )

    cancel_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    exit_button = tk.Button(
        root,
        text="Exit",
        fg='white',
        bd=0,
        bg='#1B8697',
        activebackground='#3192a1',
        command=exit
    )

    exit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    root.mainloop()

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
root.configure(bg="ghost white")
# root.attributes('-alpha',1)

# Frames

top = tk.Frame(root)
bottom = tk.Frame(root)

top.pack(
    side='top',
    fill='both',
    padx=1,
    pady=screen_height/10
)

bottom.pack(
    side='bottom',
    fill='both',
    pady=screen_height/10
)
top.configure(bg="ghost white")
bottom.configure(bg="ghost white")

# photo button
img_button = tk.Button(
    top,
    fg='white',
    bd=0,
    text='Take a photo',
    bg='#1B8697',
    activebackground='#3192a1',
    command=jd,
    width=20
)
img_button.pack(
    ipadx=screen_width / 55,
    ipady=screen_height / 55,
    expand=True,
    side='left'
)

# Show me photo

show_button = tk.Button(
    top,
    fg='white',
    bd=0,
    text='Show photo',
    bg='#1B8697',
    activebackground='#3192a1',
    command=show_photo,
    width=20
)

show_button.pack(
    ipadx=screen_width/ 55,
    ipady=screen_height / 55,
    # expand=True,
    side='left'
)
# Delete button
del_button = tk.Button(
    top,
    fg='white',
    bd=0,
    text='Delete all photos',
    bg='#1B8697',
    activebackground='#3192a1',
    command=delete_img,
    width=20
)

del_button.pack(
    ipadx=screen_width / 55,
    ipady=screen_height / 55,
    expand=True,
    side='left'
)
# Display img

disp_img = tk.Label()
disp_img.pack(
    pady=20
)

# quit button
quit_button = tk.Button(
    bottom,
    fg='white',
    bd=0,
    text='Exit',
    bg='#E7624F',
    activebackground='#e97160',
    command=sure,
    width=20
)
quit_button.pack(
    ipadx=screen_width / 55,
    ipady=screen_height / 55,
    expand=True
)

print("""\
                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /
                    """)

if __name__ == "__main__":
    root.mainloop()


# this is very simple script - please move all of this to class object - it will be more friendly :)
# please migrate ALL print to toastease migrate ALL print to toast
