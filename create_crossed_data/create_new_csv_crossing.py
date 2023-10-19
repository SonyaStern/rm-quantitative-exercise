import pandas as pd

def cross_data_pandas(file_name):
    # Read data from the given csv file
    df = pd.read_csv(file_name)

    # Initialize a list to store crossed data
    crossed_data = []

    # Cross the data
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            # Create a unique identifier for the crossed row using rownames
            crossed_rowname = f"{df.iloc[i]['rownames']}_{df.iloc[j]['rownames']}"
            
            # Create the crossed row
            crossed_row = [crossed_rowname] + df.iloc[i][1:].tolist() + df.iloc[j][1:].tolist()
            
            crossed_data.append(crossed_row)

    # Columns for the new dataframe
    columns = ['crossed_rownames'] + [col+"_1" for col in df.columns[1:]] + [col+"_2" for col in df.columns[1:]]

    # Convert list to DataFrame and write to a new csv
    crossed_df = pd.DataFrame(crossed_data, columns=columns)
    crossed_df.to_csv('crossed_data_pandas.csv', index=False)

# Call the function
cross_data_pandas('cpus.csv')
