from flask import Flask
app = Flask(__name__) 




@app.route('/heypeople')
def hello():
    return 'Hey people!'

@app.route('/cdojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def greeting(name):
    print(name)
    return "Hi, " + name

@app.route('/shout/<bat>')
def hype(bat):
    print(bat)
    return (" " + bat)*10





if __name__=="__main__":
    app.run(debug=True)

