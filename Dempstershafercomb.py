# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:32:46 2019
Dempsters-Shafer combination rule for Mass probabilities
@author: Leonard Kanashiro Felizardo
"""
from itertools import combinations

def Create_All_Combinations(evi,n):
    all_combi=[]
    for i in range(1,n+1):
        all_combi = all_combi+list(combinations(evi,i))
    return all_combi

def Normalization_Factor(a,b,evi):        
    empty_inter = 0
#    count = 0    
    for j in range(0,len(b)):
        for i in range(0,len(a)):
            if set(evi[i]).intersection(set(evi[j]))==set():
                empty_inter += a[i]*b[j]
#                count=count+1
#                print(count," ",a[i]*b[j])
#                if count%7 ==0:
#                    print("________________________")
#            else:
#                count=count+1
#                print(count," ",0)
#                if count%7 ==0:
#                    print("________________________")
    normalization_factor = 1-empty_inter
    return normalization_factor

#print(Normalization_Factor(second,first,evidences))

def Intersection_Evidence(a,b,evi,e):
    total_inter = 0
#    count = 0
    e = set(e)
    for j in range(0,len(b)):
        for i in range(0,len(a)):
            if set(evi[i]).intersection(set(evi[j]))==e:
                total_inter += a[i]*b[j]
#                count=count+1
#                print(count," ",a[i]*b[j])
#                if count%7 ==0:
#                    print("________________________")
#            else:
#                count=count+1
#                print(count," ",0)
#                if count%7 ==0:
#                    print("________________________")
    return total_inter

#print(Intersection_Evidence(second,first,evidences,evidences[0]))

def Dempster_Shafer_Mult(a,b,evi):
    #a is the first vector, b is the second vector and n is the number of possibilities
    normalization_factor = Normalization_Factor(a,b,evi)
    m_updated = []
    for i in range (0,len(evi)):
        m_updated.append(round(Intersection_Evidence(second,first,evi,evi[i])/normalization_factor,4))    
    return m_updated

############################################
#Parameters:
############################################
    
n=3
evidences = 'BJS'
first = [0.1, 0.2, 0.1, 0.1, 0.1,0.3,0.1]
second = [0.2, 0.1, 0.05, 0.3, 0.05,0.1,0.2]
evidences = Create_All_Combinations(evidences,n)

############################################
#Result:
############################################

print(Dempster_Shafer_Mult(first,second,evidences))





