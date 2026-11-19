from flask import Flask, render_template, abort
app = Flask(__name__)
@app.route('/')
@app.route('/<page>')
def view(page='home'):
    if page not in {'home','student','mentor','admin','chat','meetings','join'}:
        abort(404)
    return render_template(page + '.html')
