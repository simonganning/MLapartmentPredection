THIS PROJECT IS MADE ENTIERLY WITHOUT AI.
THAT MEANS SOME CODE MIGHT NOT BE OPTIMAL TO THE HIGHEST LEVEL
PLEASE BE ADVISED

For contact, please reach out to my email : simonganning@live.se

This is a machine learning project created by me (Simon Brzeskot Ganning) a computer science student enrolled at 
Linköping University (Sweden, Linköping)
The goal of this project is to predict apartment prices in Sweden, Stockholms län (wider area)
with a minimal avrage of 90 % accuracy across the test set.

This project is made of x amount of steps. Please read each step carefully to understand the process and 
the results. 

1. Decide where to collect the data
Hemnet and Booli are Swedens largest domains that have data from sold objects. Filtering out for apartments 
gives Hemnet just short of one million sold objects (963 148) and Booli at just over one million sold objects (1 028 746). 
Hemnet only shows 2500 objects (50 pages with 50 objects each) while Booli can show 35 000 objects 
(1000 pages with 35 objects each). I therfore decided to collect data from Booli since it would be more 
convinient. They should have a majority of same sold objects since they almost have the same amount of objects and both
Hemnet and Booli states that over 90 % of all sold objects are on their websites. Thus, the data should not be 
that different. Booli have 455 333 objects in Stockholms län. That is the amount i chose.

2. What data to collect?
Firslty we can look at what data Booli provides. And we should collect it all.
Adress, area, municipal, final price, original price, living area (m^2) , 
rooms, price per month , date sold , elevator , balcony, floor ,
We can then derive some values (like x and y cooridnates based on the adress) 
I will not collect data that can be derived e.g price per square meter as it will create 
an unessecary amount of pings to the domain.

Might want to add anything about condition?

3. How to collect the data and how much?
I used Selenium as a base and playwright on top of that to collect the data.
Booli uses cloudfare so in selenium i used stealth mode 
I also rotated on x amount of proxies and interacted with the website at random intervals to 
minimize botdetection. I collected data in batches. Booli could not provide more than 1000 pages , regardless
of what filter was used. I therfore collected the objects in batches of 6 months.
One year has between 35 000 - 40 000 objects. So each batch has 17 500 - 20 000 objects. 
Well below the 35 000 margin. 

First listing was sold 2012-07-01 and the last 2026-07-31
If we look at previous research and how much they have collected

https://arxiv.org/pdf/2505.01591 
232,057 objects from 2021-2023 with 5 static and 52 dynamic variables
https://www.sciencedirect.com/science/article/pii/S1877050920316318 
231 962 objects from 2009 - 2018 with 19 variables 
Added an extra paramater from the city center to the house
Add how close to water
Add how close to nearest bus stop
Removed objects with missing data 
Removed an attribute if more than 50 % of the objects did not contain it 
Handled outliers with q1 - Qr 
Center will be from "Sergelfontänen" 59.33259017582446, 18.065174222189306


https://www.tandfonline.com/doi/full/10.1080/09599916.2020.1832558
40,000 objects from 1996 to 2014 with 6 different variables

So 455 333 objects with 15 variables will suffice. 


4. How to save the data
The data harvesting was performed on theese dates ...
It was then stored in a database where the primary key (PK) is the unique sold object id that can be found 
in the domain name when an object is viewed. 
Because that is our sole PK, no other entry can have the same PK and every object in my DB is unique
I choose xyz as my database

5. Any missing data?
Might want to either delete or calcualte based on some mean 
High low objects in each data might be taken away, should we use log?


6. Test set, validation set and traning set?

7. What models to choose and why?
Linear Regression

Random Forest

Extreme Gradient Boosting

Hybrid Regression

Light gradient boosting machine

Stacked Generalization (best for one)

Artificial Neural Netowrk

Gradient Boosting Machine

Support Vector Machine


8. Evaluation of the different models
What previous research has performed

9. How did we perform, what can improve?



