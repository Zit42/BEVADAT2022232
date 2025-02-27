"""
1.  Értelmezd az adatokat!!!
    A feladat megoldásához használd a NJ transit + Amtrack csv-t a moodle-ból.
    A NJ-60k az a megoldott. Azt fogom használni a modellek teszteléséhez, illetve össze tudod hasonlítani az eredményedet.    

2. Írj egy osztályt a következő feladatokra:  
     2.1 Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
     2.2 Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el 
        a data (self.data) osztályszintű változóba 
     2.3 Írj egy függvényt ami sorbarendezi a dataframe-et 'scheduled_time' szerint növekvőbe és visszatér
        a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
     2.4 Dobjuk el a from és a to oszlopokat, illetve azokat a sorokat ahol van nan és adjuk vissza a df-et. 
        A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
     2.5 A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'.
        Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
     2.6 Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit.
        A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
             4:00-7:59 -- early_morning  
             8:00-11:59 -- morning  
             12:00-15:59 -- afternoon  
             16:00-19:59 -- evening  
             20:00-23:59 -- night  
             0:00-3:59 -- late_night  
    2.7 A késéseket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' 
        és térjen vissza a df-el
             0min <= x < 5min   --> 0  
             5min <= x          --> 1  
    2.8 Dobd el a felesleges oszlopokat 'train_id' 'actual_time' 'delay_minutes'. A függvény neve legyen 
        'drop_unnecessary_columns' és térjen vissza a df-el
    2.9 Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen !neve: 'path'! ,
         az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
    2.10 Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja 
        (sorbarendezés --> drop_columns_and_nan--> ... --> save_first_60k), 
        a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen ! neve. 'path' !.
        Ha default value-ja legyen 'data/NJ.csv'

3.  A feladatot a HAZI06.py-ban old meg.
    Az órán megírt DecisionTreeClassifier-t fit-eld fel az első feladatban lementett csv-re. 
    A feladat célja az, hogy határozzuk meg azt, hogy a vonatok késnek-e vagy sem.
    0p <= x < 5p --> nem késik (0), ha 5p <= x --> késik (1).
    Az adatoknak a 20% legyen test és a splitelés random_state-je pedig 41 (mint órán)
    A testset-en 80% kell elérni. Ha megvan a minimum százalék, akkor azzal paraméterezd fel a decisiontree-t és azt kell leadni.

    A leadásnál csak egy fit kell, ezt azzal a paraméterre paraméterezd fel, amivel a legjobb accuracy-t elérted.

    A helyes paraméter megtalálásához használhatsz grid_search-öt.
    https://www.w3schools.com/python/python_ml_grid_search.asp 

4.  A tanításodat foglald össze 4-5 mondatban a HAZI06.py-ban a fájl legalján kommentben.
    Írd le a nehézségeket, mivel próbálkoztál, mi vált be és mi nem. Ezen kívül írd le 10 fitelésed eredményét is,
    hogy milyen paraméterekkel probáltad és milyen accuracy-t értél el. 
Ha ezt feladatot hiányzik, akkor nem fogadjuk el a házit!

HAZI-
    HAZI06-
        -NJCleaner.py
        -HAZI06.py

##################################################################
##                                                              ##
## A feladatok közül csak a NJCleaner javítom unit test-el      ##
## A decision tree-t majd manuálisan fogom lefuttatni           ##
## NJCleaner - 10p, Tanítás - acc-nál 10%-ként egy pont         ##
## Ha a 4. feladat hiányzik, akkor nem tudjuk elfogadni a házit ##
##                                                              ##
##################################################################
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.DecisionTreeClassifier import DecisionTreeClassifier
from NJCleaner import NJCleaner

#NJCleaner("2018_03.csv").prep_df('Cleaned.csv')

data = pd.read_csv("Cleaned.csv")

X = data.iloc[:, : -1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
x_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=41)

i=50
j=11
classifier = DecisionTreeClassifier(min_samples_split=i, max_depth=j)
classifier.fit(x_train, Y_train)
Y_pred = classifier.predict(X_test)
#print("split:", i, "depth: ", j,accuracy_score(Y_test, Y_pred))


"""
Nehézség, hogy tippem se volt mire kéne fitelni. Ezen kívűl egy-egy fit vagy 1-10 percig fut itt, 
    szóval nem tudtam hogy elrontottam-e vagy némelyik tényleg ilyen sokáig fut-e.

Valamiért nem tudja behúzni az osztályokat ide, úgyhogy notebookba raktam be ezt a részt és ide csak átmásoltam, ott működik. 

A legtöbb fit 78-80% közé esett. ( split és depth 2-5 között, majd split 25, 50 és depth 5, 11) 

split: 2, depth: 2, acc: 0.7823333333333333
split: 2, depth: 3, acc: 0.7839166666666667
split: 2, depth: 4, acc: 0.7849166666666667
split: 2, depth: 5, acc: 0.7885833333333333
split: 3, depth: 2, acc: 0.7823333333333333
split: 3, depth: 3, acc: 0.7839166666666667
split: 3, depth: 4, acc: 0.7849166666666667
split: 3, depth: 5, acc: 0.7885833333333333
split: 4, depth: 2, acc: 0.7823333333333333
split: 4, depth: 3, acc: 0.7839166666666667
split: 4, depth: 4, acc: 0.7849166666666667
split: 4, depth: 5, acc: 0.7885833333333333

itt nem igazán változtatott a split mérete, csak a depth
ha a depth 8-10 értéket kapnak, akkor hibát dob 
split: 50, depth: 11, acc: 0.8026666666666666
"""
