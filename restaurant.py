import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import re

file_path = './data/chipotle.csv'

#sep = separate, 탭으로 구분한다.
chipo = pd.read_csv(file_path)

print(f'처음 5개 행 확인: \n {chipo.head(5)}')
print(f'칼럼 확인: {chipo.columns}') # 칼럼 확인

'''
Columns 
    1. order_id
    2. quantity
    3. item_name
    4. choice_description
    5. item_price     
'''

tmp_arr = chipo['item_name'].unique() #unique는 중복 데이터 제거하는 함수
len(tmp_arr)
print(f'아이템 종류: {tmp_arr}')

print()
print("######################## 메뉴당 가격 ###########################")
# 메뉴당 가격
chipo['item_price'] = chipo['item_price'].str.lstrip('$')
chipo['item_price'] = chipo['item_price'].astype(float)
# print(chipo['item_price'])
# print(type(chipo['item_price'][0]))
chipo_cost = chipo.groupby('item_name')['item_price'].mean()

print(chipo_cost.sort_values(ascending=False))

'''
제일 비싼 음식: Bowl($14.8)
'''

#####################################################################################################
#################################### 어떤 음식이 제일 선호되는지 확인 #######################################
#####################################################################################################
print()
print()
chipo.drop(['order_id', 'item_price'], axis='columns', inplace=True) # inplace = True 는 해당 변화를 즉각 DF에 반영하겠다는 의미
                                                                     # False로 한다면 새로운 DF에 변경 내용을 담아줘야함.
print(f'Order id, item price drop 이후 DF : \n {chipo.head(5)}')

print()
chipo['choice_description'].fillna('Origin', inplace = True) # 해당 컬럼에 NaN값이 많아서 해당 값들을 Origin으로 변경한다
print(f'Choice Description 내 NaN 값 변경 이후 : \n {chipo.head(5)}')


num = 0
for i in chipo['choice_description'] :
    # 알파벳과 ',' 그리고 공백을 제외하고 모두 지운다
    chipo['choice_description'][num] = re.sub(pattern='[^a-zA-Z,]', repl=' ', string=i)
    num += 1

chipo['saurce'] = chipo['choice_description'].str.split(',').str[0]
chipo['ingredients'] = chipo['choice_description'].str.split(',').str[1:]
print(chipo)
# print(len(chipo['ingredients'][0]))
num = 0
for ingredient in chipo['ingredients']:
    if len(ingredient) == 0:
        chipo['ingredients'][num] = 'Origin'
    else:
        chipo['ingredients'][num] = ','.join(ingredient)
    num += 1

chipo.drop(['choice_description'], axis='columns', inplace=True) 
# print(chipo)

# 중복되는 데이터 합치기
result_tmp = chipo.groupby(['item_name','saurce'])['ingredients'].value_counts()
result_tmp = result_tmp.to_frame()
# print(result_tmp)

file_path='./data/chipotle_result.csv'
result_tmp.to_csv(file_path, sep=',')