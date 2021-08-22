from flask import Flask,redirect
from urls_map_db import db as DB


app = Flask(__name__)

db=DB()
@app.route("/")
def null(self):
  return "Type your short url to redirect to your website"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  real_url = db.find_short_url(path)
  print(real_url, "real_url")
  return redirect(real_url, code=302)

def run():
  print("name", __name__)
  if __name__ == __name__:
    print("i'm running")
    app.run()




