#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode
init_notebook_mode (connected=True)
from plotly.subplots import make_subplots
import warnings


# In[8]:


data = pd.read_csv(r'C:\Users\iran\Desktop\dataset.exel\insurance.csv')


# In[9]:


df=pd.DataFrame(data)
df.head(10).style.set_properties(**{"background-color":"#042e60" , "color":"white", "border_color":"1.5px solid white"})


# In[10]:


df.shape


# In[11]:


def describe (df):
    variables =[]
    dtypes =[]
    count =[]
    unique =[]
    missing = []
    min_ =[]
    max_ =[]
    
    for item in df.columns :
        
        variables.append(item)
        dtypes.append(df[item].dtype)
        count.append(len(df[item]))
        unique.append(len(df[item].unique()))
        missing.append(df[item].isna().sum())
        
        if df[item].dtypes == 'float64' or df[item].dtypes == 'int64':
            min_.append(df[item].min())
            max_.append(df[item].max())
        else:
            min_.append('Str')
            max_.append('Str')
        

    output = pd.DataFrame({
        'variable': variables, 
        'dtype': dtypes,
        'count': count,
        'unique': unique,
        'missing value': missing,
        'Min': min_,
        'Max': max_
    })    
        
    return output


# In[12]:


df_describe = describe(df)
df_describe.style.set_properties(**{"background-color": "#042e60","color":"white","border": "1.5px solid white"})


# In[13]:


Styles = [dict(selector = "caption",
               props = [("color", "black"), 
                        ("text-align", "center"),
                       ('font-size', '18pt'),
                       ('background-color', 'white'),
                       ('font-weight', 'bold')])]


# In[14]:


df_describe = df_describe.style.set_caption('Overview of the dataset').set_table_styles(Styles)
df_describe.set_properties(**{"background-color": "#042e60","color":"white","border": "1.5px solid white"})


# In[15]:


df.sex.value_counts()


# In[16]:


def categorize_bmi(bmi):
    if bmi < 18.5:
        return 'Wightloss'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overwight'
    else:
        return 'Obesity'

df['BMI_category'] = df['bmi'].apply(categorize_bmi)


# In[17]:


df


# In[18]:


colors = plt.get_cmap('Pastel1').colors
df.BMI_category.value_counts().plot(kind ="pie" , autopct='%1.1f%%', colors=colors, explode=(0.05 , 0,0,0));


# In[19]:


df.groupby(["smoker"])["BMI_category"].value_counts(normalize=True).mul(100).round(2)


# In[20]:


plt.figure(figsize=(7, 4))
axis=sns.countplot(data=df, x='BMI_category', hue='smoker',palette=["#FF7777" ,"#6EACDA"])
axis.bar_label(axis.containers[0])
axis.bar_label(axis.containers[1]) 

plt.title('Count of BMI Categories by smoker')
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.legend(title='smoker')
plt.show()


# In[21]:


df.groupby(["sex"])["BMI_category"].value_counts(normalize=True).mul(100).round(2)


# In[22]:


plt.figure(figsize=(7, 4))
axis=sns.countplot(data=df, x='BMI_category', hue='sex',palette=["#FF7777" ,"#6EACDA"])
axis.bar_label(axis.containers[0])
axis.bar_label(axis.containers[1]) 

plt.title('Count of BMI Categories by sex')
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.legend(title='sex')
plt.show()


# In[23]:


df.groupby(["region"])["BMI_category"].value_counts(normalize=True).mul(100).round(2)


# In[24]:


plt.figure(figsize=(7, 4))
axis=sns.countplot(data=df, x='BMI_category', hue='region',palette=['#02ccfe', '#eecffe' , '#8d5eb7' , '#7bc8f6'])
axis.bar_label(axis.containers[0])
axis.bar_label(axis.containers[1]) 
axis.bar_label(axis.containers[2]) 
axis.bar_label(axis.containers[3]) 

plt.title('Count of BMI Categories by region')
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.legend(title='region')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[25]:


###### plot ######


# In[26]:


mean_age = df['age'].mean()
max_age = df['age'].max()
min_age = df['age'].min()

# Plotting the distribution of 'age' values
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], bins=30, kde=True, edgecolor='black', alpha=0.6 , color='#8f99fb' )
plt.axvline(mean_age, color='red', linestyle='dashed', linewidth=1, label=f'Mean Age: {mean_age:.2f}')
plt.axvline(max_age, color='green', linestyle='dashed', linewidth=1, label=f'Max Age: {max_age:.2f}')
plt.axvline(min_age, color='blue', linestyle='dashed', linewidth=1, label=f'Min Age: {min_age:.2f}')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()


# In[27]:


mean_bmi = df['bmi'].mean()
max_bmi = df['bmi'].max()
min_bmi = df['bmi'].min()

# Plotting the distribution of 'age' values
plt.figure(figsize=(8, 6))
sns.histplot(df['bmi'], bins=30, kde=True, edgecolor='black', alpha=0.6 , color='#8f99fb')
plt.axvline(mean_bmi, color='red', linestyle='dashed', linewidth=1, label=f'Mean bmi: {mean_bmi:.2f}')
plt.axvline(max_bmi, color='green', linestyle='dashed', linewidth=1, label=f'Max bmi: {max_bmi:.2f}')
plt.axvline(min_bmi, color='blue', linestyle='dashed', linewidth=1, label=f'Min bmi: {min_bmi:.2f}')
plt.title('Distribution of Bmi')
plt.xlabel('Bmi')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()


# In[28]:


smokers_by_sex = df['sex'][df['smoker'] == "yes"].value_counts()
total_smokers = smokers_by_sex.sum()
percentages = (smokers_by_sex / total_smokers) * 100

plt.figure(figsize=(6, 5))
bar_plot = sns.barplot(x=smokers_by_sex.index, y=smokers_by_sex.values, palette=['#c760ff' , '#04d9ff'] ) 

# Adding counts on top of bars
for index, value in enumerate(smokers_by_sex):
    bar_plot.text(index, value + 0.5 , f'{value}', color='black', ha='center', va='bottom')
    
    
# Adding percentage labels
for index, value in enumerate (percentages):
    bar_plot.text(index, smokers_by_sex.values[index] + 9 , f'{value:.1f}%', color='red',va='bottom' , ha='center' , fontsize = 12)
    
plt.title('Distribution of Sex Among Smokers')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.grid()
plt.ylim(0, max(smokers_by_sex.values) +20)  
plt.show()


# In[29]:


yes_count = df['smoker'].value_counts().get('1', 0)
no_count = df['smoker'].value_counts().get('no', 0)

yes_count = (df['smoker'] == 'yes').sum()
no_count = (df['smoker'] == 'no').sum()
total_count = len(df)

yes_count_percentage = (yes_count / total_count) * 100
no_count_percentage = (no_count / total_count) * 100


pie_values = [yes_count_percentage, no_count_percentage]
colors = ['deepskyblue', 'orchid']

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 7))

axes[0].pie(pie_values, labels=[' NO smokrt', 'smoker'], autopct='%1.2f%%', explode=(0.02, 0.02), colors=colors)
axes[0].set_title('Percentage of Smoking people', fontweight='bold' , fontsize = 20)

sns.countplot(x='smoker', data=df, palette=['#f7022a', '#8b88f8'], ax=axes[1])
axes[1].set_title('Distribution of smoker' , fontsize = 20 ,  fontweight='bold')
axes[1].set_xticks([0, 1])
axes[1].set_xticklabels(['No smoker', 'smoker'])
for i in axes[1].containers:
    axes[1].bar_label(i)

plt.show()


# In[30]:


region_counts = df['region'].value_counts()
# Sorting by index to maintain order in plot
region_counts = region_counts.sort_index()
total_region = region_counts.sum()
percentages = percentages = (region_counts / total_region) * 100


# Plotting the bar plot
plt.figure(figsize=(6, 4))
bar_plot = sns.barplot(x=region_counts.index, y=region_counts.values, palette='pastel')


# Adding percentages on top of bars
for index, value in enumerate (percentages):
    bar_plot.text(index, region_counts.values[index] + 20 , f'{value:.1f}%', color='red',va='bottom' , ha='center' , fontsize = 10 )



# Adding counts on top of bars
for index, value in enumerate(region_counts):
    bar_plot.text(index, value + 0.5,f'{value}', color='black', ha='center', va='bottom')

plt.title('Distribution of Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.ylim(0, max(region_counts.values) +50)  
plt.grid(axis='y')  
plt.show()


# In[31]:


num_columns = ['age','bmi','children','charges']


# In[32]:


fig, axes = plt.subplots( nrows= 2, ncols=2, figsize = (7,6))
axes = axes.flatten()

for i , column in enumerate(num_columns):
    ax = axes[i]
    sns.boxplot(data = df, x = df[column], ax=ax , color = '#c1c6fc')

plt.tight_layout()
plt.show()


# In[33]:


df["sex"].replace({"female" : 2 , "male" : 3 } , inplace = True)
df["smoker"].replace({"yes" : 2 , "no" : 3} , inplace = True)
df["region"].replace({"southwest" : 2 , "southeast" : 3 , "northwest" : 4 , "northeast" : 5} , inplace = True)


# In[34]:


correlation_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='BuPu', fmt='.2f')
plt.title('Correlation Matrix' , fontweight='bold')
plt.show()


# In[35]:


df.columns


# In[36]:


####### model linear regression ########


# In[37]:


print (pd.unique(df["sex"]))
print (pd.unique(df["smoker"]))
print (pd.unique(df["region"]))


# In[38]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures


# In[39]:


x = pd.DataFrame(df , columns = ["age" , "sex" , "bmi" , "children" , "smoker" , "region" ])
y = df["charges"].values.reshape(-1,1)


# In[40]:


x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.1 , random_state = 0)


# In[41]:


print ("x train" , x_train.shape)
print ("x test" , x_test.shape)
print ("y train" , y_train.shape)
print ("y test" , y_test.shape)


# In[42]:


regressor = LinearRegression ()


# In[43]:


regressor.fit (x_train , y_train)


# In[44]:


y_pred = regressor.predict(x_test)


# In[45]:


compare = pd.DataFrame({"Actual": y_test.flatten() , "predict": y_pred.flatten()})
compare


# In[46]:


### First model
print('mean Absolute Error:' , metrics.mean_absolute_error(y_test , y_pred))
print('mean squared Error :' , metrics.mean_squared_error(y_test , y_pred))
print('Root mean squared Error :' , np.sqrt(metrics.mean_squared_error(y_test , y_pred)))
print('R2score:' , metrics.r2_score(y_test , y_pred))


# In[47]:


def chek (Dimension , Testsize):
    r2 =  0.8215430369031267
    for column in x :
        new_col_name = column + str(Dimension)
        new_col_val = x[column]** Dimension
        x.insert(0 , new_col_name , new_col_val)
        x_train , x_test , y_train , y_test = train_test_split (x ,y ,test_size = Testsize , random_state =0)
        new_model = LinearRegression()
        new_model .fit(x_train , y_train)
        y_pred = new_model.predict(x_test)
        r2_new = metrics.r2_score(y_test , y_pred)
        
        if r2_new < r2 :
            x.drop([new_col_name] , axis = 1 , inplace = True)
        else :
                r2 = r2_new
    print  ('R2 score :', r2)       

chek(3, 0.1)
        


# In[48]:


x


# In[49]:


age_bmi = x["age"] * x["bmi"]
age3_bmi = x["age3"] * x["bmi"]

age_sex = x["age"] * x["sex"]
age3_sex = x["age3"] * x["sex"]


smokers_age = x["smoker"] * x["age"]
smokers_age3 = x["smoker"] * x["age3"]
smokers3_age = x["smoker3"] * x["age"]
smokers3_age3 = x["smoker3"] * x["age3"]


# In[50]:


x.insert(0 , "age_bmi", age_bmi)
x.insert(0 , "age3_bmi", age3_bmi)
x.insert(0 , "age_sex", age_sex)
x.insert(0 , "smokers_age", smokers_age)
x.insert(0 , "smokers_age3", smokers_age3)
x.insert(0 , "smokers3_age", smokers3_age)
x.insert(0 , "smokers3_age3", smokers3_age3)


# In[51]:


x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.1, random_state = 0)
model = LinearRegression()
model.fit(x_train , y_train)
y_pred = model.predict(x_test)
r2 = metrics.r2_score(y_test , y_pred)

print('mean Absolute Error:' , metrics.mean_absolute_error(y_test , y_pred))
print('mean squared Error :' , metrics.mean_squared_error(y_test , y_pred))
print('Root mean squared Error :' , np.sqrt(metrics.mean_squared_error(y_test , y_pred)))
print('R2score:' , metrics.r2_score(y_test , y_pred))


# In[52]:


pf = PolynomialFeatures(degree = 1)
x_train1 = pf.fit_transform(x_train)
x_test1 = pf.transform(x_test)

lr_pf = LinearRegression().fit(x_train1, y_train)


# In[53]:


print(f'model accuracy on training set : {lr_pf.score(x_train1, y_train)}')
print(f'modle accuracy on test set : {lr_pf.score(x_test1, y_test)}')


# In[54]:


df.columns


# In[55]:


####################   RandomForestRegression  ###################


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


# In[56]:


forest = RandomForestRegressor(n_estimators = 100,
                              criterion = 'squared_error',
                              max_depth= 4,
                              random_state = 0,
                              n_jobs = -1)
forest.fit(x_train, y_train)
forest_train_pred = forest.predict(x_train)
forest_test_pred = forest.predict(x_test)

print('MSE train data: %.3f, MSE test data: %.3f' % (
mean_squared_error(y_train,forest_train_pred),
mean_squared_error(y_test,forest_test_pred)))
print('R2 train data: %.3f, R2 test data: %.3f' % (
r2_score(y_train,forest_train_pred),
r2_score(y_test,forest_test_pred)))


# In[57]:


### it is necesseray to do this to get a plot
x_test.insert(0 , "y_test" , y_test)
x_test.insert(1 , "y_pred" , y_pred)
x_test


# In[ ]:





# In[ ]:





# In[ ]:




