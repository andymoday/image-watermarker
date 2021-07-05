from tkinter import *
import os, sys
from PIL import Image

BACKGROUND_COLOR = "#456456"


# ------------------------------FUNCTIONS---------------------------------------- #
def load_image():
    im = Image.open("test_img.png")
    return im


def save_image(im):
    im.save("outfile.png", "PNG")

# ------------------------------SET UP UI---------------------------------------- #

window = Tk()
window.title("Image Watermarker")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

add_image_button = Button(text="Select Image", command=load_image)
add_image_button.grid(row=0, column=0)

window.mainloop()
