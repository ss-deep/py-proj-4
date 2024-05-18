from flask import Flask, render_template, url_for, redirect
from forms import UserForm,TeamForm,ProjectForm
from model import User, Team, Project, connect_to_db

app=Flask(__name__)
app.secret_key = "keep this secret"

@app.route("/")
def home():
    user_form=UserForm()
    if user_form.validate_on_submit():
        username=user_form.username.data
        print(username)
    else:
        print("user not validated")
    return render_template("user.html",user_form=user_form)


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
    connect_to_db(app)
    app.run(debug=True) 