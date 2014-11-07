class: center, middle
# Drupal Script
---
name: agenda
## agenda
- 
- 
- 
---
##Objectif

Pas d'opétation manuelle en production

--

'Build' en une étape

--

Historique du projet

<!--
  -productivité développeur, un nouveau développeur peut construire le projet 
  sans se poser de question
  - intégration continue 
-->

---
template:agenda
---
#module.install
---
name:install
## module.install

--

Script d'installation et d'update des modules drupal

--

hook_install

--

hook_update_n

<!-- todo peut-être ajouter un exemple de code à cette étape -->

---
template:install

Commande drush

module_example_install()

--

$ drush pm-install module_example

---
template:install

Commande drush 


module_example_update_7001()

--

$ drush updb



---
template:install

Feedback !

--

```php
/**
 * Message to display on the command prompt
 */
function module_example_update_12() {
//...
```

---
template: agenda
---
#Integration
---
name: integration
## Integration

--

Un script unique c'est complexe

--

Un .install par module c'est mieux 

???
grouper les steps de déploiement par foncitonnalité

--

integration module

---
template: integration

module project_integration

--

module_enable('project_layout');


---
#Exemples
---
name: exemples

##Exemples

--

```php
/**
 * set project theme
 */
function project_layout_update_7001() {
  theme_enable(['project_theme'])
  variable_set('theme_default', 'project_theme');
}
```

---
template: exemples

$ drush pm-disable strongarm

--

```console
$ drush variable-get theme
  admin_theme: 'shiny'
  node_admin_theme: '1'
  theme_default: 'stingray'
```


---
# delete
---
taxonomy_vocabulary_delete
taxonomy_vocabulary_machine_name_load
field_delete_field

menu_load
menu_delete

---
pathauto : variable set
  variable_set('pathauto_node_advisor_pattern','find-an-advisor/[node:title]');

---
## language

    $languages = language_list();
    variable_set('language_default', $languages['en']);


---
## realm variable
  $original_realm =  variable_get('variable_realm_list_language');
  array_push($original_realm,'site_404');
  variable_set('variable_realm_list_language',$original_realm);

---
##delete taxonomy

function _delete_taxonomy_by_name($name) {
  $tax = taxonomy_vocabulary_machine_name_load($name);
  taxonomy_vocabulary_delete($tax->vid);
}

---
## delete menu

function _delete_menu_by_name($name) {
  $menu = menu_load($name);
  menu_delete($menu);
}


---
## l1on update ?!?!?
function _set_update_of_the_l10n_locally(){
  variable_set('l10n_update_download_store','sites/all/translations');
  $local_files_only = 2;
  variable_set('l10n_update_check_mode',$local_files_only);
}
---
## delete node type

node_type_delete

---
## add permission
  _add_permission_to_role('webmestre',$webmestre_permission);

  _create_role('webmestre');
/*
 * Create a role by name
 */
function _create_role($name) {
  if(!user_role_load_by_name($name)){
      $role = new stdClass();
      $role->name = $name;
      user_role_save($role);
  }else {
    watchdog(
      'stingray_permission',
      'Can\'t create the role %role, already exist',
      ['%role'=>$name],
      WATCHDOG_WARNING);
  }
}

/*
 * Change permission of a role by name, 
 * An array example for the permission is show on this page
 * https://api.drupal.org/api/drupal/modules%21user%21user.module/function/user_role_change_permissions/7
 */
function _add_permission_to_role($name,$permission) {
  $role = user_role_load_by_name($name);
  if($role) {
    user_role_change_permissions($role->rid,$permission);
  }else {
    watchdog(
      'stingray_permission',
      'Can\'t add permission to the role %role, role dont exist',
      ['%role'=>$name],
      WATCHDOG_WARNING
    );
  }
}

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
  




content vs configuration, choisir ses combats
$ drush php-script test.php
