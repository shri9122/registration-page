from tkinter import *


shri = Tk()
shri.geometry('600x400')
shri.config(bg="sky blue")
shri.title("registration page")
font="Calibiri"
lab= Label(shri,text="BCET REGISTRATION FORM ",bg="blue",fg="white",font=font,width="44",height="3")
lab.grid(row=0,column=1)

name = Label(shri,text="Your Name:-",bg="sky blue",fg="black",font=font,width="44",height="2")
name.grid(row=3,column=0)
name_entry=Entry(shri)
name_entry.grid(row=3,column=2)

name1 = Label(shri,text="Father Name:-",bg="sky blue",fg="black",font=font,width="44",height="2")
name1.grid(row=5,column=0)
name1_entry=Entry(shri)
name1_entry.grid(row=5,column=2)

dob = Label(shri,text="Student Date Of Birth",bg="sky blue",fg="black",font=font,width="44",height="2")
dob.grid(row=7,column=0)
dob_entry=Entry(shri)
dob_entry.grid(row=7,column=2)

add = Label(shri,text="Address",bg="sky blue",fg="black",font=font,width="44",height="2")
add.grid(row=9,column=0)
add_entry=Entry(shri)
add_entry.grid(row=9,column=2)

cont = Label(shri,text="Contact Number",bg="sky blue",fg="black",font=font,width="44",height="2")
cont.grid(row=11,column=0)
cont_entry=Entry(shri)
cont_entry.grid(row=11,column=2)

email = Label(shri,text="Your Email",bg="sky blue",fg="black",font=font,width="44",height="2")
email.grid(row=13,column=0)
email_entry=Entry(shri)
email_entry.grid(row=13,column=2)

xxx=Label(shri,text="Please Choose College",bg="sky blue",fg="black",font=font,width="44",height="2")
xxx.grid(row=15,column=0)


collgname = Checkbutton(shri,text="BCET",bg="white",fg="black",font=font)
collgname.grid(row=15,column=1)


collgname1 = Checkbutton(shri,text="BCP",bg="white",fg="black",font=font)
collgname1.grid(row=15,column=2)


collgname2 = Checkbutton(shri,text="BCPSR",bg="white",fg="black",font=font)
collgname2.grid(row=15,column=3)

line =Label(shri,text="_____________________________________",bg="sky blue",fg="black",font=font)
line.grid(row=16,column=0)

line2 =Label(shri,text="____________________________________",bg="sky blue",fg="black",font=font)
line2.grid(row=16,column=1)

line3 =Label(shri,text="____________________________________",bg="sky blue",fg="black",font=font)
line3.grid(row=16,column=2)


submit =Button(shri,text="Submit",bg="green",width="20",height="2")
submit.grid(row=17,column=1)



shri.mainloop()