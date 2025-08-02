# db.py
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv(r"C:\Users\remin\OneDrive - UNINTER - Aluno\web\meu_projeto_petsolidario.db.py")

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("localhost"),
        user=os.getenv("root"),
        password=os.getenv("van002"),
        database=os.getenv("petsolidario")
    )



