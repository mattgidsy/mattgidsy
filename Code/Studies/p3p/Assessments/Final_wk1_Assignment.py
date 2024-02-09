import PIL
from PIL import Image, ImageDraw, ImageFont

#make an image with additional height for the info text
def get_tall_copies(image:image, copies:int, add_ht:int) -> list:
    tall_images=[]
    for i in range(copies):
        tall_img = PIL.Image.new(image.mode, (image.width, image.height+add_ht))
        tall_img.paste(image, (0,0))
        tall_images.append(tall_img)
    return(tall_images)
    

#adjusts color channels and adds text description of those adjustments
def colorchannel(channel:int, img_list:list, intensity:list, fnt_ht:int, txt_ht:int, fnt:object ) -> list:
    color_channel_lst = []
    
    if channel == 0:
        im=0
        for i in intensity:
            d = ImageDraw.Draw(img_list[im])
            d.text((0,txt_ht),f"channel {channel} intensity {i}", fill=(255,255,255), font=fnt)
            matrix = ( i, 0, 0, 0,
                       0, 1, 0, 0,
                       0, 0, 1, 0)

            color_channel_lst.append(img_list[im].convert('RGB',matrix))
            im+=1  
        return color_channel_lst
    
    elif channel == 1:
        im=3
        for i in intensity:
            d = ImageDraw.Draw(img_list[im])
            d.text((0,txt_ht),f"channel {channel} intensity {i}", fill=(255,255,255), font=fnt)
            matrix = ( 1, 0, 0, 0,
                       0, i, 0, 0,
                       0, 0, 1, 0)

            color_channel_lst.append(img_list[im].convert('RGB',matrix))
            im+=1   
        return color_channel_lst

    elif channel == 2:
        im=6
        for i in intensity:
            d = ImageDraw.Draw(img_list[im])
            d.text((0,txt_ht),f"channel {channel} intensity {i}", fill=(255,255,255), font=fnt)
            matrix = ( 1, 0, 0, 0,
                       0, 1, 0, 0,
                       0, 0, i, 0)
            
            color_channel_lst.append(img_list[im].convert('RGB',matrix))
            im+=1
        return color_channel_lst
    
#combines 3 lists of 3 different color channels
def get_color_images(img_list:list, color_intensities:list,fnt_ht:int, txt_ht:int, fnt:object) ->list:
    color_images = []
    
    for i in [0,1,2]:
        color_images += colorchannel(i,img_list,color_intensities, fnt_ht, txt_ht, fnt)
    return color_images

#creates a contact sheet from the colored image list
def create_contact_sheet(img_list:list) ->object:
    first_image = img_list[0]
    contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,(first_image.height)*3))
    x=0
    y=0
    for img in img_list:
        contact_sheet.paste(img, (x, y) ) #pastes each image into the contact sheet
        if x+first_image.width == contact_sheet.width:  #positional data for the paste
            x=0
            y=y+first_image.height

        else:
            x=x+first_image.width

    # resize the contact sheet
    contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
    return contact_sheet

#### Configuration ####
image=Image.open("readonly/msi_recruitment.gif") #open the assigned image
image=image.convert('RGB') #convert to RGB for manipulation
color_intensities = [0.1,0.5,0.9] #assignment required intensities 0.1, 0.5, 0.9
fnt_ht = 50  #assignment font height 50
txt_ht = 460 #assignment text height position 460
var_num = 9 #assignment number of variations 9
fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", fnt_ht) #assignment font
add_ht = fnt_ht #add height equal to font height

#### Program ####
tall_images = get_tall_copies(image,var_num,add_ht)
color_images = get_color_images(tall_images, color_intensities, fnt_ht, txt_ht, fnt)
contact_sheet = create_contact_sheet(color_images)
display(contact_sheet)