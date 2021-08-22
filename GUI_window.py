from tkinter import Tk, Label, Button, Text
from generate_url import  generate_url
import pyperclip
from open_browser import open_browser

#class MyGui creates an user interface
class MyGUI:
    new_url=None
    button_color="#c13e3e"
    bg_color="#1b1515"

    #create the window with labels, buttons and text-boxes
    def __init__(self,server):
        self.master = Tk()
        self.master.title("Url Shortener")
        self.master.geometry("600x500")
        self.master.configure(bg=self.bg_color)
        self.new_url="empty"
        self.server=server

        self.label = Label(self.master,bg=self.bg_color,font= ('Helvetica', 12,  "bold",),fg="#d6c4c4", text="Paste here your long URL"               )
        self.label.pack()

        self.url_text=Text(self.master,height=2,width=28,font= ('Helvetica', 12,  "bold",))
        self.url_text.pack(padx=10, pady=10)

        self.optional_label = Label(self.master,bg=self.bg_color,font= ('Helvetica',12,"bold",),fg="#d6c4c4",text="Optoinal: You can create a name\n that will help you to find your short\n link later.")
        self.optional_label.pack()

        self.name_text = Text(self.master,width=32, height=2)
        self.name_text.pack()

        self.create_url_button = Button(self.master,width=25, font= ('Helvetica', 12,  "bold",), bg=self.button_color,text="Generate Short Url", command=self.create_url)
        self.create_url_button.pack(padx=10, pady=10)

        self.new_url_label = Label(self.master,bg=self.bg_color,font= ('Helvetica', 12,  "bold",),fg="#d6c4c4", text="Here you will see the new URL")
        self.new_url_label.pack(padx=10, pady=10)

        self.copy_url_button=Button(self.master,width=25,font= ('Helvetica', 12,  "bold",), bg=self.button_color,text="copy URL",command=self.copy)
        self.copy_url_button.pack(padx=10, pady=10)

        self.open_url_button = Button(self.master,width=25,font= ('Helvetica', 12,  "bold",), bg=self.button_color, text="open URL in chrome", command=lambda :open_browser("----"+self.new_url))
        self.open_url_button.pack(padx=10, pady=10)

        self.view_url_mapping_button = Button(self.master,width=25,font= ('Helvetica', 12,  "bold",), bg=self.button_color, text="view all urls mapping", command=self.view_all_mapping)
        self.view_url_mapping_button.pack(padx=10, pady=10)

        self.close_button = Button(self.master,width=25, text="Close",font= ('Helvetica', 12,  "bold",), bg=self.button_color, command=self.master.quit)
        self.close_button.pack(padx=10, pady=10)

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




