from selenium import webdriver
import chromedriver_autoinstaller
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import time
import statsmodels.api as sm
from statsmodels.formula.api import ols

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1&Season=2023-24")
time.sleep(5)

headerElements = driver.find_elements("xpath","//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr")
headers = []
for header in headerElements:
    headers.append(header.text)
newHeaders = headers[0].strip().split()

button1 = driver.find_element("xpath",'//*[@id="onetrust-accept-btn-handler"]')
button1.click()
button2 = driver.find_element("xpath","//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div")
button2.click()
button3 = driver.find_element("xpath","//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select/option[1]")
button3.click()
playerStats = driver.find_elements("xpath","//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody")

tempRows = []
for row in playerStats:
    tempRows.append(row.text)
playerStats2 = tempRows[0].split("\n")

formatted_data = []
for player in playerStats2:
    parts = player.split()
    if parts[3] == "Jr.":
        name = " ".join(parts[1:3])
        surname = " ".join(parts[3:4])
        formatted_data.append([f"{name} {surname}"] + parts[4:])
    elif parts[3] == "III":
        name = " ".join(parts[1:3])
        surname = " ".join(parts[3:4])
        formatted_data.append([f"{name} {surname}"] + parts[4:])
    elif parts[3] == "IV":
        name = " ".join(parts[1:3])
        surname = " ".join(parts[3:4])
        formatted_data.append([f"{name} {surname}"] + parts[4:])
    elif parts[3] == "II":
        name = " ".join(parts[1:3])
        surname = " ".join(parts[3:4])
        formatted_data.append([f"{name} {surname}"] + parts[4:])
    elif parts[3] == "Sr.":
        name = " ".join(parts[1:3])
        surname = " ".join(parts[3:4])
        formatted_data.append([f"{name} {surname}"] + parts[4:])
    elif parts[3] == "Cardoso" and parts[4] == "Pereira":
        name = " ".join(parts[1:4])
        surname = " ".join(parts[4:5])
        formatted_data.append([f"{name} {surname}"] + parts[5:])
    else:
        name = " ".join(parts[1:2])
        surname = " ".join(parts[2:3])
        formatted_data.append([f"{name} {surname}"] + parts[3:])

for row in formatted_data:
    for i in range(2,len(row)):
        if "." in row[i]:
            row[i] = float(row[i])
        else:
            row[i] = int(row[i])
    
df = pd.DataFrame(formatted_data,columns=newHeaders)

sns.histplot(data=df, x="FG%", kde=True, bins=10)
plt.title("Başarılı Şut Yüzdesi Dağılımı")
plt.xlabel("Başarılı Şut Yüzdesi")
plt.ylabel("Sıklık")
plt.show()

df_mean = df.groupby("AGE")["FG%"].mean().reset_index()
sns.lineplot(data = df_mean, x = "AGE", y = "FG%")
plt.title("Yaşa Göre Ortalama Başarılı Şut Yüzdesi")
plt.xlabel("Yaş")
plt.ylabel("Başarılı Şut Yüzdesi")
plt.show()

numeric_data = df.select_dtypes(include="number")
group_data = numeric_data[["AGE","FG%","MIN"]]
sns.heatmap(group_data.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Değişkenler Arasındaki Korelasyon Isı Haritası")
plt.show()

sns.boxplot(data = df, x = "AGE", y = "FG%")
plt.title("Yaş Gruplarına Göre Başarılı Şut Yüzdesi")
plt.xlabel("Yaş Grupları")
plt.ylabel("Başarılı Şut Yüzdesi")
plt.show()

sns.scatterplot(x=df['MIN'], y=df['FG%'],hue = df["AGE"])
plt.title("MIN ve FG% Arasındaki İlişki")
plt.xlabel("MIN")
plt.ylabel("FG%")
plt.show()

print(df["AGE"].describe().to_frame().T)
print("------------------------------------------------------------")
print(df["MIN"].describe().to_frame().T)
print("------------------------------------------------------------")

print("HİPOTEZ TESTLERİ")
corr_pts_age = df["AGE"].corr(df["FG%"])
corr_pts_min = df["MIN"].corr(df["FG%"])
print(f"Başarılı Şut Yüzdesi İle Yaş Korelasyon Katsayısı : {corr_pts_age}")
print(f"Başarılı Şut Yüzdesi İle Oynadığı Dakika Korelasyon Katsayısı : {corr_pts_min}")
print("------------------------------------------------------------")
df["yas_grubu"] = pd.cut(df["AGE"], bins=[19, 22, 30, 39], labels=["Genç (19-22)", "Orta Yaş (23-30)", "Tecrübeli (31-39)"])
df["oynama_suresi_grubu"] = pd.cut(df["MIN"], bins=[0, 191, 1885, 2988], labels=["Düşük Süre (0-191 dk)", "Orta Süre (192-1885 dk)", "Yüksek Süre (1886-2988 dk)"])
model = ols('Q("FG%") ~ C(yas_grubu) + C(oynama_suresi_grubu) + C(yas_grubu):C(oynama_suresi_grubu)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
print("------------------------------------------------------------")
for index, row in anova_table.iterrows():
    p_value = row["PR(>F)"]
    if pd.notna(p_value):
        if p_value < 0.05:
            print(f"{index} değişkeni anlamlı bir etkiye sahiptir. (p-değeri: {p_value:.4f})")
        else:
            print(f"{index} değişkeni anlamlı bir etkiye sahip değildir. (p-değeri: {p_value:.4f})")
driver.quit()
