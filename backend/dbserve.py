import urllib.parse
import redis
from flask import Flask, request, jsonify

r = redis.Redis('localhost')

app = Flask(__name__)

#Use 'keys *' to get all keys from the db
#The gather all keys with the specific class value

def convertDict(data):
    if isinstance(data, bytes):  return data.decode('utf-8')
    if isinstance(data, dict):   return dict(map(convertDict, data.items()))
    if isinstance(data, tuple):  return map(convertDict, data)
    return data

@app.route('/getClassMembers/<classname>', methods=['GET'])
def getClassMembers(classname):
	classname = bytes(classname, 'utf-8')
	members = []
	keys = r.keys()
	for key in keys:
		hash = r.hgetall(key)
		if hash[b'class'] == classname:
			members.append(key.decode('utf-8'))
	return jsonify(members)

@app.route('/getStudentData/<studentname>', methods=['GET'])
def getStudentData(studentname):
	studentname = urllib.parse.unquote(studentname)
	data = r.hgetall(str(studentname))
	data = convertDict(data)
	return jsonify(data)

@app.route('/updateWeekTotal/<studentname>')
def updateStudentData(studentname):
	if request.args.get('contrib'):
		weeklyContribToAdd = request.args.get('contrib')
		student = r.hgetall(studentname)
		student[b'weekContribution'] = float(student[b'weekContribution'].decode('utf-8')) + float(weeklyContribToAdd)
		student[b'totalContribution'] = float(student[b'totalContribution'].decode('utf-8')) + float(weeklyContribToAdd)
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
