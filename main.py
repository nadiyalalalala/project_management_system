from flask import Flask
from flask import render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/')
def home():
    """Landing page."""
    nav = [
        {'name': 'Home', 'url': 'https://example.com/1'},
        {'name': 'About', 'url': 'https://example.com/2'},
        {'name': 'Pics', 'url': 'https://example.com/3'}
    ]
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("home.html")

    # return render_template(
    #     'home.html',
    #     nav=nav,
    #     title="Jinja Demo Site",
    #     description="Smarter page templates with Flask & Jinja."
    # )
    content = template.render(
        
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )
    
    return content

app.run(host='0.0.0.0', port=81)