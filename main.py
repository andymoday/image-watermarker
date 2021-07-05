from tkinter import *

BACKGROUND_COLOR = "#456456"


# ------------------------------SET UP UI---------------------------------------- #

window = Tk()
window.title("Image Watermarker")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

add_image_button = Button(text="Select Image", command=load_image)
add_image_button.grid(row=0, column=0)

window.mainloop()
