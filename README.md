##### django_student_details
# HOW DOES IT WORK
![image](https://github.com/rumainaali/django_student_details/assets/126662274/cd9a012a-e21e-4c37-9447-3691830b2e46)

For eg: My username: 'Rumaina'\
My password: '123'

![image](https://github.com/rumainaali/django_student_details/assets/126662274/7be47139-2e5e-4d57-aeac-4c10f0a90c88)

After running the code from project using cmd ```python manage.py runserver 8000```, the default url would be at '127.0.0.1:8000' would display the student's list

![image](https://github.com/rumainaali/django_student_details/assets/126662274/7bc29bb9-6c56-421a-8011-99235ac4c463)

Now edit the url as '127.0.0.1:8000/student/id/'

For eg:'127.0.0.1:8000/student/1/'

+'127.0.0.1:8000/student/2/'

+'127.0.0.1:8000/student/3/'

and more

![image](https://github.com/rumainaali/django_student_details/assets/126662274/36e67e5b-bc2d-419f-8655-271bf07c8bc1)

![image](https://github.com/rumainaali/django_student_details/assets/126662274/aa872460-3dbd-4efc-929f-7ac0925844ef)

# HOW TO START THE PROJECT
Step 1: Creating the django project by providing a directory to create a project and run the command:
```django-admin startproject 'projectname'```

Step 2: Creating the django application by changing the directory into the project and start the app with the command:
```python manage.py startapp 'application_name'```

Step 3: Open 'settings.py' and include the app_name in 'installed apps'.

Step 4: Provide 'views.py' with function setup.

Step 5: Provide with the path to open the webpage and display the content.

Step 6: Run your server with cmd:
```python manage.py runserver```

### TEMPLATES
Create a folder in main application directory and make a file for your project in which the html file is stored.
```
BASE_DIR2 = os.path.dirname(os.path.dirname(os.path.abspath(file)))

TEMPLATE_DIR = os.path.join(BASE_DIR2, 'templates')
```
and add TEMPLATE_DIR in TEMPLATE_DIR = []

### STATIC
Html files can be stored in templates while css,images and other files can be included here.
```
STATIC_DIR = os.path.join(BASE_DIR2, 'static')
```
Add your db to be translated code into Models.py

##### Models.py
![image](https://github.com/rumainaali/django_student_details/assets/126662274/d471aae4-a113-4ad1-9156-ffd70d06bb64)

##### Admin.py
![image](https://github.com/rumainaali/django_student_details/assets/126662274/cb2855b1-2159-44a5-b590-d7da504a6c00)

##### Urls.py
![image](https://github.com/rumainaali/django_student_details/assets/126662274/e6192885-eefe-4038-ae5a-2c099dac70a4)

##### Views.py
![image](https://github.com/rumainaali/django_student_details/assets/126662274/104f9f7f-a242-482a-8e85-8277ebd41a42)

##### Students_detail.html
![image](https://github.com/rumainaali/django_student_details/assets/126662274/8353144f-68a3-4cfd-8fe1-410494f89993)

##### Students_list.html
![image](https://github.com/rumainaali/django_student_details/assets/126662274/bbbfa40e-1331-4c46-b799-b614916e1b7f)













