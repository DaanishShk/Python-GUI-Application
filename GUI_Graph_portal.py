from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
import os

import pandas as pd

# import numpy as np
import matplotlib.pyplot as plt


# import matplotlib.patches as patches
# import matplotlib.path as path


def help():
    messagebox.showinfo('Help', '1.In the Open drop down select Excel File\n\n2.Paste the data into '
                                'the excel sheet\n\n3.Save and execute graph')


def author():
    messagebox.showinfo('Author', '    Mohammad Daanish Shaikh   \n\n    Roll no. 42  \n\n    F.Y. B.Tech')


def excel():
    os.startfile('Test.xlsx')


def histogram():
    # fig, ax = plt.subplots()
    #
    # # histogram our data with numpy
    # data = np.random.randn(1000)
    # n, bins = np.histogram(data, 50)
    #
    # # get the corners of the rectangles for the histogram
    # left = np.array(bins[:-1])
    # right = np.array(bins[1:])
    # bottom = np.zeros(len(left))
    # top = bottom + n
    #
    # # we need a (numrects x numsides x 2) numpy array for the path helper
    # # function to build a compound path
    # XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
    #
    # # get the Path object
    # barpath = path.Path.make_compound_path_from_polys(XY)
    #
    # # make a patch out of it
    # patch = patches.PathPatch(barpath)
    # ax.add_patch(patch)
    #
    # # update the view limits
    # ax.set_xlim(left[0], right[-1])
    # ax.set_ylim(bottom.min(), top.max())

    df = pd.read_excel('Test.xlsx', na_values='Missing')
    df.index = range(1, df.shape[0] + 1)
    header=df.columns.ravel()
    for i in range(df.shape[1]):
        df.iloc[:, i].plot.hist()
        plt.title(header[i])
        plt.subplots()
    plt.show()

def bar():
    # n_means=5
    # means_men = (20, 35, 30, 35, 27)
    # std_men = (2, 3, 4, 1, 2)
    #
    # means_women = (25, 32, 34, 20, 25)
    # std_women = (3, 5, 2, 3, 3)

    # fig, ax = plt.subplots()    #To create multiple graphs in same rectangle

    # index = np.arange(n_mean)  # array range
    # bar_width = 0.35
    #
    # opacity = 0.4
    # error_config = {'ecolor': '0.3'}

    # rects1 = plt.bar(index, means_men, bar_width,
    #                  alpha=opacity,
    #                  color='b',
    #                  yerr=std_men,
    #                  error_kw=error_config,
    #                  label='Men')
    #
    # rects2 = plt.bar(index + bar_width, means_women, bar_width,
    #                  alpha=opacity,
    #                  color='r',
    #                  yerr=std_women,
    #                  error_kw=error_config,
    #                  label='Women')


    df = pd.read_excel('Test.xlsx', na_values='Missing')
    df.index = range(1, df.shape[0] + 1)
    df.plot.bar()  # df.iloc[:,0].plot.bar()
    plt.xlabel('Group')
    plt.ylabel('Values')
    plt.title('Values by group with subcatogories')
    # plt.xticks(index + bar_width / 2, ('A', 'B', 'C', 'D', 'E'))
    plt.legend()
    # plt.tight_layout()
    plt.show()


def box_plot():
    # fake up some data
    # spread = np.random.rand(50) * 100
    # center = np.ones(25) * 50
    # flier_high = np.random.rand(10) * 100 + 100
    # flier_low = np.random.rand(10) * -100
    # data = np.concatenate((spread, center, flier_high, flier_low), 0)
    # plt.boxplot(data)
    # plt.show()

    df = pd.read_excel('Test.xlsx', na_values='Missing')
    df.index = range(1, df.shape[0] + 1)
    df.plot.box()
    plt.show()


def scatter():
    # N = 50
    # x = np.random.rand(N)
    # y = np.random.rand(N)
    # colors = np.random.rand(N)
    # area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radii

    df = pd.read_excel('Test.xlsx', na_values='Missing')
    df.index = range(1, df.shape[0] + 1)
    header = df.columns.ravel()
    df.plot.scatter(x=header[0], y=header[1])
    plt.show()


def arrange_text(s):
    s = wrap(s, 68)
    return '\n'.join([i.ljust(70) for i in s])


image_list = []


def mini_window(s, n, f):
    frame = Canvas(canvas, bg='white', width=Width, height=Height)
    label = ttk.Label(frame, font=('Bahnschrift', 12), text=arrange_text(s), compound=RIGHT)
    # do not use image over here as once control is transfered outside the function image is forgotten
    label.place(relx=0.01, rely=0.02, relwidth=0.82, relheight=0.95)
    button = ttk.Button(frame, text='Produce Graph')
    button.place(relx=0.84, rely=0.4, relheight=0.2, relwidth=0.15)
    # Have to use create_window to let canvas display embedded frame
    canvas.create_window(483, (n - 1) * 475 + 290, window=frame)
    image = PhotoImage(file=f)
    label['image'] = image
    image_list.append(image)
    return button


Height = 400
Width = 925
main = Tk()
main.title('')
main.geometry('1000x600')
main.resizable(0, 0)
# To make window static in size


canvas = Canvas(main, bg='#D8FAF8', height=Height, width=Width, scrollregion=(0, 0, 2000, 2000))
# Scrollregion is required as canvas is infinite
canvas.place(relwidth=1, relheight=1)
# Provides more control regarding placement than pack

ftitle = LabelFrame(bg='#D8FAF8')
# frame used to make title overlap mini windows and prevent them from covering it
title = Label(ftitle, text='Data Science Portal', font=('ISOCTEUR', 28, 'bold'), bg='#FAF7F7', relief='groove')
title.pack(fill=BOTH)
ftitle.place(relx=0.5, rely=0.03, relwidth=0.55, relheight=0.08, anchor='n')


b = mini_window('A histogram is a graphical method of displaying quantitative data, similar '
                'to a box plot or stem and leaf plot. A histogram displays the single quantitative '
                'variable along the x axis and frequency of that variable on the y axis.', 1, 'Hist.png')
b['command'] = histogram
b = mini_window(
    'A bar chart or bar graph is a chart or graph that presents categorical data with rectangular bars with '
    'heights or lengths proportional to the values that they represent. The bars can be plotted vertically '
    'or horizontally. A vertical bar chart is sometimes called a column chart.', 2, 'bar.png')
b['command'] = bar
b = mini_window('Boxplots are a standardized way of displaying the distribution of data based on a five number summary '
                '(“minimum”, first quartile (Q1), median, third quartile (Q3), and “maximum”).', 3, 'Box_plot.png')
b['command'] = box_plot
b = mini_window('A scatter plot (aka scatter chart, scatter graph) uses dots to represent values for two different '
                'numeric variables. The position of each dot on the horizontal and vertical axis indicates values for '
                'an individual data point. Scatter plots are used to observe relationships between variables.', 4,
                'scatter.png')
b['command'] = scatter
# Important to avoid overlapping with widgets outside of the canvas boundary


scroll = Scrollbar(canvas)
# Parent of any widget has to be defined before hand
scroll.pack(fill=Y, side=RIGHT)
# Using pack() is the most straightforward  approach for scrollbars
canvas.configure(yscrollcommand=scroll.set)
# Configure has been used here as before scroll was not defined hence throwing error
scroll.config(command=canvas.yview)

menu = Menu(main)
About = Menu(menu, tearoff=0)
About.add_command(label='Help', command=help)
About.add_separator()
About.add_command(label='Author', command=author)
menu.add_cascade(label='About', menu=About)
Open = Menu(menu, tearoff=0)
Open.add_cascade(label='Excel File', command=excel)
menu.add_cascade(label='Open', menu=Open)

main.config(menu=menu)

main.mainloop()

# pack method causing scaling issues in create_window canvasses
