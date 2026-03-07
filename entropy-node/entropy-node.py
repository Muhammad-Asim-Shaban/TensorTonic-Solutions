import numpy as np
import math
def entropy_node(y):
  n=len(y)
  if n==0:
    return 0.0
  values=[]
  count=0
  uniq=np.unique(y)
  for i in range(len(uniq)):
    for j in range(n):
      if y[j]==uniq[i]:
        count+=1
      
    values.append(count)
    count=0 
  
  values=np.array(values)
  values=values/n
  # print(values)
  entropy=0
  for i in range(len(values)):
    if values[i]!=0:
      entropy+=-(values[i]*math.log2(values[i]))
  
  return entropy