import pandas as pd
import os

csv_route = "/home/pissarello-dev/Universidad/HPC/parcial-2/bird_songs_metadata.csv"

origin_route = "/home/pissarello-dev/Universidad/HPC/parcial-2/wavfiles"
destiny_route = "/home/pissarello-dev/Universidad/HPC/parcial-2/wavfiles_filtered"
df = pd.read_csv(csv_route)
desired_columns = ["name", "filename"]
filtered_df = df[desired_columns]

if not os.path.exists(destiny_route):
    os.makedirs(destiny_route)

for specie in filtered_df["name"].unique():
    specie_df = filtered_df[filtered_df["name"] == specie]

    selected_files = specie_df.sample(n=100)["filename"]

    for file in selected_files:
        origin_file = os.path.join(origin_route, file)
        destiny_file = os.path.join(destiny_route, file)
        os.system(f"cp {origin_file} {destiny_file}")
