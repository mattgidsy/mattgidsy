import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#goal image size: 1200x750
#my image size: 1200x675
#add25px for height each at height 225
# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')


# #Fonty business
# fntht = 75
# fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", fntht)
# d = ImageDraw.Draw(image)
# d.text((0,225),"channel testeroni", fill=(255,255,255), font=fnt)


display(image)

#make of an image with additional height for the info text
def tall_copies(image:image, copies:int, add_ht:int) -> list:
    tall_images=[]
    for i in range(copies):
        tall_img = PIL.Image.new(image.mode, (image.width, image.height+add_ht))
        tall_img.paste(image, (0,0))
        tall_images.append(tall_img)
    return(tall_images)
    
tall_images = tall_copies(image,9,75)


    

def colorchannel(channel:int, img_list:list) -> list:
    color_channel_lst = []
    intensity = [0.1,0.5,0.9]
    c = intensity
    #Fonty business
    fntht = 75
    fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", fntht)
    if channel == 0:
        for i in [0,1,2]:
            d = ImageDraw.Draw(img_list[i])
            d.text((0,451),f"channel {channel} testeroni {c[i]}", fill=(255,255,255), font=fnt)
            matrix = ( c[i], 0, 0, 0,
                          0, 1, 0, 0,
                          0, 0, 1, 0)

            color_channel_lst.append(img_list[i].convert('RGB',matrix))
        return color_channel_lst
    
    elif channel == 1:
        for i in [0,1,2]:
            d = ImageDraw.Draw(img_list[i])
            d.text((0,451),f"channel {channel} testeroni {c[i]}", fill=(255,255,255), font=fnt)
            matrix = ( 1, 0, 0, 0,
                       0, c[1], 0, 0,
                       0, 0, 1, 0)

            color_channel_lst.append(img_list[i].convert('RGB',matrix))
            
        return color_channel_lst

    elif channel == 2:
        for i in [0,1,2]:
            d = ImageDraw.Draw(img_list[i])
            d.text((0,451),f"channel {channel} testeroni {c[i]}", fill=(255,255,255), font=fnt)
            matrix = ( 1, 0, 0, 0,
                       0, 1, 0, 0,
                       0, 0, c[i], 0)
            color_channel_lst.append(img_list[i].convert('RGB',matrix))
        return color_channel_lst

color_images =[]
for i in [0,1,2]:
    color_images += colorchannel(i,tall_images)


#color_images = colorchannel(0)+colorchannel(1)+colorchannel(2)


# create a contact sheet from different brightnesses
# first_image=images[0]
first_image = color_images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,(first_image.height)*3))
x=0
y=0

# for img in images:
for img in color_images:
    
#     #Fonty business
#     fntht = 75
#     fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", fntht)
#     d = ImageDraw.Draw(img)
#     d.text((0,0),"channel testeroni", fill=(255,255,255), font=fnt)

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