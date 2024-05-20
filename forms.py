from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,SelectField,PasswordField
from wtforms.validators import DataRequired, Length
# from markupsafe import Markup


class UserForm(FlaskForm):

    user_name=StringField("User Name",validators=[DataRequired(),Length(min=4,max=255)])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=4,max=255)])
    submit=SubmitField("Submit")
    
class TeamForm(FlaskForm):

    user_selection=SelectField("Select User")
    team_name=StringField("Team Name",validators=[DataRequired(),Length(min=4,max=255)])
    submit=SubmitField("Submit")

    def update_users(self,users):
        self.user_selection.choices=[(user.id, user.username) for user in users]

class ProjectForm(FlaskForm):

    project_name=StringField("Project Name",validators=[DataRequired()])
    description=TextAreaField("Description")
    completed=BooleanField("Completed",false_values={False, 'false', ''})
    team_selection=SelectField("Select Team",choices=[('chi', 'Chicken'), ('bf', 'Beef'),
                                   ('fish', 'Fish')])
    submit=SubmitField("Submit")

    def update_teams(self,teams):
        self.team_selection.choices=[(team.id, team.team_name) for team in teams]
