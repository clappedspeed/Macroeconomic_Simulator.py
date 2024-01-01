
# Login and Sign up page

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from Database import *
import hashlib



class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Economics Simulator") # title at top of screen
        self.root.geometry("1280x720+100+50") # resolution and centering
        self.root.resizable(False, False) #does not allow for resizing

        #background image and loading it
        self.bg=ImageTk.PhotoImage(file="images/vaporwave_bg.jpg")
        #placing image as a lavel
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Frames for login (the huge box used to have sign up and login placed)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=338, y=150, width=500, height=600)

        # the titles and subtitles of the page
        title = Label(Frame_login, text="login page", font=("Arial", 36, "bold"), fg="#78877c", bg="white").place(x=98, y=30)
        subtitle = Label(Frame_login, text="Login to return", font=("Arial", 18, "bold"), fg="#1d1d1d", bg="white").place(x=98, y=100)

        # the username and password labels and their associated entry boxes
        user_label = Label(Frame_login, text="Username:", font=("Arial", 18, "bold"), fg="#1d1d1d", bg="white").place(x=98, y=180)
        self.username = Entry(Frame_login, font=("Goudy old style", 18), bg="#e7e6e6")
        self.username.place(x=90, y=250, width=328, height=35)
        password_label = Label(Frame_login, text="Password:", font=("Arial", 18, "bold"), fg="#1d1d1d", bg="white").place(x=98, y=300)
        self.password = Entry(Frame_login, font=("Goudy old style", 18), bg="#e7e6e6", show="*")
        self.password.place(x=90, y=370, width=328, height=35)

        Sign_up = Button(Frame_login,command=Signup, text="Sign Up:", font=("Arial", 18, "bold"), fg="#1d1d1d", bg="white").place(x=98, y=500)
        submit = Button(Frame_login,command=self.validation, text="login:", font=("Arial", 20, "bold"), fg="#1d1d1d", bg="white").place(x=98,y=420)

    def validation(self):
        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            # this checks only if there is something written
            cursor.execute("SELECT username, password FROM tblUserData WHERE username = ?", (username,)) # select query for records that match usernames
            row = cursor.fetchone()

            if row is not None:
                # this is executed when the fetched record has data
                database_username, database_password = row
                hashed_password = hashlib.sha256(password.encode()).hexdigest() # this hashes the user input

                if hashed_password == database_password:
                    user_id = row[0]  # Assuming row[0] is the user ID
                    self.load_main_menu(user_id)
                    user_id = self.get_user_id(username)  # Retrieve user ID based on username
                    # self.load_main_menu(user_id)  # Load main menu with user ID
                    return user_id
                else:
                    messagebox.showerror("Error", "Incorrect username or password", parent=self.root)
                    return None

            else:
                messagebox.showerror("Error", "User not found", parent=self.root)
                return None

    def get_user_id(self, username):
        """Fetch user ID based on username."""
        cursor.execute("SELECT user_id FROM tblUserData WHERE username = ?", (username,))
        result = cursor.fetchone()
        return result[0] if result else None

    def load_main_menu(self, user_id):
        """Load the main menu with the given user ID."""
        from mainwindow import EconomicSimulatorGraphs
        self.root.destroy()  # Close the login window
        main_root = Tk()  # Create a new Tk root for the main application
        EconomicSimulatorGraphs(main_root, user_id)
        main_root.mainloop()



class Signup(Login):
    # this inherits some feature from login class
    def __init__(self):
        super().__init__(root)
        # background is changed
        self.bg = ImageTk.PhotoImage(file="images/signup_background.jpeg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # Frames for login
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=338, y=150, width=500, height=600)

        # the titles and subtitles
        title = Label(Frame_login, text="Sign Up page", font=("Arial", 36, "bold"), fg="#78877c", bg="white").place(x=98,
                                                                                                                  y=30)
        subtitle = Label(Frame_login, text="Make a new account!", font=("Arial", 18, "bold"), fg="#1d1d1d",
                         bg="white").place(x=98, y=100)

        # username and password labels and entry boxes
        username_label = Label(Frame_login, text="Username:", font=("Arial", 18, "bold"), fg="#1d1d1d", bg="white").place(
            x=98, y=150)
        self.username = Entry(Frame_login, font=("Goudy old style", 18), bg="#e7e6e6")
        self.username.place(x=90, y=190, width=300, height=30)

        password_label = Label(Frame_login, text="Password:", font=("Arial", 18, "bold"), fg="#1d1d1d",
                               bg="white").place(x=98, y=250)
        self.password = Entry(Frame_login, font=("Goudy old style", 18), bg="#e7e6e6", show="*")
        self.password.place(x=90, y=300, width=328, height=30)

        password_confirm_label = Label(Frame_login, text="Confirm Password:", font=("Arial", 18, "bold"), fg="#1d1d1d",
                               bg="white").place(x=98, y=340)
        self.password_confirm = Entry(Frame_login, font=("Goudy old style", 18), bg="#e7e6e6")
        self.password_confirm.place(x=90, y=390, width=328, height=30)
        # submit box and login boxes at the bottom
        submit = Button(Frame_login,command= self.signup, text="Sign up:", font=("Arial", 20, "bold"), fg="#1d1d1d",
                        bg="white").place(x=98, y=430)
        login_page = Button(Frame_login,command=lambda: Login(root), text="Back to login", font=("Arial", 20, "bold"), fg="#1d1d1d", bg="white").place(x=98, y=500)
        # Lamnda is used as an anonymous function to call instance of login class (goes back to login page)

    def signup(self):
        # this method adds the user inputs in sign up into the database
        username = self.username.get()
        password = self.password.get()
        password_confirm = self.password_confirm.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            if password != password_confirm:
                messagebox.showerror("Error", "Passwords do not match", parent=self.root)
            elif len(str(password)) < 8:
                messagebox.showerror("Error", "Password needs to be at least 8 characters", parent=self.root)
            else:
                # Check if the username already exists
                cursor.execute("SELECT * FROM tblUserData WHERE username=?", (username,))
                existing_user = cursor.fetchone()

                if existing_user:
                    messagebox.showerror("Error", "Username already exists. Please choose a different one.",
                                         parent=self.root)
                else:
                    # Insert the new user
                    new_username, new_password = username, hashlib.sha256(password.encode()).hexdigest()
                    cursor.execute("INSERT INTO tblUserData (username, password) VALUES (?, ?)",
                                   (new_username, new_password))
                    connect.commit()
                    messagebox.showinfo("Successful", "Account created successfully", parent=self.root)



root = Tk()
obj = Login(root)
root.mainloop()
