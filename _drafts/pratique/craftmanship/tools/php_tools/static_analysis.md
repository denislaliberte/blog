static analysis tool
===================

1. [PHP_CodeSniffer](http://pear.php.net/package/PHP_CodeSniffer)
2. [PHP Coding Standards Fixer](http://cs.sensiolabs.org/)
3. [fabpot/PHP-CS-Fixer](https://github.com/fabpot/PHP-CS-Fixer)
4. [ PHPLint](http://www.icosaedro.it/phplint/)
5. [sebastianbergmann/phpcpd](https://github.com/sebastianbergmann/phpcpd)
6. [PHPMD - PHP Mess Detector](http://phpmd.org/)

- [Track your dependencies with PHP_Depend](http://manuel-pichler.de/pages/pdepend.html)
- [phpCallGraph - A Call Graph Generator for PHP](http://phpcallgraph.sourceforge.net/)
- [Is there a static code analyzer [like Lint] for PHP files? ]
(http://stackoverflow.com/questions/378959/is-there-a-static-code-analyzer-like-lint-for-php-files)
- [Be a Better PHP Developer: Coding Standards](http://jason.pureconcepts.net/2012/11/php-coding-standards/)
- [Static analysis tools for PHP](https://chrsm.org/post/static-analysis-tools-for-php/#build)



## todo 
- php valide 
  * $ php -l file.php
  * voir les différence avec phplint [ressource 4]
  * semble être remplacé par php -l
- psr-2
  * php code sniffer
    - [ressource 1]
    - $ brew install php-code-sniffer
    - $ phpcs file.php
    - valider que les regles sont bien celle du psr-2
      trop de règle... utiliser l'argument poru que ce soit juste le psr2
      $  phpcs --standard=PSR2 file.php

  * cs-fixer
    - [ressource 2, 3]
    - $ brew install php-cs-fixer
    - semble fixer les règles du psr-2 mais laisse des erreurs de phpcs
    - règle quelques truc de phpcs mais assez limité
- copy paste
  * [ressource 5]
  * brew install phpcpd
  * ne semble pas être très efficace, ne trouve pas un exemple simple
- mess detector
  * [ressource 6]
  * brew install phpmd
  * phpmd src text cleancode
  * suite de règle, cleancode semble englober les autres
  * http://phpmd.org/rules/index.html
  * ne retourne rien sur une de mes classe, et brise sur du code de drupal
  * à débugger/réessayer
