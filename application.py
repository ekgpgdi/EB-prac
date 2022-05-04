from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

application = Flask(__name__)
cors = CORS(application, resources={r"/*": {"origins": "*"}})

@application.route('/')
def main():
    return "hello python"

if __name__ == '__main__':
    application.debug = True
    application.run()