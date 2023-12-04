from PIL import Image
from entities import User

is_logged_out = True
user = None
while is_logged_out:
    print("to sign up enter 1")
    print("to login enter 2")
    option = input()
    if option == "1":
        signup()
    elif option = "2":
        user = login()

file_name =input("enter file path to image here: ")
img_obj = Image.open(file_name)
pixel_map = img_obj.load()
length, breadth = img_obj.size

for i in range(length):
    for j in range(breadth):
        r, g, b = img_obj.getpixel((i,j))
        pixel_map[i,j] = (255-r, 255-g, 255-b)


img_obj.save("output", format="png")
user.files_list.add(new app_image(file_name))

def login():
    user_name = input("enter your username please: ")
    password = input("enter your password please: ")
    if User.users_dict.get(user_name) != None:
        if User.users_dict[user_name] == password:
            is_logged_out = False
    return User.users_dict[user_name]       

def signup():
    user_name = input("enter your username please: ")
    email = input("enter your email please: ")
    password = input("enter your password please: ")
    user = new User(user_name, email, password)