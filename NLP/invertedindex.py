
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from News.models import News_DB
import math
data=News_DB.objects.all()
stop_words = set(stopwords.words('english')) 
import json

### word:[id of docs , frequency in each of those doc]
ID={}
for x in (data):
  stop_words = set(stopwords.words('english')) 
  example_sent =x.article_body
  word_tokens = word_tokenize(example_sent) 
  word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
  filtered_sentence=[]
  for w in word_tokens:
    if w not in stop_words:
      filtered_sentence.append(w)
 

  doc=x.id
  if(len(filtered_sentence)==0):
    print("empty",x.id,x.article_body,x)
  else:
    for w in set(filtered_sentence):
      #if(x in d.keys()):
      c=filtered_sentence.count(w)
      if(w in ID.keys()):
        ID[w][0].append(doc),ID[w][1].append(c)
        #print("yes")
      else:
        ID[w]=[[doc],[c]]
#for x,y in zip(ID.keys(),range(3)):
  #print(ID[x],x)
out_file = open("InvertedIndex_fin.json", "a")  
    
json.dump(ID, out_file)  
    
out_file.close() 

idf={}

#idf for each word
for x in sorted(ID.keys()):
  idf[x]=math.log(len(data)/len(ID[x][0]),2)

out_file = open("IDF_fin.json", "a")  
    
json.dump(idf, out_file)  
    
out_file.close() 

#normalized tf calculation
import numpy as np
tf={}
arr=np.zeros((len(data),len(ID.keys())))
li=sorted(ID.keys())
for x in data:
  tf[x.id]=[]
  example_sent = x.article_body
  word_tokens = word_tokenize(example_sent) 
  word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
  #filtered_sentence = [w for w in word_tokens if not w in stop_words]
  filtered_sentence=[]
  for w in word_tokens:
    if w not in stop_words:
      filtered_sentence.append(w)
  #length_arr.append(len(filtered_sentence))
  for y in li:
    tf[x.id].append(filtered_sentence.count(y)/(len(filtered_sentence)+0.0001))
  print(x.id,"over")
out_file = open("tf_fin.json", "a")  
    
json.dump(tf, out_file)  
    
out_file.close() 

  #break
  #print(word_tokens)'''
'''print(len(stop_words))'''
### idf for each word
#print(len(data))

#read=json.loads(y)
'''import json
f=open('tf.json',"r") 
data=json.load(f)'''
'''for x,y in zip(data,range(1)):
  print(x,(data[x]))'''
'''d=(data['794'])
f1=open('InvertedIndex.json',"r") 
data=json.load(f1)'''
'''for x,y in zip(data,range(1)):
  print(x,(data[x]))'''
'''print(data['corona'])
l=sorted(data.keys())
ind=l.index('corona')
print(d[ind])'''
#print(data['794'])
