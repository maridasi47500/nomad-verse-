from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_local_art_encounter", methods=["GET","POST"])
def add_one_local_art_encounter():

    if request.method == 'POST':
        user = query_db('select * from local_art_encounter')
        the_username = "anonyme"
        one_user = query_db("insert into local_art_encounter (user_id,art_type,artist_name,location_city,location_country,date,reaction) values (:user_id,:art_type,:artist_name,:location_city,:location_country,:date,:reaction)",request.form, one=True)
        return render_template("local_art_encounterform.html", local_art_encounters=user, one_user=one_user, the_title="add new local_art_encounter POST")
    user = query_db('select * from local_art_encounter')
    one_user = query_db("select * from local_art_encounter limit 1", one=True)
    return render_template("local_art_encounterform.html", local_art_encounters=user, one_user=one_user, the_title="add new local_art_encounter")

