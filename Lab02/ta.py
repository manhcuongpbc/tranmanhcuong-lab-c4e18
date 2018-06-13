import pandas as pd
# k='foo bar bar bar'.replace('bar', 'XXX', 2).find('bar')
# print(k)
file_ = 'D:\C4E18\Labs\Lab02\ki- query to conversions.xlsx'

xl = pd.ExcelFile(file_)

# print(xl.sheet_names)

df1 = xl.parse('Sheet2')

# print(type(df1))

# print(df1[:5])

# with open('D:\C4E18\Labs\Lab02\ki- query to conversions.xlsx',encoding="utf8") as f:
#     i = 0
#     while i < 10:
#         for line in f:
#             i += 1
#             print(line)

list_of_dict = []
list_of_uid = []
list_of_query = []

for index, row in df1.iterrows():
    uid_query = {}
    uid_query['uid'] = row['u']
    uid_query['query'] = row['q']
    list_of_uid.append(row['u'])
    list_of_query.append(row['q'])
    list_of_dict.append(uid_query)
    # print(row['u'])
    # print(row['u'], row['q'])
# print(list_of_dict)
list_of_list_query = []
# list_of_query_for_user = []
# print(len(set(list_of_uid)))

for uid in set(list_of_uid):
    query_user = []
    for i in range(len(list_of_query)):
        if uid == list_of_uid[i]:
            query_user.append(list_of_query[i])
    
    list_of_list_query.append(query_user)
            
# print(list_of_list_query)
outfile = open('tiki.csv', 'w', encoding= 'utf8')
for query_of_user in list_of_list_query:
    for i in range(len(query_of_user)):
        if 'checkout' in query_of_user[0]:
            continue
        elif 'checkout' in query_of_user[i]:
            print(query_of_user[:i], file = outfile)
            break