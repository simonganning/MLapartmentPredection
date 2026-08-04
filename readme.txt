THIS PROJECT IS MADE ENTIERLY WITHOUT AI.
THAT MEANS SOME CODE MIGHT NOT BE OPTIMAL TO THE HIGHEST LEVEL
PLEASE BE ADVISED

For contact, please reach out to my email : simonganning@live.se

This is a machine learning project created by me (Simon Brzeskot Ganning) a computer science student enrolled at 
Linköping University (Sweden, Linköping)
The goal of this project is to predict apartment prices in Sweden with a minimal avrage of 90 % accuracy across
the test set.
A quick google search indicates that there are a few models that have performed better than 90% accuracy on
housing data. E.g. https://www.jetir.org/papers/JETIR2404493.pdf

This project is made of x amount of steps. Please read each step carefully to understand the process and 
the results. 

1. Decide where to collect the data
Hemnet and Booli are Swedens largest domains that have data from sold objects. Filtering out for apartments 
gives Hemnet just short of one million sold objects (963 148) and Booli at just over one million sold objects (1 028 746). 
Hemnet only shows 2500 objects (50 pages with 50 objects each) while Booli can show 35 000 objects 
(1000 pages with 35 objects each). I therfore decided to collect data from Booli since it would be more 
convinient. They should have a majority of same sold objects since they almost have the same amount and both
Hemnet and Booli states that over 90 % of all sold objects are on their websites. Thus, the data should not be 
that different. 

2. What data to collect?
Firslty we can look at what data Booli provides.
Adress, area, municipal, final price, original price, living area (m^2) , 
rooms, price per month , date sold , elevator , balcony, floor ,
We can then derive some values (like x and y cooridnates based on the adress)
Because it might be difficult to know beforehand I will collect all the data. 
I will not collect data that can be derived e.g price per square meter as it will create 
an unessecary amount of pings to the domain.

3. How to collect the data?
I used Selenium as a base and playwright on top of that to collect the data.
Booli uses cloudfare so in selenium i used stealth mode 
I also rotated on x amount of proxies and interacted with the website at random intervals to 
minimize botdetection. I collected data in batches. Booli could not provide more than 1000 pages , regardless
of what filter was used. I therfore collected the objects in batches of months. Each month contains no more than
10 000 objects. I therfore had a 25 000 objects margin. In the event of a month would have more than 35 000
objects, that data would be lost. In each batch a maximal of 35 000 objects can be viewed and collected. 
First listing was sold 2006-05-29 and the last 2026-08-xx


4. How to save the data
The data harvesting was performed on theese dates ...
It was then stored in a database where the primary key (PK) is the unique sold object id that can be found 
in the domain name when an object is viewed. 
Because that is our sole PK, no other entry can have the same PK and every object in my DB is unique
I choose xyz as my database



