Drupal prototype
================

problématique agile


La problème reviens continuellement, comment est-ce qu'on peut développer
de front et rapidement des fonctinnalité en front end et backend. 

Dans un cycle de deux semaines comment on fait pour gérer les interdépendance.

## fail fast
Entre un wire frame, un psd et son implémentation il y as une grande différence
on as besoin de voir rapidement si le concept marche, comment ça réagit
en responsive etc.

La programmation c'est la composante la plus lourde de l'application 

Nurun ont développé une technique ou ils maintiennent un site statique
en express tout au long du projet et les backend copie leur code 

on viole le principe du dry et on fait du travail en double...


Pour faire un prtotype initial c'est simple, on override le page.tpl.php et le 
html.tpl.php

Ensuiste on ajouter un template dans le folder page et on peut utiliser
les partials autant dans la page que dans le page.tpl.php

Et tout ce code vie à l'intérieur de drupal, on peut le rendre dynamique morceau
par morceau 



static prototyping
http://www.phase2technology.com/blog/static-prototyping-and-keeping-drupal-simple-kds/#Static

autre problématique agile

Un prototype vaut mille meetings

interface first

https://gettingreal.37signals.com/ch09_Interface_First.php


features toggle
