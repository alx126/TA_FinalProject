Proiect de testare automata BDD Python

Implementare teste automate pentru magazin online
Site: https://demo.nopcommerce.com/

Limbaj: Python
IDE: PyCharm Community Edition 2023.2.3

Librarie                  Comanda in terminal pentru instalare
-----------------------------------------------------------------
Selenium                   pip install selenium
-----------------------------------------------------------------
Webdrive manager           pip install webdriver-manager
-----------------------------------------------------------------
Behave
-----------------------------------------------------------------



Exemple de comenzi pentru a rula teste cu tag-uri:
  behave --tags=register
  behave -f html -o behave-report.html --tags=smoke
  behave --tags=smoke,simple  (fara spatiu intre taguri in acest caz!)
