from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,SelectField
from wtforms.validators import DataRequired, Length
# from markupsafe import Markup

class TeamForm(FlaskForm):

    team_name=StringField("Team Name",validators=[DataRequired(),Length(min=4,max=255)])
    submit=SubmitField("Submit")

class ProjectForm(FlaskForm):

    project_name=StringField("Project Name",validators=[DataRequired()])
    description=TextAreaField("Description")
    completed=BooleanField("Completed",false_values={False, 'false', ''})
    team_id=SelectField("Team Id")
    submit=SubmitField("Submit")
