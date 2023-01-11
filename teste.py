import bcrypt

senha = '12345'.encode()
salt = bcrypt.gensalt(8)

print(salt)

hash = bcrypt.hashpw(senha, salt)

print(hash)