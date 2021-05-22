# Python-GUI-Application
This was my first attempt at creating a desktop GUI application using the tkinter library in python.

The project is a standalone desktop application.
The UI of the application is written in python using
the library tkinter that comes pre-installed with the
latest version of python. The code required to
implement menus, dialog boxes, buttons and widgets
was added to the program by importing the
respective classes from the tkinter library.


A function mini_window() was created to make
the process of adding new windows to the main
window simpler and hence requiring less space for
the code. The values passed to the function include
description, image path and position of the window
with respect to the top.


The size of the main window is kept locked to
avoid any scaling issues. The main window can be
scrolled vertically to view the windows out of bounds
of the current position. The top bar contains a drop
down menu for help, author info and an open drop
down to edit the data stored in the excel sheet used to
build the graphs.


Each window is created using mini_window. It
contains a relevant description for the task performed
when the button contained in it is clicked. Upon
clicking the button a corresponding function is called
within the same python script which carries out the
given task to display a relevant graph for analysis. A
picture is present next to the text to give a clearer idea
of the outcome.


The pandas library was used to read data from the
excel sheet and store it in a data frame. This
simplifies the process of building a graph using the
matplotlib library. Four types of graphs are available,
namely histogram, boxplot, bar and scatter graphs.
Their use depends on the dataset being that is being
studied. 
