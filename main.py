from oilloop import *
#maxPotential(oil=300, ratio=(0, 2, 4)); requiredOil(0, 300, 600); oilLoop(300, 300, 300)

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisisasecret!"

@app.route("/", methods=["GET", "POST"])
def head():
    class InputForm(FlaskForm):
        fuel = StringField("fuel")
        plastic = StringField("plastic")
        rubber = StringField("rubber")
    form = InputForm()
    if form.validate_on_submit():
        print(form.fuel.data, form.plastic.data, form.rubber.data)
        totalOil, plasticRefineries, rubberRefineries = oilLoop(300, 300, 300)
        return render_template("inputs.html", totalOil=totalOil, plasticRefineries=plasticRefineries, rubberRefineries=rubberRefineries, response=True)
    return render_template("inputs.html", form=form, response=False)

if __name__ == "__main__":
    app.run(debug=True)