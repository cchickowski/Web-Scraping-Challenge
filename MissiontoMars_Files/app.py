from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app  = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
mars=mongo.db.mars_collection

@app.route("/")
def home():
    site_data = mars.find()
    return render_template("index.html", mars_data=site_data)

@app.route('/scrape')
def scrape_app():
    mars.drop()
    results = scrape_mars.scrape()
    mars.insert_one(results)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
  
    



