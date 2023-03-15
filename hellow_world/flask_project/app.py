#front end --- scripts for user on browser
#backlend --- for server side scripting (tomcat, JT, WAS, gellyfish)
#java(springmvc),Javascript(nodejs),python(flask,django)
#framework for creating the script
#when insalling Flask default web server also installed
#http requests --- GET,POST,PUT,DELETE


from flask import Flask,render_template,request,redirect,url_for

posts = {
    0:{
        'postid':"Post ID",
        'postname':'Post Name',
        'description':'Post Description'
    }
}
app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template("home.html")


#<int:n1> <str:str1> called Dynamic URLs...
@app.route("/add/<int:n1>/<int:n2>")
def add(n1,n2):
    res = n1+n2
    #{{result}} jinja code for placable in html script
    return render_template("result.html" , result = res)


@app.route("/addform",methods = ['POST','GET'])
def addform():
    if request.method == "POST":
        n1 = int(request.form.get("num1"))
        n2 = int(request.form.get("num2"))
        res = n1+n2
        return render_template("result.html" , result = res)
    else:
        return render_template("addform.html")


@app.route("/addpost",methods = ['post','get'])
def addpost():
    if request.method == "POST":
        postid = int(request.form.get("postid"))
        postname = request.form.get("postname")
        description = request.form.get("description")
        posts[postid] = dict(zip(posts[0].keys(),(postid,postname,description)))
        return redirect( url_for("feed"))
    else:
        return(render_template('addpost.html'))


@app.route("/searchpost/<int:postid>")
def searchpost(postid):
    return (posts[postid])


@app.route("/feed")
def feed():
    return (render_template("feed.html",hposts = posts))


if __name__ == "__main__":
    app.run(host="192.168.0.138",port = 5000,debug=True)
