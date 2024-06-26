import tkinter as tk
from tkinter import messagebox
#import modules as needed
from tkinter import *
# try importing numpy to fix the import pandas as pd issue
import pandas as pd
from PIL import Image, ImageTk

# set root to make it easier to code and read the tkinter commands
root = tk.Tk()

# title the window
root.title("Food Sharing")

# variable for the minimum size f the window, portrait format for smartphone application
screen_width = 720
screen_height = 1080

i=-1

def user_check():
    # check if user exists

    # check if user exists
    # on_bad_lines='skip' resolves issues that arise in the csv file when writing to_csv
    user_ids = list(pd.read_csv("data/users_data.csv", sep=',', on_bad_lines='skip').user_id)
    # if user exists - go to a new page, for instance
    if user_id.get() in user_ids:
        main_page()
    # otherwise give error
    else:
        tk.messagebox.showwarning("Warning!!", "Please register as a new user")

    # if user exists - go to a new page, for instance
    #if user_id and user_password in user_ids:
      #  clear_widgets(root)
    # otherwise give error
    #else:
       # tk.messagebox.showwarning("Warning!!", "Please register as a new user")

# this function reads out the information from item_info.csv and uses them to display the item on the main page
# it creates a list of tuples that stores each row from the csv and then makes each entry from that list individually
# accessible
def item_name_retrieve_function():
    global item_info_tuples_list

    # read out the whole content of the csv file item_info and store it as a dataframe
    item_info_data_frame = pd.read_csv("data/item_info.csv", sep=',', on_bad_lines='skip', header=0)

    # create a variable that requests individual entries from the DataFrame using iloc
    #individual_entry_from_dataframe = item_info_data_frame['current_user_id'].iloc[0]
    #print(individual_entry_from_dataframe)

    # create a list that stores the value tuples taken from item_info_data_frame
    item_info_tuples_list = []

    # create a for loop that stores each row of information in a list that can be used to display the items later
    # use iterrows method of pandas to iterate over the rows of the dataframe
    #for index, row in item_info_data_frame.iterrows():
    for index, row in item_info_data_frame.iterrows():
        # append the values from the cells to the list as tuples
        item_info_tuples_list.append((row['current_user_id'], row['image_path'], row['item_description']))

    # a for loop that accesses each row in the tuples list and makes it accesible for the next function to use
    # the range(len(tuples_list)) is required to make sure the iteration continues for number of rows only i.e. the number of tuples
    # this is necessary because a list with tuples for some reason cannot be iterated >:(
    for i in range(len(item_info_tuples_list)):
       # print the message for testing purposes
       #print(item_info_tuples_list[i][0] + " posted " + item_info_tuples_list[i][1] + " with the following image " + item_info_tuples_list[i][2])
       i == i+1
# to realise the list that was created within the function
item_name_retrieve_function()

# create function for simplified image imports
def add_image(root, file_path, width, height):
    """This definition will place the image on the gui window.
    You need to specify the variable name that creates your gui window and the image file path"""

    # for some reason this image will not appear without specifying global variables
    global pic, f1

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image - make sure this is the same size as the gui window
   # img = img.resize()
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()

def clear_widgets():

    #loops through all widgets that were created so far and kills them
    for i in root.winfo_children():
        i.destroy()

# create a flexible button that brings the user back to where they just came from
#last_page_name must be entered without parenthesis at the end: main_page, login_page
def back_to_last_page_button(last_page_name):
    #create a button that displays the text back to last page and leads to the page specified in the code
    back_to_last_page_button = tk.Button(root,
                                         text='Back to last page',
                                         command=last_page_name)
    back_to_last_page_button.place(relx=0.5, rely=0.84, width=100, anchor=tk.CENTER)

def login_page():
    global user_id, user_password, entered_user_data

    # destroy the current gui page
    clear_widgets()

    #user_id = ("Flynn")

    add_image(root, "images/login.png", screen_width, screen_height)

    # ask for username
    username_label = tk.Label(root,
                              text="Enter your username:")
    username_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    # enter a name
    user_id = tk.StringVar()
    user_id_entry = tk.Entry(root,
                          textvar=user_id)
    user_id_entry.place(relx=0.5, rely=0.3, width=100, anchor=tk.CENTER)

    # ask for password
    user_password_label = tk.Label(root,
                              text="Enter your password:")
    user_password_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    # enter a password
    user_password = tk.StringVar()
    user_password_entry = tk.Entry(root,
                              textvar=user_password)
    user_password_entry.place(relx=0.5, rely=0.5, width=100, anchor=tk.CENTER)


    entered_user_data = [user_id, user_password]

    # check if the entered user data exists in the users_dat.csv file
    # create a login button
    login = tk.Button(root,
                      text='Login',
                      command=user_check)
    login.place(relx=0.5, rely=0.84, width=110, anchor=tk.CENTER)

    new_user_button = tk.Button(root,
                                text='Create a new user',
                                command=new_user_page)
    new_user_button.place(relx=0.5, rely=0.9, width=110, anchor=tk.CENTER)

#create a funciton that submits the input user information to the data base, when creating an account
def submit_user_data():

    #read out the contents of the csv file and store them in a variable
    user_ids = list(pd.read_csv("data/users_data.csv", sep=',', on_bad_lines='skip').user_id)

    #check if the user_id i.e. the user name is already present
    #if not submit the userdata to the data base
    if new_user_id.get() not in user_ids:
        # combine the user_id and user_password into a dictionary that is turned into a data frame
        # the variables are placed as lists
        user_data = pd.DataFrame({"User ID": [new_user_id.get()],
                     "User Password": [new_user_password.get()]
                     })

        #convert the dictionary into a data frame that can be added to the csv file which is also a data frame
        #user_data = pd.DataFrame([user_data])


        #append the data frame user_data to the csv file
        user_data.to_csv("data/users_data.csv", index=False, mode='a', header=False)

        return

    # if the username is present in the csv file warn the user to choose another usermane
    else:
        tk.messagebox.showwarning("This username already exists")

def new_user_page():
    # global new user data to make it available to the submit function
    global new_user_id, new_user_password

    clear_widgets()

    new_username_label = tk.Label(root,
                              text="Enter your desired username:")
    new_username_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    # enter a name
    new_user_id = tk.StringVar()
    new_user_id_entry = tk.Entry(root,
                             textvar=new_user_id)
    new_user_id_entry.place(relx=0.5, rely=0.3, width=100, anchor=tk.CENTER)

    # ask for password
    new_user_password_label = tk.Label(root,
                                   text="Enter your password:")
    new_user_password_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    # enter a password
    new_user_password = tk.StringVar()
    new_user_password_entry = tk.Entry(root,
                                   textvar=new_user_password)
    new_user_password_entry.place(relx=0.5, rely=0.5, width=100, anchor=tk.CENTER)


    #create a submit button that executes the submit_user_data function defined above
    submit_button = tk.Button(root,
                              text="Submit",
                              command=submit_user_data)
    submit_button.place(relx=0.5, rely=0.75, width=100, anchor=tk.CENTER)

    ### create a function that submits the entered data to the database, after checking if the username is still available###

    back_to_last_page_button(login_page)

def chat_page():
    #clear all widgets
    clear_widgets()

    add_image(root,"images/food-screen.png", screen_width, screen_height)

    # create a custom back button that is also functioning the same way as the previous button from the main page
    # to make sure the user does go back to exactly where they came from when clicking on the item
    back_button = tk.Button(root,
                            text='Back to last page',
                            command=lambda: [test_item_button.destroy(), item_description_label.destroy(), display_individual_post_function(False),
                                             main_page()])
    back_button.place(relx=0.5, rely=0.84, width=100, anchor=tk.CENTER)


#define a function that allows the currently logged in user to submit a new item to the main page
def submit_new_item_function(image_path, current_user_id, item_description):
    # the variables are placed as lists
    # current_user_id does not need .get() because it was already transferred to a string in the main_page() function
    item_data = pd.DataFrame({"Current User ID": [current_user_id],
                              "Image File Path": [image_path.get()],
                              "Item Description": [item_description.get()]
                              })

    # convert the dictionary into a data frame that can be added to the csv file which is also a data frame
    # user_data = pd.DataFrame([user_data])

    # append the data frame user_data to the csv file
    item_data.to_csv("data/item_info.csv", index=False, mode='a', header=False)

# create a new page that allows users to submit new items to offer in the app
def item_submit_page():
    global submit
    #submit_boolean()
    clear_widgets()

    image_file_path_label = tk.Label(root,
                                           text='Please enter the file path for your image',
                                           ).place(relx=0.5, rely=0.2, width=250, anchor=tk.CENTER)

    image_path = tk.StringVar()

    image_file_path_entry = tk.Entry(root,
                                           textvar=image_path).place(relx=0.5, rely=0.25, width=100, anchor=tk.CENTER)

    enter_item_description_label = tk.Label(root,
                                            text='Please enter an item description').place(relx=0.5, rely=0.4, width=250, anchor=tk.CENTER)

    item_description = tk.StringVar()

    item_description_entry = tk.Entry(root,
                                      textvar=item_description).place(relx=0.5, rely=0.45, width=100, anchor=tk.CENTER)

    # lambda allows the function executed in command to have expressions
    # the button executes the submit_new_item_function with the information submitted and the user name retrieved from login
    submit_button = tk.Button(root,
                              text='Submit Item',
                              command=lambda: submit_new_item_function(image_path, current_user_id, item_description))

    submit_button.place(relx=0.5, rely=0.6, width=100, anchor=tk.CENTER)

    back_to_last_page_button(main_page)

# create a function that can display a description and an image and item as a button using a filepath from the database
# as the filepath comes from the tuples list, it can be iterated and the value of i can be used to display the desired
# image and description
def display_image_as_button_function(i):
    # these variables need to go global so that they can be destroyed in the main_page function to make space for a new
    # image to be displayed
    global test_item_button, item_description_label

    if i < len(item_info_tuples_list):
        print('all good')
        # retrieve the item descriptions from the list and display it as a label
        # the same i value can be used for image and description as they are stored in the same tuple in the list
        item_description = item_info_tuples_list[i][2]
        # retrieve the user id from the list, also here i selects the correct row that matches the description and the image
        user_id = item_info_tuples_list[i][0]
        display_text = user_id + ' posted: ' + item_description
        item_description_label = tk.Label(root,
                                          text=display_text)
        item_description_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        # use pillow image to read out the jpg using the tuples list that stores the rows from item_info.csv
        # here i is the selector for the tuple that stores one row of data from the table
        pillow_image = Image.open(item_info_tuples_list[i][1])
        # .size method to get the actual dimensions of the image that is being read out
        width, height = pillow_image.size
        # resize image with pillow, use round to keep the pixel value as an integer
        resized_pillow_image = pillow_image.resize((round(width / 3), round(height / 3)))
        # define a variable that makes the image accessible for tkinter with PhotoImage method
        tkinter_image = ImageTk.PhotoImage(resized_pillow_image)

        # create a button that is a clickable image
        test_item_button = tk.Button(root,
                                     image=tkinter_image,
                                     command=lambda: [chat_page()])
        # store the image with .photo method to avoid the image being lost
        test_item_button.photo = tkinter_image
        test_item_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



# a function that calls the display image as a button function and skips either forward or backward depending on the
# user input from the main_page function
def display_individual_post_function(a=None):
    # global i so it can be used in other functions
    global i
    # if the argument passed in the function is True increment i+1 and show the next post from the database
    if a == True:
        i += 1
        display_image_as_button_function(i)
    # if the argument passed is not True, decrement i-1 and show the previous post
    else:
        i -= 1
        display_image_as_button_function(i)

# define a function for the main page
def main_page():
    global current_user_id
    # destroy the current gui page
    clear_widgets()

    # display the background image
    add_image(root, "images/mainscreen.png", screen_width, screen_height)

    # call the display individual post function one time to show the first post
    # without the need to click the next button first
    display_individual_post_function(1)
    print(i)
    show_next_image_button = tk.Button(root,
                                       text='next',
                                       command=lambda:[test_item_button.destroy(), item_description_label.destroy(), display_individual_post_function(True)])
    show_next_image_button.place(relx=0.75, rely=0.6, width=100, anchor=tk.CENTER)
    show_previous_image_button = tk.Button(root,
                                       text='previous',
                                       command=lambda:[test_item_button.destroy(), item_description_label.destroy(), display_individual_post_function(False)])
    show_previous_image_button.place(relx=0.25, rely=0.6, width=100, anchor=tk.CENTER)
        #image_label = tk.Label(root,
     #                      image=tkinter_image).place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    #image_path = "images/photo_1_2024-05-27_15-59-53.jpg"
    # create a submit a new item button
    submit_new_item_button = tk.Button(root,
                                       text="Insert a new item",
                                       command=item_submit_page).place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    # get the user_id that was used to login, so it can be displayed in the welcome message below
    current_user_id = user_id.get()

    username_label_var = tk.StringVar()
    username_label_var.set("Hi! You are logged in as " + current_user_id)

    username_label = tk.Label(root,
                              textvariable=username_label_var)
    username_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # create a logout button, that leads back to login page
    logout = tk.Button(root,
                       text='Logout',
                       command=login_page)
    logout.place(relx=0.5, rely=0.9, width=100, anchor=tk.CENTER)

#
#    # place the Label that holds the image, relwidth, relheight ensures that the image is taking up the whole screen
#    background.place(x=0, y=0, relwidth=1, relheight=1)

    #clothes_page_button = tk.Button(root,
     #                          text="Returning User",
      #                         command=clothes_page)
   # clothes_page_button.pack()
    return

#initalise the gui manually to avoid circular referencing
login_page()

# set the minimum size of the window to the variables defined above
#root.minsize(screen_width, screen_height)
# keep the tkinter looping through so that the application keeps running and the window stays open
root.mainloop()
