#! /usr/bin/env python

def buildQuery(year,borough,field):
        for i in range(len(borough)):
                if borough[i][0]==year:
                        URL=borough[i][1]
                        break
        stringQ=URL+'?&$select='+field

        return str(stringQ)

def convertField(webField,featureNames):
        for i in range(len(featureNames)):
                if featureNames[i][1]==webField:
                        dbFeature=featureNames[i][0]
                        break
        return dbFeature


def getTables():
	#tables of the condos
	bronx=[
	[2009,'https://data.cityofnewyork.us/resource/en2c-j6tw.json'],
	[2010,'https://data.cityofnewyork.us/resource/n2s5-fumm.json'],
	[2011,'https://data.cityofnewyork.us/resource/bawj-6bgn.json'],
	[2012,'https://data.cityofnewyork.us/resource/3qfc-4tta.json']
	]

	brooklyn=[
	[2009,'https://data.cityofnewyork.us/resource/rmv8-86p4.json'],
	[2010,'https://data.cityofnewyork.us/resource/w6yt-hctp.json'],
	[2011,'https://data.cityofnewyork.us/resource/5mw2-hzqx.json'],
	[2012,'https://data.cityofnewyork.us/resource/bss9-579f.json']
	]

	manhattan=[
	[2009,'https://data.cityofnewyork.us/resource/956m-xy24.json'],
	[2010,'https://data.cityofnewyork.us/resource/ad4c-mphb.json'],
	[2011,'https://data.cityofnewyork.us/resource/ikqj-pyhc.json'],
	[2012,'https://data.cityofnewyork.us/resource/dvzp-h4k9.json']
	]

	queens=[
	[2009,'https://data.cityofnewyork.us/resource/m59i-mqex.json'],
	[2010,'https://data.cityofnewyork.us/resource/crbs-vur7.json'],
	[2011,'https://data.cityofnewyork.us/resource/s3zn-tf7c.json'],
	[2012,'https://data.cityofnewyork.us/resource/jcih-dj9q.json']
	]

	statenIsland=[
	[2009,'https://data.cityofnewyork.us/resource/cyfw-hfqk.json'],
	[2010,'https://data.cityofnewyork.us/resource/wv4q-e75v.json'],
	[2011,'https://data.cityofnewyork.us/resource/a5qt-5jpu.json'],
	[2012,'https://data.cityofnewyork.us/resource/tkdy-59zg.json']
	]

	fields=[
	['comparable_rental_2_market_value_per_sqft',  'Market value per square foot'],
	['comparable_rental_2_full_market_value',      'Full market value'],
	['comparable_rental_2_year_built',             'Year Built'],
	['comparable_rental_2_estimated_gross_income', 'Estimated gross income']
	]
	return bronx, brooklyn, manhattan, queens, statenIsland, fields

