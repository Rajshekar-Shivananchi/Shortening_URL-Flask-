from flask import Flask,render_template,request
from  short_url import URL_Shortener
ab=URL_Shortener()

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("firstpage.html")

@app.route('/',methods=['POST'])
def getdata():
    aurl=request.form['aurl']
    c=ab.shorten_url(aurl)

    print(c)
    return render_template("second_page.html",a=c,b=aurl)

if __name__=='__main__':
    app.run(debug=True)
