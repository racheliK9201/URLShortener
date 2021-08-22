import threading
import server
import GUI_window

def run_server():
    server.run()

def run_window():
    my_gui = GUI_window.MyGUI(server)
    my_gui.run()

t2=threading.Thread(target=run_window).start()

t1=threading.Thread(target=run_server).start()

