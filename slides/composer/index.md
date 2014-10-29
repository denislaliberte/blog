class: center, middle
# Composer

---
### composer

Inspiration

--

bundler.rb 

--

npm.js

---
### composer

communauté

--

symfony 2 
--
zend 2 
--
laravel 4 
--
yii 2 
--
Aura

--

drupal 8 
--
wordpress 4

---
## Composer

* [Powerful component based mailing library for PHP – Swift Mailer](http://swiftmailer.org/)

--

* [Pimple - A simple PHP Dependency Injection Container](http://pimple.sensiolabs.org/)

--

* [sebastianbergmann/phpunit](https://github.com/sebastianbergmann/phpunit)

---

* [phpspec/phpspec](https://github.com/phpspec/phpspec)

--

* [fabpot/Sami](https://github.com/fabpot/Sami)

--

* [briannesbitt/Carbon](https://github.com/briannesbitt/Carbon)

--

* [igorw/compose](https://github.com/igorw/compose)

--

* [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)


---
name: agenda
### Composer

Installation

Autoload

cms

---
#Installation

---
## Installation

```console
$ curl -sS https://getcomposer.org/installer | php
```

---
##Installation

composer.json

--
```console
$ php composer.phar init
```

---
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

---
##Installation

packagist.org

![](packagist.png)


---
##Installation
require

--

```json
"require": {
    "vendor/package": "1.*"
}
```

---
## Installation

semver.org

--

MAJOR.MINOR.PATCH

--

MAJOR version != backwards-compatible

```json
    "vendor/package": "1.2.*"
```

---
## Installation

composer.lock

```console
$ composer intall
# vs 
$ composer update
```

---
template: agenda

---
#Autoload

---
## Autoload
Namespace

--

```console
Fatal error: Cannot redeclare test() (previously declared...
```

---
## Autoload
Namespace

--

```php
//Avant php 5.3
my_package_function_test();
```
--
```php
//Après php 5.3
MyPackage\function\test();
```

---
## Autoload
Namespace

```php
use MyPackage\function as f;

f\test();
```

---
## Autoload
Namespace

```php
use MyPackage\function\MyClass;

$class = new MyClass()
```

---
## Autoload

```php
//sans autoload
require 'vendor/MyPackage/function/MyClass.php';
use MyPackage\function\MyClass;
```

--

```php
//avec autoload
require 'vendor/autoload.php';

use MyPackage\function\MyClass;

```

---
## Autoload

www.php-fig.org

--

psr-4

```regexp
\<NamespaceName>(\<SubNamespaceNames>)*\<ClassName>
```

---
template: agenda

---
#CMS

---
## CMS - Drupal

Composer dans un module custom

--
drupal_get_files('')
autoload


---
## CMS - Wordpress

WPackagist


