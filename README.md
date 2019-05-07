IN104_Camille_DeKocker
==

>IN104 Project


jdgaraud@onera.fr


# unicode for card suits symbol :
  - Spade <pre><code>"\u2660"</code></pre> 
  - Club <pre><code>"\u2663"</code></pre> 
  - Heart <pre><code>"\u2665"</code></pre> 
  - Diamond <pre><code>"\u2666"</code></pre> 
  

# PEP-8 Convention :
  - Variables : lower_case_with_underscore
  - Functions : lower_case_with_underscore
  - Classes : UpperCamelCase
  - Attributes : lower_case_with_underscore
  - Protected Attributes : _lower_case_with_underscore
  - Constants : ALL_CAPS
  - Modules : lowercase


Class Enum : lister des choses

# synchroniser avec upstream :
  - git status
  - git pull upstream master
  - git commit -a -m "sync upstream"
  - git push origin master
  
  
# synchroniser avec master :
  - git status
  - git add (fichier en rouge dans status)
  - git commit -m "blabla"
  - git pull origin Camille
  - git push origin Camille
  - git checkout master
  - git pull origin master
  
# envoyer des pull request vers upstream :
  - git checkout upstream/master
  - git checkout -b "nouveau_test Alice Bob"
  - on fait les modifs dans la branche
  - git commit -a -m
  - git push origin
  
  
# unittest
  - https://realpython.com/python-testing/
  - https://docs.python.org/3/library/unittest.html
  
  
