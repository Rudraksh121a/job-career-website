from flask import Flask,render_template

app=Flask(__name__)


JOBS=[

    {
        'id':1,
        'title':"Data Analyst",
        'location':"Bangaluru,India",
        'salary':"RS. 1,00,000"
    },


    {
        'id':2,
        'title':"Data Engineer",
        'location':"Bangaluru,India",
        'salary':"RS. 1,20,000"
    },
      {
        'id':3,
        'title':"frontend Engineer",
        'location':"Bangaluru,India",
       
    },
      {
        'id':4,
        'title':"backend Engineer",
        'location':"Bangaluru,India",
        'salary':"RS. 1,20,000"
    },
]

@app.route("/")
def hello_web():
    return render_template('home.html'
                           ,jobs=JOBS,
                           company_name="Job")
if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True)
