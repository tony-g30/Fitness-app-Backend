# app.py
from flask import Flask, request, jsonify
from .models import db, User, Workout, Group, GroupMembership
from .schemas import UserSchema, WorkoutSchema, GroupSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost:5432/fitness_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize schemas
user_schema = UserSchema()
workout_schema = WorkoutSchema()
group_schema = GroupSchema()
workouts_schema = WorkoutSchema(many=True)
groups_schema = GroupSchema(many=True)

# -----------------------------------------------
# Workout Endpoints
# -----------------------------------------------

# Create a new workout
@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    new_workout = Workout(
        name=data['name'],
        duration=data['duration'],
        user_id=data['user_id']
    )
    db.session.add(new_workout)
    db.session.commit()
    return workout_schema.jsonify(new_workout), 201

# Get all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return workouts_schema.jsonify(workouts), 200

# Get a single workout
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return workout_schema.jsonify(workout), 200

# Update a workout
@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.get_json()
    workout = Workout.query.get_or_404(id)
    workout.name = data.get('name', workout.name)
    workout.duration = data.get('duration', workout.duration)
    db.session.commit()
    return workout_schema.jsonify(workout), 200

# Delete a workout
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return '', 204

# -----------------------------------------------
# Group Endpoints
# -----------------------------------------------

# Create a new group
@app.route('/groups', methods=['POST'])
def create_group():
    data = request.get_json()
    new_group = Group(
        name=data['name'],
        description=data['description']
    )
    db.session.add(new_group)
    db.session.commit()
    return group_schema.jsonify(new_group), 201

# Get all groups
@app.route('/groups', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    return groups_schema.jsonify(groups), 200

# Get a single group
@app.route('/groups/<int:id>', methods=['GET'])
def get_group(id):
    group = Group.query.get_or_404(id)
    return group_schema.jsonify(group), 200

# Update a group
@app.route('/groups/<int:id>', methods=['PUT'])
def update_group(id):
    data = request.get_json()
    group = Group.query.get_or_404(id)
    group.name = data.get('name', group.name)
    group.description = data.get('description', group.description)
    db.session.commit()
    return group_schema.jsonify(group), 200

# Delete a group
@app.route('/groups/<int:id>', methods=['DELETE'])
def delete_group(id):
    group = Group.query.get_or_404(id)
    db.session.delete(group)
    db.session.commit()
    return '', 204

# -----------------------------------------------
# User-Group Membership Endpoints
# -----------------------------------------------

# Add a user to a group
@app.route('/groups/<int:group_id>/users/<int:user_id>', methods=['POST'])
def add_user_to_group(group_id, user_id):
    membership = GroupMembership(user_id=user_id, group_id=group_id)
    db.session.add(membership)
    db.session.commit()
    return jsonify({'message': 'User added to group'}), 201

# Remove a user from a group
@app.route('/groups/<int:group_id>/users/<int:user_id>', methods=['DELETE'])
def remove_user_from_group(group_id, user_id):
    membership = GroupMembership.query.filter_by(user_id=user_id, group_id=group_id).first_or_404()
    db.session.delete(membership)
    db.session.commit()
    return jsonify({'message': 'User removed from group'}), 204

# Get all users in a group
@app.route('/groups/<int:group_id>/users', methods=['GET'])
def get_users_in_group(group_id):
    group = Group.query.get_or_404(group_id)
    return user_schema.jsonify(group.users, many=True), 200

if __name__ == '__main__':
    app.run(debug=True)
