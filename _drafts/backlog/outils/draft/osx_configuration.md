OSX configuration
====================

### tip-97  turn off effect
* popup

`$ defaults write -g NSAutomaticWindowAnimationsEnabled -bool FALSE `

* quick look

`$ defaults write  com.apple.finder QLPanelAnimationDuration -int 0;killall Finder`

* Mission Control

`$ default write com.apple.dock expose-animation-duration int -0;killall Dock`

* file and print dialog

`$ default write -g NSWindowResizeTime -float 0.01`

* Dock

`$ defaults write com.apple.dock authohide-delay -float 0
$ defaults write com.apple.dock authohide-time-modifier -int 0;killall Dock`

### tip-45 désactiver le son de la poubelle

defaults write com.apple.finder FinderSounds -bool FALSE;killall Finder


### tip 176 desactiver le bounce dans le dock

defaults write com.apple.dock no-bouncing -bool TRUE;killall Dock

### tip-243 turn off desktop

`defaults write com.apple.finder CreateDesktop -bool FALSE;killall Finder`

chmod 000 ~/Desktop

restore
`defaults delete com.apple.finder CreateDesktop;killall Finder`
<!-- todo : créer un alias, ou ajouter au profil zsh -->



### tip-208 Arrêter la réouverture des documents automatique 

Dans les préférences dans la section général, cocher "close windows when quitting an applicaiton"


### tip-294
Toujours foir la sauvegarde étandue 
`defaults write -g NSNavPanelExpandedStateForSaveMode -bool TRUE`


### tip-41 timestamp zip file
defaults write com.apple.finder ArchiveTimestamp -bool TRUE;killall Finder




