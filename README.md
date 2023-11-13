# Python-GUI-Application

The project is a standalone desktop application to plot excel data on charts. This was my first attempt at creating a GUI application.

[![Python][python]](#)
[![Pandas][pandas]](#)
[![Matplotlib][matplotlib]](#)


## Description

The UI of the application is written in python using the library tkinter. 

The pandas library was used to read data from the excel sheet and store it in a data frame. This simplifies the process of building a graph using the matplotlib library. 

Four types of graphs are available:
1. Histogram 
2. Boxplot 
3. Bar
4. Scatter

## Built with

The following technologies were used for development:
1. [Pandas](https://pandas.pydata.org/) - library for data manipulation and analysis
2. [Matplotlib](https://matplotlib.org/) - libary for plotting data

## Getting Started
For building and running the application you need:

- [Python 3.11.4](https://www.python.org/downloads/release/python-3114/) or higher

### Running the application locally

Create a new virtual environment for the project. Install the dependencies given in the  `requirements.txt` file using the following command: 
```
pip install -r requirements.txt
```

Execute the python script using the following command:
```shell
python GUI_Graph_portal.py
```


## Author

Daanish Shaikh - [@github](https://github.com/DaanishShk)\
repo link - [Python-GUI-Application](https://github.com/DaanishShk/Python-GUI-Application)


## License

This project is licensed under the MIT License.



[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black



<!-- that comes pre-installed with the
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
of the outcome. -->