from flask import Flask,redirect
from urls_map_db import db

class FlaskServer:

  app = Flask(__name__)

  @app.route("/")
  def null(self):
    return "Type your short url to redirect to your website"

  @app.route('/', defaults={'path': ''})
  @app.route('/<path:path>')
  def catch_all(path):
    real_url = db.find_short_url(path)
    print(real_url, "real_url")
    return redirect(real_url, code=302)

  def run(self):
    print("name", __name__)
    if __name__ == __name__:
      print("i'm running")
      self.app.run()




