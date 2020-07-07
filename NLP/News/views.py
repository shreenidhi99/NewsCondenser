from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
#from django import template 
from collections import Counter
from .forms import SearchForm
from News.models import News_DB
from .apps import PredictorConfig,InvertedIndex
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
import spacy
spacy.load('en_core_web_sm')
import en_core_web_sm
nlp = en_core_web_sm.load()
# Create your views here.
import pandas as pd
from scipy import spatial
from datetime import datetime



def cosine_sim(v1,v2):
  return 1 - spatial.distance.cosine(v1, v2)

def getrelevantdoc(query):
	#return[51,52,53]
	#return st+"lol"
	 # input()
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(query) 
	word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	l=sorted(filtered_sentence)
	tf_idf={}

	# tf-idf for docss
	for x in l:
	  index=sorted(InvertedIndex.invertedindex.keys()).index(x)
	  tf_idf_doc=[]
	  for y in (sorted(InvertedIndex.tf.keys())):
	    #tf_idf_doc.append(InvertedIndex.idf[x]*InvertedIndex.tf[y][index])
	    tf_idf_doc.append(InvertedIndex.tf[y][index])
	  tf_idf[x]=tf_idf_doc
	#tf-idf for query

	#print(tf_idf)
	tf_idf_query={}

	word_tokens = word_tokenize(query) 
	word_tokens=[word.lower() for word in word_tokens if word.isalpha()]
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	l=sorted(filtered_sentence)
	for x in (l):
	  tfq=l.count(x)/len(l)
	  #tf_idf_query[x]=tfq*InvertedIndex.idf[x]
	  tf_idf_query[x]=tfq
	sim=[]
	list_tf_idf=list(tf_idf.values())
	list_tf_query=list(tf_idf_query.values())

	for x in range(len(InvertedIndex.tf.keys())):
	  arr=[]
	  quer_arr=[]
	  for y in range(len(list_tf_idf)):
	    arr.append(list_tf_idf[y][x])
	    quer_arr.append(list_tf_query[y])
	  sim.append(cosine_sim(arr,quer_arr))

	dic={}
	for x,y in zip(sorted(InvertedIndex.tf.keys()),range(len(InvertedIndex.tf.keys()))):
	  if(sim[y]==sim[y])and(sim[y]!=0):
	    dic[x]=sim[y]

	#final_doc=sorted(dic.items(), key=lambda item: -item[1])
	#final_doc=final_doc[:3]
	#return list(final_doc);
	final_doc=sorted(dic, key=dic.get, reverse=True)
	#print(dic)
	#print(final_doc)
	return (dic)
def feature_extract(body, title):
	stop_words = set(stopwords.words('english')) 
	txt = body
	title = set(title)
	wordsList = nltk.word_tokenize(txt) 
	wordsFreqList = [w for w in wordsList if not w in stop_words.union(set([',','.','"','?',"'",":","''","``"]))]
	keywords = Counter(wordsFreqList).most_common(3)
	tokens = sent_tokenize(txt)
	sentence_rank = []
	if tokens != []:
		for i in tokens: 
			n = len(i)
			keywordCount = 0
			titleSimCount = 0
			wordsList = nltk.word_tokenize(i) 
			tagged = nltk.pos_tag(wordsList)
			ncount=vcount=jcount=dcount=0
			doc = nlp(i)
			labels = [x.label_ for x in doc.ents if x.label_ in ('MONEY','ORG','LAW','NORP','PERCENT')]
			for j in tagged: 
				if "NN" in j[1]:
					ncount +=1
				elif "VB" in j[1]:
					vcount +=1
				elif "JJ" in j[1]:
					jcount +=1
				elif "CD" in j[1]:
					dcount +=1
				if j[0] in keywords[0]:
					keywordCount +=1
				if j[0] in title:
					titleSimCount +=1
			if(n!=0)and(len(keywords)!=0)and(len(title)!=0):
				sentence_rank.append([ncount/n, vcount/n, jcount/n, dcount/n, Counter(labels)['ORG']/n, Counter(labels)['MONEY']/n, Counter(labels)['LAW']/n, Counter(labels)['NORP']/n, Counter(labels)['PERCENT']/n, titleSimCount/len(title), keywordCount/len(keywords)])
			else:
				print(title)
				print(keywords)
				sentence_rank.append([0]*11)			
	''' if category =="train":
			scores_cont = lxr.rank_sentences(
				tokens,
				threshold=None,
				fast_power_method=False,
		)'''
			#for i in range(len(scores_cont)):
				#sentence_rank[i].append(scores_cont[i])
	return tokens, sentence_rank
def getFeatures(body,title):
	our_news = []
	sentences = []
	sentences, features = feature_extract(body, title)
	if features != []:
		 for f in features:
			 our_news.append(f)
	return sentences, our_news

def helpersort(x):
	return datetime.strptime(x, '%d-%B-%Y')

def home(request):
	template = loader.get_template('News/home.html')
	
	if(request.method=='POST'):
		
	#template = loader.get_template('News/home.html')
	#form = SearchForm()
	#context = {'form': form}
		form=SearchForm(request.POST)
		query=form.data['keyword']
		relevant_ids=getrelevantdoc(query)
		news=[]
		objects=News_DB.objects.filter(id__in=list(relevant_ids.keys()))

		#print(relevant_ids[str(99)])
		s=set()
		for x in objects:
			#print(x.id)
			news.append([x.id,relevant_ids[str(x.id)],x.article_timestamp])
			s.add(x.article_timestamp)
		#print()
		#news.sort()

		news=sorted(news, key=lambda x: (helpersort(x[2]), x[1]))
		#print(news)
		first_article=[]
		unique_dates=sorted(s,key=lambda x:helpersort(x))
		for x in unique_dates:
			for n in news:
				if(n[2]==x):
					first_article.append(n)
					break
		#print(first_article)

		#ids=[]
		final_li=[]
		for art in first_article:
			#ids.append(art[0])
			Str=" "
			x=News_DB.objects.filter(id=art[0])
			#print(x.article_body)
			x=x[0]
			sentences,test_news=getFeatures(x.article_body,x.article_title)
			test_news_df = pd.DataFrame(test_news)
			test_news_Y = PredictorConfig.pickle_model.predict(test_news_df)
			test_results = []
			for i,j,k in zip(sentences,test_news_Y,range(len(sentences))):
				test_results.append([i,j,k])
			for i, j, k in zip(sentences, test_news_Y, range(len(sentences))):
				test_results.append([i,j,k])
			test_results = sorted(test_results, key=lambda x : x[1], reverse=True)[:3]
			test_results = sorted(test_results, key=lambda x: x[2])
			#print(test_results)
			for y in test_results:
				Str+=y[0]
				#Str+=#'''
			final_li.append([art[0],art[2],Str])
			#print(final_li)		

		'''Str=" "
		for x in objects:
			Str+=#
			Str+=x.article_timestamp
			Str+=#
			Str+=str(x.id)
			Str+=#
			Str+=#
			sentences,test_news=getFeatures(x.article_body,x.article_title)
			#print(sentences)
			print(x.article_body)
			test_news_df = pd.DataFrame(test_news)
			test_news_Y = PredictorConfig.pickle_model.predict(test_news_df)
			test_results = []
			for i,j,k in zip(sentences,test_news_Y,range(len(sentences))):
				test_results.append([i,j,k])
			for i, j, k in zip(sentences, test_news_Y, range(len(sentences))):
				test_results.append([i,j,k])
			test_results = sorted(test_results, key=lambda x : x[1], reverse=True)[:3]
			test_results = sorted(test_results, key=lambda x: x[2])
			#print(test_results)
			for y in test_results:
				Str+=y[0]
				Str+=#'''
		#return HttpResponse("hey",content_type="text/plain")
		#return render(request,'	News/summaryforfirst.html',{'final_li':final_li})
		request.session['ids']=news
		return render(request,'News/summaryforfirst.html',{'final_li':final_li})

	else:
		form = SearchForm()
		context = {'form': form}
		return HttpResponse(template.render(context, request))

def singledate(request,date):
	news=request.session['ids']
	#print(news)
	Str=""
	final_li=[]
	'''for x in news:
		if(x[2]==date):
			print(date)'''
	body_all=""
	title_all=""
	for art in news:
		if(art[2]==date):
			#Str=""
			
			x=News_DB.objects.filter(id=art[0])
			#print(x.article_body)
			x=x[0]
			body_all+=x.article_body+" "
			title_all+=x.article_title+" "

	sentences,test_news=getFeatures(body_all,title_all)
	test_news_df = pd.DataFrame(test_news)
	if(test_news_df.empty):
		print(x.id)
	else:
		test_news_Y = PredictorConfig.pickle_model.predict(test_news_df)
		test_results = []
		for i,j,k in zip(sentences,test_news_Y,range(len(sentences))):
			test_results.append([i,j,k])
		for i, j, k in zip(sentences, test_news_Y, range(len(sentences))):
			test_results.append([i,j,k])
		test_results = sorted(test_results, key=lambda x : x[1], reverse=True)[:3]
		test_results = sorted(test_results, key=lambda x: x[2])
		#print(test_results)
		for y in test_results:
			Str+=y[0]
			#Str+=#
		final_li.append([date,Str])



		'''sentences,test_news=getFeatures(x.article_body,x.article_title)
		test_news_df = pd.DataFrame(test_news)
		if(test_news_df.empty):
			print(x.id)
		else:
		#print(test_news_df)
			test_news_Y = PredictorConfig.pickle_model.predict(test_news_df)
			test_results = []
			for i,j,k in zip(sentences,test_news_Y,range(len(sentences))):
				test_results.append([i,j,k])
			for i, j, k in zip(sentences, test_news_Y, range(len(sentences))):
				test_results.append([i,j,k])
			test_results = sorted(test_results, key=lambda x : x[1], reverse=True)[:3]
			test_results = sorted(test_results, key=lambda x: x[2])
			#print(test_results)
			for y in test_results:
				Str+=y[0]
				#Str+=#
			final_li.append([art[0],art[2],Str])'''


	#print("final_li",final_li)		
	return render(request,'News/singledate.html',{'final_li':final_li})

	#return HttpResponse(date)

