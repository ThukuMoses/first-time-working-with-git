import numpy as np

space=np.array([1,2,3,4,5,6])
space_boo=[True,False,True,True,False,False]
new_space=space[space_boo]
print(new_space)#values in space corresponding to the True value in space_boo will be printed in a new array without changing the original array

#filter array
cosmos=np.array([41,51,68,89,34,36])

#create empty list
filter_cosm=[]
#go through each element in cosmos
for x in cosmos:
    if x>50:
        filter_cosm.append(True)
    else:
        filter_cosm.append(False)

new_cosmos=cosmos[filter_cosm]
print(f"Filter_cosm:\n{filter_cosm}")
print(f"New_cosmos:\n{new_cosmos}")

#return only the even elements
filter_ev=[]
for x in cosmos:
    if x%2==0:
        filter_ev.append(True)
    else:
        filter_ev.append(False)

new_ecos= cosmos[filter_ev]   
print(f"Filter_ev:\n{filter_ev}")
print(f"New_cosmos:\n{new_ecos}")

#create filter directly from array
fil_cos=cosmos>50#change here to cosmos%2==0 to get a directly filtered by even array
new_fcos=cosmos[fil_cos]
print(f"Directly filtered boolean array: \n{fil_cos}")
print(f"Directly filtered array:\n{new_fcos}")