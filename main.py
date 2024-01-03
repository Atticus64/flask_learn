from flask import Flask
from controllers import user

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

app.add_url_rule("/logout", view_func=user.logout)
app.add_url_rule("/", view_func=user.hello_cat)
app.add_url_rule("/json", view_func=user.json)
app.add_url_rule("/<name>", view_func=user.greet)
app.add_url_rule("/movies/create", view_func=user.create_movie, methods=['POST'])
app.add_url_rule("/movies", view_func=user.get_movies)

if __name__ == "__main__":
    app.run(port=port)
