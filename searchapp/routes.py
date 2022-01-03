# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com 

from flask import render_template, flash, url_for
from searchapp import searchapp
from searchapp.forms import query_form

import numpy as np
import pandas as pd
import re

import nltk
from nltk.stem import SnowballStemmer 
arr = np.random.randint(1,500, (20,5))
arr = arr.astype('str')
# df = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd', 'e'])

df = pd.read_csv('Corpus.csv')
df2 = pd.read_csv('TitleInvertedIndex.csv')
df3 = pd.read_csv('AuthorInvertedIndex.csv')
df4= pd.read_csv('BookInvertedIndex.csv')
df5= pd.read_csv('WordsInvertedIndex.csv')

sb_stemmer = SnowballStemmer("english",)
@searchapp.route('/', methods=['GET', 'POST'])
@searchapp.route('/index', methods=['GET', 'POST'])
def index():
	form=query_form()
	row=[]
	indexes=[]
	newDf=df
	label=""
	if form.validate_on_submit(): # To check info when user inputs value into the form
		try:
			q = form.title.data
			if(q!=""):
				
				indexes=df2.loc[df2['Title'] == sb_stemmer.stem(str(q))].iloc[0]["Indexes"]
				indexes=re.findall('\'(.*?)\'', indexes)
				indexes=[int(i) for i in indexes]
				newDf=df[df['Index'].isin(np.array(indexes))]
				
				newDf['frequency'] = newDf.apply(
    			lambda row: indexes.count(row.Index), axis=1)
				
				newDf=newDf.sort_values(by='frequency', ascending=False)
				row=newDf.values.tolist()
				label="Title `"+q+ "` in "+str(len(row)) +" documents, "
			
			q2 = form.author.data
			if(q2!=""):
				indexes=df3.loc[df3['Author'] == sb_stemmer.stem(str(q2))].iloc[0]["Indexes"]
				indexes=re.findall('\'(.*?)\'', indexes)
				indexes=[int(i) for i in indexes]
				newDf = newDf[newDf['Index'].isin(np.array(indexes))]
				
				newDf['frequency'] = newDf.apply(
    			lambda row: indexes.count(row.Index), axis=1)

				
				newDf=newDf.sort_values(by='frequency', ascending=False)
				row=newDf.values.tolist()
			
				label+="Author `"+q2 +"` in "+str(len(row)) +" documents, "
			q3 = form.book.data
			if(q3!=""):
				indexes=df4.loc[df4['Book'] == sb_stemmer.stem(str(q3))].iloc[0]["Indexes"]
				indexes=re.findall('\'(.*?)\'', indexes)
				indexes=[int(i) for i in indexes]
				newDf = newDf[newDf['Index'].isin(np.array(indexes))]
				
				newDf['frequency'] = newDf.apply(
    			lambda row: indexes.count(row.Index), axis=1)
				
				newDf=newDf.sort_values(by='frequency', ascending=False)
				row=newDf.values.tolist()

				label+="Book `"+q3 +"` in "+str(len(row)) +" documents, "
			
			q4 = form.words.data
			if(q4!=""):
				indexes=df5.loc[df5['Word'] == sb_stemmer.stem(str(q4))].iloc[0]["Indexes"]
				indexes=re.findall('\'(.*?)\'', indexes)
				indexes=[int(i) for i in indexes]
				newDf = newDf[newDf['Index'].isin(np.array(indexes))]
				
				newDf['frequency'] = newDf.apply(
    			lambda row: indexes.count(row.Index), axis=1)
				
				newDf=newDf.sort_values(by='frequency', ascending=False)
				row=newDf.values.tolist()
				
				label+="Word `"+q4+"` in "+str(len(row)) +" documents"
			
		except:
			return render_template('index.html', form=form,		
					noresult="true")
		if newDf.empty:
			return render_template('index.html', form=form,			
						noresult="true")
		# row = list(df.loc[df['Title'] == str(q)].values.tolist())
	return render_template('index.html',
						resultlabel=label ,
						title='Home', 
						df=list(df.values.tolist()),
						column_names = newDf.columns.values, 
						form=form,
						result=row, 
						zip=zip)
