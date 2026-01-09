"""
    1. 'tkinter' to create main window
    2. 'gui' to create gui class
"""

import tkinter as tk
from gui import TopLevel

# MAIN DRIVER
# ==================================================================================================
if __name__ == "__main__":
    root = tk.Tk()
    top = TopLevel(root)
    root.mainloop()
