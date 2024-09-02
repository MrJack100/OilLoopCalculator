from oilloop import *
#maxPotential(oil=300, ratio=(0, 2, 4)); requiredOil(0, 300, 600); oilLoop(300, 300, 300)

from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisisasecret!"

def indexFiles():
    fileList = []
    for target in ["index.html", "style.html"]:
        try:
            with open(target, "r") as file:
                fileList.append(file.read())
        except FileNotFoundError:
            exit("index.html not found")
    return(fileList)

@app.route("/")
def head():
    return redirect("/fuelBased")

@app.route("/fuelBased", methods=["GET", "POST"])
def fuelBased():
    index, style = indexFiles()
    class InputForm(FlaskForm):
        fuel = StringField("Fuel", render_kw={"placeholder": "Fuel"})
        plastic = StringField("Plastic", render_kw={"placeholder": "Plastic"})
        rubber = StringField("Rubber", render_kw={"placeholder": "Rubber"})
    form = InputForm()
    if form.validate_on_submit():
        print(form.fuel.data, form.plastic.data, form.rubber.data)
        totalOil, plasticRefineries, rubberRefineries = oilLoopFuelBased(300, 300, 300)
        return render_template("fuelBased.html", 
                               totalOil=totalOil, 
                               plasticRefineries=plasticRefineries, 
                               rubberRefineries=rubberRefineries, 
                               response=True, 
                               index=index,
                               style=style)
    return render_template("fuelBased.html", 
                           form=form, 
                           response=False, 
                           index=index,
                           style=style)

@app.route("/horBased", methods=["GET", "POST"])
def horBased():
    index, style = indexFiles()
    class InputForm(FlaskForm):
        hor = StringField("HOR", render_kw={"placeholder": "HOR"})
        plastic = StringField("Plastic", render_kw={"placeholder": "Plastic"})
        rubber = StringField("Rubber", render_kw={"placeholder": "Rubber"})
    form = InputForm()
    if form.validate_on_submit():
        print(form.hor.data, form.plastic.data, form.rubber.data)
        totalOil, plasticRefineries, rubberRefineries = oilLoopHorBased(300, 300, 300)
        return render_template("horBased.html", 
                               totalOil=totalOil, 
                               plasticRefineries=plasticRefineries, 
                               rubberRefineries=rubberRefineries, 
                               response=True, 
                               index=index,
                               style=style)
    return render_template("horBased.html", 
                           form=form, 
                           response=False, 
                           index=index,
                           style=style)

if __name__ == "__main__":
    app.run(debug=True)