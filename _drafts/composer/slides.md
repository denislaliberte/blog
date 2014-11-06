# Composer

Il y as une semaine j'ai fait une petite présentation d'introduction à 
composer. On peux voir les slides en suivant ce [lien]() <!--todo lien -->

Dans cette introduction je couvre l'installation de composer, la création 
d'un manifeste et l'utilisation de l'autoload.

Composer est le gestionnaire de dépendances de php, il est inspiré de npm dans
la communauté javascript et bundler pour celle ruby.

<!-- todo ajouter les liens ? -->

Composer as l'air de faire l'unanimité dans la communauté php, il n'as pas 
vraiment de compétiteur et il est recommandé ou peut être utilisé pour installer
la plus part des framwork, ,symfony 2  zend 2 ,laravel 4 ,yii 2 ,Aura ,CodeIgniter 
,CakePHP ,slim ,Sculpin ,Typo3 ,Magento et Joomla.

C'est ausi le gestionnaire de dépendance par défaut pour drupal 8 et il est aussi 
possible de l'utiliser avec wordpress 4 et drupal 7.

Il y as différentes façon d'utiliser composer avec drupal 7, moi j'installe composer 
dans un module custom et je require l'autoload dans les modules ou j'en ai de besoin.
 
```php
module_load_include('php','tp1_project','vendor/autoload');
```
<!-- todo -->
### Wordpress

WPackagist


 

## Installation
Le processus d'installation de l'outil en ligne de commande est assez simple, il
suffit d'exécuter la commande suivante, dans la plus part des cas composer vas 
s'implement s'installer ou vous informer de configuration système à modifier.

```console
$ curl -sS https://getcomposer.org/installer | php
```


Ensuite ça prend un manifeste composer.json dans le quels est définie les 
métadonnées du projets et les dépendances. On peut utiliser la commande 
suivante pour définir ces méta donnés de façon intéractives.
 
```console
$ php composer.phar init
```

Ce qui donne un fichier comme l'exemple suivant.
 
composer.json
```json
{
    "name": "denislaliberte/mypackage",
    "description": "Description of my package",
    "license": "MIT",
    "minimum-stability": "dev",
    "require": {}
}
```

Ensuite il faut trouver quelques librairies à installer, on peut trouver ces 
dépendances sur le registre officiel de composer [packagist](http://packagist.org)
ou encore sur ce repos maintenu par la communauté 
[ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)

Ou pour les besoin du test on peut simplement en choisir dans cette listes qui 
regroupe quelques outils que j'aime beaucoup.
* [ Swift Mailer -  le mailer de la communauté symfony ](http://swiftmailer.org/)
* [Pimple - Le contenur d'injection de dépenance le plus simple qui existe](http://pimple.sensiolabs.org/)
* [phpunit - Outils de test classique qui as fait ses preuves ](https://github.com/sebastianbergmann/phpunit)
* [phpspec - Outils de test par spécification inspiré par RSpec de la communauté ruby ](https://github.com/phpspec/phpspec)
* [Sami - Générateur de documentation ](https://github.com/fabpot/Sami)
* [Carbon - Un wrapper à l'api de date de php](https://github.com/briannesbitt/Carbon)
* [compose - Composition de fonction ](https://github.com/igorw/compose)
* [athletic - outil de benchmark de fonciton ](https://github.com/polyfractal/athletic)
* [iter - Librairies de fonction lazy sur les itérateurs ](https://github.com/nikic/iter)

 
##Installation
require

 

```json
"require": {
    "vendor/package": "1.*"
}
```

 
## Installation

semver.org

 

MAJOR.MINOR.PATCH

 

MAJOR version != backwards-compatible

```json
    "vendor/package": "1.2.*"
```

 
## Installation

composer.lock

```console
$ composer intall
# vs 
$ composer update
```

 
 

 
#Autoload

 
## Autoload
Namespace

 

```console
Fatal error: Cannot redeclare test() (previously declared...
```

 
## Autoload
Namespace

 

```php
//Avant php 5.3
my_package_function_test();
```
 
```php
//Après php 5.3
MyPackage\function\test();
```

 
## Autoload
Namespace

```php
use MyPackage\function as f;

f\test();
```

 
## Autoload
Namespace

```php
use MyPackage\function\MyClass;

$class = new MyClass()
```

 
## Autoload

```php
//sans autoload
require 'vendor/MyPackage/function/MyClass.php';
use MyPackage\function\MyClass;
```

 

```php
//avec autoload
require 'vendor/autoload.php';

use MyPackage\function\MyClass;

```

 
## Autoload

www.php-fig.org

 

psr-4

```regexp
\<NamespaceName>(\<SubNamespaceNames>)*\<ClassName>
```

 
#Composer
