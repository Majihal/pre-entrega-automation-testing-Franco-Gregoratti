import os  ## OS permite cambiar rutas relativas a absolutas
import json

def get_login_json(json_file="data_login.json"):
    current_file = os.path.dirname(__file__)
    json_file = os.path.join(current_file,'..', 'data', json_file)
    json_file = os.path.abspath(json_file) 

    casos = []


    with open (json_file) as j:
        datos = json.load(j) ##Recibe como argumento el archivo a leer

        for i in datos :
            username = i['username']
            pasword = i['password']
            login_example = i['login_example'] ## no es necesario indicarle lo del booleano por que ya esta en el JSON
            casos.append((username, pasword, login_example))
    return casos  