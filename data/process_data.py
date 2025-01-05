# import packages
import pandas as pd

def process_data(hitting_data_file, player_positions_file, output_file):

    #load data from csv
    hitting_df = pd.read_csv(hitting_data_file)
    positions_df = pd.read_csv(player_positions_file)
    
    #clean player position data
    positions_df = positions_df[['name_fielder', 'fld_name_display_club', 'position']]
    positions_df = positions_df.rename(columns={'fld_name_display_club':'team'})
    
    #match name columns
    hitting_df = hitting_df.rename(columns={'last_name, first_name': 'name'})
    positions_df = positions_df.rename(columns={'name_fielder': 'name'})

    #merge datasets
    final_df = hitting_df.merge(positions_df,'inner','name')

    #reorder columns
    hitting_columns = list(hitting_df.columns)
    position_columns = [col for col in final_df.columns if col not in hitting_columns]
    reordered_columns = position_columns + hitting_columns
    final_df = final_df[reordered_columns]
    
    #Remove duplicate players with slightly different positions (combine positions into one array)

    final_df = final_df.groupby("player_id").agg({
        "position": list,             # Combine the 'position' column into a list
        **{col: "first" for col in final_df.columns if col not in ["player_id", "position"]}  # Take the first value for all other columns
    }).reset_index()

    final_df["position"] = final_df["position"].apply(lambda x: list(set(x)))

    #save to csv and return dataframe
    final_df.to_csv(output_file, index=False)
    return final_df

