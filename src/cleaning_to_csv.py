import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json 
import os
import glob

def reading_all_json(path_name):
    files = []
    for r, d, f in os.walk(path_name):     #reads in all files in pathname
        for file in f:
            files.append(os.path.join(r, file))      #appends path to files list

    for path in files:
        with open(path, 'r') as f:           #reads in path from files list from above
            events = json.load(f)            #loads in using json
        match_id = int(path.split('/')[8].split('.')[0])         #grabs matchid from path
        events = json_normalize(events)                          #use json normalize to convert to pandas
        events['match_id'] = np.full(events.shape[0], match_id).astype(int)   #save matchid into individual df
        
        events.to_csv('data/events_csvs/events_{}.csv'.format(match_id))      #save as csv in data/events_csvs



def concat_csvs_one(path_name):
    
    all_filenames = []
    for r, d, f in os.walk(path_name):
        for file in f:
            all_filenames.append(file)
    print(all_filenames)
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    #export to csv
    combined_csv.to_csv('data/matches_csv/combined_matches.csv', index=False)
    return('Check to see if this worked :)')


def reading_match_json(path_name):
    files = []
    for r, d, f in os.walk(path_name):
        for file in f:
            files.append(os.path.join(r, file))
         
    for i, path in enumerate(files):
        with open(path, 'r') as f:
            matches = json.load(f)
        matches = json_normalize(matches)

        matches.to_csv('/Users/morganabbitt/galvanize/DSR/statsbomb_soccer/data/matches_csvs/match_{}.csv'.format(i), index=False)
    print('Check to see if this worked! :)')
    

def combining_events(pathname):
    all_filenames = []
    for r, d, f in os.walk(pathname):
        for file in f:
            all_filenames.append(pathname + '/' + file)
    print(all_filenames)
    try:
        pd.read_csv(all_filenames[5])
        print('Read csv successfully')
    except:
        print("Couldnt read csv")
    combined_events_csv = pd.concat([pd.read_csv(f) for f in all_filenames[:-3]])
    #export to csv
    combined_events_csv.to_csv('../data/combined_events.csv', index=False)
    return('Check to see if this worked :)')


def hello_world():
    print('Hello World')