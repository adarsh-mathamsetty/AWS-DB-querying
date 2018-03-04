import mysql.connector
from flask import Flask, request, render_template, make_response
import csv

app = Flask(__name__)
data = ''
cnx = mysql.connector.connect(host='mathdb.ckejskjwfpqe.us-east-2.rds.amazonaws.com', user='Adarsh', password='Adarsh1994', db='ucdata')
    
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)
lists=[]
@app.route('/')
def index():
    return render_template('a2.html')

@app.route('/delete', methods=['POST'])
def delete():
    state = request.form['state']
    tot = request.form['tot']
    
        
    #query = "SELECT latitude FROM earth WHERE place LIKE '%%%s%%'" % (file_name)
    query = "select alias from uc  WHERE STATE = '%s' or CITY = '%s' and tot_enroll > %s;"%(state,state,tot)
    print(query)
    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    cnx.close()
    return render_template('result.html', data = data)
@app.route('/query1', methods=['POST'])
def query1():
    
    #query = "SELECT latitude FROM earth WHERE place LIKE '%%%s%%'" % (file_name)
    file_name = request.form['searchStrings']
    query = "SELECT NAME FROM uc WHERE STATE = '%s'"% (file_name)
    print(query)
    cursor.execute(query)
    data1 = cursor.fetchall()
    
    query1 = "SELECT COUNT(*) FROM uc WHERE STATE = '%s'"% (file_name)
    print(query1)
    cursor.execute(query1)
    data2 = cursor.fetchall()
    data = data1+data2
    return render_template('result.html', data = data)
    cursor.close()
    
    cnx.close()
    
    
    return var
    

@app.route('/readCSV', methods=['POST'])
def readCSV(): 
    query = """LOAD DATA LOCAL INFILE 'uc.csv' IGNORE INTO TABLE uc FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES """
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    
    cnx.close()

    return '<h1>Data Load successful!</h1>'


	

if __name__ == "__main__":
    app.run(debug=True)
    # Disconnect from the account
    client.disconnect()

    


