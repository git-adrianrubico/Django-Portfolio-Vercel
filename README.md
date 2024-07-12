# Django Personal Portfolio
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


## Introduction
🚀 Welcome to my Django-powered portfolio on GitHub! Explore various aspects of my professional journey through the **Home, About, Portfolio**, and **Contact Us** sections. This project not only showcases my skills in Django development but also demonstrates successful deployment using **Render** (SaaS). Moreover, static files are efficiently managed through **Cloudinary**, ensuring a seamless and responsive user experience. Discover a thoughtfully curated collection of my projects, delve into my background with a responsive digital CV, and with the custom 404 page. This space encapsulates my creativity and dedication, illustrating how technology and passion intersect in my work. Feel free to navigate and connect—I'm thrilled to share my journey with you! 👋

![Home Page_1](</Website Screenshots/main_home.png>)
![Home Page_2](</Website Screenshots/main_home_mobile.png>)

## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Techonology Used](#technology-used)
  * [Features](#features)
  * [Website Screenshots Desktop View](#website-screenshots-desktop-view)
  * [Website Screenshots Mobile View](#website-screenshots-mobile-view)
  * [Admin Screenshots](#admin-screenshots)
  * [Deployment](#deployment)
  * [Credits](#credits)
  * [License](#License)
  * [Author](#author)

## Installation
#### 1. Clone the repository:
```bash
git clone https://github.com/git-adrianrubico/Django-Portfolio
```
#### 2. Create and activate virtual environment:
```bash
cd Django-Portfolio
python -m venv env
source env/bin/activate
```

#### 3. Next, Install all the components
```python
pip install -r requirement.txt
```
#### 4. Make a migration and migrate
```python
python manage.py makemigrations
python manage.py migrate
```
#### 5. Once the data is migrated, create a superuser to entry a data into DB.
```python
python manage.py createsuperuser
```

Primary Modules used
  - Django==4.1.4  
  - cloudinary==1.36.0
  - django-cloudinary-storage==0.3.0
  - django-recaptcha==4.0.0

## Technology Used
- Python
- HTML
- CSS
- Javascript
- Isotope Layout
- Google Recaptcha
- Cloudinary

#### Features
1. **Django-Powered**: A robust portfolio leveraging Django for dynamic content and seamless interactivity.

2. **OnRender Deployment**: Effortless project deployment using OnRender for a hassle-free hosting experience.

3. **Cloudinary Integration**: Efficient management of static files through Cloudinary for optimized performance.

4. **Curated Project Showcase**: Explore a handpicked collection of projects highlighting creativity and problem-solving skills.

5. **Responsive Digital CV**: Get insights into my professional journey with a responsive digital CV for a comprehensive overview.

6. **Contact Section**: Connect easily through the Contact Us section, open to new opportunities and collaborations.

7. **Django Admin Interface**: Streamlined data management with the user-friendly Django admin interface.

8. **Google Recaptcha**: Prevent bots and enhance security with Google Recaptcha, ensuring a secure and spam-free communication experience.

## Website Screenshots Desktop View
![Home Page](</Website Screenshots/main_home.png>)
![About_1](</Website Screenshots/About_1.png>)
![About_2.png](</Website Screenshots/About_2.png>)
![Portfolio_1](</Website Screenshots/Portfolio_1.png>)
![ContactUs_1](</Website Screenshots/ContactUs_1.png>)
![ContactUs_2](</Website Screenshots/ContactUs_2.png>)
![404 Page](</Website Screenshots/Custom404.png>)
![CV_1](</Website Screenshots/CV_1.png>)
![CV_2](</Website Screenshots/CV_2.png>)
![CV_3](</Website Screenshots/CV_3.png>)
![CV_4](</Website Screenshots/CV_4.png>)

## Website Screenshots Mobile View
![Home Page_mobile](</Website Screenshots/main_home_mobile.png>)
![About_1_mobile](</Website Screenshots/About_1_mobile.png>)
![Portfolio_1_mobile](</Website Screenshots/Portfolio_1_mobile.png>)
![ContactUs_1_mobile](</Website Screenshots/ContactUs_1_mobile.png>)
![CV_1_mobile](</Website Screenshots/CV_1_mobile.png>)
![CV_3_mobile](</Website Screenshots/CV_3_mobile.png>)

## Admin Screenshots
![(Dashboard](</AdminSite Screenshots/Dashboard.png>)
![About](</AdminSite Screenshots/About.png>)
![Description](</AdminSite Screenshots/Description.png>)
![Education](</AdminSite Screenshots/Education.png>)
![Experience](</AdminSite Screenshots/Experience.png>)
![Issue_org](</AdminSite Screenshots/Issue_org.png>)
![Personal_info](</AdminSite Screenshots/Personal_info.png>)
![Portfolio_1-1](</AdminSite Screenshots/Portfolio_1-1.png>)
![Technology](</AdminSite Screenshots/Technology.png>)

## Deployment
Elevate your Django portfolio from local development to a global stage through the deployment process. You can deploy any infrastructure as long as it can run Python application. It could be cloud-based server like AWS/Azure, or it could be PaaS Heroku, Render, & Vercel etc. In this project, we've opted for **[Render](https://render.com/)** as the hosting platform, guaranteeing a seamless and scalable environment. Here are the following Steps on how to deploy in the Render.

1. **Create an Account on Render**:
Start by creating an account on Render.com. Provide the necessary details to set up your account and log in to the Render dashboard.

2. **Initialize Web Service & Select "Build and Deploy from a Git Repository"**:
In the web service settings, choose "Build and Deploy from a Git Repository" as your deployment method. This option streamlines the process by connecting your portfolio directly to your Git repository.
![Web Service](</Deployment Screenshots/image.png>)
![Alt text](</Deployment Screenshots/image-1.png>)

3. **Connect Your Git Repository**:
Specify the repository where your Django portfolio is hosted. Connect Render to your Git account, allowing it to fetch the latest updates and changes from your repository.

4. **Use Environment Variables for Configuration**:
Utilize `os.environ.get("")` to store API keys, configuration values, and secrets securely. Access these variables in your code using `os.getenv()` in Python, ensuring sensitive information remains confidential.
```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

EMAILHOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAILHOST_PASSWD = os.environ.get("EMAIL_HOST_PASSWORD")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = EMAILHOST_USER
EMAIL_HOST_PASSWORD = EMAILHOST_PASSWD

if DEBUG is False:
    STATICFILES_DIRS = [ BASE_DIR / 'static' ]
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")

CLOUDINARY_CLOUDNAME = os.environ.get("CLOUD_NAME")
CLOUDINARY_APIKEY = os.environ.get("CLOUD_API_KEY")
CLOUDINARY_SECRET = os.environ.get("CLOUD_API_SECRET")

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': CLOUDINARY_CLOUDNAME,
    'API_KEY': CLOUDINARY_APIKEY,
    'API_SECRET': CLOUDINARY_SECRET,
}

cloudinary.config(
    cloud_name = CLOUDINARY_CLOUDNAME,
    api_key = CLOUDINARY_APIKEY,
    api_secret = CLOUDINARY_SECRET,
)
```

5. **Configure Build Settings**:
Configure the build settings to match your Django project's requirements. Define the build command, environment variables, and any other settings necessary for your application.
![Alt text](</Deployment Screenshots/image-3.png>)
![Alt text](</Deployment Screenshots/image-4.png>)
![Alt text](</Deployment Screenshots/image-5.png>)

**Note: You may include here SECRET KEY, EMAIL SNMP VARIABLE, GOOGLE RECAPTCHA KEYS, CLOUDINARY STATIC AND IMAGES (Optional: This is for fast content delivery network (CDN))**

You may follow here the youtube guide on how to setup Cloudinary & Google Django Recaptcha.

* [Host uploaded images from Django with Cloudinary](https://www.youtube.com/watch?v=fQo9ivqX4xs)
* [Deploy static files to Cloudinary from a Django app](https://www.youtube.com/watch?v=HQ1kfJpWdRI)
* [CAPTCHAs in Django forms](https://www.youtube.com/watch?v=QGz_CczcL3Q&t=3s)

6. **Optional Postgres Database Setup**:
If you choose to deploy with a Postgres database, import dj_database_url in your settings file. Configure the database settings as follows:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

database_url = os.environ.get("DATABASE_URL")
DATABASES["default"] = dj_database_url.parse(database_url, conn_max_age=600)
```

Here is the guide <a href="https://youtu.be/AgTr5mw4zdI?t=929&si=siE8yPqA5ilPcKPJ">Deploy a Django web app to a Render live server with PostgreSQL</a>
    

## Credits
- Portfolio Template Design: https://github.com/bkpecho/v1/
- Digital CV Template Design: https://github.com/FrankSiret/resume-cv/
- Render Setup: https://github.com/cloud-with-django | https://www.youtube.com/@cloudwithdjango
- Django Recaptcha Setup: https://www.youtube.com/@bugbytes3923
- Simple Icons: https://cdn.simpleicons.org

## License 
This project is licensed under the [MIT License](LICENSE).

## Author
 - GitHub - [git-adrianrubico](https://github.com/git-adrianrubico)
 - LinkedIn - [Adrian Rubico]([git-adrianrubico](www.linkedin.com/in/adrianrubico))

