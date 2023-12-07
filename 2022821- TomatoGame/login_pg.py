
# It's a class that creates a GUI window with a background image, a login button, a forget password
# button, and a new user button. 
# 
# The login button is supposed to check the user's credentials against a database and if they match,
# it should open a new window. 
# 
# The forget password button is supposed to open a new window that allows the user to reset their
# password. 
# 
# The new user button is supposed to open a new window that allows the user to create a new account. 

import hashlib
import sqlite3
from subprocess import call
from tkinter import Button, Entry, Label, PhotoImage, StringVar, Tk, messagebox


class login:
        def __init__(self,root):
                self.root = root #GUI Container
                self.root.geometry('800x600+350+100') #GUI AREA SIZE
                self.root.title(' Tomato Game') # Windows Title
                 




#Label 
                # It's creating two labels.
                user_id = Label(self.root,text='USER ID      :- ',fg='Black',bg ='Red',font=("Times New Roman",30,)).place(x=50,y=130)
                password =Label (self.root,text='PASSWORD :-',fg='Black',bg = 'Red',font=("Times New Roman",30,)).place(x=50,y=250)

# Variables
                # It's creating two variables.
                self.var_user_id = StringVar()
                self.var_password = StringVar()
# Text box
                # It's creating two text boxes.
                txt_user_id=Entry(self.root, textvariable=self.var_user_id,bg = 'white',font=("Times New ROman",30)).place(x=325,y=130)
                txt_passowrd=Entry(self.root, textvariable=self.var_password,bg ="white",font=("Times New ROman",30)).place(x=325,y=250)

#Login button
                # It's creating three buttons.
                login_button = Button(self.root,text="Login ",command =self.login,font=("Times New Roman",35,),bg="Green",fg="white",cursor='hand2', ).place(x=320,y=360,width=200,height=55)
                forget_button= Button(self.root,text="Forget ",command = self.forget,font=("Times New Roman",30,),fg="Black",cursor='hand2', ).place(x=200,y=500,width=200,height=55)
                create_button= Button(self.root,text="New One ",command = self.create,font=("Times New Roman",30,),fg="red",cursor='hand2', ).place(x=450,y=500,width=200,height=55)
                

        def forget(self):
                """
                It destroys the window
                """
                self.root.destroy()
                call(["python", "forget_password.py"])
        

        def login(self):
                # It's connecting to the database and creating a cursor.
                con= sqlite3.connect( database=r'user.db')
                cur = con.cursor()
                # It's checking if the user has entered a user id and password. If they haven't, it
                # displays an error message.
                if self.var_user_id.get()=='' or self.var_password.get() == '':
                        messagebox.showerror("Error ","Please fill the required details",parent= self.root)

                else:
                        # It's getting the user id from the database.
                        cur.execute('select user_id from user where user_id = ? ',(self.var_user_id.get()))
                        user = cur.fetchone()

                        try:
                                
                                # It's checking if the user id entered by the user exists in the
                                # database. If it doesn't, it displays an error message.
                                cur.execute('select user_id from user where user_id= ? ',(self.var_user_id.get()))
                                user_id = cur.fetchone()
                                if user_id == None:
                                        messagebox.showerror('Error',"User Doesn't exist",parent=self.root)

                                else :
                                        
                                        # It's getting the password from the database.
                                        cur.execute('select password from user where user_id= ? ',(self.var_user_id.get()))
                                        user_pass = cur.fetchone()
                                        
                                        # It's converting the password entered by the user to a hash
                                        # value.
                                        password  = hashlib.sha1(bytes(self.var_password.get(),encoding='utf-8'))
                                        hex_password = password.hexdigest()  

                                        # It's getting the name of the user from the database.
                                        cur.execute('select fullname from user where user_id= ? ',(self.var_user_id.get()))
                                        data_name = cur.fetchone()                                    
                                        

                                        
                                       # It's checking if the password entered by the user matches the
                                       # password in the database.
                                        if hex_password!= user_pass[0]:
                                                
                                                messagebox.showerror("Error",'Wrong password',parent=self.root) 
                                        else:
                                                # It's getting the name of the user from the database.
                                                # It's getting the name of the user from the database.
                                                name = data_name[0]
                                                # It's destroying the current window.
                                                
                                                messagebox.showinfo('Success','login',parent=self.root)
                                                self.root.destroy()
                                                
                                                # It's calling the main_play.py file and passing the
                                                # name variable to it.
                                                call(["python",'main_play.py',f'{name}']) 

                                        # It closes the connection to the database.
                                        con.close()                                  

                        except Exception as e:
                                messagebox.showerror("Error",'Error on login due to :',parent= self.root)



        def create(self):
                
                """
                It destroys the current window and opens a new window.
                """
                self.root.destroy()
                call(['python','registration_pg.py'])
                



                
# It's creating an instance of the login class and running the mainloop method.
if __name__ == '__main__':
    root=Tk()
    login_object = login(root)
    root.mainloop()