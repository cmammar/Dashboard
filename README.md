##DASHBOARD

   Projet d'EPITECH by Cyril et Clément

## Table of contents

   1-Présentation du projet

   2-Architecture Front End

   3-Widgets

## 1-Présentation du Projet

​	Le but du projet était de se familliariser avec la récupération et l'utilisation d'APIs, pour ensuite en les rassemblant créant comme un tableau de bord avec toutes les widgets que l'utilisateur décide d'utiliser.



## 2-Architecture du Front End

​	Le but du projet était de se familliariser avec la récupération et l'utilisation d'APIs, pour ensuite en les rassemblant créant comme un tableau de bord avec toutes les widgets que l'utilisateur décide d'utiliser.



```
.
 └── Vue
   └── dashboard
     └── src
       └── assests --> images
       └── components
                │	└── routes --> les différentes pages
        │   └── widgets --> les widgets
        └── router
                └── index.js --> les redirections
```



## 3-Widgets

+ Le dashboard dispose de 6 widgets différents. Les widgets se rafraichissent automatiquement.
+ Et il est possible pour l'utilisateur de les ajouter et les supprimer à tout moment.
+ L'utilisateur peut changer son nom et son mot de passe.
+ Les administrateurs ont accès à toute la liste des utilisateurs et peuvent les supprimer à tous moments.



    ├── 1- Actors Match
    ├── 2- Best Movie
    ├── 3- Time Widget
    ├── 4- Weather Wiget
    └── 5- Weather

1 Actor Match:

L'utilisateur rentre deux acteurs de cinéma différent, et le widget va trouver si les deux acteurs ont tournés dans un fillm similaire et si oui il va énuméré le nombre du ou des films concernés.



2 Best Movie:

Le Widget Best Movie va donné la liste des films les mieux notés en fonction du pays que l'utilisateur a au préalable rentré.



3 Time Widget:

L'utilisateur rentre une ville de son choix et l'Api va communiqué l'heure qu'il est dans cette ville



4 Weather Widget 1:

Weather Widget 1 donne la météo actuelle de la ville donné par l'utilisateur ainsi que la température maximale et minimale de la journée



5 Weather Widget 2:

Weather Widget 2 donne des information sur la ville rentrée concernant les faits métérologiques de la journée tel que l'heure à laquelle le soleil se couche et se lève ainsi que la probabilité qu'il pleuve dans cette ville aujourd'hui.

6 API :

Documentation : https://documenter.getpostman.com/view/1537991/SW7XZ9Mm
