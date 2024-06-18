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