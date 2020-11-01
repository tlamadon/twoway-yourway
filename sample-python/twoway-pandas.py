import pandas as pd
import numpy as np
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--data", help = "csv data file")
parser.add_argument("--res", help = "csv data file",default="result.json")
args, unknown = parser.parse_known_args()

# loading the data
data = pd.read_csv(args.data) 

# we simply run the zig zag algorithm
data['alpha'] = 0
data['psi'] = 0

mse_last = np.Inf
for i in range(100):
        
    # get the psi
    data['psi'] = data.assign(u = lambda d: d.lw - d.alpha).groupby('fid')['u'].transform("mean")
    # crude normalization
    data['psi'] = data['psi'] - data['psi'].mean()
                        
    # get the alpha
    data['alpha'] = data.assign(u = lambda d: d.lw - d.psi).groupby('i')['u'].transform("mean")

    mse = data.eval("(lw -alpha - psi)**2").mean()
    chg = mse_last - mse
    if (chg<1e-9):
        print("done at %i" % i)
        break
    mse_last = mse

# extracting the firm ids
dt = data[['fid','psi']].drop_duplicates()
res = dict(zip(dt.fid, dt.psi))

# save to json
with open(args.res, 'w') as fp:
    json.dump(res, fp)