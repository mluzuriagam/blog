from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_posts():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return posts


@app.route("/")
def index():
    all_posts = get_posts()
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post")
def post():
    return render_template("sample post.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def blog(num):
    all_posts = get_posts()
    c_post = all_posts[int(num) - 1]
    c_image = f"assets/img/{c_post['id']}.jpg"
    return render_template("post.html", post=c_post, image=c_image)


if __name__ == "__main__":
    app.run(debug=True)
