from PIL import Image, ImageDraw, ImageFont
import zipfile
import pytesseract
import cv2 as cv
import numpy as np
import math

## Functions ## 
#get a list of all the names of the files in the zip archive
def znamelist (zfile: str)-> list:
    with zipfile.ZipFile(zfile, "r") as archive: 
        # Get list of file names in ZIP file 
        file_names = archive.namelist() 
    return file_names

#iterate through all the files in the zip archive and display them
def show_zip_photos (zfile: str, search_str:str):
    file_names = znamelist(zfile)
    for file_name in file_names:
        with zipfile.ZipFile(zfile) as smallzip:
            with smallzip.open(file_name) as img:
                image = Image.open(img)
                image.show()


#search the image string for the search string                        
def str_search(image, search_str):
    im = Image.open(image)
    imstr = pytesseract.image_to_string(im)
    if search_str in imstr:
        return True
    else:
        return False
    
#search image and extract faces
def face_search(image,image_data) ->list:
    face_list = []
    pil_img = Image.open(image)
    #must decode image from image data as cv doesn't read images like pil
    cv_img_color = cv.imdecode(np.frombuffer(image_data, np.uint8), 1)
    cv_img_bw = cv.cvtColor(cv_img_color, cv.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(cv_img_bw,1.20,8)
    
    #iterate through the faces array of rectangle coordinates and crop the faces out
    for rec in faces:
        pil_rec = [rec[0], rec[1], rec[0]+rec[2], rec[1]+rec[3]] #convert from opencv rectangle format to PIL draw rectangle format
        face = pil_img.crop(pil_rec)
        face.thumbnail(max_size)
        face_list.append(face)
    return face_list

#create a contact sheet of all faces on a page that match the search query
def create_pg_sheet(file_name:str, img_list:list) -> object:
    base_img_ht, base_img_wt = max_size
    x_offset = 0
    y_offset = 0
    txt_ht = 18
    fnt = ImageFont.truetype("readonly/fanwood-webfont.ttf", txt_ht)
    rows = math.ceil(len(img_list) / 5)
    total_ht = base_img_ht * rows
    
    if len(img_list) > 0:
        #creat header sheet
        pg_header = Image.new("RGB",(base_img_wt*5,txt_ht),(255,255,255))
        header_draw = ImageDraw.Draw(pg_header)
        header_draw.text((0,0),f"Results found in file {file_name}",fill=(0,0,0),font=fnt)
        #create a new contact sheet image
        pg_face_sheet = Image.new("RGB",(base_img_wt*5, total_ht))
        for img in img_list:
            pg_face_sheet.paste(img,(x_offset,y_offset))
            if x_offset + base_img_wt == pg_face_sheet.width:
                x_offset =0
                y_offset += base_img_ht
            else:
                x_offset += base_img_wt
        # pg_face_sheet.show()    
        pg_sheet = Image.new("RGB",(pg_header.width, pg_header.height + pg_face_sheet.height ))
        pg_sheet.paste(pg_header,(0,0))
        pg_sheet.paste(pg_face_sheet,(0,pg_header.height))
        
    else:
        pg_sheet = Image.new("RGB",(base_img_ht*5,txt_ht*2),(255,255,255))
        header_draw = ImageDraw.Draw(pg_sheet)
        header_draw.text((0,0),f"Results found in file {file_name} \nBut there were no faces in that file!",fill=(0,0,0),font=fnt)

    return pg_sheet

#combine all individual page results
def create_result_sheet(pg_img_list:list) -> object:
    total_ht = 0
    for img in pg_img_list:
        total_ht += img.height
    result_img = Image.new("RGB",(pg_img_list[0].width +20 , total_ht),(255,255,255))
    total_ht = 0
    for img in pg_img_list:
        result_img.paste(img,(10,total_ht))
        total_ht += img.height
    return result_img

#search images for text for the search_str search string
def tesseract_face_search(zfile: str,  search_str:str):
    file_names = znamelist(zfile)
    pg_results = []
    for file_name in file_names:
        with zipfile.ZipFile(zfile) as smallzip:
            image = smallzip.open(file_name)
            image_data = smallzip.read(file_name)
            result = str_search(image, search_str)
            if result == True:
                print(f"{file_name} contains your query: {search_str}")
                faces = face_search(image,image_data)
                pg_result = create_pg_sheet(file_name, faces)
                pg_results.append(pg_result)
                print(f"faces found in {file_name}: {len(faces)}")
                
            else:
                print(f"{file_name} does not contain your query: {search_str}")
    search_results = create_result_sheet(pg_results)
    search_results.show() #display(search_results) #for jupyter notebook
   
 
## Configuration ##
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')  # loading the face detection classifier
test_zip = 'readonly/small_img.zip'
hero_zip = 'readonly/images.zip'
test_str = 'Christopher'
search_str = 'Mark'
max_size = (100,100)

## Program ##
tesseract_face_search(hero_zip, search_str)
#tesseract_face_search(test_zip, test_str)



## helpful tools ##
# with zipfile.ZipFile(test_zip) as archive: 
#     archive.printdir()
#show_zip_photos(test_zip, search_str)
#tesseract_test(test_zip)
#face_search()


    


