from . import db

class PropertyModel(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singularUserProfile) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.String(80))
    propertyDesc = db.Column(db.String(160))
    NoOfBedrooms = db.Column(db.String(10))
    NoOfBathrooms = db.Column(db.String(10))
    price = db.Column(db.String(20))
    propertyType = db.Column(db.String(20))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(160))

    def __init__(self, title, propertyDesc, NoOfBedrooms, NoOfBathrooms, price, propertyType, location, photo):
        self.title = title
        self.propertyDesc = propertyDesc
        self.NoOfBedrooms = NoOfBedrooms
        self.NoOfBathrooms = NoOfBathrooms
        self.price = price
        self.propertyType = propertyType
        self.location = location
        self.photo = photo

