import pandas as pd
import matplotlib.pyplot as plt

statslift_id = '1tRa1dLQwfHAGRCfn121nH3KSmV02TeaRogHzUzyaWrE'
SHEET_NAME = 'STATSLIFT'
url = f'https://docs.google.com/spreadsheets/d/{statslift_id}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)

ohp_1rm = []
squat_1rm = []
bench_1rm = []
deadlift_1rm = []

def one_rep_max(weight, reps):
    return round(weight / ( 1.0278 - 0.0278 * reps ), 2)

def cleanse_string(stat_value):
    weight_rep = stat_value.split('x')
    return one_rep_max(int(weight_rep[0]), int(weight_rep[1]))

for index, row in df.iterrows():
    if type(row['OHP']) == str and row['OHP'][0].isdigit():
        weight_1_max = cleanse_string(row['OHP'])
        weight = row['Weight (KG)']
        BW_relation = round((weight_1_max * 0.4535) / weight, 4)
        data = [row['Date'], weight, weight_1_max, BW_relation]
        ohp_1rm.append(data)
    if type(row['Squat']) == str and row['Squat'][0].isdigit():
        weight_1_max = cleanse_string(row['Squat'])
        weight = row['Weight (KG)']
        BW_relation = round((weight_1_max * 0.4535) / weight, 4)
        data = [row['Date'], weight, weight_1_max, BW_relation]
        squat_1rm.append(data)
    if type(row['Bench Press']) == str and row['Bench Press'][0].isdigit():
        weight_1_max = cleanse_string(row['Bench Press'])
        weight = row['Weight (KG)']
        BW_relation = round((weight_1_max * 0.4535) / weight, 4)
        data = [row['Date'], weight, weight_1_max, BW_relation]
        bench_1rm.append(data)
    if type(row['Deadlift']) == str and row['Deadlift'][0].isdigit():
        weight_1_max = cleanse_string(row['Deadlift'])
        weight = row['Weight (KG)']
        BW_relation = round((weight_1_max * 0.4535) / weight, 4)
        data = [row['Date'], weight, weight_1_max, BW_relation]
        deadlift_1rm.append(data)

ohp_df = pd.DataFrame(ohp_1rm, columns=['Date', 'BW (KG)', "1RM OHP", "1RM/BW"])
ohp_df["Date"]= pd.to_datetime(ohp_df["Date"])
squat_df = pd.DataFrame(squat_1rm, columns=['Date', 'BW (KG)', "1RM Squat", "1RM/BW"])
squat_df["Date"]= pd.to_datetime(squat_df["Date"])
bench_df = pd.DataFrame(bench_1rm, columns=['Date', 'BW (KG)', "1RM Bench Press", "1RM/BW"])
bench_df["Date"]= pd.to_datetime(bench_df["Date"])
deadlift_df = pd.DataFrame(deadlift_1rm, columns=['Date', 'BW (KG)', "1RM Deadlift", "1RM/BW"])
deadlift_df["Date"]= pd.to_datetime(deadlift_df["Date"])

plt.plot(deadlift_df['Date'], deadlift_df['1RM Deadlift'], linestyle='--', marker='o', color='orangered', label='Deadlift')
plt.plot(squat_df['Date'], squat_df['1RM Squat'], linestyle='--', marker='o', color='blue', label='Squat')
plt.plot(bench_df['Date'], bench_df['1RM Bench Press'], linestyle='--', marker='o', color='purple', label='Bench Press')
plt.plot(ohp_df['Date'], ohp_df['1RM OHP'], linestyle='--', marker='o', color='black', label='OHP')
plt.legend(title='Lift')
plt.grid()
plt.title('Calculated 1 Rep Max weight progress in 5 months', fontsize=16)
plt.xlabel("Dates")
plt.ylabel("Weight in Pounds (LB)")
plt.show()
