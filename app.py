from flask import Flask, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hindi_mos.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vmdudtukdfqgzh:f85422aa8aa9c517b117257ff8bb373a4dc0602ff671cebe4492b030ef9d10b1@ec2-52-4-111-46.compute-1.amazonaws.com:5432/d11a4b2d4nat80'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wcrxqclnjrxrlt:188f191d2b91a07cfe9cae6246213b1938b40ad3f1838732188f3583512bd026@ec2-52-45-179-101.compute-1.amazonaws.com:5432/d1ti508djvmqli' 
# Initialize the database
db = SQLAlchemy(app)

# Create db Model
class Listener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    gender = db.Column(db.String(10), nullable=False)
    mother_tongue = db.Column(db.Integer, nullable=True)

    page_1 = db.relationship('Page1score', backref='listener',  uselist=False)

    # Create a function to return a string when we add something
    def __repr__(self):
        return '<First_name %r, last_name %r>' % self.first_name, self.last_name

class Page1score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('listener.id'))

    sample_1 = db.Column(db.Integer)
    sample_2 = db.Column(db.Integer)
    sample_3 = db.Column(db.Integer)
    sample_4 = db.Column(db.Integer)
    sample_5 = db.Column(db.Integer)
    sample_6 = db.Column(db.Integer)
    sample_7 = db.Column(db.Integer)
    sample_8 = db.Column(db.Integer)
    sample_9 = db.Column(db.Integer)
    sample_10 = db.Column(db.Integer)

class Page2score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('listener.id'))

    sample_11 = db.Column(db.Integer)
    sample_12 = db.Column(db.Integer)
    sample_13 = db.Column(db.Integer)
    sample_14 = db.Column(db.Integer)
    sample_15 = db.Column(db.Integer)
    sample_16 = db.Column(db.Integer)
    sample_17 = db.Column(db.Integer)
    sample_18 = db.Column(db.Integer)
    sample_19 = db.Column(db.Integer)
    sample_20 = db.Column(db.Integer)


class Page3score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('listener.id'))

    sample_21 = db.Column(db.Integer)
    sample_22 = db.Column(db.Integer)
    sample_23 = db.Column(db.Integer)
    sample_24 = db.Column(db.Integer)
    sample_25 = db.Column(db.Integer)
    sample_26 = db.Column(db.Integer)
    sample_27 = db.Column(db.Integer)
    sample_28 = db.Column(db.Integer)
    sample_29 = db.Column(db.Integer)
    sample_30 = db.Column(db.Integer)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/forms', methods=["POST", "GET"])
def forms():

    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        mother_tongue = request.form['mother_tongue']

        new_listener = Listener(first_name=first_name, last_name=last_name, gender=gender, mother_tongue=mother_tongue)

        # Push to Database
        try:
            db.session.add(new_listener)
            db.session.commit()
            return render_template("instructions.html", listener = new_listener)
        except Exception as e:
            print(e)
            return "There was an error adding your details."
    elif request.method == "GET":
        return render_template("forms.html")

@app.route('/instructions')
def instructions():
    render_template("instructions.html")

@app.route('/a_evaluation/<int:id>', methods=["POST", "GET"])  ######################### A ##############################3
def a_evaluation(id):
    if request.method == "POST":
        s_1 = request.form['sample_1']
        s_2 = request.form['sample_2']
        s_3 = request.form['sample_3']
        s_4 = request.form['sample_4']
        s_5 = request.form['sample_5']
        s_6 = request.form['sample_6']
        s_7 = request.form['sample_7']
        s_8 = request.form['sample_8']
        s_9 = request.form['sample_9']
        s_10 = request.form['sample_10']

        page_1_scores = Page1score(
                person_id = id,
                sample_1=s_1,
                sample_2=s_2,
                sample_3=s_3,
                sample_4=s_4,
                sample_5=s_5,
                sample_6=s_6,
                sample_7=s_7,
                sample_8=s_8,
                sample_9=s_9,
                sample_10=s_10
                )

        # Push to Database
        try:
            db.session.add(page_1_scores)
            db.session.commit()
            return render_template("a_evaluation_2.html", listener_id=id)
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET": ############### BIFURCATION ################
        x = id % 3
        if x==0:
            return render_template("a_evaluation.html", listener_id = id)
        elif x==1:
            return render_template("b_evaluation.html", listener_id = id)
        elif x==2:
            return render_template("c_evaluation.html", listener_id = id)

@app.route('/b_evaluation/<int:id>', methods=["POST", "GET"])      ############################# B ###############################
def b_evaluation(id):
    if request.method == "POST":
        s_1 = request.form['sample_1']
        s_2 = request.form['sample_2']
        s_3 = request.form['sample_3']
        s_4 = request.form['sample_4']
        s_5 = request.form['sample_5']
        s_6 = request.form['sample_6']
        s_7 = request.form['sample_7']
        s_8 = request.form['sample_8']
        s_9 = request.form['sample_9']
        s_10 = request.form['sample_10']

        page_1_scores = Page1score(
                person_id = id,
                sample_1=s_1,
                sample_2=s_2,
                sample_3=s_3,
                sample_4=s_4,
                sample_5=s_5,
                sample_6=s_6,
                sample_7=s_7,
                sample_8=s_8,
                sample_9=s_9,
                sample_10=s_10
                )

        # Push to Database
        try:
            db.session.add(page_1_scores)
            db.session.commit()
            return render_template("b_evaluation_2.html", listener_id=id)
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET": 
        return render_template("b_evaluation.html", listener_id = id)


@app.route('/c_evaluation/<int:id>', methods=["POST", "GET"])      ############################# C ###############################
def c_evaluation(id):
    if request.method == "POST":
        s_1 = request.form['sample_1']
        s_2 = request.form['sample_2']
        s_3 = request.form['sample_3']
        s_4 = request.form['sample_4']
        s_5 = request.form['sample_5']
        s_6 = request.form['sample_6']
        s_7 = request.form['sample_7']
        s_8 = request.form['sample_8']
        s_9 = request.form['sample_9']
        s_10 = request.form['sample_10']

        page_1_scores = Page1score(
                person_id = id,
                sample_1=s_1,
                sample_2=s_2,
                sample_3=s_3,
                sample_4=s_4,
                sample_5=s_5,
                sample_6=s_6,
                sample_7=s_7,
                sample_8=s_8,
                sample_9=s_9,
                sample_10=s_10
                )

        # Push to Database
        try:
            db.session.add(page_1_scores)
            db.session.commit()
            return render_template("c_evaluation_2.html", listener_id=id)
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET": 
        return render_template("c_evaluation.html", listener_id = id)

@app.route('/a_evaluation_2/<int:id>', methods=["POST", "GET"]) ################### A #######################
def a_evaluation_2(id):
    if request.method == "POST":
        s_11 = request.form['sample_11']
        s_12 = request.form['sample_12']
        s_13 = request.form['sample_13']
        s_14 = request.form['sample_14']
        s_15 = request.form['sample_15']
        s_16 = request.form['sample_16']
        s_17 = request.form['sample_17']
        s_18 = request.form['sample_18']
        s_19 = request.form['sample_19']
        s_20 = request.form['sample_20']

        page_2_scores = Page2score(
                person_id = id,
                sample_11=s_11,
                sample_12=s_12,
                sample_13=s_13,
                sample_14=s_14,
                sample_15=s_15,
                sample_16=s_16,
                sample_17=s_17,
                sample_18=s_18,
                sample_19=s_19,
                sample_20=s_20
                )

        # Push to Database
        try:
            db.session.add(page_2_scores)
            db.session.commit()
            return render_template("a_evaluation_3.html", listener_id=id)
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET":
        return render_template("a_evaluation_2.html", listener_id = id)


@app.route('/b_evaluation_2/<int:id>', methods=["POST", "GET"]) ################### B #######################
def b_evaluation_2(id):
    if request.method == "POST":
        s_11 = request.form['sample_11']
        s_12 = request.form['sample_12']
        s_13 = request.form['sample_13']
        s_14 = request.form['sample_14']
        s_15 = request.form['sample_15']
        s_16 = request.form['sample_16']
        s_17 = request.form['sample_17']
        s_18 = request.form['sample_18']
        s_19 = request.form['sample_19']
        s_20 = request.form['sample_20']

        page_2_scores = Page2score(
                person_id = id,
                sample_11=s_11,
                sample_12=s_12,
                sample_13=s_13,
                sample_14=s_14,
                sample_15=s_15,
                sample_16=s_16,
                sample_17=s_17,
                sample_18=s_18,
                sample_19=s_19,
                sample_20=s_20
                )

        # Push to Database
        try:
            db.session.add(page_2_scores)
            db.session.commit()
            return render_template("b_evaluation_3.html", listener_id=id)
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET":
        return render_template("b_evaluation_2.html", listener_id = id)

@app.route('/c_evaluation_2/<int:id>', methods=["POST", "GET"]) ################### C #######################
def c_evaluation_2(id):
    if request.method == "POST":
        s_11 = request.form['sample_11']
        s_12 = request.form['sample_12']
        s_13 = request.form['sample_13']
        s_14 = request.form['sample_14']
        s_15 = request.form['sample_15']
        s_16 = request.form['sample_16']
        s_17 = request.form['sample_17']
        s_18 = request.form['sample_18']
        s_19 = request.form['sample_19']
        s_20 = request.form['sample_20']

        page_2_scores = Page2score(
                person_id = id,
                sample_11=s_11,
                sample_12=s_12,
                sample_13=s_13,
                sample_14=s_14,
                sample_15=s_15,
                sample_16=s_16,
                sample_17=s_17,
                sample_18=s_18,
                sample_19=s_19,
                sample_20=s_20
                )

        # Push to Database
        try:
            db.session.add(page_2_scores)
            db.session.commit()
            return render_template("c_evaluation_3.html", listener_id=id)
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET":
        return render_template("c_evaluation_2.html", listener_id = id)

@app.route('/a_evaluation_3/<int:id>', methods=["POST", "GET"]) ################### A ########################
def a_evaluation_3(id):
    if request.method == "POST":
        s_21 = request.form['sample_21']
        s_22 = request.form['sample_22']
        s_23 = request.form['sample_23']
        s_24 = request.form['sample_24']
        s_25 = request.form['sample_25']
        s_26 = request.form['sample_26']
        s_27 = request.form['sample_27']
        s_28 = request.form['sample_28']
        s_29 = request.form['sample_29']
        s_30 = request.form['sample_30']

        page_3_scores = Page3score(
                person_id = id,
                sample_21=s_21,
                sample_22=s_22,
                sample_23=s_23,
                sample_24=s_24,
                sample_25=s_25,
                sample_26=s_26,
                sample_27=s_27,
                sample_28=s_28,
                sample_29=s_29,
                sample_30=s_30
                )

        # Push to Database
        try:
            db.session.add(page_3_scores)
            db.session.commit()
            return render_template("thanks.html")
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET":
        return render_template("a_evaluation_3.html", listener_id = id)

@app.route('/b_evaluation_3/<int:id>', methods=["POST", "GET"]) ################### B ########################
def b_evaluation_3(id):
    if request.method == "POST":
        s_21 = request.form['sample_21']
        s_22 = request.form['sample_22']
        s_23 = request.form['sample_23']
        s_24 = request.form['sample_24']
        s_25 = request.form['sample_25']
        s_26 = request.form['sample_26']
        s_27 = request.form['sample_27']
        s_28 = request.form['sample_28']
        s_29 = request.form['sample_29']
        s_30 = request.form['sample_30']

        page_3_scores = Page3score(
                person_id = id,
                sample_21=s_21,
                sample_22=s_22,
                sample_23=s_23,
                sample_24=s_24,
                sample_25=s_25,
                sample_26=s_26,
                sample_27=s_27,
                sample_28=s_28,
                sample_29=s_29,
                sample_30=s_30
                )

        # Push to Database
        try:
            db.session.add(page_3_scores)
            db.session.commit()
            return render_template("thanks.html")
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET":
        return render_template("b_evaluation_3.html", listener_id = id)

@app.route('/c_evaluation_3/<int:id>', methods=["POST", "GET"]) ################### C ########################
def c_evaluation_3(id):
    if request.method == "POST":
        s_21 = request.form['sample_21']
        s_22 = request.form['sample_22']
        s_23 = request.form['sample_23']
        s_24 = request.form['sample_24']
        s_25 = request.form['sample_25']
        s_26 = request.form['sample_26']
        s_27 = request.form['sample_27']
        s_28 = request.form['sample_28']
        s_29 = request.form['sample_29']
        s_30 = request.form['sample_30']

        page_3_scores = Page3score(
                person_id = id,
                sample_21=s_21,
                sample_22=s_22,
                sample_23=s_23,
                sample_24=s_24,
                sample_25=s_25,
                sample_26=s_26,
                sample_27=s_27,
                sample_28=s_28,
                sample_29=s_29,
                sample_30=s_30
                )

        # Push to Database
        try:
            db.session.add(page_3_scores)
            db.session.commit()
            return render_template("thanks.html")
        except Exception as e:
            print(e)
            return "There was an error adding your scores."

    elif request.method == "GET":
        return render_template("c_evaluation_3.html", listener_id = id)

@app.route('/thanks', methods=["POST", "GET"])
def thanks():
    return render_template("thanks.html")

@app.route('/exit', methods=["POST", "GET"])
def exit():
    return render_template("exit.html")


