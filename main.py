from tkinter import *
from tkinter import ttk, filedialog
import time
from tkinter.messagebox import showinfo

from PIL import Image, ImageChops

BACKGROUND_COLOR = "#456456"


# ------------------------------FUNCTIONS---------------------------------------- #
def image_controller():
    images = load_image()
    watermark = load_watermark()
    wm_size = watermark.size
    for image in images:
        im_size = image.size
        h_pos = int((im_size[0] / 2) - (wm_size[0] / 2))
        v_pos = int((im_size[1] / 2) - (wm_size[1] / 2))
        image.paste(watermark, (h_pos, v_pos), watermark.convert("RGBA"))
        time.sleep(1)
    save_images(images)


def load_image():
    filetypes = (
        ('PNG files', '*.png'),
        ('JPEG files', '*.jpg'),
        ('All files', '*.*')
    )
    filenames = filedialog.askopenfilenames(
        title="Choose Images",
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
    ims = []
    for im in filenames:
        image = Image.open(im)
        print(image.format)
        ims.append(image)
    return ims


def load_watermark():
    filetypes = (
        ('PNG files', '*.png'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(
        title="Choose Watermark",
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filename
    )
    wm = Image.open(filename)
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


def save_images(ims):
    filetypes = (
        ('PNG files', '*.png'),
        ('All files', '*.*')
    )
    for im in ims:
        filename = filedialog.asksaveasfilename(
            title="Save Image As:",
            initialdir='/',
            filetypes=filetypes,
            defaultextension=".png",
            initialfile=f"{im.filename}-watermarked")

        showinfo(
            title='Saved Files',
            message=filename
        )

        im.save(filename, im.format)


# ------------------------------SET UP UI---------------------------------------- #

window = Tk()
window.title("Image Watermarker")
window.config(padx=105, pady=105, bg=BACKGROUND_COLOR)
window.geometry("300x300")
add_image_button = ttk.Button(text="Select Images", command=image_controller)
add_image_button.grid(row=0, column=0)
add_image_button.pack()

window.mainloop()
