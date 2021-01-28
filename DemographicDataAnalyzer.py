import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"]=="Male"]["age"].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df["education"].value_counts()["Bachelors"]*100/len(df.index)
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    a = df[df["education"] == "Bachelors"]
    b = df[df["education"] == "Masters"]
    m = df[df["education"] == "Doctorate"]
    
    x = pd.concat([a,b,m])

    k = pd.concat([df,x]).drop_duplicates(keep=False)
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = x
    lower_education = k

    # percentage with salary >50K
    higher_education_rich = x["salary"].value_counts()[">50K"]*100/len(x.index)
    higher_education_rich = round(higher_education_rich, 1)

    lower_education_rich = k["salary"].value_counts()[">50K"]*100/len(k.index)
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    n = df[df["hours-per-week"]==min_work_hours]

    num_min_workers = len(n.index)

    rich_percentage = n["salary"].value_counts()[">50K"]*100/num_min_workers
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    popRich = df[df['salary'] == '>50K']['native-country'].value_counts()
    popTotal = df['native-country'].value_counts()

    popRich = popRich/popTotal

    highest_earning_country = popRich[popRich.values == popRich.max()].index[0]
    highest_earning_country_percentage = round((popRich.max()*100),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[df["native-country"]=="India"]
    india50 = india[india["salary"]==">50K"]
    top_IN_occupation = india50["occupation"].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }