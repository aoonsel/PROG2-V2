**Beschreibung Webapp"Lauf-Rechner"**

Im Rahmen des Moduls PROG2 hatten wir Studenten den Auftrag, eine Webapp zu erstellen, welche Daten speichern, 
verarbeiten und wiedergeben kann.

Meine Idee beruht auf einen Rechner für Trainingseinheiten im Bereich von Lauftrainings.

Über ein Webformular können Sportler (Nutzer) ihre Daten erfassen, welche in Folge in eine Datenbank gespeichert werden.
Die Daten werden in einem jason gespeichert, wobei das Datum als Key dient.

Anhand der eingegebenen Daten, welche der Nutzer für eine Laufeinheit erfasst hat, werden ihm Informationen wie Datum, 
Zeit und schlussendlich auch die Laufgeschwindigkeit zurückgegeben. Die Laufgeschwindigkeit wird von einer Funktion berechnet 
und benutzt dafür die Parameter Distanz und Zeit. Die Daten werden dem Nutzer in einem plotly-Diagramm dargestellt und 
sind direkt darunter auch zeitlich geordnet aufgelistet. 

**Anleitung:**

Nach dem Training:

Zeit und Distanz eingeben und Einheit berechnen lassen.

Vor dem Training:

Gewünschte Distanz und Zeit eingeben, anschl. Pace im Training laufen. 


**UML-Darstellung der Webapplikation:**
![UML Diagramm](/UMLDiagrammWorkflow.png)
