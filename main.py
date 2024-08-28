from oilloop import *
#maxPotential(oil=300, ratio=(0, 2, 4)); requiredOil(0, 300, 600); oilLoop(300, 300, 300)

from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisisasecret!"

@app.route("/")
def head():
    return redirect("/fuelBased")

@app.route("/fuelBased", methods=["GET", "POST"])
def fuelBased():
    with open("index.html", "r") as file:
        index = file.read()
    class InputForm(FlaskForm):
        fuel = StringField("fuel")
        plastic = StringField("plastic")
        rubber = StringField("rubber")
    form = InputForm()
    if form.validate_on_submit():
        print(form.fuel.data, form.plastic.data, form.rubber.data)
        totalOil, plasticRefineries, rubberRefineries = oilLoopFuelBased(300, 300, 300)
        return render_template("fuelBased.html", 
                               totalOil=totalOil, 
                               plasticRefineries=plasticRefineries, 
                               rubberRefineries=rubberRefineries, 
                               response=True, 
                               index=index)
    return render_template("fuelBased.html", 
                           form=form, 
                           response=False, 
                           index=index)

@app.route("/horBased", methods=["GET", "POST"])
def horBased():
    with open("index.html", "r") as file:
        index = file.read()
    class InputForm(FlaskForm):
        hor = StringField("hor")
        plastic = StringField("plastic")
        rubber = StringField("rubber")
    form = InputForm()
    if form.validate_on_submit():
        print(form.hor.data, form.plastic.data, form.rubber.data)
        totalOil, plasticRefineries, rubberRefineries = oilLoopHorBased(300, 300, 300)
        return render_template("horBased.html", 
                               totalOil=totalOil, 
                               plasticRefineries=plasticRefineries, 
                               rubberRefineries=rubberRefineries, 
                               response=True, 
                               index=index)
    return render_template("horBased.html", 
                           form=form, 
                           response=False, 
                           index=index)

if __name__ == "__main__":
    app.run(debug=True)