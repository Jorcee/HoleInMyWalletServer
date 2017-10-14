import pandas as pd

def write_csv(users):
    users_CSV = pd.DataFrame(users)
    users_CSV.to_csv("users.csv", index=False, header=False)
