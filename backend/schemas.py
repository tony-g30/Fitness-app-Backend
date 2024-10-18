# schemas.py
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import User, Workout, Group

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        include_fk = True
        load_instance = True

class GroupSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        include_relationships = True
        load_instance = True
