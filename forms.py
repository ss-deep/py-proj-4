from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,SelectField,PasswordField
from wtforms.validators import DataRequired, Length
# from markupsafe import Markup


class UserForm(FlaskForm):

    user_name=StringField("User Name",validators=[DataRequired(),Length(min=4,max=255)])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=4,max=255)])
    submit=SubmitField("Submit")
    
class TeamForm(FlaskForm):

    team_name=StringField("Team Name",validators=[DataRequired(),Length(min=4,max=255)])
    submit=SubmitField("Submit")

class ProjectForm(FlaskForm):

    project_name=StringField("Project Name",validators=[DataRequired()])
    description=TextAreaField("Description")
    completed=BooleanField("Completed",false_values={False, 'false', ''})
    team_id=SelectField("Team Id",choices=[('chi', 'Chicken'), ('bf', 'Beef'),
                                   ('fish', 'Fish')])
    submit=SubmitField("Submit")


