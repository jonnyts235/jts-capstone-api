from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://dxefbgqwujzatt:44c5b6d453ae7c182a9734a0cb098a304b5afde590313a95e99ea8e01332fcc8@ec2-107-22-222-161.compute-1.amazonaws.com:5432/derg18vir39uvp"

CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
review
class Review(db.Model):
  __tablename__ = "reviews"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  rating = db.Column(db.Integer)
  comment = db.Column(db.String(200))

  def __init__(self, name, rating, comment):
    self.name = name
    self.rating = rating
    self.comment = comment

class ReviewSchema(ma.Schema):
  class Meta:
    fields = ("id", "name", "rating", "comment")
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)


@app.route("/reviews", methods=["GET"])
def get_accounts():
  all_reviews = Review.query.all()
  result = reviews_schema.dump(all_reviews)
  return jsonify(result)


@app.route("/review", methods=["POST"])
def add_account():
  name = request.json["name"]
  rating = request.json["rating"]
  comment = request.json["comment"]
  new_review = Review(name, rating, comment)

  db.session.add(new_review)
  db.session.commit()
  
  created_review = Review.query.get(new_review.id)
  return review_schema.jsonify(created_review)


@app.route("/review/<id>", methods=["PUT"])
def update_review(id):
  review = Review.query.get(id)
  review.name = request.json["name"]
  review.rating = request.json["rating"]
  review.comment = request.json["comment"]
  db.session.commit()
  return account_schema.jsonify(account)

@app.route("/review/<id>", methods=["DELETE"])
def delete_review(id):
  review = Review.query.get(id)
  db.session.delete(review)
  db.session.commit()

  return "RECORD DELETED"
  

if __name__ == "__main__":
  app.debug=True
  app.run()