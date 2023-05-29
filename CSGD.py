from tkinter import *

root = Tk()

scr_w = root.winfo_screenwidth()
scr_h = root.winfo_screenheight()
app_w = 500
app_h = 250
x = (scr_w/2) - (app_w/2)
y = (scr_h/2) - (app_h/2)
root.geometry(f"{int(app_w)}x{int(app_h)}+{int(x)}+{int(y)}")
root.minsize(app_w, app_h)
root.maxsize(app_w, app_h)
finger = PhotoImage(file = r"..\College Python Project\img\tkImg\finger.png")
fingimg = finger.subsample(1, 1)
mouse = PhotoImage(file = r"..\College Python Project\img\tkImg\mouse.png")
mouseimg = mouse.subsample(1, 1)
volume = PhotoImage(file = r"..\College Python Project\img\tkImg\volume.png")
volumeimg = volume.subsample(1, 1)
face = PhotoImage(file = r"..\College Python Project\img\tkImg\face.png")
faceImg = face.subsample(1, 1)
hand = PhotoImage(file = r"..\College Python Project\img\tkImg\hand.png")
handImg = hand.subsample(1, 1)
gender = PhotoImage(file = r"..\College Python Project\img\tkImg\gender.png")
genderImg = gender.subsample(1, 1)
emotions = PhotoImage(file = r"..\College Python Project\img\tkImg\emotions.png")
emotionsImg = emotions.subsample(1, 1)


def changeOnHover(button, colorOnHover, colorOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

def handMenu():
    handWindow = Toplevel(root)
    handWindow.title("Hand Menu")
    scr_w = handWindow.winfo_screenwidth()
    scr_h = handWindow.winfo_screenheight()
    app_w = 700
    app_h = 350
    x = (scr_w/2) - (app_w/2)
    y = (scr_h/2) - (app_h/2)
    handWindow.geometry(f"{int(app_w)}x{int(app_h)}+{int(x)}+{int(y)}")
    handWindow.minsize(app_w, app_h)
    handWindow.maxsize(app_w, app_h)
    hMenuLbl = Label(handWindow, text="Hand Menu", font=('times', 20, 'bold'), fg='red')
    hMenuLbl.pack(pady=10, padx=15, anchor = SW, side = TOP)

    from HandTask import HandFingerCounting, VirtualMouse, VolumeHandControl
    fingBtn = Button(handWindow, text="Count Finger System", image=fingimg, relief=GROOVE, padx=20, pady=10, font=("Purisa",15,"bold"), compound = LEFT, bg="white", width=300, command=HandFingerCounting.main)
    fingBtn.pack(pady=10, side=TOP)
    changeOnHover(fingBtn, "cyan", "white")

    mouseBtn = Button(handWindow, text="Virtual Mouse System", image=mouseimg, relief=GROOVE, padx=20, pady=10, font=("Purisa",15,"bold"), compound = LEFT, bg="white", width=300, command=VirtualMouse.main)
    mouseBtn.pack(pady=10, side=TOP)
    changeOnHover(mouseBtn, "cyan", "white")

    volumeBtn = Button(handWindow, text="Volume Control System", image=volumeimg, relief=GROOVE, padx=20, pady=10, font=("Purisa",15,"bold"), compound = LEFT, bg="white", width=300, command=VolumeHandControl.main)
    volumeBtn.pack(pady=10, side=TOP)
    changeOnHover(volumeBtn, "cyan", "white")

def faceMenu():
    faceWindow = Toplevel(root)
    faceWindow.title("Face Menu")
    scr_w = faceWindow.winfo_screenwidth()
    scr_h = faceWindow.winfo_screenheight()
    app_w = 700
    app_h = 250
    x = (scr_w/2) - (app_w/2)
    y = (scr_h/2) - (app_h/2)
    faceWindow.geometry(f"{int(app_w)}x{int(app_h)}+{int(x)}+{int(y)}")
    faceWindow.minsize(app_w, app_h)
    faceWindow.maxsize(app_w, app_h)
    hMenuLbl = Label(faceWindow, text="Face Menu", font=('times', 20, 'bold'), fg='red')
    hMenuLbl.pack(pady=10, padx=15, anchor = SW, side = TOP)

    from FaceTask import emotions, gender
    ageGenderBtn = Button(faceWindow, text="Gender Detection", image=genderImg, relief=GROOVE, padx=20, pady=10, font=("Purisa",15,"bold"), compound = LEFT, bg="white", width=300, command=gender.main)
    ageGenderBtn.pack(pady=10, side=TOP)
    changeOnHover(ageGenderBtn, "cyan", "white")

    emotionBtn = Button(faceWindow, text="Emotions Detection", image=emotionsImg, relief=GROOVE, padx=20, pady=10, font=("Purisa",15,"bold"), compound = LEFT, bg="white", width=300, command=emotions.main)
    emotionBtn.pack(pady=10, side=TOP)
    changeOnHover(emotionBtn, "cyan", "white")

if __name__ == "__main__":

    root.title("Control System & Gesture Detection")
    csgdLbl = Label(text="Control System & Gesture Detection", font=('times', 20, 'bold'), fg='red')
    csgdLbl.pack(pady=10, padx=15, anchor = SW, side = TOP)


    hTaskBtn = Button(text="Hand Task", image=handImg, relief=GROOVE, padx=20, pady=5, font=("Purisa",15,"bold"), compound = LEFT, bg="white", width=150, command=handMenu)
    hTaskBtn.pack(pady=10, side=TOP)
    changeOnHover(hTaskBtn, "cyan", "white")
    # hTaskBtn.bind('<Button-1>', handMenu)


    fTaskBtn = Button(text="Face Task", image=faceImg, relief=GROOVE, padx=20, pady=5, font=("Purisa",15,"bold"), compound = LEFT, bg="white", width=150, command=faceMenu)
    fTaskBtn.pack(pady=10, side=TOP)
    changeOnHover(fTaskBtn, "cyan", "white")
    root.mainloop()