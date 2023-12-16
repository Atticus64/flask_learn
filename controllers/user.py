
from flask import render_template, make_response, request
from utils.validations import validate_movie

from markupsafe import escape
import sqlite3

con = sqlite3.connect('file.db', check_same_thread=False)
cur = con.cursor()


def logout():
    resp = make_response(render_template("logout.html"))
    resp.delete_cookie('username')
    return resp


def hello_cat():
    resp = make_response(render_template("hello.html", name="Cat"))
    resp.set_cookie('username', 'cat')
    return resp


def get_movies():
    cur.execute("CREATE TABLE IF NOT EXISTS movies (title, year, score)")
    res = cur.execute("SELECT * FROM movies")
    rows = res.fetchall()
    con.commit()
    print(rows)
    return rows


def create_movie():
    movie = request.get_json()

    if "title" in movie and "year" in movie and "score" in movie:
        title = movie["title"]
        year = movie["year"]
        score = movie["score"]
        rows = [(title, year, score)]

        cur.executemany("INSERT INTO movies VALUES(?,?,?)", rows)
        con.commit()
    else:
        msg = validate_movie(movie)
        resp = make_response({
            "error": "Invalid data",
            "message": msg
        })
        resp.status = 400
        return resp

    resp = make_response({
        "Created": True
    })
    resp.status = 201
    return resp


def json():
    return {
        "name": "Carlos",
        "age": 10,
        "direction": {
            "codes": [1,2,3,4],
            "is_street": False
        }
    }


def greet(name):
    return f'Hello {escape(name)}'

