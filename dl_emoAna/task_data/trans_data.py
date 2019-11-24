import numpy as np
import pandas as pd

data = pd.read_csv('../../tra_emoAna/Train/Train_DataSet.csv', encoding='utf-8')
label = pd.read_csv('../../tra_emoAna/Train/Train_DataSet_Label.csv', encoding='utf-8')

table_merge = pd.merge(data, label)

# 转换数据类型
table_merge['title'] = table_merge['title'].astype('str')
table_merge['content'] = table_merge['content'].astype('str')
table_merge['label'] = table_merge['label'].astype('int')
# table_merge['content'].str.cat(table_merge['title']) 
# table_merge['content'] = table_merge['content'].str[:100]
# table_merge['content'] = table_merge['content'].astype('str')
# table_merge['content'].replace('\s','a')
# table_merge['content'] = table_merge['content'].str.strip('\t')
table_merge['content'] = table_merge['title']

# 删除有空值的行
# table_merge.dropna()
row_len = table_merge.shape[0]

# 保存转换后的数据

# 尝试将问题化成二分类
# table_merge['label'] = np.sign(table_merge['label'])
# train.tsv
table_merge_train = table_merge.loc[0.2*row_len:, ['label', 'content']]
# table_merge_train.rename(columns = {'content' :'text_a'}, inplace = True)
table_merge_train.columns = ['label','text_a']
table_merge_train.to_csv('train.tsv', sep='\t', index = False)

# test.tsv
table_merge_test = table_merge.loc[:0.1*row_len, ['label', 'content']]
# able_merge_test.rename(columns = {'content' :'text_a'}, inplace = True)
table_merge_test.columns = ['label','text_a']
table_merge_test.to_csv('test.tsv', sep='\t', index = False)

# dev.tsv
table_merge_dev = table_merge.loc[0.1*row_len:2*0.1*row_len, ['label', 'content']]
# table_merge_dev.rename(columns = {'content' :' text_a'}, inplace = True)
table_merge_dev.columns = ['label','text_a']
table_merge_dev.to_csv('dev.tsv', sep='\t', index = False)
