#!/usr/bin/env python
# coding: utf-8

# In[36]:


from tkinter import *
from tkinter import messagebox


top = Tk()  


# In[37]:


import numpy as np 
import pandas as pd
import os


person=pd.read_csv('gender_classification_v7.csv')
person['gender_code']=pd.factorize(person.gender)[0]
y = person.gender_code.values
x = person[["long_hair","forehead_width_cm","forehead_height_cm",
              "nose_wide","nose_long","lips_thin","distance_nose_to_lip_long"]].values
    

def NaiveBayesTahmin():
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

    from sklearn.naive_bayes import GaussianNB
    nb = GaussianNB()
    nb.fit(x_train, y_train)
    y_pred = nb.predict(x_test)

     #istatistikler için
    from sklearn.metrics import classification_report


    #kappa score hesabı için
    from sklearn.metrics import cohen_kappa_score
    kappa_score =cohen_kappa_score(y_test,y_pred)


    #tahmin 
    b1=float(e1.get())
    b2=float(e2.get())
    b3=float(e3.get())
    b4=float(e4.get())
    b5=float(e5.get())
    b6=float(e6.get())
    b7=float(e7.get())
    
    x_predict = [[b1,b2,b3,b4,b5,b6,b7]]
    y_predict = nb.predict(x_predict)
    
    if y_predict[0]==0:
        messagebox.showinfo("tahmin","male")
    elif y_predict[0]==1:
        messagebox.showinfo("tahmin","female")
        
def Istatistics():
    
    messagebox.showinfo("İstatistikler",classification_report(y_test, y_pred))

def ModelPerformance():
    import sklearn.metrics as metrics
    messagebox.showinfo('MAE', metrics.mean_absolute_error(y_test, y_pred))
    messagebox.showinfo('MSE', metrics.mean_squared_error(y_test, y_pred))
    messagebox.showinfo('RMSE', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    messagebox.showinfo("KAPPA SCORE" ,kappa_score)
    
def dataset():
    foto = Toplevel()
    canvas = Canvas(foto, width = 1500, height = 600)
    canvas.pack(expand = YES, fill = BOTH)
    image = PhotoImage(file = 'dataset.png')
    canvas.create_image(50, 20, image = image, anchor = NW)
    canvas.image = image

top.geometry("800x550")
lbl1 = Label(top, text = "Girilen Fiziksel Özellik Değerlerine Göre Cinsiyet Tahmini").place(x = 200,y = 40)  
lbl1 = Label(top, text = "Saç uzun ise 1, kısa ise 0 giriniz:").place(x = 110,y = 80)  
lbl3 = Label(top, text = "Alın genişliğini cm türünden giriniz (ör. 13.2):").place(x = 110, y = 120)  
lbl2 = Label(top, text = "Alın yüksekliğini cm türünden giriniz (ör. 5.2):").place(x = 110, y =160 )  
lbl4 = Label(top, text = "Burun geniş ise 1, dar ise 0 giriniz:").place(x = 110, y =200 ) 
lbl5 = Label(top, text = "Burun uzun ise 1, kısa ise 0 giriniz:").place(x = 110, y =240 ) 
lbl6 = Label(top, text = "Dudak ince ise 1, kalın ise 0 giriniz:").place(x = 110, y =280 ) 
lbl7 = Label(top, text = "Burun ile dudak arası mesafe uzun ise 1, kısa ise 0 giriniz:").place(x = 110, y =320 ) 

e1 = Entry(top)
e1.place(x = 500, y = 75)
e2 = Entry(top)
e2.place(x = 500, y = 115)
e3 = Entry(top) 
e3.place(x = 500, y = 155)
e4 = Entry(top)
e4.place(x = 500, y = 195)
e5 = Entry(top) 
e5.place(x = 500, y = 235)
e6 = Entry(top)
e6.place(x = 500, y = 275)
e7 = Entry(top)
e7.place(x = 500, y = 315)



button1= Button(top, text ="Naive Bayes ile Cinsiyet Tahmini",width=30,command=NaiveBayesTahmin).place(x = 240, y = 380)
button2= Button(top, text ="İstatistikler",width=30,command=Istatistics).place(x = 240, y = 410)
button2= Button(top, text ="MAE,MSE,RMSE,KAPPA",width=30,command=ModelPerformance).place(x = 240, y = 440)
button3= Button(top, text ="Dataset",width=30,command=dataset).place(x = 240, y = 470)
    
top.mainloop()


# In[ ]:





# In[ ]:




