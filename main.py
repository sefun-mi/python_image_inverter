from PIL import Image

                                              #image_list = []
file_name =input("enter file path to image here: ")
img_obj = Image.open(file_name)
pixel_map = img_obj.load()
length, breadth = img_obj.size

for i in range(length):
    for j in range(breadth):
        r, g, b = img_obj.getpixel((i,j))
        pixel_map[i,j] = (255-r, 255-g, 255-b)


img_obj.save("output", format="png")
                                                #image_list.append(file_name)
                                                #print(image_list[0])