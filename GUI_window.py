from tkinter import Tk, Label, Button, Text
from generate_url import  generate_url
import pyperclip
from open_browser import open_browser

#class MyGui creates an user interface
class MyGUI:
    new_url=None

    #create the window with labels, buttons and text-boxes
    def __init__(self,server):
        self.master = Tk()
        self.master.title("Url Shortener")
        self.master.geometry("500x400")
        self.new_url="empty"
        self.server=server

        self.label = Label(self.master, text="Paste here your long URL")
        self.label.pack()

        self.url_text=Text(self.master,height=2,width=50)
        self.url_text.pack()

        self.optional_label = Label(self.master,text="Optoinal: You can create a name that will help you to find your short link later.")
        self.optional_label.pack()

        self.name_text = Text(self.master, height=2, width=50)
        self.name_text.pack()

        self.create_url_button = Button(self.master, text="Generate Short Url", command=self.create_url)
        self.create_url_button.pack()

        self.new_url_label = Label(self.master, text="Here you will see the new URL")
        self.new_url_label.pack()

        self.copy_url_button=Button(self.master,text="copy URL",command=self.copy)
        self.copy_url_button.pack()

        self.open_url_button = Button(self.master, text="open URL in chrome", command=lambda :open_browser("----"+self.new_url))
        self.open_url_button.pack()

        self.view_url_mapping_button = Button(self.master, text="view all urls mapping", command=self.view_all_mapping)
        self.view_url_mapping_button.pack()

        self.close_button = Button(self.master, text="Close", command=self.master.quit)
        self.close_button.pack()

    #open new window that show all short URLs that in ths database
    def view_all_mapping(self):
        import view_all_urls
        view_all_urls.ViewMappingGui().run()

    #create or find short URL for the URL that user typed.
    def create_url(self):
        url = self.url_text.get("1.0", "end")
        name = self.name_text.get("1.0", "end")
        self.url_text.delete("1.0","end")
        self.name_text.delete("1.0","end")
        if len(url)<1:
            return
        if len(name)<1:
            name=""
        self.new_url=generate_url(url[0:len(url)-1],name)
        self.new_url="http://127.0.0.1:5000/"+self.new_url
        str="Your new url is "+self.new_url
        self.new_url_label.config(text=str)
        print(self.new_url)

    #copy the short URL to clipboard
    def copy(self):
        if self.new_url is not None :
            pyperclip.copy(self.new_url)

    #run the master window
    def run(self):
        self.master.mainloop()




