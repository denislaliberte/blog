class: center, middle
# Composer

---
name: agenda
### Composer

Introduction

Installation

Autoload

---
#Introduction

---
### composer

Inspiration

--

* bundler.rb 

--

* npm.js

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
CodeIgniter 
--
CakePHP 
--
slim 
--
Sculpin 
--
Typo3 
--
Magento 
--
Joomla 


--

drupal 8 
--
wordpress 4

---
## Composer

### Drupal 7

Composer dans un module custom

--
```php
module_load_include('php','tp1_project','vendor/autoload');
```


---
## Composer
### Wordpress

WPackagist


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

* [polyfractal/athletic](https://github.com/polyfractal/athletic)

--

* [nikic/iter](https://github.com/nikic/iter)

---

* [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)


---
template: agenda

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
#Composer
