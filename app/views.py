from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from app import app

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/siginup')
def siginup():
    return render_template('siginup.html')

@app.route('/login')
def login():
    return render_template('login.html')
