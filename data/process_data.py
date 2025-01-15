# import packages
import pandas as pd

"""
Python function for loading and processing csv data from multiple sources. 
(This is being replaced by data/hitting-data-cleaning.ipynb Jupyter Notebook for now)
WORK IN PROGRESS - NOT RELEASED
"""


def process_data(players_file, hitting_data_file, fielding_file, output_file):

    #load data from csv
    player_names_df = pd.read_csv(players_file, encoding='latin-1', usecols=['playerID', 'nameFirst', 'nameLast'])
    fielding_df = pd.read_csv(fielding_file)
    hitting_df = pd.read_csv(hitting_data_file)
    
    #clean player position data
    fielding_df = fielding_df.loc[fielding_df['position'] != 'P', ['playerID', 'position']]
    player_names_df = player_names_df[['playerID', 'nameFirst', 'nameLast']]

    # Merge and create name column in one step, selecting only needed columns
    players_df = (fielding_df.merge(player_names_df, 'left', 'playerID')
                 .assign(name=lambda x: x['nameLast'] + ', ' + x['nameFirst'])
                 [['name', 'position']]
                 .drop_duplicates())
    
    #match name columns
    hitting_df = hitting_df.rename(columns={'last_name, first_name': 'name'})

    #merge datasets
    final_df = hitting_df.merge(players_df,'inner','name')

    #reorder columns
    hitting_columns = list(hitting_df.columns)
    position_columns = [col for col in final_df.columns if col not in hitting_columns]
    reordered_columns = position_columns + hitting_columns
    final_df = final_df[reordered_columns]
    
    #Remove duplicate players with slightly different positions (combine positions into one array)

    final_df = final_df.groupby(["player_id", "year"], as_index=False).agg({
        "position": list,  # Combine the 'position' column into a list
        **{col: "first" for col in final_df.columns if col not in ["player_id", "year", "position"]}  # Take the first value for all other columns
    })

    final_df["position"] = final_df["position"].apply(lambda x: list(set(x)))

    #save to csv and return dataframe
    final_df.to_csv(output_file, index=False)
    return final_df

