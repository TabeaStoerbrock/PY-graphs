import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

print(pd.__version__)
print(matplotlib.__version__)

topics = [
    'IT-Security', 'IT-Sec Maßnahme 8', 'IT-Sec Maßnahme 10', 'IT-Sec Maßnahme 11',
    'IT-Sec Abschaltung Expressway - Vorgehen und Abstimmung letzte Cisco Anschlüsse',
    'TiM (Telefonie im Markt)', 'Überkipper: Pilotdurchführung WLAN-Telefonie',
    'Überkipper: Etablierung der technischen und organisatorischen Vorbereitungen für den Go Live',
    'Einführung Telefonie im Markt', 'Group Product / NEO', 'Überkipper: NEO - 2-3 Teams Rooms für Österreich',
    'Projekt Neo langfristige Strategie und Roadmap Communication & Meetings',
    'EHA - Konzeption Telefonie + Rollout', 'Blueprint Anbindung neuer Gesellschaften (kein RMD nur EPIC)',
    'Vorbereitung - REWE digital Harmonisierung der In- und Auslandsstandorte', 'Meetings',
    'Hardware Vertragsabschluss', 'Optimierung Tagesgeschäft hybride Meetings',
    'Konzeption DER Tour A-D und Umsetzung hybride Meetings Malaga',
    'Umsetzung Club 76 Präsentationstechnik', 'Lifecycle hybride Meetingräume mit 3 rollierenden Testräumen',
    'Meetings und Townhalls (Liveevents) in der REWE', 'Multi Channel Contact Center',
    'IT-ServiceDesk Hypercarephase', 'Polly Self Service für die Kundenhotline', 'Telefonie Verwaltung',
    'Osila Ablösung - Workshop und Entscheidung', 'Rollout Teams Phone Glockenbrot Frankfurt',
    'Überkipper: 22 Sammelanschlüsse in Regionen', 'Rufbereitschaft 50 weitere Umstellungen',
    'Agent One 10 Hotlines Timeline - Bauabteilung / Logistik', 'IVR Menü und Analyse Vermittlungsarbeitsplatz',
    'Teams Premium Entscheidung und Zielgruppen', 'Smarter Work im Markt', 'Überkipper: Verlängerung APK Workaround',
    'Aktualisierung APK Workaround', 'Sonstiges (ohne Feature Aufnahme)', 'Spitzensupport',
    'Produktoptimierung CM', 'Betriebsoptimierung (SIP Ostertag, Kostenoptimierung Unify ohne SW A., Poly Lens)',
    'technische Schulden', 'Dokumentation (technische Dokumentation / Vertragsmanagement)',
    'Konsolidierung Portfolio / Rollouts', 'Standortneueröffnungen Telefonie (kein RMD)',
    'Sonstiges (produktfremd)'
]

valuesApr = [
1, 0, 0, 0, 1, 4, 2, 2, 0, 5, 2, 2, 1, 0, 0, 6, 1, 3, 1, 1, 0, 0, 3, 2, 1, 8, 2, 0, 1, 2, 1, 1, 1, 0, 0, 0, 4, 1, 1, 2, 0, 0, 1, 1, 0
]

valuesMai = [
2, 0, 1, 0, 1, 3, 2, 1, 0, 3, 1, 1, 1, 0, 0, 7, 1, 2, 2, 1, 0, 1, 1, 1, 0, 9, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 4, 2, 1, 1, 0, 0, 1, 1, 0
]

valuesJun = [
2, 0, 0, 1, 1, 4, 2, 2, 0, 4, 0, 2, 2, 0, 0, 3, 0, 2, 1, 0, 0, 0, 0, 0, 0, 11, 3, 2, 2, 1, 2, 1, 0, 1, 1, 0, 6, 1, 2, 3, 0, 0, 1, 1, 0
]
data = {
    'Initiatives': topics,
    'Apr': valuesApr,
    'Mai': valuesMai,
    'Jun': valuesJun,
}

print(data)
print(len(topics) 
len(valuesApr)
len(valuesMai)
len(valuesJun))

df = pd.DataFrame(data)
df['Total_Weight'] = df[['Apr', 'Mai', 'Jun']].sum(axis=1)
df_sorted = df.sort_values(by='Total_Weight', ascending=False)
df_sorted.plot.bar(x='Initiatives', y='Total_Weight', figsize=(12, 6), rot=90, legend=False)
plt.figure(figsize=(10, 8))
sns.barplot(data=df_sorted, x='Total_Weight', y='Topic', palette='Blues_r')
plt.xlabel('Total Weight')
plt.ylabel('Topic')
plt.title('Weight of Topics in Planning')
plt.show()