import psycopg2
from flask import jsonify,Flask,request
from datetime import datetime
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)
con = psycopg2.connect(
                host = "localhost",
                database = "tubesmbcbaru", #Tinggal Ganti jadi TUBESMBC yang ada dipostgres
                user = "adamhadipratama7",
                password = "adamhadip",
)

# @app.route("/")
# def pembina():
#     return f"""<form action ="/profil" method = "get">
#                 <label for ="Pembina MBC">Name:</label><br>
#                 <input id="fname" name="Pembina Big Data" value="Dr.Nyoman Bogi Aditya Karna,S.T,M.T."><br>
#                 <input id="fname" name="Pembina Multimedia" value="Sussi,S.Si,M.T."><br>
#                 <input id ="fname" name"Pembina Cyber Security" value="Dr.Eng.Favian Dewanta,S.T.,M.Eng.">
#                 <br>
#                 <input type = "submit" value="Submit">
#                 </form>"""

# @app.route("/profil")
# def hello(): 
#     return f"""Method :" {str(request.method)}
#             <br>
#             Pembina: {str(request.args.to_dict())}"""

class Mbc(Resource): 
    def get(self):
        try : 
            sql = con.cursor()
            sql.execute("""SELECT * FROM tubesmbc_baru""")
            asisten = sql.fetchall()
            result = jsonify(asistendancaas=asisten)
            result.status_code = 200
            return(result)
        except Exception as err : 
            print(err)
            result = jsonify("failed to fetch...")
            result.status_code = 400
            return(result)
        finally : 
            sql.close()
            
    def post(self) : 
        try :
            sql = con.cursor()
            _nama = request.form['name'] #tinggal ganti nama colum 
            _panggil = request.form['nama_panggil'] #tinggal ganti nama coloumn juga 
            _jeniskelamin = request.form['jenis_kelamin']
            _jurusan = request.form['jurusan']
            _angkatan = request.form['angkatan']
            _divisi = request.form['divisi']
            _status = request.form['status']
            _banyakprojek = request.form['banyak_project']
            _skill = request.form['skill']
            create_value = """INSERT INTO tubesmbc_baru (name,nama_panggil,Jenis_kelamin,jurusan,angkatan,divisi,status,banyak project,skill) VALUES(%s,%s)"""
            sql.execute(create_value,(_nama,_panggil,_jeniskelamin,_jurusan,_angkatan,_divisi,_status,_banyakprojek,_skill))
            con.commit()
            result = jsonify(data="User telah ditambahkan")
            result.status_code = 200
            return(result)
        except Exception as err : 
            print(err)
            result = jsonify(data="data gagal")
            result.status_code = 400
            return(result)
        finally : 
            sql.close()
                   
class Dospem(Resource): 
    def get(self):
        try : 
            sql = con.cursor()
            sql.execute("""SELECT * FROM dospem""")
            doospem = sql.fetchall()
            result = jsonify(dosenpembimbing=doospem)
            result.status_code = 200
            return(result)
        except Exception as err : 
            print(err)
            result = jsonify("failed to fetch...")
            result.status_code = 400
            return(result)
        finally : 
            sql.close()
            
    def post(self) : 
        try :
            sql = con.cursor()
            _nama = request.form['nama'] #tinggal ganti nama colum 
            _divisipem = request.form['divisi'] #tinggal ganti nama coloumn juga 
            create_value = """INSERT INTO tubesmbc_baru (name,divisi) VALUES(%s,%s)"""
            sql.execute(create_value,(_nama,_divisipem))
            con.commit()
            result = jsonify(data="User telah ditambahkan")
            result.status_code = 200
            return(result)
        except Exception as err : 
            print(err)
            result = jsonify(data="data gagal")
            result.status_code = 400
            return(result)
        finally : 
            sql.close()                   
                                  
api.add_resource(Mbc,"/caasdanasisten",endpoint='mbc')
api.add_resource(Dospem,"/dosenpembimbing",endpoint='Dospem')
app.run(host = "localhost",port = "3200")