from ..Logic_Layer.GroupLogic import GroupLogic
from flask import Flask

app = Flask(__name__)
config=" "

@app.route('/Create_Group')
def Create_Group(group_name,group_admin_id):
        return "Not Implemented"

@app.route('/Add_Member')
def Add_Member(username):
        return "Not Implemented"

@app.route('/Remove_Member')
def Remove_Member(username):
        return "Not Implemented"

@app.route('/Edit_Group')
def Edit_Group(group_profile,group_name,group_admin_id):
        return "Not Implemented"

@app.route('/Get_Group_info')
def Get_Group_info():
        return "Not Implemented"