from flask import Flask, render_template,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    css_link = url_for('static', filename='style.css')
    return render_template('index.html', title="ReDI School", css_link=css_link)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #app.run()