import random
import pandas as pd
OET = 118 #per typical tree per year in kg
OEP = 369 #per typical plant per year in kg

COBT = 21 #per typical tree per year in kg
COBP = 0.0006935 # per typical plant per year in kg



def no_tree_plant(sqft,spc_sqft):
    a = round(sqft/spc_sqft)
    plt_no = round(a/3)#one third of the area is occupied by plants
    tree_no = a - plt_no #other left out area is occupied by trees
    return (tree_no,plt_no)     

def oxy_emi(st,oet,sp,oep):
    return (round((st*oet)+(sp*oep)))

def co2_obs(st,cobt,sp,cobp):
    return (round((st*cobt)+(sp*cobp)))



sqft_lst = []
OE_lst = []
COB_lst = []
area_lft_lst = []
con_tree_lst = []
con_plant_lst = []

for i in range(1,500):
    n = random.randint(2000,8000)
    sqft_lst.append(n)
for j in sqft_lst:
    spc_sqft = 12 #6 * 6 (6 spacing in row; 6 spacing in)
    no_t_p = no_tree_plant(j,spc_sqft)
    st, sp = no_t_p
    OE = oxy_emi(st,OET,sp,OEP)
    OE_lst.append(OE)
    COB = co2_obs(st,COBT,sp,COBP)
    COB_lst.append(COB)
    Area_left = round(j/8) # in most case one eighth of the area is occupied after building
    area_lft_lst.append(Area_left)
    # 4 + 4 = 8; in which we divided it by area left, so to get considerable trees and plants divide both by 4 
    Considerable_trees = round(st/4)
    Considerable_plants = round(sp/4)
    con_tree_lst.append(Considerable_trees)
    con_plant_lst.append(Considerable_plants) 


dict_df = {"Area": sqft_lst,"OE":OE_lst,"COb":COB_lst,"Area_left":area_lft_lst,"considerble trees":con_tree_lst,"considerable plants":con_plant_lst}
df = pd.DataFrame(dict_df)
df.to_csv("dataset.csv")


        
