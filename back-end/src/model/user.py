# セッション変数の取得
from setting import session
# Userモデルの取得
from ..table import user

# DBにレコードの追加
user = user.User()
user.name = 'とも太郎'
session.add(user)
session.commit()

# Userテーブルのnameカラムをすべて取得
users = session.query(user.User).all()
for user in users:
    print(user.name)
