
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









