from flask import Flask, render_template, url_for, redirect
from forms import TeamForm,ProjectForm

app=Flask(__name__)
app.secret_key = "keep this secret"

@app.route("/")
def home():
    # team_form=TeamForm()
    return render_template("home.html")

@app.route("/add_team", methods=["GET","POST"])
def add_team():
    team_form=TeamForm()
    if team_form.validate_on_submit():
        team_name=team_form.team_name.data
        print(team_name)
    else: 
        print("Form failed to validate on submit.")
    
    return render_template("teams.html",team_form=team_form)

@app.route('/add_project', methods=["GET","POST"])
def add_project():
    proj_form=ProjectForm()
    if proj_form.validate_on_submit():
        project_name=proj_form.project_name.data
        print(project_name)
    else:
        print("project not found")

    return render_template("projects.html",proj_form=proj_form)


if __name__=="__main__":
    app.run(debug=True) 