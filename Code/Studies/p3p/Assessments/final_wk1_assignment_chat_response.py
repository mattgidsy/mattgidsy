from PIL import Image, ImageDraw, ImageFont

# Function to read image and convert to RGB
def read_and_convert_image(filepath):
    return Image.open(filepath).convert('RGB')

# Function to create an image with additional height for the info text
def get_tall_copies(image, copies, add_ht):
    tall_images = []
    for _ in range(copies):
        tall_img = Image.new(image.mode, (image.width, image.height + add_ht))
        tall_img.paste(image, (0, 0))
        tall_images.append(tall_img)
    return tall_images

# Function to adjust color channels and add text description of those adjustments
def colorchannel(channel, img_list, intensity, fntht, txtht):
    fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", fntht)
    color_channel_lst = []
    for i, img in enumerate(img_list):
        d = ImageDraw.Draw(img)
        d.text((10, txtht), f"Channel {channel} intensity {intensity[i]}", fill=(255,255,255), font=fnt)
        matrix = [1 if j % 5 == 0 else 0 for j in range(12)]
        matrix[channel * 4] = intensity[i]
        color_channel_lst.append(img.convert('RGB', tuple(matrix)))
    return color_channel_lst

# Function to combine lists of different color channels
def get_color_images(image, copies, add_ht):
    tall_images = get_tall_copies(image, copies * 3, add_ht)  # Make copies for all adjustments
    color_images = []
    intensity = [0.1, 0.5, 0.9]
    fntht, txtht = 20, image.height  # Adjust font size and text height as needed
    for channel in range(3):
        color_images.extend(colorchannel(channel, tall_images[channel*3:(channel+1)*3], intensity, fntht, txtht))
    return color_images

# Function to create a contact sheet from the colored image list
def create_contact_sheet(img_list):
    if not img_list: return None
    first_image = img_list[0]
    contact_sheet = Image.new(first_image.mode, (first_image.width * 3, first_image.height * len(img_list) // 3))
    x = y = 0
    for img in img_list:
        contact_sheet.paste(img, (x, y))
        x += first_image.width
        if x >= contact_sheet.width:
            x = 0
            y += first_image.height
    contact_sheet = contact_sheet.resize((contact_sheet.width // 2, contact_sheet.height // 2))
    return contact_sheet

# Main execution
image_path = "readonly/msi_recruitment.gif"
image = read_and_convert_image(image_path)
color_images = get_color_images(image, 3, 50)  # Adjust the number of copies and additional height as needed
contact_sheet = create_contact_sheet(color_images)
contact_sheet.show()

####
# this doesn't work correctly #