import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV-Datei einlesen
# Stelle sicher, dass das Skript und die CSV-Datei im selben Ordner liegen
datei_name = 'trend_daten.csv'
df = pd.read_csv(datei_name)


print(df.head())  # Optional: Zeigt die ersten Zeilen des DataFrames an, um sicherzustellen, dass die Daten korrekt geladen wurden
print(df['Tag'])

# 2. Plot initialisieren
plt.figure(figsize=(10, 6))

# 3. Erste Trendlinie (Aufwärtstrend) plotten
plt.plot(
    df['Tag'], 
    df['Metrik_Alpha'], 
    marker='o', 
    markersize=4, 
    linestyle='--', 
    color="#1fb43a", 
    alpha=0.8, 
    label='Metrik Alpha (Aufwärtstrend)'
)

# 4. Zweite Trendlinie (Abwärtstrend) plotten
plt.plot(
    df['Tag'], 
    df['Metrik_Beta'], 
    marker='s', 
    markersize=4, 
    linestyle='-', 
    color='#d62728', 
    alpha=0.8, 
    label='Metrik Beta (Abwärtstrend)'
)

# 5. Diagramm formatieren und beschriften
plt.title('Entwicklung von Metrik Alpha und Beta über 100 Tage', fontsize=14, pad=15)
plt.xlabel('Tag', fontsize=12)
plt.ylabel('Wert', fontsize=12)

# Raster und Legende hinzufügen
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best', fontsize=10)

# Layout optimieren und anzeigen
plt.tight_layout()
plt.show()