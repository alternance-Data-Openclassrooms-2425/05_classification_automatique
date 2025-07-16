import requests
import pandas as pd


url="https://api.edamam.com/api/food-database/v2/parser"


params = {
    'ingr': "champagne",
    'app_id': "b83a90fe",
    'app_key': "ecf2cf9b54745aa27a83a255fd920271"
}

# Requête API
response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()
    
    # On récupère la liste sous la clé 'parsed'
    hint_items = data.get('hints', [])
    
    # On extrait les champs souhaités de chaque élément
    extracted_data = []
    for item in hint_items:
        food = item.get('food', {})
        extracted_data.append({
            'foodId': food.get('foodId'),
            'label': food.get('label'),
            'foodContentsLabel': food.get('foodContentsLabel'),
            'category': food.get('category'),
            'image': food.get('image')
        })
    
    # Création du DataFrame
    df = pd.DataFrame(extracted_data)
    print(df)
else:
    print("Erreur :", response.status_code, response.text)
    

df.to_csv("food_champagne.csv")