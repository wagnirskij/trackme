import tkinter as tk
from datetime import datetime, timedelta
import time
import json


class UserInterface:

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("TrackMe")
        self.window.config(padx=20,pady=20,bg="white")

        self.start_time = None
        self.good_time_start = None
        self.bad_time_start = None

        self.times_dict = {
            "productive seconds": 0,
            "fuckin around seconds": 0,

        }

        
        
        with open("F:/100DAYS/trackme/recorded_seconds.json", mode="r") as data:
            loaded_times_dict = json.load(data)

        self.good_time_total = loaded_times_dict["productive seconds"]
        self.bad_time_total = loaded_times_dict["fuckin around seconds"]

        self.canvas = tk.Canvas(width=300,height=250,highlightthickness=0,bg="white")
        self.start_button = tk.Button(text="Start", command=self.timer_start)
        self.start_button.grid(row=2,column=0)
        

       
        self.stop_button = tk.Button(text="stop", command=self.timer_stop)
        self.stop_button.grid(row=1,column=0)
        self.canvas.grid(row=1,column=0,  padx=20,pady=20)

        self.productive_button = tk.Button(text="productive", command=self.good_time_start_record)
        self.productive_button.grid(row=3, column=0)

        self.fuckin_around_button = tk.Button(text="fuckin around", command=self.bad_time_start_record)
        self.fuckin_around_button.grid(row=3, column=1)

        self.save_button = tk.Button(text="Record Time", command=self.record_time)
        self.save_button.grid(row=4, column=2)

        self.time_label = tk.Label(text="Time: ", font=("Arial", 20), bg="blue", fg="white")
        self.time_label.grid(row=0, column=1)
        self.window.mainloop()

    def timer_start(self) -> int:
          ## make it so its a button press SOLVED
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
            
            if self.fuckin_around_button.cget("state") == "disabled":
                self.bad_time_total += (datetime.now() - self.bad_time_start).seconds
            elif self.productive_button.cget("state") == "disabled":
                self.good_time_total += (datetime.now() - self.good_time_start).seconds


            self.productive_button.config(state=tk.NORMAL)
            self.fuckin_around_button.config(state=tk.NORMAL)
            self.good_time_start = None
            self.bad_time_start = None
            print(f"{self.elapsed_time.seconds=}")
            print(f"{self.good_time_total=}")
            print(f"{self.bad_time_total=}")

    def label_update(self):
        if self.start_time:
            self.elapsed_time = datetime.now() - self.start_time
            self.time_label.config(text=f"Time elapsed: {self.elapsed_time.seconds}")
            self.update_id = self.window.after(1000, self.label_update)
            
    def category_press(self, category) -> int:
        pass

    def record_time(self):

        self.times_dict["productive seconds"] = self.good_time_total
        self.times_dict["fuckin around seconds"] = self.bad_time_total
        with open("F:/100DAYS/trackme/recorded_seconds.json", mode="w") as data:
            json.dump(self.times_dict, data, indent=4)


    def good_time_start_record(self):
        if self.bad_time_start:
            self.bad_time_total += (datetime.now() - self.bad_time_start).seconds
        self.good_time_start = datetime.now()
        self.productive_button.config(state=tk.DISABLED)
        self.fuckin_around_button.config(state=tk.NORMAL)
        


    def bad_time_start_record(self):
        if self.good_time_start:
            self.good_time_total += (datetime.now() - self.good_time_start).seconds
        self.bad_time_start = datetime.now()
        self.productive_button.config(state=tk.NORMAL)
        self.fuckin_around_button.config(state=tk.DISABLED)




ui = UserInterface()
ui

