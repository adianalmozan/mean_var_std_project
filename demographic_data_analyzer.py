import pandas as pd

def calculate_demographic_data(print_data=True):
    # تحميل البيانات من ملف CSV
    df = pd.read_csv("adult.data.csv")

    # 1️⃣ عدد الأشخاص من كل عرق
    race_count = df["race"].value_counts()

    # 2️⃣ متوسط عمر الرجال
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3️⃣ نسبة الأشخاص الحاصلين على درجة البكالوريوس
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4️⃣ نسبة الأشخاص الحاصلين على تعليم متقدم (>50K)
    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round((df[advanced_education]["salary"] == ">50K").mean() * 100, 1)

    # 5️⃣ نسبة الأشخاص بدون تعليم متقدم (>50K)
    lower_education_rich = round((df[~advanced_education]["salary"] == ">50K").mean() * 100, 1)

    # 6️⃣ الحد الأدنى من ساعات العمل في الأسبوع
    min_work_hours = df["hours-per-week"].min()

    # 7️⃣ نسبة الأشخاص الذين يعملون الحد الأدنى من الساعات ويكسبون >50K
    min_workers = df["hours-per-week"] == min_work_hours
    rich_percentage = round((df[min_workers]["salary"] == ">50K").mean() * 100, 1)

    # 8️⃣ الدولة ذات النسبة الأعلى لمن يكسبون >50K
    rich_by_country = df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts()
    highest_earning_country = rich_by_country.idxmax()
    highest_earning_country_percentage = round(rich_by_country.max() * 100, 1)

    # 9️⃣ الوظيفة الأكثر شيوعًا لمن يكسبون >50K في الهند
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].mode()[0]

    # ✅ طباعة النتائج إن لزم الأمر
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country, highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
from demographic_data_analyzer import calculate_demographic_data

calculate_demographic_data(print_data=True)
