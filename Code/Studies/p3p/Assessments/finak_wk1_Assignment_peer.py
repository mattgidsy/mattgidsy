
#this is the work of my peer, They almost did it perfectly and I would like to use this approach but fix their mistake. 
import PIL
from PIL import Image
from PIL import ImageEnhance

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[]
for i in range(1, 10):
    images.append(enhancer.enhance(i/10))

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)

import PIL
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
intensitySteps = [0.1, 0.5, 0.9]  #intensity level of colors
colorChannels = [0, 1, 2] #color channels 0 = red, 1 = green, 2 = blue)
fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", 40)

images = [] # a list for holding the result images

for channel in colorChannels:
    for intensity in intensitySteps:
        # create a copy of the original image to be worked on
        workImage = image.copy()
        # create the text of the channel and the intensity
        infoText = "channel {}  intensity {}".format(channel, intensity)
        
        #create a text box at the bottom of the image
        txtImage = ImageDraw.Draw(workImage, "RGB")
        txtImage.rectangle((0, 400, 800, 450), fill=(0, 0, 0))
        txtImage.text((10,410), infoText, font=fnt, fill=(255, 255, 255))

        # seperate the image into red, green, and blue
        red = workImage.getchannel(0)
        green = workImage.getchannel(1)
        blue = workImage.getchannel(2)
        
        # change the intensity based on the current channel
        if (channel == 0):
            enhancer = ImageEnhance.Brightness(red)
            red = enhancer.enhance(intensity)
        elif (channel == 1):
            enhancer = ImageEnhance.Brightness(green)
            green = enhancer.enhance(intensity)
        elif (channel == 2):
            enhancer = ImageEnhance.Brightness(blue)
            blue = enhancer.enhance(intensity)
            
        # create the final image by merging back the red, green, and blue
        # and then append it to the images list
        images.append(Image.merge ('RGB', (red, green, blue))) 

# create a contact sheet from different channels and intensities
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)        

