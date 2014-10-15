### Layout
- page.tpl.php
- hook_preprocess_page
- menu_tree_page_data
- url
- menu_attributes
- language_negotiation_get_switch_links 
- drupal_is_front_page


Je créé un premier module `project_layout` pour gérer tout ce qui est le layout 
général du site. Le header, footer, les colonnes les menus et autres variables sont ~...

Dans le thème j'overrider le `page.tpl.php` et je déclare le hook 
`project_layout_preprocess_page` qui serviras à préparer les variables de ce template.

#### menus
J'utilise la fonction `menu_tree_page_data` pour récupérer un array contenant
les données du menu et les formater en fonction des classe custom dont on as de 
besoin.

L'array de menu contiens uniquement les machine names des liens, mais on peut 
utiliser la fonction `url` pour obtenir l'alias des items de menu.

#### Attibuts du menu
Le module `menu_attributes` fournis de nouveaux champs dans l'admin pour ajouter 
des images ou des classe aux items de menus. Ces attibut seront ajouté à l'array
de variable retourné par le `menu_tree_page_data`. Pour les images le module ajoute
un `fid` identifiant de fichier et on peut utiliser la fonction `file_create_url`
pour révupérer le chemin de ce fichier.

#### languages switcher
En quelques lignes de code on peut avoir les donnés du language swicher.

``` php
function getLanguageSwitcher(){
      $path = drupal_is_front_page() ? '<front>' : $_GET['q'];
      $switcher = language_negotiation_get_switch_links('language_url', $path);
      return $switcher->links;
  }
```

### variables
Les variables de drupal sont des 

- variable_set
- variables module pour l'admin
- realm var

### templates 
Pour éviter de tout mettre dans le `page.tpl.php` et de se retrouver avec un 
fichier gigantesque on déclare nos propres fichier tpl avec le `project_layout_theme`
et ensuite on utilise la fonction `theme()` pour récupérer le markup de ces 
templates.

### breadcrumb
la fonction thème avec 


