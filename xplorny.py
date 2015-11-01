#!/usr/bin/env python
import os
import sys
import pandas as pd
import urllib
from bokeh.plotting import *
from bokeh.models import HoverTool
from collections import OrderedDict
from flask import Flask,render_template,request,redirect
from commonFunctions import *
from bokeh.charts import Histogram, BoxPlot
from bokeh.charts import defaults, vplot, hplot, show, output_file

#defining the app
app_xplor = Flask(__name__)
app_xplor.vars={}

@app_xplor.route('/index', methods = ['GET', 'POST'] )
def processIndex():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		checked=request.form['option']
	if (checked=='feat'):
		return redirect('/getFeat') 
	elif (checked=='trend'):
		return redirect('/getTrend')
	elif (checked=='distrib'):
		return redirect('/getDistrib')

@app_xplor.route('/getTrend',methods=['GET','POST'])
def getTrend():
        if request.method == 'GET':
                return render_template('trend.html')
        else:
		bronx=[[2009,'https://data.cityofnewyork.us/resource/en2c-j6tw.json'],[2010,'https://data.cityofnewyork.us/resource/n2s5-fumm.json'],[2011,'https://data.cityofnewyork.us/resource/bawj-6bgn.json'],[2012,'https://data.cityofnewyork.us/resource/3qfc-4tta.json']]
		brooklyn=[[2009,'https://data.cityofnewyork.us/resource/rmv8-86p4.json'],[2010,'https://data.cityofnewyork.us/resource/w6yt-hctp.json'],[2011,'https://data.cityofnewyork.us/resource/5mw2-hzqx.json'],[2012,'https://data.cityofnewyork.us/resource/bss9-579f.json']]
		manhattan=[[2009,'https://data.cityofnewyork.us/resource/956m-xy24.json'],[2010,'https://data.cityofnewyork.us/resource/ad4c-mphb.json'],[2011,'https://data.cityofnewyork.us/resource/ikqj-pyhc.json'],[2012,'https://data.cityofnewyork.us/resource/dvzp-h4k9.json']]
		queens=[[2009,'https://data.cityofnewyork.us/resource/m59i-mqex.json'],[2010,'https://data.cityofnewyork.us/resource/crbs-vur7.json'],[2011,'https://data.cityofnewyork.us/resource/s3zn-tf7c.json'],[2012,'https://data.cityofnewyork.us/resource/jcih-dj9q.json']]
		statenIsland=[[2009,'https://data.cityofnewyork.us/resource/cyfw-hfqk.json'],[2010,'https://data.cityofnewyork.us/resource/wv4q-e75v.json'],[2011,'https://data.cityofnewyork.us/resource/a5qt-5jpu.json'],[2012,'https://data.cityofnewyork.us/resource/tkdy-59zg.json']]
                featureNames=[['comparable_rental_2_market_value_per_sqft',  'Market value per square foot'],['comparable_rental_2_full_market_value',      'Full market value'],['comparable_rental_2_year_built',             'Year Built'],['comparable_rental_2_gross_income_per_sqft', 'Gross income per square foot']]
                #request was a POST (get the var from the form)
                app_xplor.vars['feat'] = request.form['feat']
                app_xplor.vars['bo'] = request.form['bo']

		#Translating name of the feature into the name in the original database
		dbFeatureName = convertField(app_xplor.vars['feat'],featureNames)
		
                #Building the queries
                if  (app_xplor.vars['bo']=='Bronx'):
                        queryA = buildQuery(2009,bronx,dbFeatureName)
			queryB = buildQuery(2010,bronx,dbFeatureName)
			queryC = buildQuery(2011,bronx,dbFeatureName)
			queryD = buildQuery(2012,bronx,dbFeatureName)
                elif (app_xplor.vars['bo']=='Brooklyn'):
                        queryA = buildQuery(2009,brooklyn,dbFeatureName)
			queryB = buildQuery(2010,brooklyn,dbFeatureName)
			queryC = buildQuery(2011,brooklyn,dbFeatureName)
			queryD = buildQuery(2012,brooklyn,dbFeatureName)
                elif (app_xplor.vars['bo']=='Manhattan'):
                        queryA = buildQuery(2009,manhattan,dbFeatureName)
			queryB = buildQuery(2010,manhattan,dbFeatureName)
			queryC = buildQuery(2011,manhattan,dbFeatureName)
			queryD = buildQuery(2012,manhattan,dbFeatureName)	
                elif (app_xplor.vars['bo']=='Queens'):
                        queryA = buildQuery(2009,queens,dbFeatureName)
			queryB = buildQuery(2010,queens,dbFeatureName)
			queryC = buildQuery(2011,queens,dbFeatureName)
			queryD = buildQuery(2012,queens,dbFeatureName)		
                elif (app_xplor.vars['bo']=='Staten Island'):
                        queryA = buildQuery(2009,statenIsland,dbFeatureName)
			queryB = buildQuery(2010,statenIsland,dbFeatureName)
			queryC = buildQuery(2011,statenIsland,dbFeatureName)
			queryD = buildQuery(2012,statenIsland,dbFeatureName)

		#executing the queries on the tables
		rawA = pd.read_json(queryA)
		rawB = pd.read_json(queryB)
		rawC = pd.read_json(queryC)
		rawD = pd.read_json(queryD)
		#Managind the data to be input for a boxplot 
		rawA['year']=2009
		rawB['year']=2010
		rawC['year']=2011
		rawD['year']=2012
		allData = pd.concat([rawA, rawB, rawC, rawD])
                cleanData= allData.dropna()
		cleanData.columns=[app_xplor.vars['feat'],'year']                	

		#plot
		defaults.width = 450
		defaults.height = 350	
		box_plot = BoxPlot(cleanData, label='year',title=app_xplor.vars['bo'])
		output_file("boxplot.html")
                show(
                    vplot(
                        hplot(box_plot)
                    )
                )
		return redirect('/goTrend')	

@app_xplor.route('/getDistrib',methods=['GET','POST'])
def getDistrib():
        if request.method == 'GET':
                return render_template('distrib.html')
        else:
                bronx=[[2009,'https://data.cityofnewyork.us/resource/en2c-j6tw.json'],[2010,'https://data.cityofnewyork.us/resource/n2s5-fumm.json'],[2011,'https://data.cityofnewyork.us/resource/bawj-6bgn.json'],[2012,'https://data.cityofnewyork.us/resource/3qfc-4tta.json']]
                brooklyn=[[2009,'https://data.cityofnewyork.us/resource/rmv8-86p4.json'],[2010,'https://data.cityofnewyork.us/resource/w6yt-hctp.json'],[2011,'https://data.cityofnewyork.us/resource/5mw2-hzqx.json'],[2012,'https://data.cityofnewyork.us/resource/bss9-579f.json']]
                manhattan=[[2009,'https://data.cityofnewyork.us/resource/956m-xy24.json'],[2010,'https://data.cityofnewyork.us/resource/ad4c-mphb.json'],[2011,'https://data.cityofnewyork.us/resource/ikqj-pyhc.json'],[2012,'https://data.cityofnewyork.us/resource/dvzp-h4k9.json']]
                queens=[[2009,'https://data.cityofnewyork.us/resource/m59i-mqex.json'],[2010,'https://data.cityofnewyork.us/resource/crbs-vur7.json'],[2011,'https://data.cityofnewyork.us/resource/s3zn-tf7c.json'],[2012,'https://data.cityofnewyork.us/resource/jcih-dj9q.json']]
                statenIsland=[[2009,'https://data.cityofnewyork.us/resource/cyfw-hfqk.json'],[2010,'https://data.cityofnewyork.us/resource/wv4q-e75v.json'],[2011,'https://data.cityofnewyork.us/resource/a5qt-5jpu.json'],[2012,'https://data.cityofnewyork.us/resource/tkdy-59zg.json']]
                featureNames=[['comparable_rental_2_market_value_per_sqft',  'Market value per square foot'],['comparable_rental_2_full_market_value',      'Full market value'],['comparable_rental_2_year_built',             'Year Built'],['comparable_rental_2_gross_income_per_sqft', 'Gross income per square foot']]
                #request was a POST (get the var from the form)
		#... All Boroughs are selected by default
                app_xplor.vars['feat'] = request.form['feat']
                app_xplor.vars['year'] = request.form['year']

                #Translating name of the feature into the name in the original database
                dbFeatureName = convertField(app_xplor.vars['feat'],featureNames)

		#Building the queries
		queryA = buildQuery(int(app_xplor.vars['year']),bronx,dbFeatureName)
		queryB = buildQuery(int(app_xplor.vars['year']),brooklyn,dbFeatureName)
		queryC = buildQuery(int(app_xplor.vars['year']),manhattan,dbFeatureName)
		queryD = buildQuery(int(app_xplor.vars['year']),queens,dbFeatureName)
		queryE = buildQuery(int(app_xplor.vars['year']),statenIsland,dbFeatureName)
                #executing the queries on the tables
                rawA = pd.read_json(queryA)
                rawB = pd.read_json(queryB)
                rawC = pd.read_json(queryC)
                rawD = pd.read_json(queryD)
		rawE = pd.read_json(queryE)
		
                #Managind the data to be input for a boxplot 
                rawA['Borough']='Bronx'
                rawB['Borough']='Brooklyn'
                rawC['Borough']='Manhattan'
                rawD['Borough']='Queens'
		rawE['Borough']='Staten Island'
		
                allData = pd.concat([rawA, rawB, rawC, rawD, rawE])
                cleanData= allData.dropna()
                cleanData.columns=[app_xplor.vars['feat'],'Borough']
		
                #plot
                defaults.width = 450
                defaults.height = 350   
                box_plot = BoxPlot(cleanData, label='Borough',title=str(app_xplor.vars['year']))
		#box_plot = BoxPlot(cleanData, label='Borough',title='Year')
                output_file("boxplot.html")
                show(
                    vplot(
                        hplot(box_plot)
                    )
                )
                return redirect('/goDistrib')


@app_xplor.route('/getFeat',methods=['GET','POST'])
def getFeature():
	if request.method == 'GET':
		return render_template('feature.html')
	else:
                bronx=[[2009,'https://data.cityofnewyork.us/resource/en2c-j6tw.json'],[2010,'https://data.cityofnewyork.us/resource/n2s5-fumm.json'],[2011,'https://data.cityofnewyork.us/resource/bawj-6bgn.json'],[2012,'https://data.cityofnewyork.us/resource/3qfc-4tta.json']]
                brooklyn=[[2009,'https://data.cityofnewyork.us/resource/rmv8-86p4.json'],[2010,'https://data.cityofnewyork.us/resource/w6yt-hctp.json'],[2011,'https://data.cityofnewyork.us/resource/5mw2-hzqx.json'],[2012,'https://data.cityofnewyork.us/resource/bss9-579f.json']]
                manhattan=[[2009,'https://data.cityofnewyork.us/resource/956m-xy24.json'],[2010,'https://data.cityofnewyork.us/resource/ad4c-mphb.json'],[2011,'https://data.cityofnewyork.us/resource/ikqj-pyhc.json'],[2012,'https://data.cityofnewyork.us/resource/dvzp-h4k9.json']]
                queens=[[2009,'https://data.cityofnewyork.us/resource/m59i-mqex.json'],[2010,'https://data.cityofnewyork.us/resource/crbs-vur7.json'],[2011,'https://data.cityofnewyork.us/resource/s3zn-tf7c.json'],[2012,'https://data.cityofnewyork.us/resource/jcih-dj9q.json']]
                statenIsland=[[2009,'https://data.cityofnewyork.us/resource/cyfw-hfqk.json'],[2010,'https://data.cityofnewyork.us/resource/wv4q-e75v.json'],[2011,'https://data.cityofnewyork.us/resource/a5qt-5jpu.json'],[2012,'https://data.cityofnewyork.us/resource/tkdy-59zg.json']]
                featureNames=[['comparable_rental_2_market_value_per_sqft',  'Market value per square foot'],['comparable_rental_2_full_market_value',      'Full market value'],['comparable_rental_2_year_built',             'Year Built'],['comparable_rental_2_gross_income_per_sqft', 'Gross income per square foot']]

		#request was a POST (get the var from the form)
		#common feature
		app_xplor.vars['feat'] = request.form['feat']
		#groups A and B
		app_xplor.vars['boA'] = request.form['boA']
		app_xplor.vars['boB'] = request.form['boB']
		app_xplor.vars['yA'] = request.form['yA']
		app_xplor.vars['yB'] = request.form['yB']

		#Translating name of the feature into the name in the original database
		dbFeatureName = convertField(app_xplor.vars['feat'],featureNames)

		#group A
		if  (app_xplor.vars['boA']=='Bronx'):
			queryA = buildQuery(int(app_xplor.vars['yA']),bronx,dbFeatureName)
		elif (app_xplor.vars['boA']=='Brooklyn'):
			queryA = buildQuery(int(app_xplor.vars['yA']),brooklyn,dbFeatureName)
		elif (app_xplor.vars['boA']=='Manhattan'):
			queryA = buildQuery(int(app_xplor.vars['yA']),manhattan,dbFeatureName)
		elif (app_xplor.vars['boA']=='Queens'):
			queryA = buildQuery(int(app_xplor.vars['yA']),queens,dbFeatureName)
		elif (app_xplor.vars['boA']=='Staten Island'):
			queryA = buildQuery(int(app_xplor.vars['yA']),statenIsland,dbFeatureName)
		
                #group B
                if  (app_xplor.vars['boB']=='Bronx'):
                        queryB = buildQuery(int(app_xplor.vars['yB']),bronx,dbFeatureName)
                elif (app_xplor.vars['boB']=='Brooklyn'):
                        queryB = buildQuery(int(app_xplor.vars['yB']),brooklyn,dbFeatureName)
                elif (app_xplor.vars['boB']=='Manhattan'):
                        queryB = buildQuery(int(app_xplor.vars['yB']),manhattan,dbFeatureName)
                elif (app_xplor.vars['boB']=='Queens'):
                        queryB = buildQuery(int(app_xplor.vars['yB']),queens,dbFeatureName)
                elif (app_xplor.vars['boB']=='Staten Island'):
                        queryB = buildQuery(int(app_xplor.vars['yB']),statenIsland,dbFeatureName)

		rawA = pd.read_json(queryA)
		rawB = pd.read_json(queryB)
		allData = pd.concat([rawA, rawB], axis=1)
		cleanData= allData.dropna()
		cleanData.columns=['A','B']
		
		#plot
		defaults.width = 450
		defaults.height = 350
		tA=str(app_xplor.vars['boA'])+'/'+str(app_xplor.vars['yA']) + '/' + str(app_xplor.vars['feat'])
		tB=str(app_xplor.vars['boB'])+'/'+str(app_xplor.vars['yB']) + '/' + str(app_xplor.vars['feat'])
		histA = Histogram(cleanData['A'], title=tA)
		histB = Histogram(cleanData['B'], title=tB)
		output_file("histograms.html")
		show(
		    vplot(
        		hplot(histA,histB)
		    )
		)
                return redirect('/goFeat')

@app_xplor.route('/goFeat',methods=['GET','POST'])
def goFeature():
	return render_template('featureResults.html')

@app_xplor.route('/goTrend',methods=['GET','POST'])
def goTrend():
        return render_template('trendResults.html')

@app_xplor.route('/goDistrib',methods=['GET','POST'])
def goDistrib():
        return render_template('distribResults.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app_xplor.run(host='0.0.0.0', port=port)
