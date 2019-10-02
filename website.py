from flask import Flask, render_template, request, jsonify
import os, optparse, sys

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Fer González")
environment = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def info():
    yml_info = 0
    return render_template("info.html", yml_info=yml_info)


@app.route("/studies")
def studies():
    institutions = 0
    return render_template("studies.html", institutions=institutions)


@app.route("/experience")
def experience():
    xps = 0
    return render_template("experience.html", xps=xps)


if __name__ == "__main__":
    debug = False
    if environment == "development" or environment == "local":
        debug = True
    print("Local change.")
    app.run(host="0.0.0.0", debug=debug)
