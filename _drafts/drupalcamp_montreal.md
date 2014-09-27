Drupalcamp Montréal
===================

Voici un résumé des conférences que j'ai vu au drupal camp montréal 2014.

tl;dr
-----
Pour un résumé de mon résumé en 8 points.
1. Un outil intéressant pour faire des diff de html entre deux sites
2. Modéliser ses features par use case vs par type de configuration
3. J'ai hâte que drupal 8 sorte pour utiliser twig
6. Faire un prototype "front end" ça permet de développer plus rapidement
2. Des exemples de drupal migrate d6-d7
4. Entity meta data wrapper c'est un incontournable
7. L'interface administrateur dans un cms c'est important
8. Une approche originale aux tests drupal...


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

Gérer la configuration de son site avec Features
--------
Je ne peux pas me passe de features... mais je le déteste...

Features c'est indispensable pour exporter la configuration de drupal 7. Je sait
que certains arrivent à tout configurer dans le code sans utiliser features et 
j'ai étudié la possibilité mais pour l'instant la façon la plus productive pour
moi de travailler avec drupal 7 c'est features.

J'avais vraiment hâte d'avoir le point de vue de Pierre Buyle sur l'utilisation 
de features.

J'ai souvent la même discussion avec d'autres dev sur features... comment on
sépare les features, une seul features pour tout le site c'est définitivement 
ingérable, une features par use case ça peut être complexe et emporter des 
conflits et souvent on finis par exporter une features par type de configuration
- content_type, configuration_wysiwyg, configuration_metadata etc...

Pierre Buyle de phéromone nous as présenté une vision intéressante. Il modélise 
ses features par use case, map ses dépendances créé des features intermédiaire pour
les configurations qui sont utilisé par plusieur features et ajoute une 
features d'intégration qui dépend de tout les features du site.

Je n'ai pas pu trouver les slides de la présentation mais il as dit qu'un
billet de blogue expliquant sa technique étais en préparation.



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

<!-- todo 
Why Aren't You Using Entity Metadata Wrappers Yet?
----------------------
Au moment de sortir drupal 7 l'api des 'entity' n'étais pas complètes l'équipe as
donc choisit de faire un module contribué qui offre un wrapper aux entité.

C'est vraiment un incontournable lorsqu'on doit aller chercher les valeurs d'une
node programmatiquement, je ne peux vraiment pas m'en passer. 

On as eu droit à une introduction sommaire à l'api avec exmeple de getter et setter
je doit avouer que pour une séance indentifié comme avancé je m'attendais à en 
apprendre un peu plus sur les opportunités de l'api.

Des tests modernes pour Drupal
------------------------------

Étant donné le titre de présentation je m'attendais à apprendre quelques trucs
intéressant à intégrer à ma stratégie de tests pour drupal 7 [liens] mais le 
conférencier avais une philosophie de tests assez loin de la mienne.

Il utilise phpunit pour automatiser ses tests et il bootstrap drupal à chaque tests.

Étant donné que ses exemples ne testais que des opération mathématique simple (1+1)
on n'as pas su quel étais sa stratégie pour les données. 

L'autre point original c'est qu'il utilise selenium créer des tests d'interface
(ce qu'il appelle des tests d'intégration) 

et il appelle ses tests unitaire depuis les script généré par sélénium.

Finalement il utilise behat pour créer des "acceptance tests" mais au lieu de 
l'utiliser comme un outil de collaboration et de communication avec le client 
il as plutôt suggérer que ce soit un gestionnaire de projet membre de l'équipe
de production qui s'en charge...


Le conférencier as présenté une technique ou il bootstrap drupal dans 
avant de rouler ses tests unitaires 

http://fr.slideshare.net/hellosct1/des-testsmodernespourdrupal


Les sessions que j'ai manqué
----------------------------

### personnaliser l'interface administrateur de Drupal

J'ai vu plusieurs projets drupal ou on oubliais un utilisateur très important
le créateur de contenu. Si on adapte pas l'interface d'administration de drupal
on peut se retrouver avec CMS dont le créateur de contenu as peurs... alors que 
c'est l'objectif principal du système permettre à des gens sans background technique
d'éditer le contenu.

De plus en plus dans les cas de site vitrine on essaie de voir le créateur de 
contenu comme l'utilisateur principal du site. 


### Approche alternative au développement front-end Drupal.

Les gens de chez nurun avais fait une présentation il y as quelques semaines 
pour le site qu'ils ont développé pour l'aéroport de montréal et ils avaient 
présenté et ils nous avaient présenté leur approche pour le développement frontend
à ce moment.

L'idée est intéressante, l'équipe front end développe un prototype de site statique
en express.js et l'équipe backend utilise leur exemple pour l'intégrer au site en 
développement.

On as commencé à appliquer cette idée dans mon équipe et ça aide vraiment à 
avancer rapidement. La seul diférence c'est qu'on fait ce prototypage à même
drupal. Pour une nouvelle page on vas simplement déclarer un hook_menu et
un hook_theme et on vas 

Donc si on as des modifications à faire au layout di site ces modification se
représente 

Dans un context de développement itératif ou le client peut demander des changements
à chaque itération j'ai l'impression que de maintenir un site statique en plus 
site réel demande un dédoublement du travail et que ça rentre en conflit avec le
principe du dry.






### A code-driven development workflow for Drupal 8

La séance d'albert l'an passé m'avais beaucoup impressionné, depuis j'utilise sa 
technique d'update automatisé sur tout mes projets et c'est aussi une des raison 
qui m'as poussé à venir travailler chez tp1 (à ce moment là la seul façon dont
on pouvais déployer les sites dans mon entreprise étais par dump de db sql...
j'ai entendu dire que depuis quelques équipes expérimente avec cette technique aussi)


De ce que j'ai pus voir su son billet la présentation de cette année est un update
de celle de l'an passé avec drupal 8.

Donc features n'est plus requis puisque la configuraiton est automatiquement 
exporté dans des fichier de configuration yml (mercy symfony, bye bye features).

C'est étonnant mais il faut un peu contouner le système de configuration pour
pouvoir avoir la même configuration sur plusieurs instance (WTF drupal)... un 
uuid est assigné à l'installation et on présume que la database est cloné entre 
les instances...

Pour voir les exemples de code et les explicaiton complète voir le résumé sur le
blogue dcycle


http://dcycleproject.org/blog/68/approach-code-driven-development-drupal-8






### Exigences de sécurité Drupal

-->








