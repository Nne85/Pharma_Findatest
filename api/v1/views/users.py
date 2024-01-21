#!/usr/bin/python3
"""
api view for users
"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort, render_template, session, flash, redirect, url_for
import hashlib
from models import storage
from models.users import User
from models.pharmacy_store import PharmacyStore
from models.drugs import Drug
import os



def hash_password(password):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Encode the password as bytes (assuming it's in UTF-8)
    password_bytes = password.encode('utf-8')

    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)

    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()

    return hashed_password


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects."""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object by ID."""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object by ID."""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/register", methods=["POST", "GET"], strict_slashes=False)
def create_user():
    """Creates a new User object."""
    if request.method == 'POST':
        data = {}
        form_data = request.form
        for key, value in form_data.items():
            data[key] = value

        if not form_data:
            return redirect(url_for('appviews.create_user'))

        if 'password' not in form_data:
            print('Missing password')
            return redirect(url_for('appviews.create_user'))

        if 'email' not in form_data:
            print('Missing email')
            return redirect(url_for('appviews.create_user'))

        if 'name' not in form_data:
            print('Missing name')
            return redirect(url_for('appviews.create_user'))

        hashed_password = hashed_password(data['password'])
        data['password'] = hashed_password
        new_user = User(**data)
        new_user.save()
        return redirect(url_for('appviews.login_user'))
    else:
        return render_template('register.html')


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """Updates a User object by ID."""
    updated = False
    updates = request.get_json()
    user = storage.get(User, user_id)
    if user:
        for key, value in updates.items():
            if key == 'id' or key == 'email' or key == 'created_at' or key == 'updated_at' or key == 'name':
                pass
            else:
                if key == 'password':
                    user.password = hashed_password(value)['password']
                    updated = True
                elif key == 'name':
                    updated = True
                    user.name = value
        if updated:
            storage.new(user)
            storage.save()
        return jsonify(user.to_dict()), 200
    else:
        abort(400, description="Not a JSON")

@app_views.route("/login", strict_slashes=False, methods=['POST', 'GET'])
def login_user():
    """
    check passed password and username against password and
    username stored in database
    """
    if request.method == 'POST':
        user = storage.get(User, name=request.form['name'])
        if user:
            user_dict = user.to_dict()
            if user_dict['password'] == hashed_password(request.form['password']):
                session['user_id'] = user_dict['id']
                session['name'] = user_dict['name']
                return redirect(url_for('appviews.landing_page'))
            else:
                return redirect(url_for('appviews.landing_page'))
        else:
            return redirect(url_for('appviews.landing_page'))
    else:
        return render_template('login.html')


@app_views.route('/logout', strict_slashes=False)
def logout():
    """
    logout from current session
    """
    session.clear()
    return redirect(url_for('appviews.login_user'))


@app_views.route("/", strict_slashes=False)
def landing_page():
    """
    direct user to the landing page
    """
    return render_template('landing.html', pharmacy_shops=pharmacy_shops)
