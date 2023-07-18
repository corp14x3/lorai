from flask import Flask , request , render_template , redirect , url_for , flash

import sqlite3 , random, os , subprocess, pymem , datetime , requests as r

username = os.getlogin()
con = sqlite3.connect("lorai.db", check_same_thread=False) 

cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS programsc (pn TEXT, pw TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS drpc (header TEXT, details TEXT , pictureheader TEXT , picturelink TEXT , header1 TEXT , link1 TEXT , header2 TEXT , link2 TEXT )")

app = Flask(__name__,template_folder='./pages')
app.debug = True
app.config['SECRET_KEY'] = str(random.randint(0, 74123))

@app.route("/",methods=["GET"])
def lorai():
    return render_template("lorai.html")

@app.route("/zaman-al", methods=["GET"])
def zaman_al():
    zaman = datetime.datetime.now()
    zaman = zaman.strftime("%d,%B,%A ; %H:%M:%S")
    return zaman

@app.route("/shortcuts",methods=["GET","POST"])
def loraiprogram():
    liste = cursor.execute("SELECT * FROM programsc")
    data = liste.fetchall()
    if request.method == "POST":
        progn = request.form.get("programname")
        progw = request.form.get("programway")
        cursor.execute("INSERT INTO programsc VALUES(?,?)",(progn,progw))
        con.commit()
        flash(message='Kısayol başarıyla eklendi')
        return redirect('shortcuts')
    return render_template('loraisc.html',liste = data)

@app.route("/shortcuts-delete",methods=["GET","POST"])
def loraiprogramd():
    liste = cursor.execute("SELECT * FROM programsc")
    data = liste.fetchall()
    if request.method == "POST":
        progn = request.form.get("programname")
        cursor.execute("DELETE FROM programsc WHERE pn = ?",[progn])
        con.commit()
        flash(message='Kısayol başarıyla kaldırıldı')
        return redirect('shortcuts-delete')
    return render_template('loraiscd.html',liste = data)

@app.route("/discordrpc",methods=["GET","POST"])
def lorairpc():
    from lorairpc import LoraiDRPC
    modulefd = LoraiDRPC()
    if request.method == "POST":
        if "button" in request.form:
            subprocess.Popen(r"C:\Users\{}\Desktop\lorai\lorairpc.py".format(username),shell=True)
        # elif "button2" in request.form:
        #     modulefd.presence(status=False)
        else:
            header = request.form.get("header")
            details = request.form.get("details")
            pictureheader = request.form.get("pictureheader")
            picturelink = request.form.get("picturelink")
            header1 = request.form.get("header1")
            link1 = request.form.get("link1")
            header2 = request.form.get("header2")
            link2 = request.form.get("link2")
            liste = con.execute("SELECT * FROM  drpc")
            data = liste.fetchall()

            if data == []:
                cursor.execute("INSERT INTO drpc VALUES(?,?,?,?,?,?,?,?)",(header,details,pictureheader,picturelink,header1,link1,header2,link2))
                con.commit()
            else:
                cursor.execute("UPDATE drpc SET header = ? ",[header])
                cursor.execute("UPDATE drpc SET details = ? ",[details])
                cursor.execute("UPDATE drpc SET pictureheader = ? ",[pictureheader])
                cursor.execute("UPDATE drpc SET picturelink = ? ",[picturelink])
                cursor.execute("UPDATE drpc SET header1 = ? ",[header1])
                cursor.execute("UPDATE drpc SET link1 = ? ",[link1])
                cursor.execute("UPDATE drpc SET header2 = ? ",[header2])
                cursor.execute("UPDATE drpc SET link2 = ? ",[link2])
                con.commit()
        
        return redirect('discordrpc')
    return render_template('loraidc.html')



if __name__ == '__main__':
    app.run(port=7432)