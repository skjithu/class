import mysql.connector

def insertProduct(line):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Python@12",
        database="ecomm")
    mycursor = mydb.cursor()
    word_list = line.split(",")
    sql = "INSERT INTO products (product_id, product_name, category, price, quantity) VALUES (%s, %s, %s, %s, %s)"
    values = (word_list[0].strip(),word_list[1].strip(),word_list[2].strip(),float(word_list[3].strip()),int(word_list[4].strip()))
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

with open("product_data.txt","r") as myfile:
    line = myfile.readline()
    while(line):
        try:
            insertProduct(line)
        except:
            continue
        finally:
            line = myfile.readline()
