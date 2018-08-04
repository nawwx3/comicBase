from flask import Flask, render_template, session, request, flash, redirect, url_for, g
from functools import wraps
import sqlite3

def app_login(username, password):
    if request.method == 'POST':
        if username == 'f' and password == 'f':
            session['logged_in'] = True
