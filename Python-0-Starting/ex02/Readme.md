### **README - ex02**

#### **Description**
Ce programme en Python utilise la fonction `all_thing_is_obj` pour identifier et afficher le type d'un objet passé en argument. La fonction retourne toujours `42`.

#### **Fichiers**
- **find_ft_type.py** : Contient la fonction `all_thing_is_obj`.
- **tester.py** : Teste la fonction avec différents types d'objets.

#### **Fonctionnalités**
- La fonction `all_thing_is_obj` affiche un message spécifique en fonction du type de l'objet :
  - **Liste**, **Tuple**, **Set**, **Dictionnaire** : Affiche le type de l'objet.
  - **Chaîne de caractères (str)** : Affiche un message personnalisé.
  - **Entier (int)** : Affiche "Type not found".
- La fonction retourne toujours `42`.

#### **Exécution**
Pour exécuter le programme :
```bash
python3 tester.py
```
#### **Exemple de sortie**
```bash
List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
```