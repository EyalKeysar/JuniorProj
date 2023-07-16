import sys
import os
import time
import socket
from Network.constants import *
from networks import *
from logger import Logger

from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash, Markup


def main():
    logger =  Logger() 
    logger.log(" * Starting game")

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html', users=["tal", "shay", "david"], rest_of_chat=Markup("<h1>hello</h1>"))
                            
    

if __name__ == "__main__":
    app.run()