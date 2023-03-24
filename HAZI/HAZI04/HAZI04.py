# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
#1
def csv_to_df(inp: str )->pd.core.frame.DataFrame:
    xc = pd.read_csv(inp)
    return xc

#print(csv_to_df("StudentsPerformance.csv"))
#print(type(csv_to_df("StudentsPerformance.csv")))
#df=csv_to_df("StudentsPerformance.csv")

# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
#2
def capitalize_columns(inp:  pd.core.frame.DataFrame )->pd.core.frame.DataFrame:
    xc = inp.copy()
    xc.columns= xc.columns.where( xc.columns.str.contains( 'e') == True, xc.columns.str.upper())
    return xc 

#print(capitalize_columns(df))

# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
#3
def math_passed_count(inp:  pd.core.frame.DataFrame )->int:
    xc = inp.copy()
    return sum(xc['math score']>=50)

#print(math_passed_count(df))
#print(type(math_passed_count(df)))

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
#4
def did_pre_course(inp:  pd.core.frame.DataFrame )->pd.core.frame.DataFrame:
    xc = inp.copy()
    return xc.loc[xc['test preparation course']=='completed']

#print(did_pre_course(df))
#print(type(did_pre_course(df)))

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
#5
def average_scores(inp:  pd.core.frame.DataFrame )->pd.core.frame.DataFrame:
    xc = inp.copy()
    a= 'math score'
    #xc = xc.groupby('parental level of education', as_index=False).agg(**{
    #    'math score':('math score', 'mean'),
    #    'reading score':('reading score', 'mean'),
    #    'writing score':('writing score', 'mean')
    #})
    xc = xc.groupby('parental level of education', as_index=False).agg({'math score':'mean','reading score':'mean','writing score': 'mean'})
    #xc= xc.groupby('parental level of education', as_index=False)['math score', 'reading score','writing score' ].mean()
    return xc

#print(average_scores(df))
#print(type(average_scores(df)))

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
#6
def add_age(inp:  pd.core.frame.DataFrame )->pd.core.frame.DataFrame:
    xc = inp.copy()
    np.random.seed(42)
    xc['age']= np.random.randint(18, 67, xc.shape[0])
    return xc

#print(add_age(df))
#print(type(add_age(df)))

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
#7
def female_top_score(inp:  pd.core.frame.DataFrame )->tuple:
    xc = inp.copy()
    xc = xc.loc[xc['gender']=='female']
    xc['sum'] = xc['math score']+xc['reading score']+xc['writing score']
    a = xc.nlargest(1,'sum')
    return (int(a['math score']), int(a['reading score']), int(a['writing score']))

#print(female_top_score(df))
#print(type(female_top_score(df)))

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
#8
def add_grade(inp:  pd.core.frame.DataFrame )->pd.core.frame.DataFrame:
    xc = inp.copy()
    xc['grade'] = (xc['math score']+xc['reading score']+xc['writing score'])/3
    for d in range(len(xc['grade'])):
        match xc['grade'][d]:
            case a if 0<= a <60:
                xc['grade'][d]='F'
            case a if 60<= a <70:
                xc['grade'][d]='D'
            case a if 70<= a<80:
                xc['grade'][d]='C'
            case a if 80<= a<90:
                xc['grade'][d]='B'
            case a if 90<= a<=100:
                xc['grade'][d]='A'
    return xc

#print(add_grade(df))
#print(type(add_grade(df)))


# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
#9
def math_bar_plot(inp:  pd.core.frame.DataFrame ):
    xc = inp.copy()

    fig, ax = plt.subplots()
    xc = xc.groupby('gender', as_index=False).agg({'math score':'mean'})
    ##print(xc)

    ax.bar(['male','female'], xc['math score'])
    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')

    return fig

#math_bar_plot(df)

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
#10


# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
#11


# %%



