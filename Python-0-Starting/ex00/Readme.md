## **README - ex00**

### **Description**
Ce programme en Python illustre la manipulation de différentes structures de données : liste, tuple, ensemble et dictionnaire. Il met en évidence les modifications possibles sur ces structures et leur comportement en mémoire.

### **Fichiers**
- **Hello.py** : Contient le code principal du programme.

### **Explication du code**
1. **Déclaration de quatre structures de données différentes** :
   - Une **liste** (`ft_list`)
   - Un **tuple** (`ft_tuple`)
   - Un **ensemble** (`ft_set`)
   - Un **dictionnaire** (`ft_dict`)

2. **Modification des structures** :
   - La liste est modifiable, donc l'élément d'index 1 est remplacé.
   - Les tuples étant immuables, une nouvelle instance est créée avec une nouvelle valeur.
   - L'ensemble est recréé avec une nouvelle valeur.
   - La valeur associée à la clé "Hello" dans le dictionnaire est modifiée.

3. **Affichage du résultat après modification**.

### **Exécution**
Pour exécuter le programme, utilisez la commande suivante dans un terminal :
```bash
python3 Hello.py
```

### **Résultat attendu**
Après exécution, le programme affichera :
```python
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

