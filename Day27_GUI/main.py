"""Project: GUI/Tkinter Practice
Start: April 25th, 2024
Last touched: April 25th, 2024
Author: Madeleine L.
"""

import tkinter
window = tkinter.Tk()
window.title("Practice GUI Program")
window.minsize(width=500, height=300)

# Create label
my_label = tkinter.Label(text="Test label", font=("Arial", 24, "bold"))
# place formatted label on screen
my_label.pack(side="top")

#

# to keep window on screen
window.mainloop()
