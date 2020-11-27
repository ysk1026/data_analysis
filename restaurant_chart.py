import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import re

file_path = './data/chipotle.csv'

#sep = separate, 탭으로 구분한다.
chipo = pd.read_csv(file_path)
# print(chipo.item_name)

#차트의 크기를 조정. (가로, 세로)
plt.rcParams["figure.figsize"] = (20,10)

#차트 눈금선을 표기
plt.rcParams['axes.grid'] = True 
plt.rcParams.update({'font.size': 8})

top_menu = chipo.item_name.value_counts()[:10]
temp_df = pd.DataFrame({'item_name' : top_menu.index, 'quantity': top_menu.values})

x=temp_df['item_name']
y=temp_df['quantity']

plt.bar(x,y)
plt.xlabel('x=item_name')
plt.ylabel('y=quantity')
plt.title('Best Top10')
plt.show()

#음식마다 들어간 'ingredients' 각각의 총합을 알기 위해, 모든 데이터를 추출하여 배열로 재조합
file_path2 = './data/chipotle_result.csv'

#sep = separate, 탭으로 구분한다.
chipo_result = pd.read_csv(file_path2)

sum=''
for i in chipo_result['ingredients'] :
    if i !='Origin' :
        sum+=i.strip()
        
arr=sum.split(',')

#한 줄의 배열로 재조합 한 뒤, 재료별로 합쳐 갯수를 세아리기 위해 DataFrame으로 재변환
df=pd.DataFrame(arr,columns=['ingredients'])
df_Top10=df['ingredients'].value_counts().head(10)

#차트로 나타내기 위한 과정
df_temp=pd.DataFrame({'ingredients':df_Top10.index, 'amounts':df_Top10.values})
x=df_temp['ingredients']
y=df_temp['amounts']

plt.bar(x,y)
plt.xlabel('x=ingredients')
plt.ylabel('y=amounts')
plt.show()