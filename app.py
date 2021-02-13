from flask import Flask, render_template,url_for,redirect,flash, request, redirect,session
from bson import ObjectId
from hashlib import md5
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from  pymongo import MongoClient
from MySQLdb import escape_string as thwart
from flask.wrappers import Response
import re
import os  
import bcrypt
app=Flask(__name__)
client=MongoClient("mongodb://127.0.0.1:27017")
db=client.studentscorner
users=db.users
edu=db.Education
exp=db.Experience
certify=db.Certifications
project=db.Projects
volunteership=db.Volunteership
contactss=db.Contacts

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/main')
def main():
    educationlist=edu.find()
    experiencelist=exp.find()
    certificatelist=certify.find()
    projectlist=project.find()
    volunteerlist=volunteership.find()
    contactlist=contactss.find()
  
 
    return render_template('main.html',educationlist=educationlist,experiencelist=experiencelist,certificatelist=certificatelist,projectlist=projectlist,volunteerlist=volunteerlist,contactlist=contactlist)

@app.route('/login',methods=["GET","POST"])
def login():
    message = 'Please login to your account'
    if "username" in session:
        return redirect(url_for("main"))
    if request.method == "POST":
        username= request.form.get("username")
        password = request.form.get("psw")
        username_found = users.find_one({"username": username})
        if username_found:
            username_val = username_found['username']
            passwordcheck = username_found['password']
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["username"] = username_val
                return redirect(url_for('main'))
            else:
                if "username" in session:
                    return redirect(url_for("main"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == 'POST':
        existing_user = users.find_one({'username' : request.form['username']})
        email = users.find_one({'email' : request.form['email']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['psw'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass,'email':email})
            session['username'] = request.form['username']
            return render_template('login.html')
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/logout', methods = ['GET'])
def logout():
    session.pop('username')
    return redirect(url_for('index'))

@app.route('/education',methods=['get','post'])
def education():
    if request.method=='GET':
        return render_template("main.html")
    elif request.method=='POST':
        
        educationtitle=request.values.get('educationtitle')
        specializationtitle=request.values.get('specializationtitle')
        edujoinmonth=request.values.get('edujoinmonth')
        edujoinyears=request.values.get('edujoinyears')
        eduendmonth=request.values.get('eduendmonth')
        eduendyear=request.values.get('eduendyear')
        collegetitle=request.values.get('collegetitle')
        cgpaselect=request.values.get('cgpaselect')
        cgpaname=request.values.get('cgpaname')
        edu.insert({'educationtitle':educationtitle,'specializationtitle':specializationtitle,'edujoinmonth':edujoinmonth,'edujoinyears':edujoinyears,'eduendmonth':eduendmonth,'eduendyear':eduendyear,'collegetitle':collegetitle,'cgpaselect':cgpaselect,'cgpaname':cgpaname})
        return  redirect(url_for('main'))

@app.route('/delete')
def delete():
    edu.delete_one({})
    return redirect(url_for('main'))

@app.route("/experience",methods=['GET','POST'])
def experience():
    if request.method=='GET':
        return render_template('main.html')
    elif(request.method=='POST'):
        exptitle=request.values.get("exptitle")
        comptitle=request.values.get("comptitle")
        emptitle=request.values.get("emptitle")
        expjoinmonth=request.values.get("expjoinmonth")
        expjoinyear=request.values.get("expjoinyear")
        expendmonth=request.values.get("expendmonth")
        expendyear=request.values.get("expendyear")
        expdescription=request.values.get("expdescription")
        expdrivelink=request.values.get("expdrivelink")
        exp.insert({'exptitle':exptitle,'comptitle':comptitle,'emptitle':emptitle,'expjoinmonth':expjoinmonth,'expjoinyear':expjoinyear,'expendmonth':expendmonth,
        'expendyear':expendyear,'expdescription':expdescription,'expdrivelink':expdrivelink})
        return  redirect(url_for('main'))
@app.route('/deleteexperience')
def deleteexp():
    exp.delete_one({})
    return redirect(url_for('main'))

@app.route("/certification",methods=['GET','POST'])
def certification():
    if request.method=='GET':
        return render_template('main.html')
    elif(request.method=='POST'):
        certifytitle=request.values.get("certifytitle")
        certorgtitle=request.values.get("certorgtitle")
        certjoinmonth=request.values.get("certjoinmonth")
        certjoinyear=request.values.get("certjoinyear")
        certendmonth=request.values.get("certendmonth")
        certendyear=request.values.get("certendyear")
        certurl=request.values.get("certurl")
        certify.insert({'certifytitle':certifytitle,'certorgtitle':certorgtitle,'certjoinmonth':certjoinmonth,'certjoinyear':certjoinyear,'certendyear':certendyear,
        'certendmonth':certendmonth,'certurl':certurl})
        return  redirect(url_for('main'))
@app.route('/deletecertification')
def deletecertify():
    certify.delete_one({})
    return redirect(url_for('main'))

@app.route("/project",methods=['get','post'])
def projects():
    if request.method=='GET':
        return render_template('main.html')
    else:
        protitle=request.values.get("protitle")
        prostartmonth=request.values.get("prostartmonth")
        prostartyear=request.values.get("prostartyear")
        proendmonth=request.values.get("proendmonth")
        proendyear=request.values.get("proendyear")
        prourl=request.values.get("prourl")
        prodescription=request.values.get("prodescription")
        project.insert({'protitle':protitle,'prostartmonth':prostartmonth,'prostartyear':prostartyear,'proendmonth':proendmonth,
        'proendyear':proendyear,'prourl':prourl,'prodescription':prodescription})
        return redirect(url_for("main"))
@app.route('/deleteproject')
def deleteproject():
    project.delete_one({})
    return redirect(url_for('main'))

@app.route("/volunteership",methods=['get','post'])
def volunteer():
    if request.method=='GET':
        return render_template('main.html')
    else:
        voltitle=request.values.get("voltitle")
        volorgtitle=request.values.get("volorgtitle")
        volstartmonth=request.values.get("volstartmonth")
        volstartyear=request.values.get("volstartyear")
        volendmonth=request.values.get("volendmonth")
        volendyear=request.values.get("volendyear")
        voldescription=request.values.get("voldescription")
        volurl=request.values.get("volurl")
        volunteership.insert({'voltitle':voltitle,'volorgtitle':volorgtitle,'volstartmonth':volstartmonth,'volstartyear':volstartyear,'volendmonth':volendmonth,
        'volendyear':volendyear,'volurl':volurl,'voldescription':voldescription})
        return redirect(url_for("main"))
@app.route('/deletevolunteership')
def deletevolunteer():
    volunteership.delete_one({})
    return redirect(url_for('main'))


@app.route("/contact",methods=['get','post'])
def contacts():
    if request.method=='GET':
        return render_template('main.html')
    else:
        website=request.values.get("website")
        emailtitle=request.values.get("emailtitle")
        phno=request.values.get("phno")
        addresstitle=request.values.get("addresstitle")
        contactss.insert({'website':website,'emailtitle':emailtitle,'phno':phno,'addresstitle':addresstitle})
        return redirect(url_for("main"))
@app.route('/deletecontact')
def deletecontact():
    contactss.delete_one({})
    return redirect(url_for('main'))

@app.route('/search',methods=["GET","post"])
def searchuser():
    exuname= users.find_one({'username' :request.values.get('unname')})
    if exuname is not None:
        return render_template('usersprofile.html')
    return "not exist"
  



    

    

if __name__=='__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)

