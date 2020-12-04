from datetime import datetime
from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index=True)
    lastName = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    companyName = db.Column(db.String(140))
    memberSince = db.Column(db.DateTime, default=datetime.?)
    userToLocation = db.relationship("UserToLocation", backref='user', lazy='dynamic')
    paymentInfo = db.relationship("PaymentInfo", backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(64), index=True)
    address = db.Column(db.String(120), index=True, unique=True)
    country = db.Column(db.String(64), index=True)
    userToLocation=db.relationship("UserToLocation",backref='location', lazy='dynamic')

    def __repr__(self):
        return '<Location: {}>'.format(self.zipcode)


class UserToLocation(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    locationID = db.Column(db.Integer, db.ForeignKey('location.id'))
    Product = db.relationship("Product",backref='user to location', lazy='dynamic')

    def __repr__(self):
        return '<UserToLocation {}>'.format(self.body)




class PaymentInfo(db.Model)
  id=db.Column(db.Integer,primary_key=True)
  cardType=db.Column(db.String(20), index=True)
  cardNumber=db.Column(db.String(9), index=True)
  securityNumber=db.Column(db.String(3))
  userId=db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Payment Info {}>'.format(User.query.filter_by(id=self.userId).first().firstName)


class Product(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    userToLocationID = db.Column(db.Integer, db.ForeignKey('userToLocation.id'))
    dateHarvested = db.Column(db.DateTime, default=datetime.?)
    amount = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(400), index=True)
    price = db.Column(db.String(20), index=True)

    def __repr__(self):
        return '<Product: {}>'.format(self.name)
