from flask import Flask, jsonify, request
from service.authLog import signUp,logIn,logout,deleteUser,updateUser,readManager
from service.projects import createProject,asignProjectToManager,updateProject,deleteProject,displayProjects,display_single_project
from service.resource import addResource,deleteResouce,updateResource,showResources,asignResourceToTask,show_single_resource
app = Flask(__name__)

@app.route('/user/signup')
def dosignUp():return signUp(request.get_json())

@app.route('/user/login')
def doLogIn():return logIn(request.get_json())
@app.route('/user/logout/<email>')
def doLogOut(email):return logout(email)

@app.route('/user/delete/<email>')
def delete_user_route(email):return deleteUser(email)
@app.route('/user/update/<email>')
def update_user_route(email):return updateUser(email,request.get_json())

@app.route('/user/managers/<email>')
def show_managers(email):return readManager(email)
@app.route('/project/<email>',methods=['POST'])
def addProject(email):return createProject(email,request.get_json())

@app.route('/project/<email>',methods=['PUT'])
def assignProject(email):return asignProjectToManager(email,request.get_json())
@app.route('/project/<email>',methods=['PATCH'])
def updateProject(email):return updateProject(email,request.get_json())

@app.route('/project/<email>',methods=['GET'])
def allProjects(email):return displayProjects(email);

@app.route('/project/<email>/<projectid>',methods=['GET'])
def getProject(email,projectid):return display_single_project(email, projectid);

@app.route('/project/<email>/<projectid>',methods=['DELETE'])
def deleteProject(email,projectid):return deleteProject(email,projectid)

@app.route('/res/<email>',methods=['POST'])
def createResource(email):return addResource(email,request.get_json())
@app.route('/res/<email>/<resid>',methods=['DELETE'])
def removeResource(email,resid):return deleteResouce(email,resid)

@app.route('/res/<email>/<resid>',methods=['PATCH'])
def updateResource(email,resid):return updateResource(email,resid,request.get_json())
@app.route('/res/<email>',methods=['GET'])
def getAllResources(email):return showResources(email)
@app.route('/res/<email>/<task>/<resId>',methods=['PATCH'])
def assignResources(email,task,resId):return asignResourceToTask(email,task,resId)
@app.route('/res/<email>/<resid>')
def getSingleResource(email,resid):return show_single_resource(email,resid)



if __name__ == '__main__':
    app.run(debug=True)

