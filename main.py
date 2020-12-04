from flask import Flask, render_template
from categories import generate_note_dict
import pprint as pp
from categories import get_note_content
from categories import title_dict

# Remove the GET /favicon issue
from flask import send_from_directory


import os
import sys

import categories as cat

# Get the category files
category_files = cat.categories

# Set the dictionary of note links mapping to metadata
note_dict = cat.note_dict

# Initialize Flask
app = Flask(__name__)

# Favicon issue resolution
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Homepage Route
@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html')

# CATEGORY ROUTES

# To create a route for a category, create a dictionary with the following parameters: 
    # title - Category title
    # description - What does this category show?
    # image_route - Image to be displayed as the category's logo of sorts
    # get_note_content - an obligatory function for parsing HTML files
    # category_files - should resemble category_files[<category title goes here>]
    # note_dict - Also necessary, simply pass in note_dict = note_dict 

data_sci_route_params = {
    'title': 'Data Science',

    'description': 'Data science. Statistics.  TensorFlow, Pandas, Sci-Kit Learn, and so much more!  This page will house all of my personal notes.  Additionally, I will post some external resources which I have found helpful.',

    'image_route': 'static/assets/media/stat-homepage-violin-plots.png',

    'get_note_content': get_note_content, 

    'category_files': category_files['Data Science'], 

    'note_dict': note_dict,

}

# Then, to create the route, use render template, passing in the template file as a positional argument, and unpack the dictionary for the **kwargs to be used in rendering the page

# Data Science Route
@app.route('/data-science')
def data_science():
    return render_template('/category-indices/data-science.html', **data_sci_route_params)


# NOTES ROUTES

# First, initialize a dictionary containing the content of the title you gave your category.  Here's an example:

data_sci_title_dict = title_dict['Data Science']

# To initialize a routes for notes, pass in the following **kwargs in a similar manner as we did for category routes. 
    # title_dict = <the title dictionary you just created goes here> 
data_sci_notes_params = {
    'title_dict': data_sci_title_dict
}

# Then, unpack that dictionary in the render-template. Additionally, place the **kwarg note_title=note_title before the dictionary unpacking step.  

@app.route('/data-science-notes/<note_title>')
def note(note_title):
    return render_template('notes.html', note_title=note_title,**data_sci_notes_params)


# Machine learning **kwargs dictionary initialization for category homepage 

machine_learning_route_params = {

    'title': 'Machine and Deep Learning',

    'description': 'The majority of content here will consist of Jupyter Notebooks.  These are best for note-taking and presentation.  Note that Python scripts are preferable in some cases, but for the sake of readability and experimentation, I choose Jupyter Notebooks for this.  I also have .py scripts in my GitHub repository for different modules and packages I have created myself.',

    'image_route': 'static/assets/media/ml-category-homepage.png',

    'get_note_content': get_note_content, 

    'category_files': category_files['Machine and Deep Learning'], 

    'note_dict': note_dict,
}

# Machine Learning Projects
@app.route('/machine-learning')
def machine_learning():
    return render_template('/category-indices/machine-learning.html', **machine_learning_route_params)

# Python Route


@app.route('/python')
def python():
    return render_template('/category-indices/python.html')

# Linear Algebra Route


# JS Route


# export FLASK_APP=main FLASK_ENV=development
# flask run

# Remedy GET /favicon issue


if __name__ == '__main__':
    app.run(port=5000)
