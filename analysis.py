from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def create_dataframe_object(path):
    return pd.read_csv(path)


def merge_dataframes(df_first, df_second, df_third):
    main_headers = [x for x in df_first.columns]
    df_second.columns = main_headers
    df_third.columns = main_headers
    return pd.concat([df_first, df_second, df_third],
                     ignore_index=True)


def cleaning_data_df(df):
    df = df.drop(columns='Unnamed: 0')
    df.dropna(axis=0, how='all', inplace=True)
    return df


def processing_missing_values(df):
    df.gender = df.gender.replace(['man', 'woman'], ['m', 'f'])
    df.gender = df.gender.replace(['male', 'female'], ['m', 'f'])
    df.gender = df.gender.fillna('f')
    df.iloc[:, 5:] = df.iloc[:, 5:].fillna(0)
    return df


def qn_1(df):
    ages_group = {'0 - 15': range(16),
                  '15 - 35': range(15, 36),
                  '35 - 55': range(35, 56),
                  '55 - 70': range(55, 71),
                  '70 - 80': range(70, 81)}
    value = int(Counter(df.age).most_common(1)[0][0])
    age = [x for x, y in ages_group.items() if value in y]
    print("The answer to the 1st question: {}".format(*age))
    df.plot(y='age', kind='hist')
    plt.show()


def qn_2(df):
    diagnosis = Counter(df.diagnosis).most_common(1)
    print(f"The answer to the 2nd question: {diagnosis[0][0]}")
    title = [x[0] for x in Counter(pmv.diagnosis).items()]
    number = [x for x in Counter(pmv.diagnosis).values()]
    plt.pie(number, labels=title, autopct='%1.1f%%')
    plt.show()


def qn_3(df):
    height = df.height
    sns.violinplot(x=height)
    print("The answer to the 3rd question: It's because different metric system")
    plt.show()


general_df = create_dataframe_object('test\\general.csv')
prenatal_df = create_dataframe_object('test\\prenatal.csv')

sports_df = create_dataframe_object('test\\sports.csv')
all_dfs = merge_dataframes(general_df, prenatal_df, sports_df)
clean_data = cleaning_data_df(all_dfs)

pmv = processing_missing_values(clean_data)

# -------------------------- Questions 1 --------------------------------
# What is the most common age of a patient among all hospitals? Plot a
# histogram and choose one of the following age ranges: 0 - 15, 15 - 35,
# 35 - 55, 55 - 70, or 70 - 80
qn_1(pmv)

# -------------------------- Questions 2 --------------------------------
# What is the most common diagnosis among patients in all hospitals?
# Create a pie chart
qn_2(pmv)

# -------------------------- Questions 3 --------------------------------
# Build a violin plot of height distribution by hospitals. Try to answer
# the questions. What is the main reason for the gap in values? Why there
# are two peaks, which correspond to the relatively small and big values?
qn_3(pmv)
