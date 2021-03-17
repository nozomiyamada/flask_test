import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__) # flask app instance

# top page
@app.route('/', methods=['GET', 'POST'])
def page_top():
    return render_template('toppage.html') # rendering "toppage.html"

# second page
@app.route('/second', methods=['GET', 'POST'])
def page_second():
    return render_template('secondpage.html') # rendering "top.html"

# length page - return character length of the word as JSON
@app.route('/<word>', methods=['GET', 'POST'])
def page_length(word):
    return jsonify({'word': word, 'length': len(word)})

if __name__ == "__main__":
    # debug=True -> reload automatically when update app.py
    app.run(host="0.0.0.0", port=8000, debug=True)