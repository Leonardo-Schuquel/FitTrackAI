import os
import json
from colorama import Fore, Style

objectives = {
    1 : ('Emagrecer', 'Cardio e treino de musculação'),
    2 : ('Ganhar massa', 'Treino de força e resistência com cardio'),
    3 : ('Manter peso', 'Aeróbicos leves + resistência'),
}

def clear():
    os.system('clear')

# simple imc classification
def classify_imc(imc):
    tracks = [
    (18.5, "Abaixo do peso"),
    (25.0, "Peso normal"),
    (30.0, "Sobrepeso"),
    (35.0, "Obesidade grau 1"),
    (40.0, "Obesidade grau 2"),
    (float('inf'), "Obesidade grau 3"),
]
    for limit, rank in tracks:
        if imc < limit:
            return rank
    
# function responsible for calculating the imc
def calc_imc(height, weight):
    imc = weight/(height ** 2)
    return round(imc, 2)

# validating the data for the function
def validate_data(user_data):
    try:
        user_data['age'] = int(user_data['age'])
        user_data['height'] = float(user_data['height'])
        user_data['weight'] = float(user_data['weight'])
        user_data['goal'] = int(user_data['goal'])
        return True
    
    except ValueError:
        print('Parece que alguns dados não foram preenchidos corretamente')
        print('Por favor tente novamente')
        return False
    
def show_data(user_data):
    print(50 * '=')
    print(f"👤 Olá {user_data['name']} É um prazer ter você por aqui!")
    print(50 * '=')
    print()

    print(Fore.GREEN + "📊 DADOS DO USUÁRIO:" + Style.RESET_ALL)
    print(f"-> Idade {user_data['age']} anos")
    print(f"-> Altura {user_data['height']} m")
    print(f"-> Peso {user_data['weight']} Kg")
    print(f"-> IMC {user_data['bmi']} ({user_data['bmi_classification']})")
    print()


    print(Fore.GREEN +"🎯 OBJETIVO:" + Style.RESET_ALL)
    print(f"-> Objetivo {objectives[user_data['goal']][0]}")
    print()

    print(Fore.GREEN + "💪 SUGESTÃO DE TREINO:" + Style.RESET_ALL)
    print(f"-> {objectives[user_data['goal']][1]}")
    print(50 * '=')

# Save user data
def save_user_data(user_data):
    with open("data/data.json", 'w') as file:
        json.dump(user_data, file, indent=2)