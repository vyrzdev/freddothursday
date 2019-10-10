import redis
from flask import Flask, requests

r = redis.Redis('localhost')

app = Flask(__name__)

#Use 'keys *' to get all keys from the db
#The gather all keys with the specific class value

def byteCodeDictToStr(diction):
	newdict = {}
	for key in diction.keys():
		newdict[key.decode("utf-8")] = diction[key].decode("utf-8")
	return newdict

@app.route('/getClassMembers/<classname>', methods=['GET'])
def getClassMembers(classname):
	members = []
	keys = r.keys()
	for key in keys:
		hash = r.hgetall(key)
		if hash[b'class'] == classname:
			members.append(key)
	return members

@app.route('/getStudentData/<studentname>', methods=['GET'])
def getStudentData(studentname):
	data = r.hgetall(studentname)
	return data

@app.route('/updateWeekTotal/<studentname>', methods=['POST'])
def updateStudentData(studentusername):
	if request.args.get('contrib'):
		weeklyContribToAdd = request.args.get('contrib')
		student = r.hgetall(studentname)
		student['weeklyContribution'] = student['weeklyContribution'] + weeklyContribToAdd
		student['totalContribution'] = student['totalContribution'] + weeklyContribToAdd
		r.hmset(studentname, student)
	return 'Contribution updated by: ' + request.args.get('contrib')

#uuid update
@app.route('/updateUUID/<studentname>', methods=['POST'])
def updateStudentUUID(studentname):
	# There is no implamentation of UUIDs in the database currently
	return None

#register user
@app.route('/registerUser/', methods=['POST'])
def registerUser():
	studentname = request.args.get('studentname')
	initCon = 0.00
	userInit = {'weeklyContribution':initCon, 'totalContribution':initCon}
	r.hmset(studentname, userInit)
	return 'New user created with key ' + studentname



if __name__ == '__main__':
	app.run(debug=True)
