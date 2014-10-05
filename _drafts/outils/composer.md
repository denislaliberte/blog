# composer 

![composer logo](/images/composer/composer.png)

## history 
Composer c'est le gestionnaire de dépendance de la communauté php. Le projet 
assez jeune (2012) mais son usage et assez répendu dans la 
communauté php. Il est utilisé par la plus part des communautés, symfony, zend,
joomla, phalcon, laravel, silex, yii, drupal8, aura php

Et il est aussi possible de l'utiliser dans drupal 7 et wordpress (wpackagist)

Composer est inspiré de Bundler de la communauté ruby et de npm pour le javascript.
L'idée est de créer un manifeste qui décrit les librairies utilisé par le projet
et de laisser composer se charger de les télécharger et les garder à jours.

## installation
Composer s'installe en une ligne de commande :

` curl -sS https://getcomposer.org/installer | php `

[ Voir la documentation officielle ](https://getcomposer.org/doc/00-intro.md)

## composer.json

Une fois installé on peut générer de façon intéractive un manifeste composer.

` $ composer init`

Un manifeste composer au minimum doit contenir les dépendances à installer

``` json
{
  "require": {
    "igorw/get-in": "~1.0",
    "anahkiasen/underscore-php": "dev-master",
    "nesbot/Carbon": "~1.9",
    "swiftmailer/swiftmailer": "@stable"
  }
}

```

## autoload 
On peut aussi déclarer les information pour l'autoloader.

``` json
    "autoload": {"psr-0": {"": "src"}},
```

En effet composer viens avec un autoloader pour ses dépendances 

On n'as plus qu'à charger l'autoloader pour 
i

## psr-0

Le PHP Framework Interop Group est un groupe qui vise à publier des standards 
pour faciliter la collaboration entre les communautés des différent framework php
le premier standard qu'ils ont publié est le standard d'autoload de classe 
le [psr-0](http://www.php-fig.org/psr/psr-0/).

Alors plus besoin de faire un include de chaque fichier qu'on veux utiliser
on as juste à utiliser le namspace

donc pour utiliser la classe dans le fichier /tp1/test/class.php
on as juste à ajouter la ligne ` use tp1\test\class; `


## namespace
Pourquoi utiliser les namespace, en gros l'utilité du namespace c'est
d'éviter les colission de nom. Déclarer 


http://www.phptherightway.com/#namespaces
http://php.net/manual/en/language.namespaces.php


## packagist


## librairies utiles
j'ai certain package dont je ne peut plus me passer

PHPSpec(PHPUnit), carbon, athletic, get_in, compose, 

Composer permet d'installer rapidement et de faire facilement les updates 
de librairies

https://github.com/ziadoz/awesome-php

## prs-0


## à éviter
commiter le folder de libairies /vendors , ça peut causer des problèmes de git

## drupal 7
Drupal avais déjà un système pour gérer ses packages, mais 

plusieurs approches


## autoload


https://delicious.com/denislaliberte/composer
