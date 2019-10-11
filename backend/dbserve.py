import urllib.parse
import redis
import hashlib
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

@app.route('/getStudentData/<uuid>', methods=['GET'])
def getStudentData(uuid):
	data = r.hgetall(str(uuid))
	data = convertDict(data)
	return jsonify(data)

@app.route('/updateWeekTotal/<uuid>')
def updateStudentData(uuid):
	if request.args.get('contrib'):
		weeklyContribToAdd = request.args.get('contrib')
		student = r.hgetall(uuid)
		student[b'weekContribution'] = float(student[b'weekContribution'].decode('utf-8')) + float(weeklyContribToAdd)
		student[b'totalContribution'] = float(student[b'totalContribution'].decode('utf-8')) + float(weeklyContribToAdd)
		r.hmset(uuid, student)
	return 'Contribution updated by: ' + request.args.get('contrib')

#uuid update
@app.route('/updateUUID/<uuid>', methods=['POST'])
def updateStudentUUID(studentname):
	# This requires thought and im not doing that rn
	return None

#register user
@app.route('/registerUser/')
def registerUser():
	studentname = urllib.parse.unquote(request.args.get('studentname'))
	classs = urllib.parse.unquote(request.args.get('class'))
	initCon = 0.00
	userInit = {'weeklyContribution':initCon, 'totalContribution':initCon, 'studentName':studentname, 'class':classs}
	r.hmset(hashlib.sha256(bytes(studentname, 'utf-8')).hexdigest(), userInit)
	return 'New user created with key ' + hashlib.sha256(bytes(studentname, 'utf-8')).hexdigest()

if __name__ == '__main__':
	app.run(debug=True)
