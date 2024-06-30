#users_data = pd.read_csv("data/users_data.csv")
    #user_ids = users_data.values.tolist()
    #print(user_ids)
    #user_password = list(pd.read_csv("data/users_data.csv").user_password)
  #  for Tuples in user_ids:
 #       print(Tuples)
#
     #   for elements in Tuples:
    #        #print(elements, end=' ')
   #         #if new_variable in elements:
  #           #   print("main_page")
 #       else:
#            print("Error when checking username")


# use pillow image to read out the jpg
# pillow_image = Image.open(image_path.get())
# resize image with pillow
# resized_pillow_image = pillow_image.resize((100, 200))
# define a variable that reads out an image with PhotoImage method
# tkinter_image = ImageTk.PhotoImage(resized_pillow_image)
# create a button that is a clickeable image
# test_item_button = tk.Button(root,
#                            text=current_user_id+" posted: "+item_description,
#                           image=tkinter_image,
#                          command=chat_page).place(relx=0.5, rely=0.3, width=200, height=100, anchor=tk.CENTER)



#create a mechanism that allows the submit process to happen
    #submit = False
    submit = False
    #define a function that can set submit to True
    def submit_boolean():
        global submit
        submit = True
    # if the button is pressed commit the changes to the database
    if submit is True:
        # submit_new_item(image_path, current_user_id, item_description)
        print(image_path)
        print(item_description)
        print("harmless testing message from your beloved item_submit_page() function :33")
        # submit = False



Flynn,images/cursed-lasagna.jpg,"This is a very cursed Lasagna with colgate taste, but I swear it will be the most delicious Lasagna you'll ever try!!!!"
Felix,images/food-screen.png,"Hey, this is just a home screen of my food page, sorry to bother you with kind of random, unrelated content"
 ,data/cursed-lasagna.jpg,again the very cursed lasagna
 ,images/cursed-lasagna.jpg,once more this is the cursed lasagne
Flynn,images/cursed-lasagna.jpg,ye yeslasagna lasagne cursed cursed
Flynn,images/cursed-lasagna.jpg,AAAnd again the same lasagna
Felix,images/cursed-lasagna.jpg,Hey this is Felix I also have a cursed lasagna to offer
 ,images/cursed-lasagna.jpg,what the hell another cursed lasagna
 ,,
 ,images/cursed-lasagna.jpg,not a cursed lasagna
 ,,
 ,images/cursed-lasagna,also not a cursed lasagna
 ,images/cursed-lasagna.jpg,"No, I will not enter an Item description!!!!"



item_data.to_csv("data/item_info.csv", index=True, mode='a', header=['current_user_id', 'image_path', 'item_description'])


# individual_entry_from_dataframe = item_info_data_frame[index].iloc[row]


        #print(row['current_user_id'], row['image_path'], row['item_description'])
        #return individual_entry_from_dataframe

# print(individual_entry_from_dataframe)


# separate the dataframe into variables that hold the separate columns
current_user_id_column = item_info_data_frame.current_user_id
image_path_column = item_info_data_frame.image_path
item_info_column = item_info_data_frame.item_description


# create individual lists for each item column data to be stored
    item_info_user_ids_list = []
item_info_user_ids_list.append(row['current_user_id'])

new_variable = "Flynn"


#print(item_info_user_ids_list)
    #print(item_info_tuples_list[0][0] + " posted " + item_info_tuples_list[0][2] + " with the following image " + item_info_tuples_list[0][1])

#cread out all the entries in the item_info.csv table
    #all_item_info = list(pd.read_csv("data/item_info.csv", sep=',', on_bad_lines='skip'))
#print(all_item_info)

# tkinter_image = add_image(root, "images/photo_3_2024-05-27_15-59-53.jpg", 10, 20)

#image_label = tk.Label(root,
     #                      image=tkinter_image).place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    #image_path = "images/photo_1_2024-05-27_15-59-53.jpg"

#
#    # place the Label that holds the image, relwidth, relheight ensures that the image is taking up the whole screen
#    background.place(x=0, y=0, relwidth=1, relheight=1)

    #clothes_page_button = tk.Button(root,
     #                          text="Returning User",
      #                         command=clothes_page)
   # clothes_page_button.pack()


for i in range(len(chat_data_tuples_list)):
    # print the message for testing purposes
    # print(item_info_tuples_list[i][0] + " posted " + item_info_tuples_list[i][1] + " with the following image " + item_info_tuples_list[i][2])
    print(chat_data_tuples_list[i][0] + " texted " + chat_data_tuples_list[i][1] + " to " + chat_data_tuples_list[i][2])
    i == i + 1
    meta_list = [chat_data_tuples_list[i][0], chat_data_tuples_list[i][1], chat_data_tuples_list[i][2]]

message_receiver = meta_list[2]


#user_id = ("Flynn")

    #add_image(root, "images/login.png", screen_width, screen_height)


elif i <= -1 * (len(item_info_tuples_list)):
i = 1 - len(item_info_tuples_list)

# call the display individual post function one time to show the first post
# without the need to click the next button first
# display_individual_post_function(1)

display_message_label = tk.Label(root,
                                            text=display_message_text,
                                            )
            display_message_label.place(relx=0.6, rely=0.3 + (c / 20), anchor=tk.CENTER)


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
            break
        # increment d by one for each iteration of the loop
        d += 1

    #if item_poster in chat_data_tuples_list[][2]

    if current_chat_partner == chat_data_tuples_list[d][2]:
        True
        c = 0
        while True:
            display_message_text = current_chat_partner + " received the message: " + "\'" + chat_data_tuples_list[d][
                1] + "\'"

            text_box.insert('end', display_message_text)
            c += 1
            print('yeah yeah')
            d += 1
            break
        d += 1


, display_individual_post_function(False)

# get the user_id that was used to login, so it can be displayed in the welcome message below
current_user_id = user_id.get()

username_label_var = tk.StringVar()
username_label_var.set("Hi! You are logged in as " + current_user_id)

username_label = tk.Label(root,
                          textvariable=username_label_var,
                          font=font1)
username_label.place(relx=0.5, y=30, width=200, anchor=tk.CENTER)


, relwidth=width+0.1, relheight=height+0.1,

item_description_label = tk.Label(root,
                                          text=display_text,
                                          font=font1)
        item_description_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# a for loop that accesses each row in the tuples list and makes it accesible for the next function to use
    # the range(len(tuples_list)) is required to make sure the iteration continues for number of rows only i.e. the number of tuples
    # this is necessary because a list with tuples for some reason cannot be iterated >:(
    for i in range(len(item_info_tuples_list)):
       # print the message for testing purposes
       #print(item_info_tuples_list[i][0] + " posted " + item_info_tuples_list[i][1] + " with the following image " + item_info_tuples_list[i][2])
       i == i+1


# convert the dictionary into a data frame that can be added to the csv file which is also a data frame
# user_data = pd.DataFrame([user_data])

# if item_poster in chat_data_tuples_list[][2]

# elif statement to avoid i being larger than the number of items in the list
    elif i > len(item_info_tuples_list):
        i = round(len(item_info_tuples_list)-1)
        display_individual_post_function(i)
