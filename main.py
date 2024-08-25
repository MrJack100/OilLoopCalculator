from oilloop import *
#maxPotential(oil=300, ratio=(0, 2, 4)); requiredOil(0, 300, 600); oilLoop(300, 300, 300)

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisisasecret!"

@app.route("/", methods=["GET", "POST"])
def hello():
    class InputForm(FlaskForm):
        fuel = StringField("fuel")
        plastic = StringField("plastic")
        rubber = StringField("rubber")
    form = InputForm()
    if form.validate_on_submit():
        print(form.fuel.data, form.plastic.data, form.rubber.data)
        totalOil, plasticRefineries, rubberRefineries = oilLoop(300, 300, 300)
        return render_template("calculated.html", totalOil=totalOil, plasticRefineries=plasticRefineries, rubberRefineries=rubberRefineries)
    return render_template("landing.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)