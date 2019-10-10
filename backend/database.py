import redis
#import flask

r = redis.Redis(host='localhost', port=6379, db=0)

def create12VCo1db():
	f = open('students.txt', 'r')
	students = []
	for line in f:
	    students.append(line.strip('\n'))

	#print(students[0])
	
	data = {"weekContribution":"0.00", "totalContribution":"0.00"}

	for i in range(0, len(students)):
		r.hmset(students[i], data)

	#r.hset('Max Stanford-Taylor', 'weekContribution', '0.00')

create12VCo1db()

print(r.hgetall('Max Stanford-Taylor'))


