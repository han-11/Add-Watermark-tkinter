from tkinter import *
# import file dialog to open the image
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.withdraw()
file_name = filedialog.askopenfilename(
    initialdir='/Users/serenawang/Documents/100DaysofPython/day-84-water marker app GUI')
print(file_name)


def add_watermark(image):
    '''Create an image object from an image'''
    img = Image.open(image)
    img_width, img_height = img.size

    draw = ImageDraw.Draw(img)
    text = "some watermark"

    '''Create font of the watermark'''
    font = ImageFont.truetype('Arial.ttf', 36)
    text_width, text_height = draw.textsize(text, font)

    ''' Calculate the coordinates of the watermark'''
    margin = 100
    x = img_width - text_width - margin
    y = img_height - text_height - margin

    ''' Create watermark in the bottom at right corner'''
    draw.text((x, y), text, font=font)
    img.show()

    img.save(
        f'/Users/serenawang/Documents/100DaysofPython/watermarked{image}.jpg')


add_watermark(file_name)
