# import calendar
# def display_calendar(year, month):
#     # Create a TextCalendar instance
#     cal = calendar.TextCalendar(calendar.SUNDAY)

#     # Format the mont/year into a string
#     month_calendar = cal.formatmonth(year, month)

#     # Display the calendar
#     print(month_calendar)

# year = 2024
# month = 7
# display_calendar(year, month)

import tkinter as tk
from tkinter import ttk
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar")

        self.year_var = tk.IntVar(value = 2024)
        self.month_var = tk.IntVar(value = 7)

        self.create_widgets()
        self.show_calendar()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady = 10)

        year_label = ttk.Label(frame, text = "Year:")
        year_label.grid(row = 0, column = 0, padx = 5)

        year_entry = ttk.Entry(frame, textvariable = self.year_var, width = 5)
        year_entry.grid(row = 0, column = 1, padx = 5)

        month_label = ttk.Label(frame, text = "Month:")
        month_label.grid(row = 0, column = 2, padx = 5)

        month_entry = ttk.Entry(frame, textvariable = self.month_var, width = 3)
        month_entry.grid(row = 0, column = 3, padx = 5)

        show_button = ttk.Button(frame, text = "Show Calendar", command = self.show_calendar)
        show_button.grid(row = 0, column = 4, padx = 5)

        self.calendar_text = tk.Text(self.root, width = 20, height = 8, font = ("Courier", 14))
        self.calendar_text.pack(pady = 10)

    def show_calendar(self):
        year = self.year_var.get()
        month = self.month_var.get()

        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_calendar = cal.formatmonth(year, month)

        self.calendar_text.delete("1.0", tk.END)
        self.calendar_text.insert(tk.END, month_calendar)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()