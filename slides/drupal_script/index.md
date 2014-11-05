class: center, middle
# Drupal Script
---
name: agenda
## agenda
- 
- 
- 
---


Objectif
Éliminer les étapes manuelles dans la construction du site.
Construire le sites avec un minimum d'étapes qui peuvent être automatisée
en une seule étape 

Avoir un historique de la construction du site



---
première étape vers l'Intégration continue


---
template:agenda
---
#module.install
---
name:install
## module.install

--

hook_update_n

---
template:install

hook_update doc string

---
template: install

integration module

dependecy graph

plusieurs  module avec chacun le .install
---
template: install

module_enable

--

theme_enable

--

variable_set


---
# variable
---

variable:
no strongarm
variable_set
$ drush vget


---
#drush 
---

drush command
 
$ drush si
$drush en integration_module
$drush updb
$drush feature-revert


---
#features
---


---
#problemes
---

Strongarm
Realm variables
roles et droits
delete operation

---
# delete
---
taxonomy_vocabulary_delete
taxonomy_vocabulary_machine_name_load
field_delete_field

menu_load
menu_delete







<!--
  options profil d'installation ?!
  
  http://dcycleproject.org/
  
  
  
  
  
  
  function manage_deploy_install() {
      manage_deploy_update_dependencies();
        for ($i = 7001; $i < 8000; $i++) {
              $candidate = 'manage_deploy_update_' . $i;
                  if (function_exists($candidate)) {
                          $candidate();
                              }
                                }
  }
  
  
  
  devmodule.install
  
  
  //
  
  drupal_parse_info_filedrupal_parse_info_file
  
  
  
  
  * [Blog | Dcycle](http://dcycleproject.org/blog)
  * [Do not clone the database | Dcycle](http://dcycleproject.org/blog/48/do-not-clone-database)
  * [Continuous deployment, Drupal style | Dcycle](http://dcycleproject.org/blog/46/continuous-deployment-drupal-style)
  * [What is a site deployment module? | Dcycle](http://dcycleproject.org/blog/44/what-site-deployment-module)
  * [Continuous integration - Wikiwand](http://www.wikiwand.com/en/Continuous_integration)
  * [Continuous Integration | ThoughtWorks](http://www.thoughtworks.com/continuous-integration)
  * [Continuous Integration](http://www.martinfowler.com/articles/continuousIntegration.html)
  
