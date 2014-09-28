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
Pour un résumé de mon résumé en "bullet point':

- Un outil intéressant pour faire des diff de html entre deux sites
- Docker est plus rapide et simple que vagrant
- J'ai hâte que drupal 8 sorte pour utiliser twig
- Des exemples de drupal migrate d6-d7

Test-Driven Drupal Using Docker
--------------------------------
La présentation que j'ai trouvé la plus intéressante cette année est celle de 
Alex Dergachev de Evolvingweb qui nous as présenté rapidement comment utiliser 
Doker et quelques aventages vs vagrant.

En gros docker est plus léger que vagrant et simple à utiliser puisqu'il est 
configuré en bash au lieu de chef ou puppet. Mais Docker ne roule que sur linux
donc si on développe sur OSX ou Windows il faut avoir une machine virtuelle 
linux pour rouler Docker.

Mais ce qui étais vraiment intéressant c'est la présentation de deux projets, une 
migration complexe drupal 6-7 pour l'université McGill et l'autre une migration 
markdown-drupal pour la documentation d'un projet opensource.

Une migration du site de mcgill d6-d7 et d'un outils qu'ils ont développé pour 
faire des diffs entre le html original et celui de la migration.

Pour la migration du site de McGill ils ont développé un outils qui permet 
de faire un diff entre deux pages html. Donc on peut comparer l'ancienne version
avec la nouvelle de façon automatisé.

[Repo Github de Sitediff](https://github.com/dergachev/sitediff)

Et l'autre c'est une migration d'un site en markdown vers drupal ou ils ont 
étendu le framework migrate.
Docker 
L'idée de migrer du contenu markdown dans drupal est un projet au quel je réfléchit
depuis longtemps. Pourvoir gérer les copydeck d'un site en clear text et les importer
automatiquement serais vraiment plus productif que d'intégrer manuellement le 
contenu sur chacune des instances du site.

Ils ont utilisé le framework migrate pour importer le contenu mais faute de temps
on n'as pas pu en savoir plus.

On as aussi appris qu'ils utilisent phpunit pour tester le code des modules avec
des mock pour les appels à l'api de drupal

[slides de la présentation](http://dergachev.github.io/presentations/nyccamp-2014-docker/build/out.html)

Twig et drupal 8
----------------
J'ai beaucoup aimé travaillé avec twig sur un projet symfony, et je doit avouer
que je déteste vraiment comment fonctionne l'outil de templating de drupal 7.
J'étais donc curieux de voir comment twig avais été intégré à drupal 8.

La bonne nouvelle c'est qu'il n'y as pas grande surprise, twig as été intégré 
à drupal tel quel. Il y as simplement quelques fonction qui ont été intégré.

On peut appeler la fonction t `{{ variable | t}}` et ils ont ajouté une fonction
pour cacher des éléments dans une node {{ content | without links}} et ils ont 
ajouté le block `{{trans}} text à traduire {{endtrans}}` pour les traductions.

La conférencière nous as conseiller de voir la présentation de Fabien Potentier
le créateur de twig au drupal con [Youtube | DrupalCon Prague 2013: TWIG](https://www.youtube.com/watch?v=18sxjsLTesE)

Drupal to drupal data migration
-------------------------------

Migrate est un des outils de drupal avec le quel j'aime vraiment travailler. C'est 
un framework orienté objet qui permet de scripté l'importation de donnés.
Et son architecture permet de configurer rapidement les sources externes, la 
destination dans drupal et toutes modifications qu'on as besoin de faire entre 
temps. Et son outils en ligne de commandes permet de faire les imports tester et 
de faire des rool back.

La présentation étais assez somaire pour quelqu'un qui as déjà utiliser le module
mais c'est devenu vraiment intéressant lorsqu'on as pus voir des exemples 
concrets, files term, location multgroup field collection, taxonomy term et 
ces exemples sont disponible sur ce lien : 
[migrate_stuff](http://mvc.koumbit.org/presentations/2014-drupalcampmtl/migrate_stuff.tar.gz)

[slides](http://mvc.koumbit.org/presentations/2014-drupalcampmtl/)



