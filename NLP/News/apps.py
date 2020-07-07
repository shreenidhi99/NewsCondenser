from django.apps import AppConfig
from django.conf import settings
import pickle
import pandas as pd
import os
import json

class NewsConfig(AppConfig):
	name = 'News'


class PredictorConfig(AppConfig):    # create path to models
	path = os.path.join(settings.MODELS, 'pickle_model.pkl')
 
	# load models into separate variables
	# these will be accessible via this class
	with open(path, 'rb') as pickled:
	   pickle_model = pickle.load(pickled)
	#def predict(y):
		#return pickle_model.predict(y)

class InvertedIndex(AppConfig):    # create path to models
	idf_path = os.path.join(settings.MODELS,'IDF_fin.json')
	tf_path	= os.path.join(settings.MODELS, 'tf_fin.json')
	invertedindex_path=os.path.join(settings.MODELS, 'InvertedIndex_fin.json')

	#f=open('IDF.json',"r") 
	idf=json.load(open(idf_path,"r"))
	tf=json.load(open(tf_path,"r"))
	invertedindex=json.load(open(invertedindex_path,"r"))
	#idf=[json.loads(line) for line in (open(idf_path,"r"))]
	#tf=[json.loads(line) for line in (open(tf_path,"r"))]
	#	invertedindex=json.load(open(invertedindex_path,"r"))
    #invertedindx=[json.loads(line) for line in (open(invertedindex_path,"r"))]

 
	
