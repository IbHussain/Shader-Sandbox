import tkinter as tk
from pynput import mouse
import random
import threading
import customtkinter

mouse_x, mouse_y = 0, 0
sValue = 150

def on_move(x, y):
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y

# Draw the square in the middle of the screen
def update_canvas():
    col = random.randrange(0,9)
    dim = random.randrange(1,100)
    half_size = dim // 2
    x0 = mouse_x - half_size
    y0 = mouse_y - half_size
    x1 = mouse_x + half_size
    y1 = mouse_y + half_size
    canvas.create_rectangle(
        x0, y0, x1, y1,
        fill=colours[col], outline=colours[col]
        )
    # Bind the ESC key to exit fullscreen
    root.bind('<Escape>', lambda e: root.quit())
    root.after(sValue, update_canvas)

#slider value get
def slider_callback(value):
    global sValue
    sValue = round(value)

#window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-alpha', 1)
#root.wm_attributes('-transparentcolor', 'black')
#root.attributes('-topmost', True)

#slider for intensity
slider = customtkinter.CTkSlider(master=root, from_=0, to=300, command=slider_callback)
slider.pack(pady=20)

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


colours = ['red', 'green', 'blue', 'yellow', 'gray', 'cyan', 'magenta', 'orange', 'purple', 'brown']

# Create a canvas widget
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

def startMouseTracker():
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()

listener_thread = threading.Thread(target=startMouseTracker)
listener_thread.start()

# Start updating the canvas
update_canvas()

# Bind the ESC key to exit fullscreen
root.bind('<Escape>', lambda e: root.quit())

# Run the application
root.mainloop()

# Ensure the listener thread is stopped when the application exits
listener_thread.join()