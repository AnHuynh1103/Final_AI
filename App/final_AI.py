from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import Image, ImageTk

from keras.models import load_model
from keras.utils import load_img,img_to_array

import numpy as np
import cv2 as cv
import time
img_size = 200
model_final = load_model("c:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Artificial Intelligence\\Final_AI\\Save\\Final_AI_good.h5")

def main():
    window = Tk()
    window.title('Celebrity identification')
    window.geometry('600x450')
    
    def read_filename():
        global filename
        filename=askopenfilename(initialdir='c:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Artificial Intelligence\\Final_AI\\', 
                                 title = 'Select Image File',  
                                 filetypes=[('PNG file', '*.png'), ('JPG file', '*.jpg'), ('GIF file', '*.gif'),('All files', '*')])
        #show loading img
        '''load_img = Image.open('c:\\Users\\Admin\\Documents\\Tai_lieu_mon_hoc\\HKII_2022_2023\\Artificial Intelligence\\Final_AI\\App\\loading.gif')
        load_img_resize = load_img.resize((100,100), Image.ANTIALIAS)
        converted_img = ImageTk.PhotoImage(load_img_resize)
        L5.configure(image = converted_img)
        L5.image = converted_img
        time.sleep(5)'''
        #show img
        my_img = Image.open(filename)
        my_img = ImageTk.PhotoImage(my_img)
        L3.configure(image = my_img)
        L3.image = my_img
        load_image(filename)
    
    # load and prepare the image
    def load_image(filename):
        # load the image
        global img
        img = load_img(filename, target_size=(img_size, img_size))
        img = img_to_array(img)
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        img = img.reshape(1,img_size,img_size,1)
        show_result(img)

    def show_result(img):
        result = model_final.predict(img)
        print(result)
        np.argmax(result)
        print('Prediction: ',labels[np.argmax(result)])
        E2.delete(0,END)
        E2.insert(0,labels[np.argmax(result)])
        
        
    def clear():
        E2.delete(0,END)
        L3.configure(image = '')
        

    labels = {0:'Huu Chau',
              1:'Ninh Duong Lan Ngoc',
              2:'Ngoc Giau',
              3:'Son Tung M-TP',
              4:'Thanh Loc',
              5:'Thuy Ngan',
              6:'Toc Tien',
              7:'Tran Thanh',
              8:'Truong Giang',
              9:'Viet Huong' }
    
    #
    BT = Button(window,text = 'Browse Image',font = ('Times New Roman', 12, 'bold'),command = read_filename)
    BT.place(relx=0.2, rely=0.35, anchor = 'center')
    #
    clrBT = Button(window,text = 'Clear',font = ('Times New Roman', 12, 'bold'),command = clear)
    clrBT.place(relx=0.2, rely=0.52, anchor = 'center')
    #
    
    L1 = Label(window, text = 'Recognizing famous people in Vietnam',font = ('Times New Roman', 12, 'bold'))
    L1.place(relx = 0.45, rely = 0.05, anchor = 'center')
    
    E2 = Entry(window, text = '',font = ('Times New Roman', 12, 'bold'))
    E2.place(relx = 0.2, rely=0.75, anchor = 'center')
    
    L3 = Label(window, image = '')
    L3.place(relx = 0.5, rely = 0.2)
    
    L4 = Label(text = 'Prediction: ',font = ('Times New Roman', 12, 'bold'),fg = 'red')
    L4.place(relx = 0.2,rely = 0.68, anchor = 'center')
    #
    
    '''L5 = Label(window,image = '')
    L5.place(relx = 0.63, rely = 0.4)'''
    
    
    
    window.mainloop()
    
    
if __name__ == "__main__":
    main()