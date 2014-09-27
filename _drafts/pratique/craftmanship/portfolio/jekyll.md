site static
===========

## jekyll ##
-Jekyll est un utilitaire en ligne de commande qui permet de générer un site html
statique.
-Semble être la solution la plus simple pour un site si l'administrateur est développeur
-Il est utilisé pour les page github.

[ installation ](http://jekyllrb.com/docs/installation/)
[ usage ](http://jekyllrb.com/docs/usage/)
[ Gihub Pages](http://pages.github.com/)

### talk ###
[ Introduction to Blogging with Jekyll ](http://www.youtube.com/watch?v=c5WkxIzK0eA)
[ Jekyll Static Site Generator ](http://www.youtube.com/watch?v=7mXeJlFdZ2c)
## gihub ##
Les pages github sont des repos hébergé pensé pour des sites statique généré par
Jekyll

[github pages ](http://pages.github.com/)

## farmework frontend ##
### Twitter bootstrap ###
Bootstrap pour monter une simple page sans style semble être la solution la plus rapide
Using Twitter Bootstrap with Jekyll
http://brizzled.clapper.org/blog/2012/03/05/using-twitter-bootstrap-with-jekyll/


## exemples ##
Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}




## distribution jekyll ##
-J'ai trouvé deux distributions jekyll, Octopress et Jekyll-Bootstrap.
-Désavantage: je me demande si elles sonts stables et si elles sont simples. 
-Pour l'instant installer un framework front end et faire le reste à la main semble être la solution la plus simple.

### octopress ###
tagline : "A blogging framework for hackers."
C'est un genre de framework bati sur jekyll
[ octopress ](http://octopress.org/)
[ github repo ](https://github.com/imathis/octopress)

Je ne suis pas sur si c'est assez mature, compliqué pour rien à installer, je m'inquiète aussi de ce qu'il contiens... je ne suis pas sur que je veux quelque choses d'aussi compliqué.


### jekyll bootstrap ###
tagline : The Quickest Way to Blog on GitHub Pages.
[ Jekyll bootstrap ](http://jekyllbootstrap.com/)
-Backed by Twitter Bootstrap
http://jekyllbootstrap.com/lessons/jekyll-introduction.html

-Pas sur si c'est mature et stable
-Installer en clonant le repo
-Ajoute des rake task pour ajouter des pages et autres
-Donne des templates et permet de changer de thèmes avec des rake task
