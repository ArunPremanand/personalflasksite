from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Arun Premanand',
        'title': 'Blog Post 1',
        'content': 'first post content stuff',
        'date_posted': 'April 20th, 2019'
    },
    {
        'author': 'Arun Premanand',
        'title': 'Blog Post 2',
        'content': 'second post content stuff',
        'date_posted': 'May 27th, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts, title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


def main():
    app.run(debug=True, port=49750)

if __name__ == '__main__':
    main()