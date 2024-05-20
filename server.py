from flask import Flask, render_template, url_for, redirect
from forms import UserForm,TeamForm,ProjectForm
from model import User, Team, Project, connect_to_db,db

app=Flask(__name__)
app.secret_key = "keep this secret"

@app.route("/",methods=["GET","POST"])
def home():
    user_form=UserForm()
    if user_form.validate_on_submit():
        # user_name=user_form.user_name.data
        db.session.add(User(user_form.user_name.data, user_form.password.data))
        db.session.commit()
    else:
        print("user not validated")
    return render_template("user.html",user_form=user_form)


@app.route("/add_team", methods=["GET","POST"])
def add_team():
    team_form=TeamForm()
    # print(User.query.all())
    team_form.update_users(User.query.all())
    if team_form.validate_on_submit():
        team_name=team_form.team_name.data
        #use '.data' to access value from the input fields
        db.session.add(Team(team_form.team_name.data, team_form.user_selection.data)) 
        db.session.commit()
    else: 
        print("Form failed to validate on submit.")
    return render_template("teams.html",team_form=team_form)

@app.route('/add_project', methods=["GET","POST"])
def add_project():
    proj_form=ProjectForm()
    proj_form.update_teams(Team.query.all())
    if proj_form.validate_on_submit():
        project_name=proj_form.project_name.data
        db.session.add(Project(proj_form.project_name.data, proj_form.description.data, proj_form.completed.data, proj_form.team_selection.data))
        db.session.commit()
    else:
        print("project not found")

    return render_template("projects.html",proj_form=proj_form)


if __name__=="__main__":
    connect_to_db(app)
    app.run(debug=True) 