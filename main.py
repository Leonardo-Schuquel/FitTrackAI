from utils import clear, calc_imc, validate_data, show_data, classify_imc

def collect_data():
    name = input('Qual é o seu nome? ')
    clear()
    age = input('Qual é a sua idade? ')
    clear()
    height = input('informe a sua altura em metros: ').replace(',','.')
    clear()
    weight = input('Qual é o seu peso: ').replace(',','.')
    clear()
    goal = input('agora só falta o objetivo [1]emagrecer, [2]ganhar massa, [3]manter o peso ')
    clear()
    user_data = {
        'name': name,
        'age': age,
        'height' : height,
        'weight' : weight,
        'goal' : goal,
        }
    return user_data


while True:
    user_data = collect_data()
    if validate_data(user_data):
        bmi = calc_imc(user_data['height'], user_data['weight'])
        user_data["bmi"] = bmi
        user_data["bmi_classification"] = classify_imc(bmi)
    
    show_data(user_data)

    break