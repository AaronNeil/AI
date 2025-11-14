import pandas as pd
import joblib
import sys

# Load Random Forest model and reference data
model = joblib.load('model/pokemon_type_predictor.joblib')
df_ref = pd.read_csv('data/reference_data.csv')

feature_cols = ['attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed'] 

def predict_pokemon_type(pokemon_name):
    pokemon_data = df_ref[df_ref['name'].str.lower() == pokemon_name.lower()]
    if pokemon_data.empty:
        print(f"Pokémon '{pokemon_name}' not found.")
        return
    stats = pokemon_data[feature_cols]
    prediction = model.predict(stats)
    print(f"Predicted Type1 for {pokemon_name}: {prediction[0]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py <pokemon_name>")
        sys.exit(1)
    predict_pokemon_type(sys.argv[1])
                                                                                                                                                                                                                                                                                                                                                                                                                                                            #                                                                     predict_pokemon_type(name))
