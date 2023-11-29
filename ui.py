import tkinter as tk
from datetime import datetime, timedelta
import time

class UserInterface:

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("TrackMe")
        self.window.config(padx=20,pady=20,bg="white")

        self.start_time = None

        self.canvas = tk.Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.start_button = tk.Button(text="Start", command=self.timer_start)
        self.start_button.grid(row=2,column=0)
        

       
        self.stop_button = tk.Button(text="stop", command=self.timer_stop)
        self.stop_button.grid(row=1,column=0)
        self.canvas.grid(row=1,column=0,  padx=20,pady=20)

        

        self.time_label = tk.Label(text="Time: ", font=("Arial", 20), bg="blue", fg="white")
        self.time_label.grid(row=0,column=1)
        self.window.mainloop()

    def timer_start(self) -> int:
          ## make it so its a button press
        self.start_time = datetime.now()
        print("its running!")
        self.label_update()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
       

    def timer_stop(self) -> int:
        if self.start_time:
            self.time_label.config(text=f"timer stopped! total time: {self.elapsed_time.seconds}")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.window.after_cancel(self.update_id)

    def label_update(self):
        if self.start_time:
            self.elapsed_time = datetime.now() - self.start_time
            self.time_label.config(text=f"Time elapsed: {self.elapsed_time.seconds}")
            self.update_id = self.window.after(1000, self.label_update)
            
    def category_press(self, category) -> int:
        pass


ui = UserInterface()
ui