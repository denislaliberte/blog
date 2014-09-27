Drupal camp Montréal - Docker, Twig, d2d migration
=========================

Voici un résumé des conférences que j'ai vu au drupal camp montréal 2014 en trois 
billets.

<!-- todo
1. Drupal camp montréal - Docker, twig, d2d migration
2. [todo] Drupal camp Montréal - Features, Entity metatdata wrapper, unit tests
3. [todo] Drupal camp Montréal - DCycle, Interface d'administration, front end, sécurité
-->

tl;dr
-----
Pour un résumé de mon résumé en "bullet point'
- Un outil intéressant pour faire des diff de html entre deux sites
- Docker est plus rapide et simple que vagrant
- J'ai hâte que drupal 8 sorte pour utiliser twig
- Des exemples de drupal migrate d6-d7

Docker 
------
La présentation que j'ai troué la plus intéressante cette année est celle de Alex Dergachev de evolving web
qui nous as présenté rapidement comment utiliser Doker et quelques aventages
vs vagrant.

Mais ce qui étais vraiment intéressant c'est la présentation de deux projet

Une migration du site de mcgill d6-d7 et d'un outils qu'ils ont développé pour 
faire des diffs entre le html original et celui de la migration.

https://github.com/dergachev/sitediff

Et l'autre c'est une migration d'un site en markdown vers drupal ou ils ont 
étendu le framework migrate.


Pour ses tests unitaire il utilise phpunit avec des mock de drupals.

phpunit tests per module (works with D7 "OK")
bootstrap drupal => can't mock global functions, need process isolation
instead, use fixtures and mocks in your tests w/o drupal process isolation, can't mock global functions

http://dergachev.github.io/presentations/nyccamp-2014-docker/build/out.html

Twig et drupal 8
----------------
J'ai beaucoup aimé travaillé avec twig sur un projet symfony, et je déteste 
vraiment comment fonctionne l'outil de templating de drupal 7 [lien]. J'étais 
donc curieux de voir comment twig avais été intégré à drupal 8.

La bonne nouvelle c'est qu'il n'y as pas grande surprise, twig as été intégré 
à drupal tel quel. 

On retrouve les overrides de templates et 

Il y as simplement quelques fonction qui ont été intégré.

On peut appeler la fonction t `{{ variable | t}}` et ils ont ajouté une fonciton
pour cacher des éléments dans une node {{ content | without links}} et le block 
`{{trans}} {{endtrans}}` pour les traduction.

La conférencière nous as conseiller de voir la présentation de Fabien Potentier
le créateur de twig au drupal con [lien].

Drupal to drupal data migration
-------------------------------

Migrate est un des outils de drupal que je trouve vraiment bien fait. C'est 
un framework orienté objet qui permet de scripté l'importation de donnés. 
Et son architecture permet de configurer rapidement les sources externes, la 
destination dans drupal et toutes modifications qu'on as besoin de faire entre 
temps. Et son outils en ligne de commandes permet de faire les imports tester et 
de faire des rool back.

La présentation étais assez somaire pour quelqu'un qui as déjà utiliser le module
mais c'est devenu vraiment intéressant lorsqu'on as pus voir plusieurs exemples 
concrets, files term, location multgroup field collection, taxonomy term et 
ces exemples sont disponible sur ce lien : 
http://mvc.koumbit.org/presentations/2014-drupalcampmtl/migrate_stuff.tar.gz

http://mvc.koumbit.org/presentations/2014-drupalcampmtl/



