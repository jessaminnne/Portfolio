from flask import Flask, render_template  #NEW IMPORT!!
from flask import request, url_for #url import for active class

portfolio = Flask(__name__)    #This is creating a new Flask object

#decorator that links...
@portfolio.errorhandler(404)
def page_Not_Found(e):
    return render_template('index.html'), 404

@portfolio.route('/')
@portfolio.route('/index')         					#This is the main URL
def home():
    return render_template("index.html", title= "Portfolio")

@portfolio.route('/about')
def interests():
    return render_template("about.html", title= "About")

@portfolio.route('/contact')
def courses():
    return render_template("contact.html", title="Contact")

@portfolio.route('/photography')
def other():
    return render_template("photography.html", title="Photography")

if __name__ == '__main__':
    portfolio.run(debug=True)		#debug=True is optional
