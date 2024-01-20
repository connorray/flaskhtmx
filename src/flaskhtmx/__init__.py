import jinja_partials
import feedparser
from flask import Flask, render_template

feed = {
  # provided by users when they create new feeds
  "title": "The Teclado Blog",
  "href": "https://blog.teclado.com/rss/",
  "show_image": True,
  "entries": {
    # the actual blog posts in the rss feed
  }
}

def create_app():
  # good idea to use app factory patthern
  # create an "app" function and create the app and routes in this function
  app = Flask(__name__)
  # this allows us to call jinja partials function from within our templates
  jinja_partials.register_extensions(app)

  @app.route("/feed/")
  def render_feed():
    feed_url = feed["href"]
    parsed_feed = feedparser.parse(feed_url)
    for entry in parsed_feed.entries:
      # simply keeping all the entries in the parsed feed
      if entry.link not in feed["entries"]:
        feed["entries"][entry.link] = entry
    
    return render_template("feed.html", feed=feed, entries=feed["entries"].values())
  
  return app
