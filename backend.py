import os
import psycopg2

DATABASE_URL = "postgresql://varun:EKoZ-DySh65JeT4ND_Qa-A@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/EduLife?sslmode=verify-full&options=--cluster%3Dwood-bee-6064"
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

def create_user_table():
    try:
        query = "CREATE TABLE IF NOT EXISTS user_data (user_name STRING, name STRING, password STRING, balance INT, loan INT, credit_score INT, health INT, job STRING);"
        cur.execute(query)
        conn.commit()
    except (Exception) as error:
       print("Could Not Create Table", error)
def drop_table():
    query = "DROP TABLE All"
    cur.execute(query)
    conn.commit()

def create_user(username,name,password):
    query =  "INSERT INTO user_data (user_name,name,password, balance, loan, credit_score, health, job) VALUES (%s, %s, %s, 10000, 0, 690, 100, null)"
    val = (username,name,password)
    cur.execute(query,val)
    conn.commit()

def login_validation(username, password):
    query = "SELECT password FROM user_data where user_name=%s"
    cur.execute(query, (username,))
    c_pass = cur.fetchone()
    c_pass = ''.join(c_pass)

    if c_pass == password:
        print("Login Succesful:")
        print("Username:",username, "Password:",password)
        return True
    else:
        print("Username and Password did not match")
        return False

    return None
def set_bal(username, amount):
    query = "UPDATE user_data SET balance = %s WHERE user_name = %s"
    val = (amount, username)
    cur.execute(query,val)
    conn.commit()

def get_bal(username):
    query = "SELECT balance FROM user_data where user_name=%s"
    cur.execute(query, (username,))
    bal = cur.fetchone()
    bal = int(''.join(str(bal)).replace("(","").replace(")","").replace(",",""))
    return bal

def add_bal(username,amount_increase):
    set_bal(username, (get_bal(username)+amount_increase))

def subtract_bal(username,amount_decrease):
    set_bal(username, (get_bal(username)-amount_decrease))

def get_loan(username):
    query = "SELECT loan FROM user_data where user_name=%s"
    cur.execute(query, (username,))
    loan = cur.fetchone()
    loan = int(''.join(str(loan)).replace("(", "").replace(")", "").replace(",", ""))
    return loan

def set_loan(username, amount):
    query = "UPDATE user_data SET loan = %s WHERE user_name = %s"
    val = (amount, username)
    cur.execute(query, val)
    conn.commit()

def add_loan(username, amount_increase):
    set_bal(username, (get_bal(username) + amount_increase))

def subtract_loan(username, amount_decrease):
    set_bal(username, (get_bal(username) - amount_decrease))

def add_job(username):
    query = "UPDATE user_data SET job = %s WHERE user_name = %s"
    job = "yes"
    val = (job, username)
    cur.execute(query, val)
    conn.commit()

def remove_job(username):
    query = "UPDATE user_data SET job = %s WHERE user_name = %s"
    job = "no"
    val = (job, username)
    cur.execute(query, val)
    conn.commit()

def get_creditscore(username):
    query = "SELECT credit_score FROM user_data where user_name=%s"
    cur.execute(query, (username,))
    cscore = cur.fetchone()
    cscore = int(''.join(str(cscore)).replace("(", "").replace(")", "").replace(",", ""))
    return cscore

def set_creditscore(username, amount):
    query = "UPDATE user_data SET credit_score = %s WHERE user_name = %s"
    val = (amount, username)
    cur.execute(query, val)
    conn.commit()

def add_creditscore(username, amount_increase):
    set_creditscore(username, (get_creditscore(username) + amount_increase))

def subtract_creditscore(username, amount_decrease):
    set_creditscore(username, (get_creditscore(username) - amount_decrease))
