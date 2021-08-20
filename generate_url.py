import random
from urls_map_db import db as DB

db=DB()
# get URL and name, and return shortcut that natched to the URL
def generate_url(long_url,name):
    if len(name)==0:
        name=None

    #check if url is exists in the database
    found_url=db.find_long_url(long_url)
    if found_url is not None:
        print("found1",found_url)
        if type(found_url)==tuple:
            return found_url[0]
        return found_url

    #if not exists, create new shortcut:

    # choose url size
    size=random.randint(3,9)
    print("size",size)
    if (len(long_url) < size):
        # if url size shorter than size, push the url to db as the shortcut
        db.insert_new_mapping(long_url,long_url,name)
        print("url < size")
        return long_url

    # generate new random short url
    new_url=""
    step_size= int(len(long_url)/size)
    for i in range(0,len(long_url),step_size):
        if str.isalpha(long_url[i]) or str.isdigit(long_url[i]):
            new_url = new_url + long_url[i]

    # check if new short URL already exists
    found_url=db.find_short_url(new_url)

    # while new URL exists, create new
    while found_url is not None and found_url!=long_url:
        size = random.randint(5, 12)
        step_size = int(len(long_url) / size)
        for i in range(0, len(long_url), step_size):
            if str.isalpha(long_url[i]) or str.isdigit(long_url[i]):
                new_url = new_url + long_url[i]
        # check if new short url already exists
        found_url = db.find_short_url(new_url)

    # push the new URL to db
    if name is None:
        name=new_url
    print("long url to insert", long_url)
    db.insert_new_mapping(long_url,new_url,name)


    if type(new_url) == tuple:
        print("arrived to unknown")
        return found_url[0]
    return new_url

