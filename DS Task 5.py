import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Accident_ID': range(1, 16),
    'Date': pd.date_range(start='2024-06-01', periods=15, freq='D'),
    'Time': ['08:00', '12:00', '18:00', '22:00', '14:00',
             '09:30', '16:00', '11:00', '07:30', '20:00',
             '13:00', '17:30', '10:00', '19:00', '15:30'],
    'Weather_Condition': ['Clear', 'Rain', 'Fog', 'Clear', 'Snow',
                          'Rain', 'Clear', 'Fog', 'Clear', 'Snow',
                          'Rain', 'Clear', 'Fog', 'Clear', 'Snow'],
    'Road_Condition': ['Dry', 'Wet', 'Wet', 'Dry', 'Icy',
                       'Wet', 'Dry', 'Wet', 'Dry', 'Icy',
                       'Wet', 'Dry', 'Wet', 'Dry', 'Icy'],
    'Latitude': [12.97, 12.96, 12.95, 12.94, 12.97,
                 12.98, 12.99, 12.95, 12.96, 12.97,
                 12.93, 12.92, 12.91, 12.90, 12.99],
    'Longitude': [77.59, 77.60, 77.61, 77.62, 77.59,
                  77.58, 77.57, 77.61, 77.60, 77.59,
                  77.63, 77.64, 77.65, 77.66, 77.57],
}
df = pd.DataFrame(data)
df['DateTime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'])
df['Hour'] = df['DateTime'].dt.hour
print("Dataset:\n", df)

plt.figure(figsize=(8,5))
sns.countplot(x='Weather_Condition', data=df)
plt.title("Accidents by Weather Condition")
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='Road_Condition', data=df)
plt.title("Accidents by Road Condition")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['Hour'], bins=6, kde=False)
plt.title("Accidents by Time of Day")
plt.xlabel("Hour of the Day")
plt.ylabel("Accident Count")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df['Longitude'], df['Latitude'], color='red', alpha=0.7)
plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()