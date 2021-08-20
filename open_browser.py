import webbrowser

#get an URL and open chrome browser with directing to the URL that givven
def open_browser(url):
    #Check if a string is a valid URL
    if url=="" or url==None:
        print("URL is empty")
        return None
    browser_path = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
    webbrowser.register("Chrome", None, webbrowser.BackgroundBrowser(browser_path))
    webbrowser.get('Chrome').open(url)
    return 'OK'