# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com 

from flask import render_template, flash, url_for
from searchapp import searchapp
from searchapp.forms import query_form
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

import numpy as np
import pandas as pd
import re

import nltk
from nltk.stem import SnowballStemmer 
arr = np.random.randint(1,500, (20,5))
arr = arr.astype('str')
# df = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd', 'e'])

df = pd.read_csv('Corpus.csv')
df2 = pd.read_csv('CorpusInvertedIndex.csv')

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
			ii = form.title.data
			for q in ii.split():
				if(q!="" and q not in en_stops):
					
					indexes=df2.loc[df2['keyword'] == sb_stemmer.stem(str(q))].iloc[0]["Indexes"]
					indexes=re.findall('\'(.*?)\'', indexes)
					indexes=[int(i) for i in indexes]
					if(len(newDf)==0):
						newDf=df[df['Index'].isin(np.array(indexes))]
					else:
						newDf=newDf[newDf['Index'].isin(np.array(indexes))]
					
					newDf['ranking'] = newDf.apply(
					lambda row: indexes.count(row.Index), axis=1)
					
					newDf=newDf.sort_values(by='ranking', ascending=False)
					row=newDf.values.tolist()
			label="Title `"+ii+ "` in "+str(len(row)) +" documents, "
			
			
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
