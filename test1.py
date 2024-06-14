from flask import Flask,render_template,request,session,url_for
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import pymysql
import os
from werkzeug.utils import secure_filename
import joblib
import datetime
 
# for timezone()
import pytz
 

app=Flask(__name__)

UPLOAD_FOLDER='static/uploads/'

app.secret_key = "abc" 
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

model=joblib.load("Breast_cancer1.pkl")

model12=joblib.load("Lung_cancer1.pkl")

model123=joblib.load("Diabetes.pkl")

model1234=joblib.load("Disease_detection.pkl")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/machineproject'
db=SQLAlchemy(app)


#*************************************User Database part start here **********************************************************************


class User(db.Model):
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(5),nullable=False)
    date=db.Column(db.String(12),nullable=True)
    address=db.Column(db.String(100),nullable=False)
    gender=db.Column(db.String(5),nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True)

#*************************************User Database part end here **********************************************************************


#*************************************Booking Database part start here **********************************************************************

class Book(db.Model):
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    doctor=db.Column(db.String(200),nullable=False)
    date=db.Column(db.String(12),nullable=True)
    message=db.Column(db.String(100),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    time=db.Column(db.String(12),nullable=True)
    id = db.Column(db.Integer, primary_key=True)

#*************************************Booking Database part end here **********************************************************************



#*************************************Approved Database part start here **********************************************************************

class Approved(db.Model):
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    doctor=db.Column(db.String(200),nullable=False)
    date=db.Column(db.String(12),nullable=True)
    message=db.Column(db.String(100),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    time=db.Column(db.String(12),nullable=True)
    agree=db.Column(db.String(100),nullable=True)
    id = db.Column(db.Integer, primary_key=True)

#*************************************Approved Database part end here **********************************************************************



#************************************* Disease detection database part start here *************************************************

class Disease(db.Model):
    name=db.Column(db.String(100),nullable=False)
    name1=db.Column(db.String(100),nullable=False)
    name2=db.Column(db.String(100),nullable=False)
    name3=db.Column(db.String(100),nullable=False)
    name4=db.Column(db.String(100),nullable=False)
    name5=db.Column(db.String(100),nullable=False)
    name6=db.Column(db.String(100),nullable=False)
    name7=db.Column(db.String(100),nullable=False)
    name8=db.Column(db.String(100),nullable=False)
    name9=db.Column(db.String(100),nullable=False)
    name10=db.Column(db.String(100),nullable=False)
    name11=db.Column(db.String(100),nullable=False)
    name12=db.Column(db.String(100),nullable=False)
    name13=db.Column(db.String(100),nullable=False)
    name14=db.Column(db.String(100),nullable=False)
    name15=db.Column(db.String(100),nullable=False)
    name16=db.Column(db.String(100),nullable=False)
    name17=db.Column(db.String(100),nullable=False)
    name18=db.Column(db.String(100),nullable=False)
    name19=db.Column(db.String(100),nullable=False)
    name20=db.Column(db.String(100),nullable=False)
    name21=db.Column(db.String(100),nullable=False)
    name22=db.Column(db.String(100),nullable=False)
    name23=db.Column(db.String(100),nullable=False)
    name24=db.Column(db.String(100),nullable=False)
    name25=db.Column(db.String(100),nullable=False)
    name26=db.Column(db.String(100),nullable=False)
    name27=db.Column(db.String(100),nullable=False)
    name28=db.Column(db.String(100),nullable=False)
    name29=db.Column(db.String(100),nullable=False)
    name30=db.Column(db.String(100),nullable=False)
    name31=db.Column(db.String(100),nullable=False)
    name32=db.Column(db.String(100),nullable=False)
    name33=db.Column(db.String(100),nullable=False)
    name34=db.Column(db.String(100),nullable=False)
    name35=db.Column(db.String(100),nullable=False)
    name36=db.Column(db.String(100),nullable=False)
    name37=db.Column(db.String(100),nullable=False)
    name38=db.Column(db.String(100),nullable=False)
    name39=db.Column(db.String(100),nullable=False)
    name40=db.Column(db.String(100),nullable=False)
    name41=db.Column(db.String(100),nullable=False)
    name42=db.Column(db.String(100),nullable=False)
    name43=db.Column(db.String(100),nullable=False)
    name44=db.Column(db.String(100),nullable=False)
    name45=db.Column(db.String(100),nullable=False)
    name46=db.Column(db.String(100),nullable=False)
    name47=db.Column(db.String(100),nullable=False)
    name48=db.Column(db.String(100),nullable=False)
    name49=db.Column(db.String(100),nullable=False)
    name50=db.Column(db.String(100),nullable=False)
    name51=db.Column(db.String(100),nullable=False)
    name52=db.Column(db.String(100),nullable=False)
    name53=db.Column(db.String(100),nullable=False)
    name54=db.Column(db.String(100),nullable=False)
    name55=db.Column(db.String(100),nullable=False)
    name56=db.Column(db.String(100),nullable=False)
    name57=db.Column(db.String(100),nullable=False)
    name58=db.Column(db.String(100),nullable=False)
    name59=db.Column(db.String(100),nullable=False)
    name60=db.Column(db.String(100),nullable=False)
    name61=db.Column(db.String(100),nullable=False)
    name62=db.Column(db.String(100),nullable=False)
    id = db.Column(db.Integer, primary_key=True)

#************************************* Disease detection database part end here ***************************************************


#************************************* Medicine database part start here **********************************************************

class Medicine(db.Model):
    medicinename=db.Column(db.String(200),nullable=False)
    diseasename=db.Column(db.String(200),nullable=False)
    price=db.Column(db.String(20),nullable=False)
    img=db.Column(db.String(200),nullable=False)
    id = db.Column(db.Integer, primary_key=True)
#************************************* Medicine database part end here ************************************************************





#************************************* Doctor database part end here ************************************************************

class Doctor(db.Model):
    doctorname=db.Column(db.String(200),nullable=False)
    specialization=db.Column(db.String(200),nullable=False)
    degree=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    location=db.Column(db.String(200),nullable=False)
    img=db.Column(db.String(200),nullable=False)
    password=db.Column(db.String(50),nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    
#************************************* Doctor database part end here ************************************************************


#*************************************Index page start here **********************************************************************
@app.route("/")
def home():
    return render_template('index.html')
    
#*************************************Index page end here ************************************************************************




#*************************************Main page start here **********************************************************************

@app.route("/home")
def home1(): 
    if 'email' in session: 
        h4=Hum()
        l=h4.getname(session['email'])
        return render_template('home.html',l=l)
    

#*************************************Main page end here ************************************************************************



#*************************************Hum Class to fetch data form data base start here **********************************************************************

class Hum(): #class for user
        
    def getuserdetail(self,email1,password1):
        try:
            socks = db.session.execute(db.select(User)
                                       .filter_by(email=email1 )
                                       .filter_by(password=password1)
                                       .order_by(User.name)).scalars()
            for sock in socks:
                if(sock.name):
                    return sock.name
                else:
                    False
                    
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
        
    def getdoctordetail(self,email1,password1):
        try:
            socks = db.session.execute(db.select(Doctor)
                                       .filter_by(email=email1 )
                                       .filter_by(password=password1)
                                       .order_by(Doctor.doctorname)).scalars()
            for sock in socks:
                if(sock.doctorname):
                    return sock.doctorname
                else:
                    False
                    
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
    
    def getuser(self,email1):
        try:
            socks = db.session.execute(db.select(User)
                                       .filter_by(email=email1 )
                                       .order_by(User.name)).scalars()
            for sock in socks:
                if(sock.name):
                    l=[sock.name,sock.email,sock.password,sock.date,sock.address,sock.gender,sock.mobile]
                    return l
                else:
                    False
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
        
    def getid(self,email1):
        try:
            socks = db.session.execute(db.select(User)
                                       .filter_by(email=email1 )
                                       .order_by(User.name)).scalars()
            for sock in socks:
                if(sock.name):
                    return sock.id
                else:
                    False
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
    
    def getname(self,email1):
        try:
            socks = db.session.execute(db.select(User)
                                       .filter_by(email=email1 )
                                       .order_by(User.name)).scalars()
            for sock in socks:
                if(sock.name):
                    return sock.name
                else:
                    False
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
    
    def getdoctorname(self,email1):
        try:
            socks = db.session.execute(db.select(Doctor)
                                       .filter_by(email=email1 )
                                       .order_by(Doctor.doctorname)).scalars()
            for sock in socks:
                if(sock.doctorname):
                    return sock.doctorname
                else:
                    return False
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
        
    def getpatient(self,id1):
    
        try:
            socks = db.session.execute(db.select(Book)  
                                       .filter_by(id=id1)
                                       .order_by(Book.name)).scalars()
            for sock in socks:
                if(sock.name):
                    l=[sock.name,sock.email,sock.doctor,sock.date,sock.message,sock.age,sock.time]
                    return l
                else:
                    False
        except Exception as e:
                error_text = "<p>The error:<br>" + str(e) + "</p>"
                hed = '<h1>Something is broken.</h1>'
                return error_text+hed
            
    def getapproved(self):
            host='localhost'
            user = 'root'
            password = ''
            db = 'machineproject'

            try:
                con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
            except Exception as e:
                print('error',e)

            cur = con.cursor()
            cur.execute("SELECT * FROM approved")
            data = cur.fetchall()
            return data
    
    def getapproveddoctor(self,doctor1):
            try:
                socks = db.session.execute(db.select(Approved)
                                           .filter_by(doctor=doctor1)
                                           .order_by(Approved.name)).scalars()
                return socks
                                    
                
            except Exception as e:
                error_text = "<p>The error:<br>" + str(e) + "</p>"
                hed = '<h1>Something is broken.</h1>'
                return error_text+hed
        
        
    
    def getappointment(self,email1):
        try:
            socks = db.session.execute(db.select(Approved)
                                       .filter_by(email=email1 )
                                       .order_by(Approved.name)).scalars()
            return socks
                                
            
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
    
    def deleted(self,id1):
        d=Book.query.filter_by(id=id1).first()
        db.session.delete(d)
        db.session.commit()
        
        
    def getbook(self):
        host='localhost'
        user = 'root'
        password = ''
        db = 'machineproject'

        try:
            con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
        except Exception as e:
            print('error',e)

        cur = con.cursor()
        cur.execute("SELECT * FROM book")
        data = cur.fetchall()
        return data
        
    def getdoctor(self):
        
        host='localhost'
        user = 'root'
        password = ''
        db = 'machineproject'

        try:
            con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
        except Exception as e:
            print('error',e)

        cur = con.cursor()
        cur.execute("SELECT * FROM doctor")
        data = cur.fetchall()
        return data
    
    
    def getmedicine(self):
        host='localhost'
        user = 'root'
        password = ''
        db = 'machineproject'
        try:
            con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
        except Exception as e:
            print('error',e)
        cur = con.cursor()
        cur.execute("SELECT * FROM medicine")
        data = cur.fetchall()
        return data
    
    def getdisease(self,disease1):
        try:
            socks = db.session.execute(db.select(Disease)
                                   .filter_by(name=disease1 )
                                   .order_by(Disease.name)).scalars()
            return socks
        except Exception as e:
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return error_text+hed
    
#*************************************Hum Class to fetch data form data base end here **********************************************************************



#************************************* Medicine info fetch data from form page start here ***********************************************

@app.route('/addmedicine',methods=['GET','POST'])
def addmedicine():
    if request.method=='POST':
        medicinename1=request.form.get('medicine')
        diseasename1= request.form.get('disease')
        price1= request.form.get('price')
        file = request.files['file']
        picture = file.filename
        upload=Medicine(medicinename=medicinename1,diseasename=diseasename1,price=price1,img=picture)
        db.session.add(upload)
        db.session.commit()
        filename1 = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        h441=Hum()
        l=h441.getname(session['email'])
        return render_template('index123.html',l=l)
    return render_template('index123.html')

#************************************* Medicine fetch data from form page end here ************************************************



#************************************* Doctor info fetch data from form page start here ************************************************

@app.route('/adddoctor',methods=['GET','POST'])
def adddoctor():
    if request.method=='POST':
        doctorname1=request.form.get('doctor')
        specialization1= request.form.get('specialist')
        degree1= request.form.get('degree')
        email1= request.form.get('doctor_email')
        location1= request.form.get('address')
        file = request.files['file']
        password1=request.form.get('doctor_password')
        picture = file.filename
        upload=Doctor(doctorname=doctorname1,specialization=specialization1,degree=degree1,email=email1,location=location1,img=picture,password=password1)
        db.session.add(upload)
        db.session.commit()
        filename1 = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        h441=Hum()
        l=h441.getname(session['email'])
        return render_template('index123.html',l=l)
    return render_template('index123.html')

#************************************* Doctor info fetch data from form page end here ************************************************


#************************************* Fetch doctor details and display on the screen start here *************************************

@app.route("/doctor")
def doctor():  
    if 'email' in session:  
        h0=Hum()
        data=h0.getdoctor()
        return render_template('doctor.html',data=data)
    else:  
        err='Please login first'
        return render_template('login.html',err=err)

#************************************* Fetch doctor details and display on the screen end here *************************************



#************************************* approve the appointment as well as remove from the approve page start here ************************************************


@app.route('/<int:id>/approveclient/', methods=('POST',))
def approveclient(id):
    
    h555=Hum()  
    l=h555.getpatient(id)
    entry1 = Approved(name=l[0],email=l[1],doctor=l[2],date=l[3],message=l[4],age=l[5],time=l[6])
    db.session.add(entry1)
    db.session.commit()
    h555.deleted(id)
    data=h555.getbook()
    return render_template('approve.html',book=data)
    
#************************************* approve the appointment as well as remove from the approve page end here ************************************************



#************************************* remove from the approve page start here ************************************************

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    d=Approved.query.filter_by(id=id).first()
    db.session.delete(d)
    db.session.commit()
    h50=Hum()
    data=h50.getapproved()
    return render_template('approveappointment.html',data=data)
#*************************************  remove from the approve page end here ************************************************




#************************************* delete appointment by client from the database start here ************************************************

@app.route('/<int:id>/delete1/', methods=('POST',))
def delete1(id):
    if(id):
        d=Approved.query.filter_by(id=id).first()
        db.session.delete(d)
        db.session.commit()
    return render_template('clientapprove.html')
#*************************************  delete appointment by client from the database end here ************************************************


#*************************************  Fatch appointment by client from the database start here ************************************************

@app.route('/clientapprove', methods=['GET','POST'])
def clientapprove():
    if(request.method=='POST'):
        name=request.form.get('user_email')  #problem here ****************************************
        hu1=Hum()
        data=hu1.getappointment(name)
        if(data):
            return render_template('clientapprove.html',data=data)
        else:
            d="Appointment is not Approved"
            return render_template('clientapprove.html',d=d)
    return render_template('clientapprove.html')
#*************************************  Fatch appointment by client from the database end here ************************************************







#************************************* cancle the appointment start here **********************************************************************

@app.route('/<int:id>/deletee/', methods=('POST',))
def deletee(id):
    h51=Hum()
    h51.deleted(id)
    data=h51.getbook()
    return render_template('approve.html',book=data)


#************************************* cancle the appointment end here **********************************************************************



#*************************************Approveappointment page start here **********************************************************************

@app.route("/approveappointment")
def approveappointment():
    h145=Hum()
    data=h145.getapproved()
    return render_template('approveappointment.html',data=data)

#*************************************Approveappointment page end here ************************************************************************


#*************************************Medicine page start here **********************************************************************
   
@app.route("/index12")
def index12():
    h102=Hum()
    data=h102.getmedicine()
    return render_template('index12.html',data=data)
 
#*************************************Medicine page end here ************************************************************************


#*************************************Appointment page start here **********************************************************************

@app.route("/appointment")
def appointment():
    h120=Hum()
    data=h120.getdoctor()
    return render_template('appointment.html',data=data)
    
   
#*************************************Appointment page end here ************************************************************************

#*********************************** Doctor Profile details start here ***********************************************************
@app.route("/pateint")
def pateint():
    ha1=Hum()
    name=ha1.getdoctorname(session['email'])
    data=ha1.getapproveddoctor(name)
    return render_template('pateint.html',data=data)

@app.route("/doctorprofile")
def doctordetail():
    h130=Hum()
    d=h130.getdoctorname(session['email'])
    if(d):
        # using now() to get current time
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
        if current_time.hour<12:
            f="Good Morning Dr. "+d
            return render_template('doctorprofile.html',a=f)
        elif current_time.hour>=12 and current_time.hour<=17:
            f="Good Afternoon Dr. "+d
            return render_template('doctorprofile.html',a=f)
        else:
            f="Good Evening Dr. "+d
            return render_template('doctorprofile.html',a=f)
#*********************************** Doctor Profile details end here ***********************************************************


#*************************************update in profile function start here **********************************************************************

@app.route("/update", methods=['GET','POST']) 
def update():
    h3=Hum()
    a=h3.getid(session['email'])
    u=User.query.filter_by(id=a).first()
    if(request.method=='POST'):
        u.name=request.form['user_name']
        u.mobile=request.form['user_mobile']
        u.email=request.form['user_email']
        u.password=request.form['user_password']
        u.address=request.form['user_address']
        u.gender=request.form['user_gender']
        u.date=request.form['user_dof']
        try:
            db.session.commit()
        except:
            return "there was a problem updating that"
    h1=Hum()
    a=h1.getuser(session['email'])
    return render_template('profile.html',l=a)


#*************************************update in profile function end here ************************************************************************



#*************************************Medicine page start here **********************************************************************

@app.route("/medicine")
def medicine():
    if 'email' in session:  
        return render_template('medicine.html')
    else:  
        err='Please login first'
        return render_template('login.html',err=err)

#*************************************Medicine page end here ************************************************************************


#*************************************Admin page start here **********************************************************************
    
@app.route("/index123")
def index123():
    h41=Hum()
    l2=h41.getid(session['email'])
    
    if 'email' in session and l2==1: 
        
        l=h41.getname(session['email'])
        return render_template('index123.html',l=l)
    else:  
        err='You do not have authority'
        return render_template('error.html',err=err)
 
#*************************************Admin page end here ************************************************************************


#*************************************Approve function to fetch data from (Book) database start here **********************************************************************
        
@app.route("/approve")
def approve():
    if 'email' in session: 
        host='localhost'
        user = 'root'
        password = ''
        db = 'machineproject'

        try:
            con = pymysql.connect(host=host,user=user,password=password,db=db, use_unicode=True, charset='utf8')
        except Exception as e:
            print('error',e)

        cur = con.cursor()
        cur.execute("SELECT * FROM book")
        data = cur.fetchall()
        return render_template('approve.html',book=data)
    else:  
        err='Please login first'
        return render_template('login.html',err=err)

#*************************************Approve function to fetch data from database end here ************************************************************************


#*************************************Disease test Model start here **********************************************************************

@app.route("/test11")
def test11():
    return render_template('test_15.html')

@app.route("/test10",methods=['GET','POST'])
def test10():
    if (request.method == 'POST'):
        disease = request.form.get('browser')
        h1001= Hum()
        data=h1001.getdisease(disease)
        return render_template('test_16.html',data=data)
@app.route("/test12",methods=['GET','POST'])
def test12():    
    if (request.method == 'POST'):
        itching = request.form.get('itching')
        skin_rash = request.form.get('skin_rash')
        nodal_skin_eruptions = request.form.get('nodal_skin_eruptions')
        continuous_sneezing = request.form.get('continuous_sneezing')
        shivering = request.form.get('shivering')
        chills = request.form.get('chills')

        joint_pain = request.form.get('joint_pain')
        stomach_pain = request.form.get('stomach_pain')
        acidity = request.form.get('acidity')
        ulcers_on_tongue = request.form.get('ulcers_on_tongue')
        muscle_wasting = request.form.get('muscle_wasting')
        vomiting = request.form.get('vomiting')

        burning_micturition = request.form.get('burning_micturition')
        spotting_urination = request.form.get('spotting_urination')
        fatigue = request.form.get('fatigue')
        weight_gain = request.form.get('weight_gain')
        anxiety = request.form.get('anxiety')
        cold_hands_and_feets = request.form.get('cold_hands_and_feets')

        mood_swings = request.form.get('mood_swings')
        weight_loss = request.form.get('weight_loss')
        restlessness = request.form.get('restlessness')
        lethargy = request.form.get('lethargy')
        patches_in_throat = request.form.get('patches_in_throat')
        irregular_sugar_level = request.form.get('irregular_sugar_level')

        cough = request.form.get('cough')
        high_fever = request.form.get('high_fever')
        sunken_eyes = request.form.get('sunken_eyes')
        breathlessness = request.form.get('breathlessness')
        sweating = request.form.get('sweating')
        dehydration = request.form.get('dehydration')

        indigestion = request.form.get('indigestion')
        headache = request.form.get('headache')
        yellowish_skin = request.form.get('yellowish_skin')
        dark_urine = request.form.get('dark_urine')
        nausea = request.form.get('nausea')
        loss_of_appetite = request.form.get('loss_of_appetite')

        pain_behind_the_eyes = request.form.get('pain_behind_the_eyes')
        back_pain = request.form.get('back_pain')
        constipation = request.form.get('constipation')
        abdominal_pain = request.form.get('abdominal_pain')
        diarrhoea = request.form.get('diarrhoea')
        mild_fever = request.form.get('mild_fever')

        yellow_urine = request.form.get('yellow_urine')
        yellowing_of_eyes = request.form.get('yellowing_of_eyes')
        acute_liver_failure = request.form.get('acute_liver_failure')
        fluid_overload = request.form.get('fluid_overload')
        swelling_of_stomach = request.form.get('swelling_of_stomach')
        swelled_lymph_nodes = request.form.get('swelled_lymph_nodes')

        malaise = request.form.get('malaise')
        blurred_and_distorted_vision = request.form.get('blurred_and_distorted_vision')
        phlegm = request.form.get('phlegm')
        throat_irritation = request.form.get('throat_irritation')
        redness_of_eyes = request.form.get('redness_of_eyes')
        sinus_pressure = request.form.get('sinus_pressure')

        runny_nose = request.form.get('runny_nose')
        congestion = request.form.get('congestion')
        chest_pain = request.form.get('chest_pain')
        weakness_in_limbs = request.form.get('weakness_in_limbs')
        fast_heart_rate = request.form.get('fast_heart_rate')
        pain_during_bowels_movement= request.form.get('pain_during_bowels_movement')

        pain_in_anal_region = request.form.get('pain_in_anal_region')
        bloody_stool = request.form.get('bloody_stool')
        irritation_in_anus = request.form.get('irritation_in_anus')
        neck_pain = request.form.get('neck_pain')
        dizziness = request.form.get('dizziness')
        cramps = request.form.get('cramps')

        bruising = request.form.get('bruising')
        obesity = request.form.get('obesity')
        swollen_legs = request.form.get('swollen_legs')
        swollen_blood_vessels = request.form.get('swollen_blood_vessels')
        puffy_face_and_eyes = request.form.get('puffy_face_and_eyes')
        enlarged_thyroid = request.form.get('enlarged_thyroid')

        brittle_nails = request.form.get('brittle_nails')
        swollen_extremeties = request.form.get('swollen_extremeties')
        excessive_hunger = request.form.get('excessive_hunger')
        extra_marital_contacts = request.form.get('extra_marital_contacts')
        drying_and_tingling_lips = request.form.get('drying_and_tingling_lips')
        slurred_speech = request.form.get('slurred_speech')

        knee_pain = request.form.get('knee_pain')
        hip_joint_pain = request.form.get('hip_joint_pain')
        muscle_weakness = request.form.get('muscle_weakness')
        stiff_neck = request.form.get('stiff_neck')
        swelling_joints = request.form.get('swelling_joints')
        movement_stiffness = request.form.get('movement_stiffness')

        spinning_movements = request.form.get('spinning_movements')
        loss_of_balance = request.form.get('loss_of_balance')

        unsteadiness = request.form.get('unsteadiness')
        weakness_of_one_body_side = request.form.get('weakness_of_one_body_side')
        loss_of_smell = request.form.get('loss_of_smell')
        bladder_discomfort = request.form.get('bladder_discomfort')
        foul_smell_of_urine = request.form.get('foul_smell_of_urine')

        continuous_feel_of_urine = request.form.get('continuous_feel_of_urine')
        passage_of_gases = request.form.get('passage_of_gases')
        internal_itching = request.form.get('internal_itching')
        toxic_look = request.form.get('toxic_look')
        depression = request.form.get('depression')
        irritability = request.form.get('irritability')

        muscle_pain = request.form.get('muscle_pain')
        altered_sensorium = request.form.get('altered_sensorium')
        red_spots_over_body = request.form.get('red_spots_over_body')
        belly_pain = request.form.get('belly_pain')
        abnormal_menstruation = request.form.get('abnormal_menstruation')
        dischromic_patches = request.form.get('dischromic_patches')

        watering_from_eyes = request.form.get('watering_from_eyes')
        increased_appetite = request.form.get('increased_appetite')
        polyuria = request.form.get('polyuria')
        family_history = request.form.get('family_history')
        mucoid_sputum = request.form.get('mucoid_sputum')
        rusty_sputum = request.form.get('rusty_sputum')

        lack_of_concentration = request.form.get('lack_of_concentration')
        visual_disturbances = request.form.get('visual_disturbances')
        receiving_blood_transfusion = request.form.get('receiving_blood_transfusion')
        receiving_unsterile_injections = request.form.get('receiving_unsterile_injections')
        coma = request.form.get('coma')
        stomach_bleeding = request.form.get('stomach_bleeding')

        distention_of_abdomen = request.form.get('distention_of_abdomen')
        history_of_alcohol_consumption = request.form.get('history_of_alcohol_consumption')
        fluid_overload = request.form.get('fluid_overload')
        blood_in_sputum = request.form.get('blood_in_sputum')
        prominent_veins_on_calf = request.form.get('prominent_veins_on_calf')

        palpitations = request.form.get('palpitations')
        painful_walking = request.form.get('painful_walking')
        pus_filled_pimples = request.form.get('pus_filled_pimples')
        blackheads = request.form.get('blackheads')
        scurring = request.form.get('scurring')
        skin_peeling = request.form.get('skin_peeling')

        silver_like_dusting = request.form.get('silver_like_dusting')
        small_dents_in_nails = request.form.get('small_dents_in_nails')
        inflammatory_nails = request.form.get('inflammatory_nails')
        blister = request.form.get('blister')
        red_sore_around_nose = request.form.get('red_sore_around_nose')

        yellow_crust_ooze = request.form.get('yellow_crust_ooze')

        l=[itching,skin_rash,nodal_skin_eruptions,continuous_sneezing,shivering,chills,joint_pain,stomach_pain,acidity,ulcers_on_tongue,muscle_wasting,vomiting,burning_micturition,spotting_urination,fatigue,weight_gain,anxiety,cold_hands_and_feets,mood_swings,weight_loss,restlessness,lethargy,patches_in_throat,irregular_sugar_level,cough,high_fever,sunken_eyes,breathlessness,sweating,dehydration,indigestion,headache,yellowish_skin,dark_urine,nausea,loss_of_appetite,pain_behind_the_eyes,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine,yellowing_of_eyes,acute_liver_failure,fluid_overload,swelling_of_stomach,swelled_lymph_nodes,malaise,blurred_and_distorted_vision,phlegm,throat_irritation,redness_of_eyes,sinus_pressure,runny_nose,congestion,chest_pain,weakness_in_limbs,fast_heart_rate,pain_during_bowels_movement,pain_in_anal_region,bloody_stool,irritation_in_anus,neck_pain,dizziness,cramps,bruising,obesity,swollen_legs,swollen_blood_vessels,puffy_face_and_eyes,enlarged_thyroid,brittle_nails,swollen_extremeties,excessive_hunger,extra_marital_contacts,drying_and_tingling_lips,slurred_speech,knee_pain,hip_joint_pain,muscle_weakness,stiff_neck,swelling_joints,movement_stiffness,spinning_movements,loss_of_balance,unsteadiness,weakness_of_one_body_side,loss_of_smell,bladder_discomfort,foul_smell_of_urine,continuous_feel_of_urine,passage_of_gases,internal_itching,toxic_look,depression,irritability,muscle_pain,altered_sensorium,red_spots_over_body,belly_pain,abnormal_menstruation,dischromic_patches,watering_from_eyes,increased_appetite,polyuria,family_history,mucoid_sputum,rusty_sputum,lack_of_concentration,visual_disturbances,receiving_blood_transfusion,receiving_unsterile_injections,coma,stomach_bleeding,distention_of_abdomen,history_of_alcohol_consumption,fluid_overload,blood_in_sputum,prominent_veins_on_calf,palpitations,painful_walking,pus_filled_pimples,blackheads,scurring,skin_peeling,silver_like_dusting,small_dents_in_nails,inflammatory_nails,blister,red_sore_around_nose,yellow_crust_ooze]
        l1=[]
        for i in l:
            if(i):
                n1=1
            else:
                n1=0
            l1.append(n1)
            
        features_value=np.array([l1])
        m1=model1234.predict(features_value)
        d={15:"Fungal infection",
           4:"Allergy",16:"GRED",9:"Chronic cholestasis",
           14:"Drug Reaction",33:"Peptic ulcer disease",
           1:"AIDS",12:"Diabetes",17:"Gastroenteritis",
           6:"Bronchial Asthma",23:"Hypertension",30:"Migraine",
           7:"Cervical spondylosis",32:"Paralysis (brain hemorrhage)",
           28:"Jaundice",29:"Malaria",8:"Chicken pox",
           11:"Dengue",37:"Typhoid",40:"Hepatitis A",
           19:"Hepatitis B",20:"Hepatitis C",21:"Hepatitis D",
           22:"Hepatitis E",3:"Alcoholic hepatitis",
           36:"Tuberculosis",10:"Common Cold",34:"Pneumonia",
           13:"Dimorphic hemmorhoids(piles)",18:"Heart Attack",
           39:"Varicose veins",26:"Hypothyroidism",24:"Hyperthyroidism",
           25:"Hypoglycemia",31:"Osteoarthristis",5:"Arthritis",
           0:"(vertigo) Paroymsal  Positional Vertigo",
           2:"Acne",38:"Urinary tract infection",35:"Psoriasis",
           27:"Impetigo",15:"Fungal Infection"}
        
        for i,val in d.items():
            if m1[0]==i:    
                val1="You have "+val
                return render_template('test12.html',abc=val1)
    #return render_template('test11.html')


#*************************************Disease test Model end here ************************************************************************



#*************************************Login page start here **********************************************************************

@app.route("/login",methods=['GET','POST']) 
def login():
    if (request.method == 'POST'):
        session['email']= request.form.get('user_name')
        name1=session['email']
        password1 = request.form.get('user_password')
        h=Hum()
        l=h.getuserdetail(name1,password1)
        d=h.getdoctordetail(name1, password1)
        if(l):
            if(l==1):
               n=h.getname(name1)
               return render_template('index123.html',l=n)
            else:
               return render_template('home.html',l=l)
        if(d):
            # using now() to get current time
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            if current_time.hour<12:
                f="Good Morning Dr. "+d
                return render_template('doctorprofile.html',a=f)
            elif current_time.hour>=12 and current_time.hour<=17:
                f="Good Afternoon Dr. "+d
                return render_template('doctorprofile.html',a=f)
            else:
                f="Good Evening Dr. "+d
                return render_template('doctorprofile.html',a=f)

        else:
            la = 'Please register your self first go to the signup page'
            return render_template('login.html',la=la)

    return render_template('login.html')

#*************************************Login html end here ************************************************************************

   

# **************************Logout function start here  *****************************************************************************

@app.route("/logout")
def logout():
    if 'email' in session:
        session.pop('email',None)
        return render_template('index.html')
    else:  
       return '<h1>user already logged out</h1>' 
    

#*************************************Logout function end here **********************************************************************


#************************************* Registeration function start here**********************************************************************

@app.route("/registration", methods=['GET','POST'])#registration function
def registration():

    if(request.method=='POST'):
        name1=request.form.get('user_name')
        mobile1=request.form.get('user_mobile')
        email1=request.form.get('user_email')
        password1=request.form.get('user_password')
        address1=request.form.get('user_address')
        gender1=request.form.get('gender')
        h5=Hum()
        if(h5.getid(email1)):
            dil="You have already registered please login"
            return render_template('registration.html',dil=dil)
        else:
            entry = User(name=name1, mobile=mobile1, email=email1,password=password1,address=address1,gender=gender1)
            db.session.add(entry)
            db.session.commit()
            return render_template('registration.html')

    return render_template('registration.html')

#************************************* Registeration function end here************************************************************



#************************************* Booking function start here****************************************************************

@app.route("/booking", methods=['GET','POST']) #booking function
def booking():
    if(request.method=='POST'):
        name1=request.form.get('user_name')
        email1=request.form.get('user_email')
        doctor1=request.form.get('doctor')
        appointment1=request.form.get('appointment_date')
        message1=request.form.get('message')
        age1=request.form.get('user_age')
        time1=request.form.get('appointment_time')
        entry1 = Book(name=name1,email=email1,doctor=doctor1,date=appointment1,message=message1,age=age1,time=time1)
        db.session.add(entry1)
        db.session.commit()
        n1="your appointment is booked"
    return render_template('appointment.html',n=n1)

#************************************* Booking function end here**********************************************************************



#************************************* profile page start here**********************************************************************

@app.route("/profile", methods=['GET','POST']) 
def profile():
    if 'email' in session:
    
        h1=Hum()
        a=h1.getuser(session['email'])
        
        return render_template('profile.html',l=a)
    else:  
        err='Please login first'
        return render_template('login.html',err=err)

#************************************* profile page end here**********************************************************************

    

    
if __name__ == "__main__":
    app.run(debug=True)

    