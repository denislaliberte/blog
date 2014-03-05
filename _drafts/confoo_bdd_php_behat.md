---
layout: post
title:  "Conférence Confoo Montréal - BEHAT - Behaviour Driven Developpement"
date:   2014-03-01 17:19:33
categories: BDD PHP BEHAT
---
Au dernier confoo j'ai assisté à la conférences de Thobias Schlitt sur le Behavior 
Driven Developpent. Depuis quelques mois je m'intéresse à cette méthodologie et 
au librairies qui y sont associé Cucumber pour le ruby et Behat pour le php. 
Dans ce billet je fait un mélange entre les notes que j'ai pris lors de la 
conférence avec mes notes personnelle sur le sujet.

Pour un résumé plus précis de la conférece voir les 
[slides](http://qafoo.com/talks/14_02_confoo_behave_behavior_driven_development.pdf)

- Behaviours Driven Developpement vs Test Driven Developpement
- Gherkin un language non technique pour décrire les tests
- Acceptace testing
- Tests de non régression
- Des sécifications exécutables
- BDD et l'Intégration continue
- Le vrais BDD et les tests d'interfaces
- Mink, du faux bdd abordable
    
    
********************************************************************************
  
## Behaviours Driven Developpement vs Test Driven Developpement ##

Le BDD c'est un peu une évolution du TDD, une pratique technique qui consiste 
à créer des tests unitaire avant d'écrire le code, et c'est une pratique qui 
concerne surtout les développeurs. À l'opposé du TDD, le BDD est un outil de 
communication qui permet à une équipe multidisciplinaire  d'avoir un langage 
commun pour définir les fonctionnalités de l'application et des tests automatisé 
sont généré à partir de ces descriptions de fonctionnalité, c'est un peu du TDD 
collaboratif avec un focus sur la création de "business value".

## Gherkin un language non technique pour décrire les tests  ##

En BDD on décrit les scénarios d'utilisation avec un langage formel qui est facile
d'approche pour tout les membres non technique de l'équipe et les clients. Le 
langage contiens au maximum dix mot clés. On utilise surtout les termes Given, 
When et Then et on peut aussi le traduire en français selon ce qui est le plus 
approprié pour le client.

Exemple en français :
- Attendu  *un état du système*
- Quand  *je fait une action*
- Alors  *je valide un résultat*

Voici un exemple de scénario qui décrit une validation d'un champ courriel dans 
un formulaire web:

- Given  *I am on the contact form page*
- When  *I enter "mon email@gmail.com" in the email*
- Then  *I shoud see a error message about the space in the mail*
- And  *the submit button should be innactive*

On pourrais arrêter ici et ce serais suffisant. Avoir une liste de tests claire
pour décrire chacunes des user stories ce serais déjà un avancement face aux 
liste de "vérifier que" et aux descriptions remplis de "bullet point". Une 
situation ou on finis souvent par deviner ce qu'il faut développer et qui
ne répond pas toujours au besoin d'affaire que le client avais en tête.

Mais là ou le BDD deviens intéressant c'est quand on commence à générer des 
tests automatisés à partir de ces scénarios pour servir de tests d'acceptation 
et de tests de non régression.

## Acceptace testing ##

Un des avantages du BDD est qu'on génère des tests d'acceptation. On écris des
tests qui vérifie la fonctionnalité demandés par le client avant d'implémenter 
cette fonctionnalité. Une fois que ces tests sont écrit on travaille à faire 
passer ce tests et uniquement à faire passer ce tests... donc on évite de 
développer plus que ce que le client as demandé et de dépenser du budget sur 
des fonctionnalités qui sont moins prioritaires. On reste continuellement focus
sur les objectif d'affaire et les user stories du sprint.

## tests de non régression - spécification exécutable ##

Un autres avantage c'est que ces tests deviennent ensuite des tests de non 
régression. Chaque nouveau développement peut briser n'importe quelles autres 
fonctionnalité déjà développé. En théorie il faudrait tester toutes les 
fonctionnalité du site à chaque itération après quelques itérations le temps de 
tests commence à devenir plus important que le temps de développement et si on ne 
tests pas on accepte le risque que les bugs soient découvert par le client ou en 
production. Les tests automatisé deviennent donc vraiment intéressants.

Avec les tests automatisé en une commande on sait qu'on n'as pas introduit de bugs
et sinon on sait exactement ou et on le sait au moment ou on introduit ce bug.

## Des sécifications exécutables ##

L'avantage majeur de cette méthodologie c'est que ces spécification ne sont 
jamais dépassées. À chaque fois qu'on modifie le système on peut exécuter 
l'ensemble des tests et si on modifie une fonctionnalité qui est documenté on 
sait immédiatement quel partie de la documentation doit être modifiée.

## intégration continue ##

En tant que développeurs on peut ignorer les tests ou oublier de les exécuter, à
moins qu'on intègre ces test à notre processus d'intégration continue. Par exemple 
le serveur Jenkins peut rouler les tests et rejeter les commits qui brisent les
tests, donc même si un site est en ligne depuis des mois, on vas toujours avoir
des spécifications claire du comportement attendu.

### Vrais BDD vs tests d'interfaces  ###

Évidement tout ce que font les librairies de BDD c'est relier les "steps" du 
scénario avec une fonciton qu'on doit implémenter. Si on suis une vision puriste
du BDD il faudrais implémenter ces fonctions pour testers directement la logique
d'affaire de nos objets backend, mais dans le cas de projet de type CMS tester
directement l'interface semble être une solution acceptable et surtout abordable
pour la plus part des scénarios.

## Mink ##

Mink est une extension de BEHAT qui offre une api pour commander des browsers de
tests que ce soit des browser dit "headless" qui analyse seulement le html ou
des 'browser drivers' comme Selenium qui simule les actions des tests sur de 
vrais navigateurs, donc un tests peut s'exécuter sur tout les browser 
automatiquement.

Mink as une api qui offre une abstraction du http et du html. On peut demander 
une page, remplir un formulaire, l'envoyer et tests le résultats retourné en quelques
lignes de tests.

## Ressources ##

- La librairie ruby Cucumber est le premier outils à implémenter les concepts du
BDD  :
[ Cucumber ](http://cukes.info/)

- Le livre sur cucumber :
[ The Cucumber Book ](http://pragprog.com/book/hwcuc/the-cucumber-book)

- Dans ce livre sur rspec, il y as du contenu intéressant sur le BDD et sur cucumber
[ The RSpec Book ](http://pragprog.com/book/achbd/the-rspec-book)

- Behat, est un clone de cucumber en php.
[ Behat ](http://behat.org/)

- Mink, l'api de behat pour intéragir avec Selenium, Goute et sahi
[ Mink ](http://mink.behat.org/)

- Une extension qui définie des steps spécifique à drupal.
[ Behat drupal extension ](https://drupal.org/project/drupalextension)

- La suite de tests que l'équipe de drupal.org as développé pour la migration
drupal 6 à drupal 7 du site immense de la communauté drupal
[ doobie ](https://drupal.org/project/doobie)

