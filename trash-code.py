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
