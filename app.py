#FLASK
from flask import Flask, jsonify, render_template, request
import os,optparse
app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")



alumnos = {
    "Andrea Reyes": 19,
    "Katherine Garcia": 17,
    "Fabricio Juarez": 18,
    "Jean Mejicanos": 17,
    "Steven Wilson": 19,
    "Ian Jenatz": 19,
    "Anesbeth Maatens": 17,
    "Tirso Cordova": 20,
    "Abner Xocop": 21,
    "Andres Bolanos": 21,
    "Katherin Mazariegos": 19,
    "Daniel Hernandez": 20,
    "Maite de la Roca": 20,
    "Diego Quan": 22,
    "Fernando Gonzalez": 20,
    "Boris Rendon": 19,
    "Adriana Mundo": 20,
    "Alejandra Lemus": 19,
    "Juan Barillas": 21,
    "David Corzo": 19,
    "Giovanny Telon": 25
}

@app.route("/alumnos")
def api_students():
    return jsonify(alumnos)


@app.route("/ages")
def ages():
    edades=[edad for estudiante,edad in alumnos.items()]
    average=int(sum(edades)/len(edades))
    return render_template("ages.html", alumnos=alumnos, average=average)


@app.route("/students")
def students():
    return render_template("students.html", alumnos=alumnos)


def search_student(student):
    """
    A function that searches in data source
    """
    result=[]
    for name,age in alumnos.items():
        if student.lower() in name.lower():
            result.append(name)

    print(f"Result {result}")
    return result


@app.route("/search",methods=["GET"])
def search():
    """
    /search route, to search from an input form.
    """
    student_to_find=request.args.get("student", None)
    print(f"A buscar: {student_to_find}")
    student_list=search_student(student_to_find)
    return render_template("search.html",student_list_result=student_list)

@app.route("/")
def home():
    foo="bar"
    return render_template("home.html", mivariable=foo ,developer=developer)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
