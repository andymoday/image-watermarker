from tkinter import *
from tkinter import ttk, filedialog
import time
from tkinter.messagebox import showinfo

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


def open_file_dialog(filetypes, type):
    if type == "image":
        message = "Choose an Image"
    elif type == "watermark":
        message = "Choose a Watermark"

    filename = filedialog.askopenfilename(
        title=message,
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    return filename


def load_image():
    filetypes = (
        ('PNG files', '*.png'),
        ('JPEG files', '*.jpg'),
        ('All files', '*.*')
    )
    filename = open_file_dialog(filetypes, type="image")
    im = Image.open(filename)
    print(im.format)
    return im


def load_watermark():
    filetypes = (
        ('PNG files', '*.png'),
        ('All files', '*.*')
    )
    watermark = open_file_dialog(filetypes, type="watermark")
    wm = Image.open(watermark)
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
window.config(padx=110, pady=110, bg=BACKGROUND_COLOR)
window.geometry("300x300")
add_image_button = ttk.Button(text="Select Image", command=image_controller)
add_image_button.grid(row=0, column=0)
add_image_button.pack()

window.mainloop()
