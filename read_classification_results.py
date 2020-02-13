import pickle
import pprint

with open('classification_results.pkl', 'rb') as f:
    mynewlist = pickle.load(f)

print(len(mynewlist),' images classified of dataset')
pprint.pprint(mynewlist)