import sqlite3

conn = sqlite3.connect('login.db')
cursor = conn.cursor()

# テーブル作成
cursor.execute(CREATE TABLE IF NOT EXISTS login (
    id INTEGER PRIMARY KEY,
    password TEXT NOT NULL
))

name = input("名前を入力してください: ")
age = int(input("年齢を入力してください: "))
email = input("メールアドレスを入力してください: ")

