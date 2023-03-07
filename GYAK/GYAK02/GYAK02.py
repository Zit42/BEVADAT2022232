# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
#Paraméterei: mérete (tuple-ként), default mérete pedig legyen egy (2,2)
#Be: (2,2)
#Ki: [[0,0],[0,0]]
#create_array()

# %%
#1
def create_array(size: tuple=(2,2))->np.array:
    return np.zeros(size)

#print(create_array())

# %%
#Készíts egy függvényt ami a paraméterként kapott array-t főátlóját feltölti egyesekkel
#Be: [[1,2],[3,4]]
#Ki: [[1,2],[3,1]]
#set_one()

# %%
#2
def set_one(inp: np.array)->np.array:
    np.fill_diagonal(inp, 1)
    return inp


#print(set_one(np.array([[1,2],[3,4]])))

# %%
# Készíts egy függvényt ami transzponálja a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 2], [3, 4]]
# do_transpose()

# %%
#3
def do_transpose(inp: np.array)-> np.array:
    return inp.transpose()

#print(do_transpose(np.array([[1,2],[3,4]])))
#print(type(do_transpose(np.array([[1,2],[3,4]]))))

# %%
# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, ha nincs megadva ez a paraméter, akkor legyen az alapértelmezett a kettő 
# Be: [0.1223, 0.1675], 2
# Ki: [0.12, 0.17]
# round_array()

# %%
#4
def round_array(inp: np.array, r: int=2)-> np.array:
    return np.around(inp, r)

#print(round_array([0.1223, 0.1675], 2))
#print(type(round_array([0.1223, 0.1675], 2)))

# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 0 - False-ra, az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()

# %%
#5
def bool_array(inp: np.array)->np.array:
    return np.array(inp, dtype=bool)

#print(bool_array(np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]])))

# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# invert_bool_array()

# %%
#6
def bool_array(inp: np.array)->np.array:
    xc=np.array(inp, dtype=bool)
    return np.invert(xc, dtype=bool)
#print(bool_array([[1, 0, 0], [1, 1, 1],[0, 0, 0]]))

# %%
# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()


# %%
#7

# %%



