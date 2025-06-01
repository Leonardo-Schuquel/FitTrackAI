import os

suggestion = ''

def calcimc (height, weight):
    imc = weight / (height ** 2)
    return round(imc, 2)

while True:
    name = input('Qual é o seu nome? ')
    os.system('clear')
    age = input('Qual é a sua idade? ')
    os.system('clear')
    height = input('Por favor informe a altura em metros: ').replace(',','.')
    os.system('clear')
    weight = input('Agora informe o seu Peso: ').replace(',','.')
    os.system('clear')
#Posteriormente eu quero que o usuario selhecione o objetivo em uma lista.
    goal = input('Agora só falta o objetivo [1]emagrecer, [2]ganhar massa, [3]manter. ')
    os.system('clear')
    ok = None
    
    try:
        age = int(age)
        height = float(height)
        weight = float(weight)
        goal = int(goal)
        ok = None
    except ValueError:
        print("Parece que alguns dos dados não foram preenchidos corretamente.")
        print('Por favor tente novamente')
        ok = True

    if goal == 1:
        print("O seu objetivo é emagrecer")
        suggestion = 'Cardio e treino de musculação'
        print(suggestion)
    elif goal == 2:
        print("O seu objetivo é ganhar massa")
        suggestion = 'Treino de força e resistencia com cardio'
        print(suggestion)
    elif goal == 3:
        print("O seu objetivo é manter o seu estado atual")
        suggestion = 'A1eróbicos de baixa intensidade e treino de resistencia'
        print(suggestion)
    else:
        os.system('clear')
        print("O objetivo que você colocou não está no nosso banco de dados")
        print('Por favor tente novamente.')
        print(100 * '-')
        ok = True

    if ok == None:
        user_data = {
            "name": name,
            "age": age,
            "height": height,
            "weight": weight,
            "goal": goal         
        }
        bmi = calcimc(height, weight)
        user_data["bmi"] = bmi
        user_data["suggestion_training"] = suggestion
        break