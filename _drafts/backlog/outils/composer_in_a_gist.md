# Composer in a gist

https://gist.github.com/denislaliberte/82e54bcce3d56767e1d3

http://jeffkreeftmeijer.com/2011/microgems-five-minute-rubygems/

```bash 
$ gist --help
$ gist --login
Obtaining OAuth2 access_token from github.
GitHub username: denislaliberte
GitHub password:
$ gist -o composerinagist.php
$ hub clone https://gist.github.com/82e54bcce3d56767e1d3 composerinagist
$ cd composerinagist
$ vim composer.json
$ git add -A
$ git commit
$ git push
```

```json

{
  "require": {
    "denislaliberte/composerinagist": "dev-master"
  },
  "repositories": [
  {
    "type": "vcs",
    "url": "https://gist.github.com/82e54bcce3d56767e1d3.git"
   }
  ]
}
```

Pour créer un repo à partir d'un gist
``` bash
$git clone https://gist.github.com/82e54bcce3d56767e1d3.git test
$ cd test
$ git remote remove origin
$ hub create testfastrepo
```




