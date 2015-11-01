This repository contains python/html code for an app named xplor. The app uses data from several public databases from the New York City open data website (https://data.cityofnewyork.us).

You can access the app at: https://xplorny.herokuapp.com/index


Intended use: This is an exploratory prototype application to showcase the use of several tools and techniques:

*integration of python - html using flask to process user requests.
*Programaticaly use of external APIs to access, filter, and combine data obtained from external sources using SQL-like commands.
*Use of pandas to manipulate the data.
*use of Bokeh to produce online interactive plots.
*Integration of Github - Heroku for collaborative work and web hosting of the app. 

  
The app uses real state data from 2009 to 2012 of the 5 boroughs of New York (Bronx, Brooklyn, Manhattan, Queens, and Staten Island). Specifically the data is related to rental profitability indexes in this area. The app starts with a landing page that invites the user to select a type of exploratory analysis to perform:

(a) A selected feature. Here the user will be able to compare (using histograms) the probability distributions corresponding to the selected real state feature on two different conditions created from combinations of NY Boroughs and time in years. 
(b) A trend. Here the user will the be able to analyze the trend (using a boxplot) followed by a selected real state feature on a NY borough.  
(c) A territorial distribution.  Here the user will explore (using a boxplot) the NY territorial distribution of a selected real state feature and year.  

The App was design as a prototype desition making guide for real state companies or investors. Specifically we would explore questions such as: what are the diferences in the market value per sqft of rental properties between the Bronx in 2009 and Staten Island in 2010? How does the full market value of properties in Queens has changes between 2009 and 2012? What was the NY borough that reported the worst/best rental gross income per sqft during 2012?
As a prototype we do not include here all the real state features and we limit the exploratory analysis to a few examples. Surely a few things could still be done to improve the prototype: inclusion of other types of data (e.g., criminality indexes), adding recent records (-2015), or including predictive analytics.

