import tkinter as tk
from tkinter import messagebox
import time

class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Le Timer Heh 😉")
        master.configure(bg='black')
        
        # set window size to full screen
        master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))

        
        # create a frame to hold the labels and entries
        self.frame = tk.Frame(master, bg='black')
        self.frame.pack(fill='both', expand=True, padx=50, pady=50)

        self.hours = tk.StringVar()
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()

        self.hours_label = tk.Label(self.frame, text="Hours:", fg='white', bg='black')
        self.hours_label.grid(row=0, column=0, padx=5, pady=5)
        self.hours_entry = tk.Entry(self.frame, textvariable=self.hours, width=5, fg='white', bg='black')
        self.hours_entry.grid(row=0, column=1, padx=5, pady=5)

        self.minutes_label = tk.Label(self.frame, text="Minutes:", fg='white', bg='black')
        self.minutes_label.grid(row=1, column=0, padx=5, pady=5)
        self.minutes_entry = tk.Entry(self.frame, textvariable=self.minutes, width=5, fg='white', bg='black')
        self.minutes_entry.grid(row=1, column=1, padx=5, pady=5)

        self.seconds_label = tk.Label(self.frame, text="Seconds:", fg='white', bg='black')
        self.seconds_label.grid(row=2, column=0, padx=5, pady=5)
        self.seconds_entry = tk.Entry(self.frame, textvariable=self.seconds, width=5, fg='white', bg='black')
        self.seconds_entry.grid(row=2, column=1, padx=5, pady=5)

        # create a frame to hold the buttons
        self.button_frame = tk.Frame(master, bg='black')
        self.button_frame.pack(fill='both', expand=True)

        self.start_button = tk.Button(self.button_frame, text="Start", fg='white', bg='green', font=('Arial', 12), command=self.start_timer)
        self.start_button.pack(side='left', padx=10, pady=10)

        self.quit_button = tk.Button(self.button_frame, text="Quit", fg='white', bg='red', font=('Arial', 12), command=master.quit)
        self.quit_button.pack(side='right', padx=10, pady=10)

    def start_timer(self):
        try:
            if self.seconds.get() == '':
                total_seconds = 0
            else:
                total_seconds = int(self.seconds.get())
            if self.minutes.get() != '':
                total_seconds += int(self.minutes.get()) * 60
            if self.hours.get() != '':
                total_seconds += int(self.hours.get()) * 3600
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values for hours, minutes, and seconds.")
            return
        if total_seconds <= 0:
            messagebox.showerror("Error", "Please enter a positive value for the timer.")
            return



        self.hours_entry.configure(state='disabled')
        self.minutes_entry.configure(state='disabled')
        self.seconds_entry.configure(state='disabled')
        self.start_button.configure(state='disabled')
        self.quit_button.configure(state='disabled')

        while total_seconds > 0:
            time_string = self.get_time_string(total_seconds)
            self.master.title(time_string)
            self.master.update()
            time.sleep(1)
            total_seconds -= 1

        self.master.title("Timer")
        self.hours.set("")
        self.minutes.set("")
        self.seconds.set("")
        self.hours_entry.configure(state='normal')
        self.minutes_entry.configure(state='normal')
        self.seconds_entry.configure(state='normal')
        self.start_button.configure(state='normal')
        self.quit_button.configure(state='normal')
        messagebox.showinfo("Timer", "Time's up!")

    def get_time_string(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        if hours > 0:
            time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        else:
            time_string = "{:02d}:{:02d}".format(minutes, seconds)
        return time_string


def main():
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()


if __name__ == '__main__':
    main()


