from tkinter import *
import time
from PIL import Image, ImageChops

BACKGROUND_COLOR = "#456456"


# ------------------------------FUNCTIONS---------------------------------------- #
def image_controller():
    image = load_image()
    watermark = load_watermark()
    im_size = image.size
    wm_size = watermark.size
    h_pos = int((im_size[0] / 2) - (wm_size[0] / 2))
    v_pos = int((im_size[1] / 2) - (wm_size[1] / 2))
    image.paste(watermark, (h_pos, v_pos), watermark.convert("RGBA"))
    time.sleep(2)
    save_image(image)


def load_image():
    im = Image.open("test_img.png")
    print(im.format)
    return im


def load_watermark():
    wm = Image.open("watermark.png")
    wm = wm.convert("RGBA")
    wm_data = wm.getdata()

    new_data = []
    for item in wm_data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    wm.putdata(new_data)
    return wm


def save_image(im):
    im.save("outfile.png", "PNG")


# ------------------------------SET UP UI---------------------------------------- #

window = Tk()
window.title("Image Watermarker")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

add_image_button = Button(text="Select Image", command=image_controller)
add_image_button.grid(row=0, column=0)

window.mainloop()
