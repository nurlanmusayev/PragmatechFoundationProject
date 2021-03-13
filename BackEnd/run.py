from flask import Flask,render_template

app=Flask(__name__)

data=[
    {
        'title':'Sampiyon',
        'content':'2010-2011 sezonu sampiyonu',
        'img':'../static/img/1.jpg'
    },
    {
        'title':'FB',
        'content':'2010-2011 sezonu 2-cisi',
        'img':'../static/img/5.jpg'
    },
    {
        'title':'GS',
        'content':'2010-2011 sezonu 8-cisi',
        'img':'../static/img/8.jpg'
    },{
        'title':'Fourth Card Title',
        'content':'Fourth Card Content'
    },
]

@app.route('/')
def index():
    return render_template("index.html",melumatlar=data)

@app.route('/panel')
def panel():
    return "<h2>Salam.Bizim sehifemize xos gelmisiz.Size nece komek ede bilerem?</h2>"
if __name__=="__main__":
    app.run(debug=True)




