from flask import Flask, render_template, url_for, redirect
from forms import TeamForm

app=Flask(__name__)
app.secret_key = "keep this secret"

@app.route("/")
def home():
    team_form=TeamForm()
    return render_template("home.html", team_form=team_form)

@app.route("/add_team", methods=["GET","POST"])
def add_team():
    team_form=TeamForm()
    if team_form.validate_on_submit():
        team_name=team_form.team_name.data
        print(team_name)
    else: 
        print("Form failed to validate on submit.")
    
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True) 