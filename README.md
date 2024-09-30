# Projektantrag - Drohnen-Wärmebildanalyse

## 1. Ausgangslage

### 1.1. Ist-Situation

Das Rote Kreuz verwendet Drohnen, um vermisste Personen mithilfe von Wärmebildaufnahmen ausfindig zu machen. Dabei müssen die Piloten die Drohnen steuern und dabei ein aktives Auge auf die Übertragung werfen.

Die JKU hatte bereits ein Projekt, das mehrere Bilder mithilfe von Integralbildtechnologie und KI analysiert und Menschen darauf ausfindig macht.

### 1.2. Verbesserungspotenziale

Das Rote Kreuz braucht ein Framework um das KI-Model aktiv mit ihren Drohnen zu verknüpfen und mithilfe eines Web Interfaces die Auswertungen anzuzeigen. Dadurch wird die Personensuche effizienter und zuverlässiger, da die KI in der Lage ist, Personen aufzuspüren, die mit dem bloßen Auge nicht zu erkennen sind.

## 2. Zielsetzung

![image](assets/mindmap.jpg)

## 3. Chancen und Risiken

### 3.1 Chancen

* Das Projekt bietet die Möglichkeit, vermisste Personen schnell aufzuspüren. Mit dem Web Interface hat man eine Liste an Treffern und den dazugehörigen Koordinaten. Diese wird dann von den Helfern genutzt, um mit Suchhunden in dem jeweiligen Gebiet nach den verschwundenen Personen zu suchen.

### 3.2 Risiken

* Technisches Realisierungsrisiko - Es kann sein, dass wir es nicht hinbekommen, die Bildübertragung der Drohne an die KI effizient anzubinden und die Auswertungen zeitgerecht an unser Web Interface auszuliefern
* Verwertbarkeitsrisiko - Vielleicht ist unsere Implementierung nicht reif genug für eine hilfreiche Unterstützung beim RK
* Aufwandsrisiko - Unter Umständen können sich die Anforderungen im Laufe der Zeit ändern

## 4. Planung

1. MS - Recherche bzgl. der KI, Equipment und Einsatzplanung und Kontaktaufnahme mit der JKU (4.11.2024)
2. MS - Web Interface Mockups (26.11.2024)
3. MS - Organisation einer Drohne (19.12.2024)
4. MS - Bildübertragung von der Drohne zur KI (13.2.2025)
5. MS - Verarbeitung der Übertragung im Backend unserer WebApp (29.4.2025)
6. MS - Anzeigen der Daten im Interface + Gestaltung (17.6.2025)
7. MS - Optimierungen ()

## User Stories

### Als ein: Pilot
* Möchte ich dass: Die Bilder, die mit der Drohne aufgenommen werden, an die KI weitergeleitet werden
* Damit: Die KI eventuell vermisste Personen ausfindig machen kann

Akzeptanzkriterien:
1. Es besteht eine direkte Verbindung zwischen Drohne und KI
2. Die KI bekommt die Wärmebilder der Drohne
3. Der Pilot kann die Übertragung starten, stoppen und anhalten
4. Jeder Pilot kann eine eigene Session erstellen

### Als ein: Beobachter
* Möchte ich dass: Die ausgewerteten Bilder inklusive der dazugehörigen, wichtigen Metadaten auf einer Web page angezeigt werden
* Damit: Die Suche von vermissten Personen für Einsatzkräfte leichter und effektiver wird

Akzeptanzkriterien:
1. Es wird ein Integralbild zurückgegeben, auf dem (eine) Person(en) erkennbar ist/sind
2. Beobachter können zwischen Sessions wechseln
3. Die Bilder und Metadaten werden auf der Seite angezeigt
4. Die Liste von Koordinaten kann exportiert werden
5. Daten werden gespeichert
6. Daten können zur Löschung freigegeben werden

## Technologien

### Frontend:

- Typescript
- Angular
- Websockets
- CSS

### Backend:

- C#
- ASP.NET.Core
- Websockets

### KI-Anbindung

- C++

### Drone Video Capture

- Python