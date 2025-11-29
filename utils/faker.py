## Faker se utiliza para crear datos falsos y utilizarlos para probar cosas

from faker import Faker


fake = Faker() # Faker me genera datos aleatoriamente

def get_login_faker(num_casos=5):


    casos = []
    usuarios_validos = ["standard_user", "locked_out_user"]
    password_valido = 'secret_sauce'

    for _ in range (num_casos):
        # username = fake.user_name()
        # password = fake.password(length=12) 
        # login_example = fake.boolean(chance_of_getting_true=50) ##El valor de chance of getting true hace que el 50% de los casos sean true y el resto false. Si cambias el numero EJ a 70. El 70 van a ser true y el 30% false

        if fake.boolean(chance_of_getting_true=30):
            username = fake.random.choice(usuarios_validos)
            password = password_valido
            login_example = True
        else:
            username = fake.user_name()
            password = fake.password(length=12)
            login_example = False


        casos.append((username, password, login_example))

    return casos    