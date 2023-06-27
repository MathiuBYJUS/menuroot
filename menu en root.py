from tkinter import*
from PIL import ImageTk , Image
from tkinter import ttk

root=Tk()
root.geometry("500x500")
root.config(bg="lightblue")

a1=["Hamburgesa","Cafe"]
a2=["Queso","Jalapeño","Chocolate","Caramelo"]
image1=ImageTk.PhotoImage(Image.open("th.jpg"))




class padre():
    def __init__(self):
        print("Esta es la clase made")
        
    def menu(dish):
        if dish=="Hamburgesa":
            print("Pediste una hamburgesa")
            print("Si quieres puedes añadir queso o jalapeño a tu hamburgesa y tendria un costo extra")
            a3=["Queso","Jalapeño"]
            combobox1["value"]=a3
            
            
        elif dish=="Cafe":
            print("Pediste un cafe")
            print("Si quieres puedes añadir caramelo o chocolate a tu cafe y tendria un costo extra")
            a4=["Chocolate","Caramelo"]
            combobox2["value"]=a4
            
        else :
            print("Ingresa algo valido")
            
    def addons(dish,new_addons):
        if dish=="Hamburgesa" and new_addons=="Queso":
            print("Pediste una hamburgesa con queso $10")
            
        elif dish=="Hamburgesa" and new_addons=="Jalapeño":
            print("Pediste una hamburgesa con jalapeños $10")
            
        elif dish=="Cafe" and new_addons=="Caramelo":
            print("Pediste un cafe con caramelo $10")
            
        elif dish=="Cafe" and new_addons=="Chocolate":
            print("Pediste un cafe con chocolate $10")
        
        
    
        
        
        
        
        
            
        
class hijo1(padre):
    def __init__(self,dish):
        self.new_dish=dish
        
    def get_menu(self):
        new_dish=combobox1.get()
        padre.menu(self.new_dish)

class hijo2(padre):
    def __init__(self,dish,addons):
        self.new_dish=dish
        self.new_addons=addons
        
    def get_final_amount(self):
        new_dish=combobox1.get()
        addons=combobox2.get()
        padre.final_amount(new_dish,addons)
        
        
        


label_1=Label(root,text="Que quieres pedir hoy")
label_1.place(relx=0.2,rely=0.2,anchor=CENTER)
combobox1=ttk.Combobox(root,state="readonly",value=a1)
combobox1.place(relx=0.2,rely=0.3,anchor=CENTER)
label_2=Label(root,text="a")
label_2["image"]=image1
label_2.place(relx=0.7,rely=0.4,anchor=CENTER)
button_1=Button(root,text="Ver condimentos")
button_1.place(relx=0.2,rely=0.4,anchor=CENTER)
label_3=Label(root,text="Elegir suplementos")
label_3.place(relx=0.2,rely=0.6,anchor=CENTER)
combobox2=ttk.Combobox(root,state="readonly",value=a2)
combobox2.place(relx=0.2,rely=0.7,anchor=CENTER)
button_2=Button(root,text="Ver el precio")
button_2.place(relx=0.2,rely=0.8,anchor=CENTER)
label_4=Label(root,text="a")
label_4.place(relx=0.2,rely=0.9,anchor=CENTER)

niño1=hijo1(combobox1.get())
niño1.get_menu()
niño2=hijo2(combobox2.get(),combobox1.get())
niño2.get_final_amount()


root.mainloop()
