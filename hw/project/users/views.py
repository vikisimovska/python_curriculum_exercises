from flask import Blueprint, redirect, render_template, request, url_for
from project.users.models import User
from project import db
# let's create the owners_blueprint to register in our __init__.py
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates/users'
)
