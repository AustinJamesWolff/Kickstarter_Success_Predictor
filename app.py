from flask import Flask, render_template, request
from
from 

# this is a functino to create app
def create_app():
    app = FLASK(__name__)
    
    @APP.route('/'):
    def home():
        '''Landing page to the Kickstarter Prediction project'''
        