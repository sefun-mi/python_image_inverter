from PIL import Image

image_list = []
file_name ="eren.jpg"                         #input("enter file path to image here: ")
img_obj = Image.open(file_name)
length, breadth = img_obj.size

for i in range(0,length):
    for j in range(0,breadth):

        
image_list.append(file_name)
print(image_list[0])