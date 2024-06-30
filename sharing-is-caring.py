'''
This is an application for sharing items with other people on the platform.
It features a login and registration interface as well as a chat interface.
The main page shows items submitted by other users. The user can click on each item,
which opens a chat page to the corresponding user.
'''

requirements_message = '''
You will have to run Python in a virtual environment with following dependencies:
pip install pandas
pip install PIL
'''
print(requirements_message)

import tkinter as tk
from tkinter import messagebox, Tk, Frame, Canvas
#import modules as needed
from tkinter import *
import pandas as pd
from PIL import Image, ImageTk

# variable for the minimum size f the window, portrait format for smartphone application
screen_width = 720
screen_height = 1080
# set root to make it easier to code and read the tkinter commands
root = tk.Tk()

# title the window
root.title("Food Sharing")

# define the colours for the design
light_green='#236966'
dark_green='#124222'
violet='#A99ACA'
blue='#2375B9'
teal='#226D88'

# define a font
font1='Helvetica'

# set the minimum size of the window to the variables defined above
root.minsize(round(screen_width*1.2), round(screen_height*0.8))

# i=-1 to initialise the function that displays the individual posts in the main_page
i=-1

# define a function that checks whether the input user data from the login page is present in the dater base
# and load the main_page when the check is correct
def user_check():
    # create a list that stores the user_id column from the users_data.csv file
    user_ids = list(pd.read_csv("data/users_data.csv", sep=',', on_bad_lines='skip').user_id)
    # if the user input string is present in the list open the main_page() function
    if user_id.get() in user_ids:
        # clear the widgets of the login_page()
        clear_widgets()
        main_page()
        # call the display individual post function to reset the counter to -1 so that when a user logs in for the second
        # time using the app without restarting, they are not shown an empty page
        display_individual_post_function(False)
    # otherwise give error
    else:
        tk.messagebox.showwarning("Warning!!", "Please register as a new user")

# this function reads out the information from item_info.csv and uses them to display the item on the main page
# it creates a list of tuples that stores each row from the csv and then makes each entry from that list individually
# accessible
def item_name_retrieve_function():
    # the list must be global so that the tuples stored in the list can be accessed by other functions
    global item_info_tuples_list

    # read out the whole content of the csv file item_info and store it as a dataframe
    item_info_data_frame = pd.read_csv("data/item_info.csv", sep=',', on_bad_lines='skip', header=0)

    # create a list that stores the value tuples taken from item_info_data_frame data frame
    item_info_tuples_list = []

    # create a for loop that stores each row of information in a list that can be used to display the items later
    # use iterrows method of pandas to iterate over the rows of the dataframe
    # taken from https://stackoverflow.com/questions/16476924/how-can-i-iterate-over-rows-in-a-pandas-dataframe
    for index, row in item_info_data_frame.iterrows():
        # append the values from the cells to the list as tuples
        item_info_tuples_list.append((row['current_user_id'], row['image_path'], row['item_description']))

# create function for simplified image imports
# this function was taken from Sarah Haq
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

# this functions destroys the current gui and all its widgets to make space for a new page
# this function was taken from Sarah Haq
def clear_widgets():
    #loops through all widgets that were created so far and kills them
    for e in root.winfo_children():
        e.destroy()

# create a flexible button that brings the user back to where they just came from
# last_page_name must be entered without parenthesis at the end: main_page, login_page
def back_to_last_page_button(last_page_name):
    # create a button that displays the text back to last page and leads to the page specified in the code
    back_to_last_page_button = tk.Button(root,
                                         text='Back to last page',
                                         command=last_page_name,
                                         font=font1)
    back_to_last_page_button.place(relx=0.5, rely=0.84, anchor=tk.CENTER)

# the login page allow the user to enter their credentials or go to the registration page
def login_page():
    # global the entered user data so they can be used in the user check
    global user_id, user_password, entered_user_data
    # destroy the current gui page
    clear_widgets()

    # set the background colour of the window
    root.config(bg=dark_green)
    # display the logo of the app
    add_image(root, "images/logo_dark_green.png", 270, 205)

    # ask for username
    username_label = tk.Label(root,
                              text="Enter your username:",
                              bg=light_green,
                              fg='white',
                              font=font1)
    username_label.place(relx=0.5, y=270, width=200, anchor=tk.CENTER)

    # let the user enter a name
    user_id = tk.StringVar()
    user_id_entry = tk.Entry(root,
                          textvar=user_id,
                             font=font1)
    user_id_entry.place(relx=0.5, y=300, width=200, anchor=tk.CENTER)

    # ask for password
    user_password_label = tk.Label(root,
                              text="Enter your password:",
                              bg=light_green,
                              fg='white',
                              font=font1)
    user_password_label.place(relx=0.5, y=350, width=200, anchor=tk.CENTER)

    # let the user enter a password
    user_password = tk.StringVar()
    user_password_entry = tk.Entry(root,
                              textvar=user_password,
                                   font=font1)
    user_password_entry.place(relx=0.5, y=380, width=200, anchor=tk.CENTER)

    # make a list that stores the entered user data
    entered_user_data = [user_id, user_password]

    # check if the entered user data exists in the users_dat.csv file
    # create a login button
    login = tk.Button(root,
                      text='Login',
                      command=lambda:[user_check()],
                              bg='white',
                              fg='DodgerBlue',
                      font=font1)
    login.place(relx=0.5, y=440, width=200, anchor=tk.CENTER)

    # create a button that leads to the registration page
    new_user_button = tk.Button(root,
                                text='Create a new user',
                                command=new_user_page,
                              bg=light_green,
                              fg='white',
                                font=font1)
    new_user_button.place(relx=0.5, y=490, width=200, anchor=tk.CENTER)

#create a funciton that submits the input user information to the data base, when creating an account
def submit_user_data():

    #read out the contents of the csv file and store them in a list
    user_ids = list(pd.read_csv("data/users_data.csv", sep=',', on_bad_lines='skip').user_id)

    #check if the user_id i.e. the user name is already present
    #if not submit the userdata to the data base
    if new_user_id.get() not in user_ids:
        # combine the user_id and user_password into a dictionary that is turned into a data frame
        # the variables are placed as lists
        user_data = pd.DataFrame({"User ID": [new_user_id.get()],
                     "User Password": [new_user_password.get()]
                     })

        #append the data frame user_data to the csv file
        user_data.to_csv("data/users_data.csv", index=False, mode='a', header=False)
        return

    # if the username is present in the csv file warn the user to choose another usermane
    else:
        tk.messagebox.showwarning("This username already exists")

#  create a page that allow the new users to register and create a new account
def new_user_page():
    # global new user data to make it available to the submit function
    global new_user_id, new_user_password

    clear_widgets()

    # change the background color of the page
    root.config(bg=light_green)
    # display the logo of the app
    add_image(root, "images/logo_light_green.png", 270, 205)

    # ask for a username
    new_username_label = tk.Label(root,
                              text="Choose a username:",
                                  font=font1,
                                  bg=teal,
                                  fg='white')
    new_username_label.place(relx=0.5, y=270, width=200, anchor=tk.CENTER)

    # define a variable that can store the changing input from the entry field
    new_user_id = tk.StringVar()
    # let the new user pick  a name
    new_user_id_entry = tk.Entry(root,
                             textvar=new_user_id,
                                  font=font1)
    new_user_id_entry.place(relx=0.5, y=300, width=200, anchor=tk.CENTER)

    # ask for password
    new_user_password_label = tk.Label(root,
                                   text="Choose password:",
                                  font=font1,
                                  bg=teal,
                                  fg='white')
    new_user_password_label.place(relx=0.5, y=350, width=200, anchor=tk.CENTER)

    # define a variable that can store the changing input from the entry field
    new_user_password = tk.StringVar()
    # let the new user enter a password
    new_user_password_entry = tk.Entry(root,
                                   textvar=new_user_password,
                                  font=font1)
    new_user_password_entry.place(relx=0.5, y=380, width=200, anchor=tk.CENTER)

    #create a submit button that executes the submit_user_data function defined above
    submit_button = tk.Button(root,
                              text="Submit and go to login",
                              command=lambda:[submit_user_data(), login_page()],
                              font=font1,
                                  bg='white',
                                  fg='DodgerBlue')
    submit_button.place(relx=0.5, y=440, width=210, anchor=tk.CENTER)

    # the back button leads back to the log in page
    back_button = tk.Button(root,
                              text="Go back to last page",
                              command=lambda:login_page(),
                              font=font1,
                              bg=teal,
                              fg='white')
    back_button.place(relx=0.5, y=490, width=210, anchor=tk.CENTER)

# the main design function calls sets the background color of each page and the corresponding logo image and it also
# displays the currently logged in users name with the correctly colored background on the top of each page
# background_color is the actual hex code of the color, and color name is the name of the color that corresponds to the
# file name of the logo_color.png
def main_design_function(background_color, color_name):
    # global the logged in user's name for other fuctions to use
    global current_user_id

    # get the path of the image with the color that was passed in the color_name argument
    logo_image_path = f'images/logo_{color_name}.png'

    # change the window to the background_color passed in the function
    root.config(bg=background_color)
    # display the logo of the app with the color dependent file name
    add_image(root, logo_image_path,270, 205)

    # get the user_id that was used to login, so it can be displayed in the welcome message below
    current_user_id = user_id.get()

    # create a string variable that can store dynamic values to be displayed
    username_label_var = tk.StringVar()
    # use the .set method to display the text without any unwanted brackets
    # taken from https://www.askpython.com/python-modules/tkinter/stringvar-with-examples
    username_label_var.set("Hi! You are logged in as " + current_user_id)

    # display the message
    username_label = tk.Label(root,
                              textvariable=username_label_var,
                              font=font1,
                              bg=background_color,
                              fg='white')
    username_label.place(relx=0.5, y=30, anchor=tk.CENTER)

# a function that stores the entered messages from the csv into a csv file when the submit button is pressed
def submit_message_function(submitted_message):

    # get the input message from the entry box in the submit button on the chat page
    # transform the message, the current user, and the receiver into a data frame
    submitted_message_data_frame = pd.DataFrame({"submitter_id": [current_user_id],
                     "submitter_message": [submitted_message],
                     "message_receiver": [item_info_tuples_list[i][0]]
                     })

    # append the data frame as a csv file
    submitted_message_data_frame.to_csv("data/chat_data.csv", index=False, mode='a', header=False)

# a function that reads out chat_data.csv and stores the information as a tuples list
def retrieve_chat_message_function():
    # global the list so that the information can be used in other functions
    global chat_data_tuples_list

    # read out the whole content of the csv file chat_data and store it as a dataframe
    chat_data_data_frame = pd.read_csv("data/chat_data.csv", sep=',', on_bad_lines='skip', header=None)

    # create a list that stores the value tuples taken from chat_data_data_frame
    chat_data_tuples_list = []

    # create a for loop that stores each row of information in a list that can be used to display the items later
    # use iterrows method of pandas to iterate over the rows of the dataframe
    # taken from https://stackoverflow.com/questions/16476924/how-can-i-iterate-over-rows-in-a-pandas-dataframe
    for index, row in chat_data_data_frame.iterrows():
        # append the values from the cells to the list as tuples
        chat_data_tuples_list.append((row[0], row[1], row[2]))

    # retrieve the name of the person whose chat page is currently open
    # i is selecting the right tuple from the list because it is the corresponding number to the item that the user
    # clicked on before
    item_poster = item_info_tuples_list[i][0]

    # initalising a new iteration variable for the while loop to follow
    d = 0
    # a while loop that loops until the message receiver function is found in the item_info_tuples_list
    # so, it checks whether the person that is currently being chatted with is the receiver of a message that is stored
    # in the chat_data.csv table
    while d < len(chat_data_tuples_list):
        # retrieve each username from the list that reads out the data from the csv file
        message_receiver = chat_data_tuples_list[d][2]
        if item_poster == message_receiver:
            # if two identical names are found the correct name is stored as a variable and the while loop breaks
            current_chat_partner = message_receiver

            # if the user who posted the item and a message in chat data csv are the same --> display the message
            if current_chat_partner == chat_data_tuples_list[d][2]:
                # establish True to initiate the while loop running
                True
                while True:
                    # let the corresponding message be read out from the list and displayed as a text box
                    display_message_text = current_chat_partner + " received the message: " + "\'" + \
                                           chat_data_tuples_list[d][
                                               1] + "\'"
                    # place the text box
                    text_box.insert('end', display_message_text)
                    # increment d +1 to progress the iteration over the messages
                    d += 1
                    # break the loop to display the message once
                    break
                # increment by one to avoid an endless loop of loading the same usernames
                d += 1
                # break again to stop the loop and let the rest of program load
                break
        # increment d by one for each iteration of the loop
        d += 1


# a page that display the text that were reteived in the function above and als offers an interface for users to
# submit their own messages
def chat_page():
    # text box needs to be global for other functions to be refreshed
    global text_box
    #clear all widgets
    clear_widgets()

    # set the design with thte main design function
    main_design_function(background_color=violet, color_name='violet')

    # create the text box
    text_box = tk.Text(root,
                       width=60,
                       bg=violet,
                       fg='white',
                       font=font1
                       )
    text_box.place(x=0, rely=0.35, relwidth=1, relheight=0.5)  # these attributes ensure it takes up the entire screen

    # create a scrollbar for the textbox
    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=0.9, relx=0.974)

    entry_box = tk.Entry(root,
                         font=font1
                         )
    entry_box.place(x=5, rely=0.825, relwidth=0.6, height=30)

    # a send button that submits the messag from the entry box
    send_button = tk.Button(root,
                            text="Send",
                            command=lambda: [submit_message_function(entry_box.get()),
                                             retrieve_chat_message_function()],
                            width=10,
                            font=font1)

    send_button.place(relx=0.77, rely=0.825)

    # run the retrieve message function to load the list that is being created in the function
    retrieve_chat_message_function()

    # create a custom back button that is also functioning the same way as the previous button from the main page
    # to make sure the user does go back to exactly where they came from when clicking on the item
    back_button = tk.Button(root,
                            text='Back to last page',
                            command=lambda: [main_page()],
                            font=font1)
    back_button.place(relx=0.5, rely=0.925, width=200, anchor=tk.CENTER)

    # display the name of the user that is being chatted with
    username_label_var = tk.StringVar()
    # the username that is being chatted with is in the same position in item info csv as the curerntly displayed item
    # that the user clicked on for the chat so i can b used to get the corresponding name from the tuples list
    username_label_var.set("Chat with: " + item_info_tuples_list[i][0])

    username_label = tk.Label(root,
                              textvariable=username_label_var,
                              font=font1
                              )
    username_label.place(relx=0.5, y=270, anchor=tk.CENTER)

#define a function that allows the currently logged in user to submit a new item to the main page
def submit_new_item_function(image_path, current_user_id, item_description):
    # createa a new data frame from the needed information
    # current_user_id does not need .get() because it was already transferred to a string in the main_page() function
    item_data = pd.DataFrame({"Current User ID": [current_user_id],
                              "Image File Path": [image_path.get()],
                              "Item Description": [item_description.get()]
                              })

    # append the data frame user_data to the csv file
    item_data.to_csv("data/item_info.csv", index=False, mode='a', header=False)

    # display a message that thanks the user for sharing a new item
    tk.messagebox.showinfo("Sharing successful", "Thank you for sharing!!! And always remember: SHARING IS CARING")

# create a new page that allows users to submit new items to offer in the app
def item_submit_page():
    clear_widgets()

    main_design_function(background_color=blue, color_name='blue')

    image_file_path_label = tk.Label(root,
                                           text='Please enter the file path for your image',
                                           font=font1,
                                        bg="DarkBlue",
                                        fg="white",
                                           ).place(relx=0.5, y=270, anchor=tk.CENTER)

    image_path = tk.StringVar()
    image_file_path_entry = tk.Entry(root,
                                           textvar=image_path,
                                           font=font1,
                                     ).place(relx=0.5, y=300, width=400, anchor=tk.CENTER)

    enter_item_description_label = tk.Label(root,
                                            text='Please enter an item description',
                                           font=font1,
                                        bg="DarkBlue",
                                        fg="white",
                                            ).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    item_description = tk.StringVar()
    item_description_entry = tk.Entry(root,
                                      textvar=item_description,
                                           font=font1,
                                      ).place(relx=0.5, rely=0.535, width=400, anchor=tk.CENTER)

    # lambda allows the function executed in command to have expressions
    # the button executes the submit_new_item_function with the information submitted and the user name retrieved from login
    submit_button = tk.Button(root,
                              text='Submit Item',
                              command=lambda: submit_new_item_function(image_path, current_user_id, item_description),
                              font=font1,
                              bg="white",
                              fg="DodgerBlue",
                              )
    submit_button.place(relx=0.5, rely=0.7, width=200, anchor=tk.CENTER)

    # create a custom back button that is also functioning the same way as the previous button from the main page
    # to make sure the user does go back to exactly where they came from when clicking on the item
    back_button = tk.Button(root,
                            text='Back to last page',
                            command=lambda: main_page(),
                                        font=font1,
                                        bg="DarkBlue",
                                        fg="white",)
    back_button.place(relx=0.5, rely=0.85, width=200, anchor=tk.CENTER)

# create a function that can display a description and an image and item as a button using a filepath from the database
# as the filepath comes from the tuples list, it can be iterated and the value of i can be used to display the desired
# image and description
def display_image_as_button_function(i):
    # these variables need to go global so that they can be destroyed in the main_page function to make space for a new
    # image to be displayed
    global test_item_button, item_description_box

    # if i is smaller than the length of the list of items it means an item with the number of i can be  displayed
    # taken from https://stackoverflow.com/questions/3685974/iterate-a-certain-number-of-times-without-storing-the-iteration-number-anywhere
    if i < len(item_info_tuples_list):
        i = int(i)
        # use pillow image to read out the jpg using the tuples list that stores the rows from item_info.csv
        # here i is the selector for the tuple that stores one row of data from the table
        file_path = item_info_tuples_list[i][1]
        pillow_image = Image.open(file_path)
        # .size method to get the actual dimensions of the image that is being read out
        # taken from https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil
        width, height = pillow_image.size
        # resize image with pillow, use round to keep the pixel value as an integer
        resized_pillow_image = pillow_image.resize((round(width / 3), round(height / 3)))
        # define a variable that makes the image accessible for tkinter with PhotoImage method
        tkinter_image = ImageTk.PhotoImage(resized_pillow_image)

        # create a button that is a clickable image
        # taken from https://stackoverflow.com/questions/62502791/how-to-add-image-in-a-button
        test_item_button = tk.Button(root,
                                     image=tkinter_image,
                                     command=lambda: [chat_page()],
                                     text=None)
        # store the image with .photo method to avoid the image being lost
        test_item_button.photo = tkinter_image
        test_item_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # retrieve the item descriptions from the list and display it as a label
        # the same i value can be used for image and description as they are stored in the same tuple in the list
        item_description = item_info_tuples_list[i][2]
        # retrieve the user id from the list,
        # also here i selects the correct row that matches the description and the image
        user_id = item_info_tuples_list[i][0]
        display_text = user_id + ' posted: ' + item_description
        item_description_box = tk.Text(root,
                                       width=60,
                                       bg='DodgerBlue',
                                       fg='white',
                                       font=font1
                                       )
        item_description_box.place(relx=0.5, rely=0.725, width=400, height=100, anchor=tk.CENTER)

        # add the text to the text box
        item_description_box.insert('end', display_text)

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
    elif a == False:
        i -= 1
        display_image_as_button_function(i)

def destroy_old_image_button_function():
    test_item_button.destroy()
    item_description_box.destroy()

# define a function for the main page
def main_page():
    # destroy the current gui page
    clear_widgets()

    main_design_function(background_color=blue, color_name='blue')

    # recall the item name retrieve function to update the item info csv table in case new items were added
    item_name_retrieve_function()

    # create a logout button, that leads back to login page
    logout = tk.Button(root,
                       text='Logout',
                       command=login_page,
                       font=font1,
                       bg='DodgerBlue',
                       fg='white')
    logout.place(relx=0.5, rely=0.9, width=200, anchor=tk.CENTER)

    # create a submit a new item button
    submit_new_item_button = tk.Button(root,
                                       text="Insert a new item",
                                       command=item_submit_page,
                                       font=font1,
                                       bg='DodgerBlue',
                                       fg='white')
    submit_new_item_button.place(relx=0.5, rely=0.85, width=200, anchor=tk.CENTER)

    # creat a button that skips to the next post
    show_next_image_button = tk.Button(root,
                                       text='next',
                                       command=lambda:[destroy_old_image_button_function(), display_individual_post_function(True)],
                                       font=font1,
                                           bg='DodgerBlue',
                                           fg='white')
    show_next_image_button.place(relx=0.85, rely=0.6, width=150, anchor=tk.CENTER)
    # create a button that skips to the previous post
    show_previous_image_button = tk.Button(root,
                                       text='previous',
                                       command=lambda:[destroy_old_image_button_function(), display_individual_post_function(False)],
                                       font=font1,
                                           bg='DodgerBlue',
                                           fg='white')
    show_previous_image_button.place(relx=0.15, rely=0.6, width=150, anchor=tk.CENTER)
    return

#main_design_function(background_color=dark_green, color_name='dark_green')
# to realise the list that was created within the function
item_name_retrieve_function()

# initialise the variables in the display individual post function
display_individual_post_function(True)

#initalise the gui manually to avoid circular referencing
login_page()

# this message pops up when the app is launched. It greets the new user and introduces the sharing is caring app
starting_message = '''
Hi! Welcome to the Sharing is Caring app! Please register or sign in first.

This app is a platform for non-commercial exchange. Help the environment by giving away things that would otherwise go to waste.

Exchange goods and have fun :)
    '''
messagebox.showinfo("WELCOME!", starting_message)

# keep the tkinter looping through so that the application keeps running and the window stays open
root.mainloop()
