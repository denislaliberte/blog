class: center, middle
# Composer

---
### Composer

Autoload

Installation

cms

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
## CMS - Drupal

Composer dans un module custom

--
drupal_get_files('')
autoload


---
## CMS - Wordpress

WPackagist



