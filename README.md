# Proiect de testare automata BDD Python

## Implementare teste automate pentru magazin online


**Site:** https://demo.nopcommerce.com/

**Limbaj:** Python (https://www.python.org/downloads/)

**Metodologie:** Behavior Driven Design (BDD)

**Design pattern:** Page object model (POM)

**IDE:** PyCharm Community Edition 2023.2.3  (https://www.jetbrains.com/pycharm/download/?section=windows)
___

**Instalarea librariilor necesare se poate face folosind urmatoarele comenzi in terminal:**

**Selenium:**   _pip install selenium_

**Webdrive-manager:** _pip install webdriver-manager_

**Behave:** _pip install behave_

**Behave-html-formatter:** _pip install behave-html-formatter_
___

**Instructiuni clonare proiect**

1. Copiaza linkul proiectului: https://github.com/alx126/TA_FinalProject.git
2. Creeaza un folder nou local, aici se va instala proiectul
3. In folder se deschide Git BASH cu comanda Git Bash Here: Click dreapta in folder si selectezi Git Bash Here din context menu  ![image](https://github.com/alx126/TA_FinalProject/assets/93679540/f50ca661-f78c-4533-81ff-2b9d10b6ad1c)
4. In fereastra deschisa se introduce: git clone + link proiect (click dreapta - Paste) + Enter  ![image](https://github.com/alx126/TA_FinalProject/assets/93679540/4f2c22fa-cd2c-458b-be53-703854a49363)
___

**Instructiuni rulare proiect**

1. Deschide proiectul in PyCharm:
   
   ![image](https://github.com/alx126/TA_FinalProject/assets/93679540/1345a113-919d-4d74-bbe8-0e7b69366128)
2. Instaleaza librariile mentionate mai sus

In terminalul PyCharm se introduc comenzile de instalare pentru librariile mentionate.

(am folosit comanda _pip install -U selenium_ pentru a instala ultimele update-uri selenium)

![image](https://github.com/alx126/TA_FinalProject/assets/93679540/324e7b36-8464-4f69-9a33-bfeb96e707e8)

___   




**Exemple de comenzi pentru a rula teste cu tag-uri:**

  _behave --tags=register_

  _behave --tags=smoke,simple_  (fara spatiu intre taguri in acest caz!)
  
  _behave -f html -o behave-report_smoke.html --tags=smoke_