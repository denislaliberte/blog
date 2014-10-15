
Quand j'ai changé d'entreprise au début de l'année mon objectif principal étais
de trouver un context ou je pourrais mettre en place des pratiques de tdd et 
d'intégration continue avec drupal 7. Pour pouvoir faire ça j'avais besoin de deux
choses une technique de déploiement automatisé qui me permet de construire mon 
projet en une ligne de commande et une suite de tests qui roule en quelques secondes.

Écrire des tests automatisé pour drupal 7 comporte certain défits. Drupal intègre 
le framework de tests simpletests mais à chaque test case il fait une installation
complète de drupal... une suite de tests complète pour un site prend donc plusieurs 
minutes à rouler.

Même lorsqu'on cache l'installation de la db le feedback arrvie trop tard pour 
pouvoir faire du tdd efficace. J'ai finis par utiliser phpspec et par  mocker 
tout mes appels à l'api de drupal et mes tests roules vraiment rapidement.
