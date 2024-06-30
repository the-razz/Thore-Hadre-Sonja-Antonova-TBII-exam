#### Thore-Hadre-Sofya-Antonova-TBII-exam

# Sharing is Caring
###
#### Come and share with us!
This is an application that aims to provide a platform
for the act of sharing your stuff online. We appreciate
the presence of strong communities that want to share their
resources among each other. However, we believe that the current
platforms are lacking some features to make the process of sharing easy
and convenient for everyone.
That is why we produced this application. We hope it marks a step into
the right direction, as have the telegram sharing is caring
group chats.
####
For the realisation of the app the libraries tkinter, pandas and pillow were used
exclusively.

#### Getting started
You will have to run this app in a virtual python environment such as venv
or conda.

For Windows:
* ``python -m venv dev``
* ``.\dev\Scripts\activate``

For Mac:
* ``virtualenv -p python dev``
* ``source dev/bin/activate``

Then you will have to install the following libraries:
* ``pip freeze``
* ``pip install pandas``
* ``pip install pillow``
* ``python sharing-is-caring.py``

### Important notes 

When launching the app, a greeting window is displayed, and it can lead to a bug
where the user is not able to click into the entry boxes on the login page.
This is fixed by clicking out of the window onto your desktop or any other window
and then clicking back into the gui. Or you can click the login button, click okay
on the pop up error message, that appears because of the empty user name field,
and then you will be able to click into the entry box.
####
Currently, it can appear that the main page is not always showing a post when opened.
This is easily resolved by clicking the "next" or "previous" buttons in the GUI. 
Then a post will be properly displayed.
####
Also, the app is not yet launched online and thus the chat function is rather a
demonstration and does not offer a fully fledged chat, that allows receiving and
responding to messages.