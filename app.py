from flask import Flask, render_template, redirect
from flask import request
from flask import url_for
import forms
from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
crsf = CSRFProtect()

@app.route("/", methods=["GET", "POST"])
def index():
    create_form = forms.UseForms(request.form)
    if request.method == 'POST':
        alumn = Alumnos(nombre = create_form.nombre.data,
                        apellidos =  create_form.apellidos.data,
                        email = create_form.email.data
                        )
        db.session.add(alumn)
        db.session.commit()
    return render_template("index.html", form = create_form)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UseForms(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre  = create_form.nombre.data
        alum.apellidos  = create_form.apellidos.data
        alum.email  = create_form.email.data
        db.session.add(alum)
        db.session.commit()

        return redirect(url_for('ABCompleto'))
    return render_template("modoficar.html", form = create_form)
    
@app.route("/ABCompleto", methods=["GET", "POST"])
def abc():
    create_form = forms.UseForms(request.form)
    alumno = Alumnos.query.all()
    return render_template("ABCompleto.html", form = create_form, alumno = alumno)

if __name__ =="__main__":
    crsf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)