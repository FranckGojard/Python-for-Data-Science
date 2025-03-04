## **README - ex03**

### **Description**
Ce programme en Python utilise la fonction `NULL_not_found` pour identifier et afficher des objets considérés comme "nuls" ou "faux" en Python. La fonction retourne `0` si un objet "nul" est trouvé, sinon `1`.

### **Fichiers**
- **NULL_not_found.py** : Contient la fonction `NULL_not_found`.
- **tester.py** : Teste la fonction avec différents objets.

### **Fonctionnalités**
La fonction `NULL_not_found` vérifie si l'objet est considéré comme "nul" ou "faux" :
- `None` : Affiche "Nothing".
- `NaN` (float) : Affiche "Cheese".
- `0` (int) : Affiche "Zero".
- Chaîne vide (`''`) : Affiche "Empty".
- `False` : Affiche "Fake".

Si l'objet ne correspond à aucun des cas ci-dessus, la fonction affiche "Type not Found" et retourne `1`. Sinon, elle retourne `0`.

### **Exécution**
Pour exécuter le programme :
```bash
python3 tester.py
```

### **Exemple de sortie**
```bash
Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
```