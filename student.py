from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

         # First Image
        img = Image.open(r"D:\face_recognition system\college_images\face-recognition.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(r"D:\face_recognition system\college_images\smart-attendance.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(r"D:\face_recognition system\college_images\clg.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)


        # Background Image
        img3 = Image.open(r"D:\face_recognition system\college_images\bgimgnew.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM ", font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50, width=1480, height=600)



if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
