# this is the file meant to be run to begin program

import tkinter as tk
from loginpage import Login
from mainwindow import EconomicSimulatorGraphs



def main():
    root = tk.Tk()
    user_id = Login.validation  # Implement this function
    app = None

    if user_id:
        app = EconomicSimulatorGraphs(root, user_id)
    else:
        app = Login(root)  # or Signup(root) based on the context

    root.mainloop()

if __name__ == "__main__":
    main()
