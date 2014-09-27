#Python
Utiliser le "toolbox" python pour générer du code et dealer avec les taches 
répétitive en programmation

Python est vraiment un language simple à utiliser pour dealer avec les string
et il viens avec plusieurs libraries simple pour 

#talk 
cmd interactif :
http://blip.tv/pycon-us-videos-2009-2010-2011/pycon-2010-easy-command-line-applications-with-cmd-and-cmd2-153-3280763

#fabric 
tool box pour gérer les commandes bash et l'exécution en ssh 

#yaml
language parfait pour faire des fichiers de configuration lisible

#clize
semble être la façon la plus simple de générer des commande à partir 
de décorateur python, semble suivre un pattern un peu semblable à fabric
https://pypi.python.org/pypi/clize/
http://clize.readthedocs.org/en/latest/

#jinja2 
templating engine, utiliser pour des templates de fichier de programmation.

#glob 
pour trouver des fichier
http://docs.python.org/2/library/glob.html


#cucumber
https://github.com/cucumber/aruba
talk:
http://www.confreaks.com/videos/694-rubyconf2011-test-drive-the-development-of-your-command-line-applications
https://github.com/cucumber/cucumber/wiki
#cucumber avec python : 
https://github.com/cucumber/cucumber/wiki/Python
http://rubypython.rubyforge.org/

#path
path as python object
https://pypi.python.org/pypi/path.py

#sh
pour rouler des commandes shell en python ext git.checkout()
http://amoffat.github.io/sh/

#docopt
génère un parser à partir d'une man page, concept vraiment intéressant
un alternative à clize, cool interface, multiplateforme
http://docopt.org/
https://github.com/docopt/docopt
talk 
http://www.youtube.com/watch?v=pXhcPJK5cMc&feature=youtu.be
##
#outils intéressant mais overkill
##

#cmd curse 
pour développer des application en ligne de commande
http://docs.python.org/3/library/cmd.html
http://docs.python.org/2/howto/curses.html
http://www.dev-explorer.com/articles/python-with-curses


#facker 
générateur de dummy content
Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you.
https://github.com/joke2k/faker


#ruby 
atout : générer un gem plus facile à distribuer
peut utiliser les même test cucumber et l'indeface docopt
http://www.youtube.com/watch?v=1ILEw6Qca3U
https://github.com/davetron5000/methadone
http://www.amazon.ca/Build-Awesome-Command-Line-Applications-Ruby/dp/1937785750/ref=sr_1_10?ie=UTF8&qid=1393298588&sr=8-10&keywords=command+line

#Bottle
présenter des rapport et de l'information en format web

#beautifulsoup
parse html 

#pyquery
port de jquery en python, 
query html et xml document comme jquery
https://pythonhosted.org/pyquery/

#scrappy
web scrapper
http://scrapy.org/

#cog 
code genenrator un peu overkill
http://nedbatchelder.com/code/cog/
embeder du python en commentaire dans un autre language en commentaire pour qu'il génère du code

#argh et argpars pour parser des argument en ligne de commande
argh
génère des man page à partir de parser, docopt semble plus intéressant
http://pythonhosted.org/argh/

argparse 
trop boillerplate vs clize, docopt et même argh
librarie python pour gérer les arguments en ligne de commande
voir s'il est possible d'intégrer avec fabric
http://docs.python.org/2.7/library/argparse.html

http://stackoverflow.com/questions/18591879/call-python-fabric-functions-from-within-the-same-script





