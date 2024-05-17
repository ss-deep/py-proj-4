from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length
from markupsafe import Markup

class TeamForm(FlaskForm):

    team_name=StringField("team name",validators=[DataRequired(),Length(min=4,max=255)])
    submit=SubmitField("submit")

    