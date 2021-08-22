from  urls_map_db import  db as DB
from tkinter import Tk,Button,Label,Grid,Text
from open_browser import open_browser

# class ViewMappingGui creates a window that showing all short URLs from database
class ViewMappingGui:
    new_url=None
    button_color = "#c13e3e"
    bg_color = "#1b1515"

    # create a window with list of all shortcuts mapping
    def __init__(self):
        self.db=DB()
        #define window
        self.master = Tk()
        self.master.title("Url Shortener")
        self.master.configure(bg=self.bg_color)
        self.data=[]
        self.buttons=[]
        size= "900x"+str(len(self.data)*50)
        self.master.geometry(("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight())))


        self.label = Label(self.master,width=20,bg=self.bg_color,font= ('Helvetica', 12,  "bold",),fg="#d6c4c4", text="Paste here your long URL").pack()

        self.delete_all = Button(self.master,width=20,bg=self.button_color, text="Delete all shortcuts", command=self.db.delete_all).pack()

        self.delete_one = Button(self.master,width=20,bg=self.button_color, text="delete one", command=self.delete_one_func).pack()

        self.refresh = Button(self.master,width=20,bg=self.button_color, text="refresh",command=self.refresh).pack()

        self.close_button = Button(self.master,width=20,bg=self.button_color, text="Close", command=self.close).pack()

        self.add_data_view()


    # creates a button for each shortcuts,
    # which open a browser with it's URL on click.
    def add_data_view(self):
        self.data = self.db.select_all()
        self.buttons = []
        for i in self.data:
            url = i[0]
            short="http://127.0.0.1:5000/"+i[1]
            print("short",short)
            self.buttons.append(
                Button(self.master,width=30,font= ('Helvetica', 11,  ), text="Name: " + i[2] + ", Short URL: "+short
                       , command=lambda: self.open_browser_click(short)))

        for i in self.buttons:
            i.pack(padx=1, pady=1)

    # update shortcuts buttons if deleted
    def refresh(self):
        for l in self.buttons:
            l.destroy()
        self.add_data_view()

    def open_browser_click(self,url):
        print("url from view",url)
        open_browser(url)
        self.master.destroy()

    # run the window
    def run(self):
        self.master.mainloop()

    # open a text box to type which shortcut to delete,
    # and destroy it when finished
    def delete_one_func(self):
        if len(self.data)>0:
            self.delete_Label = Label(self.master,bg=self.bg_color,font= ('Helvetica', 12,  "bold",),fg="#d6c4c4", text="Type here last part of url to delete")
            self.delete_Label.pack()
            self.delete_text = Text(self.master,height=2,width=20)
            self.delete_text.pack(padx=1, pady=1)
            self.delete_button = Button(self.master,width=30,bg=self.button_color, font= ('Helvetica', 11,  ), text="OK",
                                        command=self.ok_delete)
            self.delete_button.pack(padx=1, pady=1)

    #delete data and destroy delete widgets from window
    def ok_delete(self):
        self.db.delete_one(self.delete_text.get("1.0","end")[0:-1])
        self.delete_Label.destroy()
        self.delete_text.destroy()
        self.delete_button.destroy()

    # closw window
    def close(self):
        self.master.destroy()



