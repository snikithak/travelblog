from flask import Flask, render_template, request, url_for, jsonify
import random

app = Flask(__name__)

@app.route('/index', methods = ['GET', 'POST'])
def index():
    searchData={
        "nature":"nature.html",
        "entertainment": "ent.html"
    }

    if request.method== 'POST':
        query=request.form['query']
        if query not in searchData:
            return "No data found for" + query
        
        # need to fix lines 19-22 to go to ent.html when entertainment is typed
        if query in searchData:
            return render_template(searchData[query], searchData= searchData[query])
        

    return render_template('index.html', url=url_for('index'))

if __name__== "__main__":
    app.run(host='0.0.0.0', port = 80, debug=True)