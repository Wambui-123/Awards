# Awards
## Author

~ Yvonne Muthui
## Description

A Django framework Python application that lets users post their own sites or projects which can be viewed and rated by other users.

## User Story
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page  

## [Demo](https://wambo-awwwards.herokuapp.com/) click to view

![Image](/static/img/Screenshot%20from%202022-06-14%2010-34-26.png)

## Author
[Yvonne Muthui](https://github.com/wambui-123)

## Description
A web application just like instagram that lets you upload posts and edit your own profile pictures made using Django.

## Technologies Used
* Python 3.7.4
* Django 1.11.23
* SQLite3
* HTML5  
* CSS3
* Bulma 
* Bootstrap 4.3.1
* Google Font API

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: * **`pip install django==1.11.23`**
* This project requires you to have a secret key from Uploadcare to facilitate cloud storage of uploaded images.
    * The secret key can be gotten by creating a free uploadcare account, starting a new project and navigating to the dashboard
    * The key should be stored as an environmental variable in an .env file as shown below
        * **`SECRET=<your secret key here>`**
    * More info on how to use the Django pyuploadcare library can be found [here](https://uploadcare.com/docs/guides/django/)

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/Wambui-123/Instagram.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 5** : You can now launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    * To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.    

## Known Bugs
* None at the momment, report any by contacting me

## Support and contact details
If you find a bug on the website or its not working as expected, please feel free so send me an email @yvonnewambui28@gmail.com

## Licence
* MIT License
* Copyright (c) 2022 Yvonne Muthui

