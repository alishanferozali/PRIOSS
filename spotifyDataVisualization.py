import tkinter as tk
from tkinter import *
from tkinter import Tk,Canvas,Frame,Scrollbar,BOTH, messagebox,Label,Button,ttk,W,E
import os, json
import pandas as pd
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import textwrap
def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=0)
try:
    matplotlib.use('TkAgg')
    def UserData():
        f = open('Userdata.json',"r")
        data = json.load(f)
        checker = ""
        if isinstance(data,list):
            checker = "list"
        else:
            checker = "dict"

        getNames = []
        if checker == "list":
            for i in data:
                getNames.append(i["username"])
        else:
            getNames.append(data["username"])
        # print(getNames)

        root = Tk()
        root.title('Spotify Data Visualization')
        root.geometry("900x600")
        root.configure(bg='green')

        def on_canvas_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def scroll_start(event):
            canvas.scan_mark(event.x, event.y)

        def scroll_move(event):
            canvas.scan_dragto(event.x, event.y, gain=1)

        # Create a canvas for scrolling
        canvas = Canvas(root, bg='green')

        # Create a frame inside the canvas which will hold your content
        frame = Frame(canvas, bg='green')

        def _on_mouse_wheel(event):
            if isinstance(event.widget, str):  # String because it does not have an actual reference
                if event.widget.endswith('.!combobox.popdown.f.l'):  # If it is the listbox
                    return 'break'

            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")  # Else scroll the canvas
            frame.event_generate('<Escape>')  # Close combobox

        def dontscroll(e):
            return "dontscroll"

        def on_enter(e):
            frame.bind_all("<MouseWheel>", dontscroll)

        def on_leave(e):
            frame.bind_all("<MouseWheel>", _on_mouse_wheel)

        frame.event_generate('<Escape>')

        frame.bind_class('Listbox', '<Enter>',
                         on_enter)
        frame.bind_class('Listbox', '<Leave>',
                         on_leave)
        canvas.pack(side='left', fill=BOTH, expand=True)

        # enable scrolling with the mouse wheel (2 finger) on Windows
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        # enable scrolling with the mouse button on Windows
        frame.bind("<B1-Motion>", scroll_move)
        frame.bind("<Button-1>", scroll_start)
        # Create a scrollbar and associate it with the canvas
        scrollbar = Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas_frame = canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.bind('<Configure>', on_canvas_configure)


        def cancel():
            root.destroy()
        def goBack():
            root.destroy()
            main_func()
        def show_info():
            messagebox.showinfo("Select User",
                                "Select user so that you can see the details of user")
        def on_entry_change(*args):
            if select_user.get().strip():
                if checker == "dict":
                    Username.configure(text=data["username"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["username"] else None
                    Email.configure(text=data["email"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["email"] else None
                    Country.configure(text=data["country"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["country"] else None
                    Birthday.configure(text=data["birthdate"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["birthdate"] else None
                    Gender.configure(text=data["gender"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["gender"] else None
                    PostalCode.configure(text=data["postalCode"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["postalCode"] else None
                    Mobile.configure(text=data["mobileNumber"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["mobileNumber"] else None
                    Operator.configure(text=data["mobileOperator"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["mobileOperator"] else None
                    Brand.configure(text=data["mobileBrand"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["mobileBrand"] else None
                    CreatedAt.configure(text=data["creationTime"], font=("Helvetica", 11, "bold"), bg='lightblue') if data["creationTime"] else None
                elif checker == "list":
                    getItem = [item for item in data if item["username"] == select_user.get().strip()]
                    getItems = getItem[0]
                    print(getItems["username"])
                    Username.configure(text=getItems["username"], font=("Helvetica", 11, "bold"), bg='lightblue') if getItems[
                        "username"] else None
                    Email.configure(text=getItems["email"], font=("Helvetica", 11, "bold"), bg='lightblue') if getItems[
                        "email"] else None
                    Country.configure(text=getItems["country"], font=("Helvetica", 11, "bold"), bg='lightblue') if getItems[
                        "country"] else None
                    Birthday.configure(text=getItems["birthdate"], font=("Helvetica", 11, "bold"), bg='lightblue') if getItems[
                        "birthdate"] else None
                    Gender.configure(text=getItems["gender"], font=("Helvetica", 11, "bold"), bg='lightblue') if getItems[
                        "gender"] else None
                    PostalCode.configure(text=getItems["postalCode"], font=("Helvetica", 11, "bold"), bg='lightblue') if \
                    getItems["postalCode"] else None
                    Mobile.configure(text=getItems["mobileNumber"], font=("Helvetica", 11, "bold"), bg='lightblue') if getItems[
                        "mobileNumber"] else None
                    Operator.configure(text=getItems["mobileOperator"], font=("Helvetica", 11, "bold"), bg='lightblue') if \
                    getItems["mobileOperator"] else None
                    Brand.configure(text=getItems["mobileBrand"], font=("Helvetica", 11, "bold"), bg='lightblue') if getItems[
                        "mobileBrand"] else None
                    CreatedAt.configure(text=getItems["creationTime"], font=("Helvetica", 11, "bold"), bg='lightblue') if \
                    getItems["creationTime"] else None


        Label(frame, text="User Data", bg='lightyellow', font=("Helvetica", 13, "bold")).grid(row=0, sticky=W,
                                                                                                     padx=10, pady=10,
                                                                                                     column=0)
        Label(frame, text="Select User: ", bg='lightblue', font=("Helvetica", 13)).grid(row=1, sticky=W, padx=(10,50), pady=10)
        info_button = Button(frame, text="?", command=show_info, pady=0).grid( row=1,
                                                                                column=0,sticky=E)  # question mark help 1
        select_user = ttk.Combobox(frame, values=getNames, state="normal", width=30)
        select_user.grid(row=1, column=1,padx=(20,10),sticky=W)
        select_user.set('')
        Button(frame, text="Search", command=on_entry_change, pady=0).grid(row=1,
                                                                              column=2, sticky=W,padx = (10,0))
        Label(frame, text="Username: ", bg='lightblue', font=("Helvetica", 11)).grid(row=2, sticky=W, padx=10,
                                                                                      pady=10)
        Username = Label(frame, text="", bg='green', font=("Helvetica", 11))
        Username.grid(row=2,column=1, sticky=W, padx=10,pady=10)

        Label(frame, text="Email: ", bg='lightblue', font=("Helvetica", 11)).grid(row=3, sticky=W, padx=10,
                                                                                     pady=10)
        Email = Label(frame, text="", bg='green',font=("Helvetica", 11))
        Email.grid(row=3, column=1, sticky=W, padx=10,
                                                                           pady=10)
        Label(frame, text="Country: ", bg='lightblue', font=("Helvetica", 11)).grid(row=4, sticky=W, padx=10,
                                                                                     pady=10)
        Country = Label(frame, text="", bg='green', font=("Helvetica", 11))
        Country.grid(row=4, column=1, sticky=W, padx=10,
                                                                           pady=10)
        Label(frame, text="Birthdate: ", bg='lightblue', font=("Helvetica", 11)).grid(row=5, sticky=W, padx=10,
                                                                                     pady=10)
        Birthday = Label(frame, text="", bg='green', font=("Helvetica", 11))
        Birthday.grid(row=5, column=1, sticky=W, padx=10,
                                                                           pady=10)
        Label(frame, text="Gender: ", bg='lightblue', font=("Helvetica", 11)).grid(row=6, sticky=W, padx=10,
                                                                                     pady=10)
        Gender = Label(frame, text="", bg='green', font=("Helvetica", 11))
        Gender.grid(row=6, column=1, sticky=W, padx=10,
                                                                           pady=10)

        Label(frame, text="Postal Code: ", bg='lightblue', font=("Helvetica", 11)).grid(row=7, sticky=W, padx=10,
                                                                                     pady=10)
        PostalCode = Label(frame, text="", bg='green', font=("Helvetica", 11))
        PostalCode.grid(row=7, column=1, sticky=W, padx=10,
                                                                           pady=10)
        Label(frame, text="Mobile No.: ", bg='lightblue', font=("Helvetica", 11)).grid(row=8, sticky=W, padx=10,
                                                                                     pady=10)
        Mobile = Label(frame, text="", bg='green', font=("Helvetica", 11))
        Mobile.grid(row=8, column=1, sticky=W, padx=10,
                                                                           pady=10)
        Label(frame, text="Mobile Operator: ", bg='lightblue', font=("Helvetica", 11)).grid(row=9, sticky=W, padx=10,
                                                                                     pady=10)
        Operator = Label(frame, text="", bg='green', font=("Helvetica", 11))
        Operator.grid(row=9, column=1, sticky=W, padx=10,
                                                                           pady=10)
        Label(frame, text="Mobile Brand: ", bg='lightblue', font=("Helvetica", 11)).grid(row=10, sticky=W, padx=10,
                                                                                     pady=10)
        Brand = Label(frame, text="", bg='green', font=("Helvetica", 11))
        Brand.grid(row=10, column=1, sticky=W, padx=10,
                                                                           pady=10)
        Label(frame, text="Created At: ", bg='lightblue', font=("Helvetica", 11)).grid(row=11, sticky=W, padx=10,
                                                                                     pady=10)
        CreatedAt = Label(frame, text="", bg='green', font=("Helvetica", 11))
        CreatedAt.grid(row=11, column=1, sticky=W, padx=10,
                                                                           pady=10)

        Button(frame, text="Go back to Home Page", command=lambda: goBack()).grid(row=12, column=1,sticky=E)
        Button(frame, text="Cancel", command=lambda: cancel()).grid(row=12, column=1, sticky=W,
                                                                                          padx=20, pady=10)
        root.mainloop()

    def Streaming():
        f = open('StreamingHistory.json', "r")
        data = json.load(f)
        f.close()
        sortedData = sorted(data, key=lambda mplayed: mplayed['msPlayed'], reverse=True)
        topTenDataValues = []
        topTenDataNames = []
        j=0
        for i in sortedData:
            if j >= 10:
                break
            topTenDataValues.append(i["msPlayed"])
            if "$" in i["trackName"] :
                i["trackName"] = i["trackName"].replace('$', '\$')
            if "_" in i["trackName"] :
                i["trackName"] = i["trackName"].replace('_', '')
            topTenDataNames.append(i["trackName"]+", "+i["artistName"])

            j+=1
        print(topTenDataNames)

        root = Tk()
        root.title('Spotify Data Visualization')
        root.geometry("1000x900")  # specify the window size
        root.configure(bg='green')  # change background color

        def on_canvas_configure(event):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

        def scroll_start(event):
            canvas.scan_mark(event.x, event.y)

        def scroll_move(event):
            canvas.scan_dragto(event.x, event.y, gain=1)

        # Create a canvas for scrolling
        canvas = Canvas(root, bg='green')

        # Create a frame inside the canvas which will hold your content
        frame = Frame(canvas, bg='green')

        def _on_mouse_wheel(event):
            if isinstance(event.widget, str):  # String because it does not have an actual reference
                if event.widget.endswith('.!combobox.popdown.f.l'):  # If it is the listbox
                    return 'break'

            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")  # Else scroll the canvas
            frame.event_generate('<Escape>')  # Close combobox

        # root.bind_all("<MouseWheel>", _on_mouse_wheel)

        def dontscroll(e):
            return "dontscroll"

        def on_enter(e):
            frame.bind_all("<MouseWheel>", dontscroll)

        def on_leave(e):
            frame.bind_all("<MouseWheel>", _on_mouse_wheel)

        frame.event_generate('<Escape>')

        frame.bind_class('Listbox', '<Enter>',
                         on_enter)
        frame.bind_class('Listbox', '<Leave>',
                         on_leave)
        canvas.pack(side='left', fill=BOTH, expand=True)

        # enable scrolling with the mouse wheel (2 finger) on Windows
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        # enable scrolling with the mouse button on Windows
        frame.bind("<B1-Motion>", scroll_move)
        frame.bind("<Button-1>", scroll_start)
        # Create a scrollbar and associate it with the canvas
        scrollbar = Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas_frame = canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.bind('<Configure>', on_canvas_configure)
        def goHome():
            root.destroy()
            main_func()

        Label(frame, text="Top 10 Music played Graph:", bg='lightyellow', font=("Helvetica", 15, "bold")).grid(row=0,
                                                                                                            sticky=W,
                                                                                                            padx=10,
                                                                                                            pady=10,
                                                                                                            column=0)
        Button(frame, text="Go Home", command=goHome, font=("Helvetica", 12)).grid(row=1, column=0, padx=1, pady=10,
                                                                                   sticky=W)
        print("Streaming")
        figure = Figure(figsize=(10, 8), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, frame)
        axes = figure.add_subplot()
        axes.legend(fontsize=14)
        axes.bar(topTenDataNames, topTenDataValues)
        wrap_labels(axes, 10)
        axes.set_title('Top 10 Songs')
        axes.set_ylabel('How many times listened')
        figure_canvas.get_tk_widget().grid(row=2, padx=1,)
        root.mainloop()
    def Interferences():
        f = open('Inferences.json', "r")
        data = json.load(f)
        f.close()

        root = Tk()
        root.title('Spotify Data Visualization')
        root.geometry("900x600")  # specify the window size
        root.configure(bg='green')  # change background color

        def on_canvas_configure(event):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

        def scroll_start(event):
            canvas.scan_mark(event.x, event.y)

        def scroll_move(event):
            canvas.scan_dragto(event.x, event.y, gain=1)

        # Create a canvas for scrolling
        canvas = Canvas(root, bg='green')

        # Create a frame inside the canvas which will hold your content
        frame = Frame(canvas, bg='green')

        def _on_mouse_wheel(event):
            if isinstance(event.widget, str):  # String because it does not have an actual reference
                if event.widget.endswith('.!combobox.popdown.f.l'):  # If it is the listbox
                    return 'break'

            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")  # Else scroll the canvas
            frame.event_generate('<Escape>')  # Close combobox

        # root.bind_all("<MouseWheel>", _on_mouse_wheel)

        def dontscroll(e):
            return "dontscroll"

        def on_enter(e):
            frame.bind_all("<MouseWheel>", dontscroll)

        def on_leave(e):
            frame.bind_all("<MouseWheel>", _on_mouse_wheel)

        frame.event_generate('<Escape>')

        frame.bind_class('Listbox', '<Enter>',
                         on_enter)
        frame.bind_class('Listbox', '<Leave>',
                         on_leave)
        canvas.pack(side='left', fill=BOTH, expand=True)

        # enable scrolling with the mouse wheel (2 finger) on Windows
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        # enable scrolling with the mouse button on Windows
        frame.bind("<B1-Motion>", scroll_move)
        frame.bind("<Button-1>", scroll_start)
        # Create a scrollbar and associate it with the canvas
        scrollbar = Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas_frame = canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.bind('<Configure>', on_canvas_configure)
        def goHome():
            root.destroy()
            main_func()

        Button(frame, text="Go Home", command=goHome, font=("Helvetica", 12)).grid(row=1, column=0, padx=1, pady=10,
                                                                                   sticky=W)
        Label(frame, text="First Party: ", bg='lightblue', font=("Helvetica", 13,"bold")).grid(row=2, column=0,sticky=E, padx=10,
                                                                                     pady=10)
        Label(frame, text="Third Party: ", bg='lightblue', font=("Helvetica", 13, "bold")).grid(row=2, column=1,
                                                                                                sticky=W, padx=10,
                                                                                                pady=10)
        firstParty = []
        thirdParty = []
        for i in data["inferences"]:
            if "1P" in i:
                firstParty.append(i)
            elif "3P" in i:
                thirdParty.append(i)
        height_of_listbox = firstParty if firstParty>thirdParty else thirdParty
        firstPartyData = Listbox(frame,bg='lightblue',width=20,height=len(height_of_listbox))
        thirdPartyData = Listbox(frame, bg='lightblue',width=20,height=len(height_of_listbox))
        for i in data["inferences"]:
            if "1P" in i:
                firstPartyData.insert(END,i.replace("1P_",""))
            elif "3P" in i:
                thirdPartyData.insert(END,i.replace("3P_",""))
        firstPartyData.grid(row=3, column=0,sticky=E, padx=10, pady=10)
        thirdPartyData.grid(row=3, column=1, sticky=E, padx=10, pady=10)
        # print(firstPartyData)
        # print(thirdPartyData)
        root.mainloop()
    def main_func():
        root = Tk()
        root.title('Spotify Data Visualization')
        root.geometry("900x600")  # specify the window size
        root.configure(bg='green')  # change background color
        def on_canvas_configure(event):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

        def scroll_start(event):
            canvas.scan_mark(event.x, event.y)

        def scroll_move(event):
            canvas.scan_dragto(event.x, event.y, gain=1)

        # Create a canvas for scrolling
        canvas = Canvas(root, bg='green')

        # Create a frame inside the canvas which will hold your content
        frame = Frame(canvas, bg='green')

        def _on_mouse_wheel(event):
            if isinstance(event.widget, str):  # String because it does not have an actual reference
                if event.widget.endswith('.!combobox.popdown.f.l'):  # If it is the listbox
                    return 'break'

            canvas.yview_scroll(-1 * int((event.delta / 120)), "units")  # Else scroll the canvas
            frame.event_generate('<Escape>')  # Close combobox

        # root.bind_all("<MouseWheel>", _on_mouse_wheel)

        def dontscroll(e):
            return "dontscroll"

        def on_enter(e):
            frame.bind_all("<MouseWheel>", dontscroll)

        def on_leave(e):
            frame.bind_all("<MouseWheel>", _on_mouse_wheel)

        frame.event_generate('<Escape>')

        frame.bind_class('Listbox', '<Enter>',
                         on_enter)
        frame.bind_class('Listbox', '<Leave>',
                         on_leave)
        canvas.pack(side='left', fill=BOTH, expand=True)

        # enable scrolling with the mouse wheel (2 finger) on Windows
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
        # enable scrolling with the mouse button on Windows
        frame.bind("<B1-Motion>", scroll_move)
        frame.bind("<Button-1>", scroll_start)
        # Create a scrollbar and associate it with the canvas
        scrollbar = Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas_frame = canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.bind('<Configure>', on_canvas_configure)

        def runUserData():
            if not os.path.isfile(os.getcwd() + "/Userdata.json"):
                messagebox.showerror("Error retrieving file","No User data file is present")
                return
            root.destroy()  # Close the window
            UserData()
        def runStreaming():
            if not os.path.isfile(os.getcwd() + "/StreamingHistory.json"):
                messagebox.showerror("Error retrieving file","No User data file is present")
                return
            root.destroy()  # Close the window
            Streaming()
        def runInterferences():
            if not os.path.isfile(os.getcwd() + "/Inferences.json"):
                messagebox.showerror("Error retrieving file","No User data file is present")
                return
            root.destroy()  # Close the window
            Interferences()
        def submit():
            getType = check_type.get().strip()
            if getType == "User Data":
                runUserData()
            elif getType == "Streaming":
                runStreaming()
            elif getType == "Inferences":
                runInterferences()
            else:
                messagebox.showerror("Error","No Type is selected")

        def cancel():
            root.destroy()  # Close the window

        def show_info():
            messagebox.showinfo("Spotify Data Visualization Help",
                                "Select User Data to see details of any User, " +
                                "OR Select Streaming data to see top 10 listened music"+
                                "OR Select interferences to see First party or Third party categories to which the user may belong to.")


        options = ['User Data','Streaming','Inferences']  # options for combobox

        Label(frame, text="Select Data For Visualization", bg='green', font=("Helvetica", 15, "bold")).grid(row=0, sticky=W,
                                                                                                     padx=10, pady=10,
                                                                                                     column=0)

        Label(frame, text="Select Type: ", bg='green', font=("Helvetica", 13)).grid(row=1, sticky=W, padx=10,pady=10)
        info_button_1 = Button(frame, text="?", command=show_info, pady=0).grid(padx=(15,0),row=1, column=0)  # question mark help 1
        check_type = ttk.Combobox(frame, values=options, state="normal", width=50)
        check_type.grid(row=1, column=1)
        check_type.set('')
        Button(frame, text="Cancel", command=cancel, font=("Helvetica", 12)).grid(row=2, column=1, padx=1,pady=10,sticky=W)
        Button(frame, text="Submit", command=submit, font=("Helvetica", 12)).grid(row=2, column=1, padx=1,pady=10)

        root.mainloop()


    if __name__ == '__main__':
        main_func()

except Exception as e:
    print({str(e)})