from tkinter import *
import random

root=Tk()
root.title("Random Country and Capital")
root.geometry("2000x2000")

enter_name = Entry(root)
enter_name.place(relx=0.5,rely=0.2,anchor=CENTER)

country_list = Label(root)
capital_list = Label(root)
random_number_label_1 = Label(root)
random_number_label_2 = Label(root)
random_country = Label(root)
random_capital = Label(root)

list1 = []
def addcountry():
    country_name = enter_name.get()
    list1.append(country_name)
    country_list["text"] = "Country Name : " + str(list1)
  
list2 = []
def addcapital():
    capital_name = enter_name.get()
    list2.append(capital_name)
    capital_list["text"] = "Capital Name : " + str(list2)

def random_number1():
    length= len(list1)
    random_no1 = random.randint(0, length-1)
    random_number_label_1["text"] + str(random_no1)
    generated_random_number_1 = list1[random_no1]
    random_country["text"] = "Random Country " + str(generated_random_number_1)
    
def random_number2():
    length= len(list2)
    random_no2 = random.randint(0, length-1)
    random_number_label_2["text"] + str(random_no2)
    generated_random_number_2 = list2[random_no2]
    random_capital["text"] = "Random Capital" + str(generated_random_number_2)

btn1 = Button(root, text="Add to the Country list", command = addcountry)
btn1.place(relx=0.5,rely=0.3,anchor=CENTER)

country_list.place(relx=0.5,rely=0.4,anchor=CENTER)

btn2 = Button(root, text="Add to the Capital list", command = addcapital)
btn2.place(relx=0.5,rely=0.5,anchor=CENTER)

capital_list.place(relx=0.5,rely=0.6,anchor=CENTER)

btn3 = Button(root,text="Display random Country name ", command = random_number1)
btn3.place(relx=0.5,rely=0.7,anchor=CENTER)

random_number_label_1.place(relx=0.5,rely=0.8,anchor=CENTER)
random_capital.place(relx=0.5,rely=0.9,anchor=CENTER)

btn4 = Button(root,text="Display random Capital name ", command = random_number2)
btn4.place(relx=0.5,rely=0.10,anchor=CENTER)

random_number_label_2.place(relx=0.5,rely=0.11,anchor=CENTER)
random_capital.place(relx=0.5,rely=0.12,anchor=CENTER)

root.mainloop()