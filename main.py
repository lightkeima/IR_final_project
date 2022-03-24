import os
from flask import Flask, render_template
app = Flask(__name__, template_folder='html')

@app.route('/')
def main():
    
    return render_template('main_screen.html')

@app.route('/res/')
def res():
    return render_template('search_results.html')

app.run()
