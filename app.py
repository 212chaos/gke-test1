from flask import Flask
app = Flask('hello-world')
@app.route('/')
def hello():
 return "CloudageSkill Microservices\n"
if __name__ == '__main__':
 app.run(host = '0.0.0.0', port = 8080)
