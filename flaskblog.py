from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':'Marcin Weglowski',
        'title': 'Blog post 1',
        'content' : 'First post content.',
        'date_posted':'31.10.2019',
    },
    {
        'author':'Grzegorz Braun',
        'title': 'Blog post 2',
        'content' : 'Second post content.',
        'date_posted':'01.11.2019',
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)