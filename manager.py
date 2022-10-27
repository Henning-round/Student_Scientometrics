import pickle
from Homework import Homework
def save_obj(works, name):
    with open(name, "wb") as fp:   #Pickling
        pickle.dump(works, fp)
        
def load_obj(name):
    with open(name, "rb") as fp:  
        obj= pickle.load(fp) # Unpickling
        return obj
