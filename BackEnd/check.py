from flask import Flask,render_template

app=Flask(__name__)

data=[
    {
        'name':'Nurlan',
        'surname':'Musayev'
    },
    {
        'name':'Mehemmed',
        'surname':'Musayev'
    },
]

@app.route('/about/<ad>')
def index(ad):
    for user in data:
        if user['name']==ad:
            return render_template('user.html',user=user)

 
if __name__=='__main__':
    app.run(debug=True)
    