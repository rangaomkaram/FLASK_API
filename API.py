from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


# configure sqlite3 to enforce foregin key contraints
@event.listens_for(Engine,"connect")
def _set_sqlite_pragma(dbapi_connection,connection_record):
    if isinstance(dbapi_connection,SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_key =ON;")
        cursor.close()

db = SQLAlchemy(app)
now = datetime.now()

# models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")

class BlogPost(db.Model):
    __table__name = "blog_post"
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(50))
    body  = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

# creating routes
@app.route("/user",methods=["POST"])
def create_user():
    data = request.get_json()
    newUser=User(
        name=data["name"],
        email=data["email"],
        phone=data["phone"],
        address=data["address"]
    )
    db.session.add(newUser)
    db.session.commit()
    return jsonify({"Message":"User is Created"}),200
    pass

@app.route("/user/descending_id",methods=["GET"])
def get_all_users_descending():
    pass

@app.route("/user/ascending_id",methods=["GET"])
def get_all_users_ascending():
    pass

@app.route("/user/<user_id>",methods=["GET"])
def get_all_blog_posts(user_id):
    pass

@app.route("/blog_post/<blog_post_id>",methods=["GET"])
def get_one_blog_post(blog_post_id):
    pass

@app.route("/blog_post/<blog_post_id>",methods=["DELETE"])
def delete_blog_post(blog_post_id):
    pass
if __name__ == "__main__":
    app.run(debug=True)


