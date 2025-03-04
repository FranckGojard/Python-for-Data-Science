## **README - ex01**

### **Description**
Ce programme en Python utilise les modules `datetime` et `time` pour récupérer et afficher des informations temporelles.

### **Fichiers**
- **format_ft_time.py** : Contient le code principal du programme.

### **Explication du code**
1. **Importation des modules** :
   - `datetime` et `time` sont importés pour manipuler le temps et les dates.

2. **Récupération du temps actuel** :
   - `time()` est utilisé pour obtenir le nombre de secondes écoulées depuis le 1er janvier 1970 (l'epoch).
   - `datetime.now()` récupère la date et l'heure actuelles.

3. **Formatage de la date** :
   - `strftime('%b %d %Y')` formate la date sous la forme : `Mois Jour Année` (exemple : `Mar 04 2025`).

4. **Affichage des résultats** :
   - La première ligne du `print` affiche :
     - Le nombre de secondes écoulées depuis l'epoch sous forme décimale (`timeEpoch`).
     - La même valeur en notation scientifique (`f"{timeEpoch:.2e}"`), qui permet de mieux représenter de grands nombres sous un format compact.
   - La seconde ligne affiche la date actuelle au format abrégé avec le mois (trois lettres), le jour et l'année.

### **Exécution**
Pour exécuter le programme, utilisez la commande suivante dans un terminal :
```bash
python3 format_ft_time.py
```

### **Exemple de sortie**
```bash
Seconds since January 1, 1970: 1700000000.123456 or 1.70e+09 in scientific notation
Mar 04 2025
```

