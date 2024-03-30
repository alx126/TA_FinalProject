Proiect de testare automata BDD Python



Implementare teste automate pentru magazin online


Site: https://demo.nopcommerce.com/

Limbaj: Python (https://www.python.org/downloads/)

Metodologie: Behavior Driven Design (BDD)

Design pattern: Page object model (POM)

IDE: PyCharm Community Edition 2023.2.3  (https://www.jetbrains.com/pycharm/download/?section=windows)

Librarie              |    Comanda in terminal pentru instalare
-----------------------------------------------------------------
Selenium              |    pip install selenium
-----------------------------------------------------------------
Webdrive-manager      |    pip install webdriver-manager
-----------------------------------------------------------------
Behave                |    pip install behave
-----------------------------------------------------------------
Behave-html-formatter |   pip install behave-html-formatter
-----------------------------------------------------------------



Instructiuni clonare proiect

1. Copiaza linkul proiectului: https://github.com/alx126/TA_FinalProject.git
2. Creare un folder nou local, aici se va instala proiectul
3. In folder se deschide Git BASH cu comanda Git Bash Here: Click dreapta in folder si selectezi Git Bash Here din context menu  ![image](https://github.com/alx126/TA_FinalProject/assets/93679540/f50ca661-f78c-4533-81ff-2b9d10b6ad1c)
4. In fereastra deschisa introduci: git clone + link proiect (click dreapta - Paste) si apesi Enter





Exemple de comenzi pentru a rula teste cu tag-uri:

  behave --tags=register
  
  behave -f html -o behave-report.html --tags=smoke
  
  behave --tags=smoke,simple  (fara spatiu intre taguri in acest caz!)
