str1="Shikha is working in Wipro. She is from Jhanshi. Jhanshi is the automotive hub in India. Wipro is not having a office in Coimbatore"
str2="Wipro is HQ in Bangalore and it works in different domains like Automotive, aerospace etc. Wipro may open a centre in Jhanshi soon"
lst1=str1.split(" ")
lst2=str2.split(" ")
import re
lst3=[]
lst4=[]
for i in range(len(lst1)):
    if re.search(lst1[i],str2):
        lst4.append(lst1[i])
        continue
    lst3.append(lst1[i])
print("the common words:",lst4)
print("common words removed in str1:"," ".join(map(str,lst3)))