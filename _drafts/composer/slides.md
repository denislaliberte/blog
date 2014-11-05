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
### Wordpress

WPackagist


 
Voici quelques 
* [Powerful component based mailing library for PHP – Swift Mailer](http://swiftmailer.org/)
* [Pimple - A simple PHP Dependency Injection Container](http://pimple.sensiolabs.org/)
* [sebastianbergmann/phpunit](https://github.com/sebastianbergmann/phpunit)
* [phpspec/phpspec](https://github.com/phpspec/phpspec)
* [fabpot/Sami](https://github.com/fabpot/Sami)
* [briannesbitt/Carbon](https://github.com/briannesbitt/Carbon)
* [igorw/compose](https://github.com/igorw/compose)
* [polyfractal/athletic](https://github.com/polyfractal/athletic)
* [nikic/iter](https://github.com/nikic/iter)
* [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)


 
 

 
#Installation

 
## Installation

```console
$ curl -sS https://getcomposer.org/installer | php
```

 
##Installation

composer.json

 
```console
$ php composer.phar init
```

 
## Installation
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

 
##Installation

packagist.org

![](packagist.png)


 
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
