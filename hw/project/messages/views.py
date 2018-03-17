from flask import Blueprint, redirect, render_template, request, url_for, flash
#from project.messages.forms import EmployeeForm
from project.messages.models import Message
from project import db

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates/messages'
)
