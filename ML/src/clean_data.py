import pandas as pd

DATAPATH = 'data/pokemon.csv'

df = pd.read_csv(DATAPATH)
training_data = [
    'abilities','against_bug', 'against_dark', 'against_dragon', 'against_electric', 'against_fairy',
    'against_fight', 'against_fire', 'against_flying', 'against_ghost', 'against_grass',
    'against_ground', 'against_ice', 'against_normal', 'against_poison', 'against_psychic',
    'against_rock', 'against_steel', 'against_water', 'base_egg_steps', 'base_happiness', 'base_total',
    'capture_rate', 'classfication', 'experience_growth', 'height_m', 'japanese_name',
    'percentage_male', 'pokedex_number', 'weight_kg', 'generation', 'is_legendary'

]
df = df.drop(columns=training_data)
df.to_csv('data/training_data.csv', index=False)


rdf = pd.read_csv('data/training_data.csv')
reference_data = [
    'type1', 'type2'
]
rdf = rdf.drop(columns=reference_data)
rdf.to_csv('data/reference_data.csv', index=False)

