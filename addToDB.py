'''from News.models import News_DB
import json
f=open('/home/shreenidhi/Json/compose.json') 
data=json.load(f) 
s=set()
for i in  data['news']: 
      
    if(data['news'][i]['article_link'] not in s):
        news=News_DB.objects.create(article_link=data['news'][i]['article_link'],article_title=data['news'][i]['article_title'],article_timestamp=data['news'][i]['article_timestamp'],article_intro=data['news'][i]['article_intro'],article_body=data['news'][i]['article_body'])
        s.add(data['news'][i]['article_link'])
        news.save()
    else:
        continue'''
        
 
'''from News.models import News_DB
import json
from datetime import datetime

f=open("/home/shreenidhi/Downloads/news_ie.json")
data=json.load(f)

for i in data['news']:
    News_DB.objects.filter(article_link=data["news"][i]["article_link"].rstrip()).update(article_body=data["news"][i]["article_body"].rstrip())'''



##Date

'''import datetime
from News.models import News_DB
def validate(date_text):
    import datetime
    try:
        datetime.datetime.strptime(date_text, '%d-%B-%Y')
        val=True
        #return True
    except ValueError:
        #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        #return False
        val=False
    return val
lis_id=[]

for x in News_DB.objects.all():
    if(validate(x.article_timestamp)==False):
        #print(x.id,x.article_timestamp,x.article_link)
        lis_id.append(x.article_link)
print(lis_id)
#print(x.id,x.article_timestamp)
#print("lol")'''
'''if(x.article_link.startswith("https://www.thehindu")):
        date=x.article_timestamp+"-"+"2020"
        News_DB.objects.filter(id=x.id).update(article_timestamp=date)    '''

'''for x in News_DB.objects.all():
    if(x.article_link.startswith("https://www.ndtv.")):
        
            lis=x.article_timestamp.split(" ")
            date=""
            date+=lis[3]
            date+="-"
            date+=lis[1]
            date+="-"
            #date+=lis[4]
            if(len(lis)!=5):
                date=""
                date+=lis[2][:-1]
                date+="-"
                date+=lis[1]
                date+="-"
                date+=lis[3]
                #print(date)
            else:
                date=""
                date+=lis[3][:-1]
                date+="-"
                date+=lis[1]
                date+="-"
                date+=lis[4]
                #print(date)
    elif(x.article_link.startswith("https://indianexpress")):
        lis=x.article_timestamp.split(" ")
        date=""
        date+=lis[1][:-1]
        date+="-"
        date+=lis[0]
        date+="-"
        date+=lis[2]
        #print(date)
    else:
        lis=x.article_timestamp.split(" ")
        date=""
        date+=lis[1][:-1]
        date+="-"
        date+=lis[0]
    News_DB.objects.filter(id=x.id).update(article_timestamp=date)
        #date+="-"
        #date+=lis[2]
        #print(date)'''

'''import json
f=open('/home/shreenidhi/Json/compose.json') 
data=json.load(f) 
s=set()
for i in  data['news']: 
      
    if(data['news'][i]['article_link'] in lis_id):
        #print(data['news'][i]['article_timestamp'])
        lis=data['news'][i]['article_timestamp'].split(" ")
        date=""
        date+=lis[3]
        date+="-"
        date+=lis[1]
        date+="-"
        #date+=lis[4]
        if(len(lis)!=5):
            date=""
            date+=lis[2][:-1]
            date+="-"
            date+=lis[1]
            date+="-"
            date+=lis[3]
            #print(date)
        else:
            date=""
            date+=lis[3][:-1]
            date+="-"
            date+=lis[1]
            date+="-"
            date+=lis[4]
            #print(date)
        News_DB.objects.filter(article_link=data['news'][i]['article_link']).update(article_timestamp=date)
        #news=News_DB.objects.create(article_link=data['news'][i]['article_link'],article_title=data['news'][i]['article_title'],article_timestamp=data['news'][i]['article_timestamp'],article_intro=data['news'][i]['article_intro'],article_body=data['news'][i]['article_body'])
        #s.add(data['news'][i]['article_link'])
        #ews.save()'''



    
        
