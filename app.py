import customtkinter as ctk
import tkinter as tk
from murmur import Murmur
from threading import Thread

primary_color = "#635985"
secondary_color = "#443C68"
background_color = "#18122B"


root = ctk.CTk(fg_color='magenta')
screen_height = root.winfo_screenheight()
root.geometry(f"800x600+0+{screen_height/2}")
root.title("Murmur - AI assistant")
root.overrideredirect(True)
root.wm_attributes("-topmost",True)
root.wm_attributes("-transparentcolor", "magenta")
def set_drag_offset(e):
    drag_offset["x"] = e.x
    drag_offset["y"] = e.y
drag_offset = {"x":0,"y":0}
def move_app(e):
    root.geometry(f"+{0}+{e.y_root-drag_offset['y']}")


# title_label = ctk.CTkLabel(root,text="Murmur", font=ctk.CTkFont(size=30,weight="bold"),fg_color='transparent',bg_color='transparent')
# title_label.pack(anchor='w')




# start_button = ctk.CTkButton(root,text="X",font=ctk.CTkFont(size=16,weight="bold"),command=murmur.start)
# start_button.pack(padx=4)

canvas = ctk.CTkCanvas(root, height=500, width=1000, background='magenta',highlightthickness=0)
canvas.pack(fill="both")

def round_rectangle(canvas,x1, y1, x2, y2, r, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return canvas.create_polygon(points, **kwargs, smooth=True)
def blade(canvas,x1, y1, x2, y2, r, **kwargs):    
    points = (x1, y1, x1, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2, x1, y2, x1, y1, x1, y1, x1, y1)
    return canvas.create_polygon(points, **kwargs, smooth=True)

blade(canvas,0,10,200,110,24, fill=secondary_color)
blade(canvas,0,0,200,100,24, fill=primary_color)

panel = tk.Frame(canvas,background=primary_color,height=100,width=200)

title_bar = ctk.CTkFrame(panel,fg_color=primary_color,corner_radius=0)
title_bar.pack(fill="x",anchor="n")
thinking_text = ctk.CTkLabel(panel,font=ctk.CTkFont(size=16,weight="bold"),fg_color=primary_color)
thinking_text.pack(fill="both",anchor="n")

title_bar_label = ctk.CTkLabel(title_bar,text="Murmur - AI assistant",text_color='white')
title_bar_label.pack(side="left",padx=4)
title_bar_label.bind("<Button-1>",set_drag_offset)
title_bar_label.bind("<B1-Motion>",move_app)

exit_button = ctk.CTkLabel(title_bar,text="X",font=ctk.CTkFont(size=16,weight="bold"),corner_radius=0,fg_color=None)
exit_button.bind("<Button-1>",lambda x: root.quit())
exit_button.pack(fill="y",side="right",padx=4)



canvas.create_window(12, 0, window=panel,height=100,width=200-24, anchor="nw")

thinking_text.configure(text="Hello world")
def update_thinking_text(text):
    thinking_text.configure(text=text)

model = Murmur(['computer'])
model.calibrate()
thread = Thread(target=model.start, args=(update_thinking_text,))
thread.start()
root.mainloop()