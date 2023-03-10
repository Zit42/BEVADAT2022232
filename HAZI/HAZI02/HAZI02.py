# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%
# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait. Bemenetként egy array-t vár.
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()

# %%
#1
def column_swap(inp: np.array)->np.array:
    if len(inp)==0:
        return inp
    ###inp[:,[0,1]] = inp[:,[1,0]]
    res=np.flip(inp, 1)
    return res

#print(column_swap(np.array([[1,2],[3,4]])))
#print(column_swap(np.array([])))
#print(type(column_swap(np.array([[1,2],[3,4]]))))

# %%
# Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek 
# Pl Be: [7,8,9], [9,8,7] 
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön

# %%
#2
def compare_two_array(inp1: np.array, inp2:np.array)->np.array:
    return np.where(np.equal(inp1,inp2))

#print(compare_two_array([7,8,9], [9,8,7] ))
#print(compare_two_array([], [] ))


# %%
# Készíts egy olyan függvényt, ami vissza adja string-ként a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!, 

# %%
#3
def get_array_shape(inp: np.array)->str:
    shaped = np.shape(inp)
    return f"sor: {shaped[0]}, oszlop: {shaped[1]}, melyseg: {shaped[2] if len(shaped) == 3 else 1}"

#print(get_array_shape(np.array([[1,2,3], [4,5,6]])))
#print(get_array_shape(np.array([[], []])))
#print(type(get_array_shape(np.array([[1,2,3], [4,5,6]]))))

# %%
# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges pred-et egy numpy array-ből. 
# Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek.
# Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli. 
# Pl. ha 1 van a bemeneten és 4 classod van, akkor az adott sorban az array-ban a [1] helyen álljon egy 1-es, a többi helyen pedig 0.
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()

# %%
#4
def encode_Y(inp: np.array, cnt:int)->np.array:
    a=np.zeros((cnt,cnt), int)
    a[np.arange(len(a)), inp] = 1
    return a

#print(encode_Y([1, 2, 0, 3], 4))
#print(type(encode_Y([1, 2, 0, 3], 4)))

# %%
# A fenti feladatnak valósítsd meg a kiértékelését. Adj meg a 2d array-t és adj vissza a decodolt változatát
# Be:  [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# Ki:  [1, 2, 0, 3]
# decode_Y()

# %%
#5
def decode_Y(inp: np.array)->np.array:
    return np.nonzero(inp)[1]

#print(decode_Y([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]))
#print(type(decode_Y([[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]])))
#print(decode_Y([[]]))

# %%
# Készíts egy olyan függvényt, ami képes kiértékelni egy neurális háló eredményét! 
# Bemenetként egy listát és egy array-t és adja vissza azt az elemet, aminek a legnagyobb a valószínüsége(értéke) a listából.
# Be: ['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]. 
# Az ['alma', 'körte', 'szilva'] egy lista!
# Ki: 'szilva'
# eval_classification()

# %%
#6
def eval_classification(l:list, a:np.array)->str:
    xc = np.argmax(a)
    ##xc= np.where(a==np.amax(a))
    return l[xc]

#print(eval_classification(['alma', 'körte', 'szilva'], [0.2, 0.2, 0.6]))

# %%
# Készíts egy olyan függvényt, ahol az 1D array-ben a páratlan számokat -1-re cseréli
# Be: [1,2,3,4,5,6]
# Ki: [-1,2,-1,4,-1,6]
# repalce_odd_numbers()

# %%
#7
def replace_odd_numbers(inp: np.array)->np.array:
    inp[inp%2 !=0 ] =-1
    return inp

#print(replace_odd_numbers(np.array([1,2,3,4,5,6])))
#print(type(replace_odd_numbers(np.array([1,2,3,4,5,6]))))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit -1 és 1-re változtatja, 
#   attól függően, hogy az adott elem nagyobb vagy kisebb a paraméterként megadott számnál.
# Ha a szám kisebb mint a megadott érték, akkor -1, ha nagyobb vagy egyenlő, akkor pedig 1.
# Be: [1, 2, 5, 0], 2
# Ki: [-1, 1, 1, -1]
# replace_by_value()

# %%
#8
def replace_by_value(inp: np.array, numb: int)->np.array:
    inp=np.where(inp <numb,-1,1)
    return inp

#print(replace_by_value(np.array([1, 2, 5, 0]), 2))
#print(type(replace_by_value(np.array([1, 2, 5, 0]), 2)))

# %%
# Készíts egy olyan függvényt, ami egy array értékeit összeszorozza és az eredményt visszaadja
# Be: [1,2,3,4]
# Ki: 24
# array_multi()
# Ha több dimenziós a tömb, akkor az egész tömb elemeinek szorzatával térjen vissza

# %%
#9
def array_multi(inp: np.array)->np.array:
    if len(inp)==0:
        return 0
    return np.prod(inp)

#print(array_multi(np.array([1,2,3,4])))
#print(array_multi(np.array([[2,2],[3,4]])))
#print(array_multi(np.array([])))

# %%
# Készíts egy olyan függvényt, ami egy 2D array értékeit összeszorozza és egy olyan array-el tér vissza, aminek az elemei a soroknak a szorzata
# Be: [[1, 2], [3, 4]]
# Ki: [2, 12]
# array_multi_2d()

# %%
#10
def array_multi_2d(inp: np.array)->np.array:
    if len(inp)==0:
        return 0
    return np.prod(inp, axis=1)

#print(array_multi_2d(np.array([[2,2],[3,4]])))
#print(array_multi_2d(np.array([])))
#print(array_multi_2d(np.array([],[])))

# %%
# Készíts egy olyan függvényt, amit egy meglévő numpy array-hez készít egy bordert nullásokkal.
# Bementként egy array-t várjon és kimenetként egy array jelenjen meg aminek van border-je
# Be: [[1,2],[3,4]]
# Ki: [[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,0]]
# add_border()


# %%
#11
def add_border(inp: np.array)->np.array:
    return np.pad(inp, pad_width=1, mode='constant', constant_values=0)

#print (add_border([[1,2],[3,4]]))
#print (add_border([]))

# %%
# A KÖTVETKEZŐ FELADATOKHOZ NÉZZÉTEK MEG A NUMPY DATA TYPE-JÁT!

# %%
# Készíts egy olyan függvényt ami két dátum között felsorolja az összes napot és ezt adja vissza egy numpy array-ben.
# A fgv ként str vár paraméterként 'YYYY-MM' formában.
# Be: '2023-03', '2023-04'  # mind a kettő paraméter str.
# Ki: ['2023-03-01', '2023-03-02', .. , '2023-03-31',]
# list_days()

# %%
#12
def list_days(start_date:str, end_date:str)->np.array:
    return np.arange(start_date, end_date, dtype='datetime64[D]')

#print(list_days("2011-01","2011-02"))
#print(type(list_days("2011-01","2011-02")))

# %%
# Írj egy fügvényt ami vissza adja az aktuális dátumot az alábbi formában: YYYY-MM-DD. Térjen vissza egy 'numpy.datetime64' típussal.
# Be:
# Ki: 2017-03-24
### get_act_date()

# %%
#13
def get_act_date()->np.datetime64:
    return np.datetime64('today')

#print(get_act_date())
#print(type(get_act_date()))

# %%
# Írj egy olyan függvényt ami visszadja, hogy mennyi másodperc telt el 1970 január 01. 00:02:00 óta. Int-el térjen vissza
# Be: 
# Ki: másodpercben az idó, int-é kasztolva
# sec_from_1970()

# %%
#14
def sec_from_1970()->int:
    xc=np.datetime64('now')
    return xc.astype('datetime64[s]').astype('int')-120

#print(sec_from_1970())
#print(type(sec_from_1970()))

# %%



