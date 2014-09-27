homebrew
========


## ressources ##

1. [homebrew Troubleshooting](https://github.com/Homebrew/homebrew/wiki/troubleshooting)
2. [Homebrew common issues](https://github.com/Homebrew/homebrew/wiki/Common-Issues)
3. [stackoverflow "config" scripts exist outside your system or Homebrew directories.](http://stackoverflow.com/questions/15225312/brew-doctor-gives-out-warnings)
4. [josegonzalez / homebrew-php : php54 fails to install on GD build test failed ]
(https://github.com/josegonzalez/homebrew-php/issues/313)
5. [brew install php53 error](https://github.com/josegonzalez/homebrew-php/issues/141)
6. [josegonzalez / homebrew-php](https://github.com/josegonzalez/homebrew-php#common-issues)
7. [Common upgrade issues](https://github.com/josegonzalez/homebrew-php#common-upgrade-issues)
8. [Xcode, GCC, and Homebrew](Xcode, GCC, and Homebrew)
9. [github kennethreitz / osx-gcc-installer ](https://github.com/kennethreitz/osx-gcc-installer/)

## bug ##
- installation de php55 problématique

  $ brew upgrade php55

  * 2 message d'erreur 
    1. message d'erreur Backing up all known pear.conf and .pearrc files
    2. message d'erreur configure: error: GD build test failed. Please check the config.log for details.
       ressources 4
        $ brew rm freetype jpeg libpng gd
        $ brew install freetype jpeg libpng gd
        la solution règle le message d'erreur #2 mais génère un nouveau message d'erreur le #3
    3. configure: error: Don't know how to define struct flock on this system, set --enable-opcache=no
       ressources #5 propose "$ brew cleanup" aucun effet
    4. ressource #4 "$ brew rm zlib ; brew install php54" aucun effet
    5. tentative de régler l'autre message lié au pear.com "$ rm ~/.pearrc" 
      aucun effet même sur le message d'erreur de pearrc
    6. retour à la case départ ressources #6 et #7
       l'installation des command line tools semble être différente sur maverik
       on dirais qu'il n'étais pas à jours
       Message d'erreur l'orsque j'essaie d'installer les command lines tool,
       l'installeur me dit qu'ils ne sont pas disponible pour ma version d'osx 10.9 et 
       aucune version ne semble être disponible pour mon os
        
       installation de gcc directement ressources #8 et #9
       il n'y as pas d'installer pour la version 10.9
       
       on dirais que la gestion des command lines tools est différente dans 10.9
       gcc est disponible et brew doctor n'as pas de commentaire sur les command 
       lines tools
