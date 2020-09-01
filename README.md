
<h3> Django by Tutorialspoint </h3>
<p>The tutorial introduces the web framework Django and its uses.</p>
<i>Tutorialspoint django tutorial is outdated but can still be useful in learning</i>

<h3>Configuring settings.py</h3>
<p>Replace BASE_DIR with BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))</p>
<p>Then add the following:</p>
<ul>
    <li>(Add this at beginning) import os</li>
    <li>TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")</li>
    <li>STATIC_DIR = os.path.join(BASE_DIR, "static")</li>
</ul>
<p>To see the tutorial click <a href="https://www.tutorialspoint.com/django/index.htm">here</a></p>

<h3>Databases</h3>
<p>Copy the one that starts with 'django.db.backends.'; MongoDB has a different format than the rest</p>
<ul>
    <li>MySQL: <b>django.db.backends.mysql</b></li>
    <li>PostGreSQL: <b>django.db.backends.postgresq</b></li>
    <li>Oracle: <b>django.db.backends.oracle</b></li>
    <li>MongoDB: <b>django_mongodb_engine</b></li>
</ul>

<h3>Command for creating the appliaction/s</h3>
<p>Using the terminal (make sure it's on the right directory) type: </p>
<b>python manage.py startapp appname</b>
<p>After creating the app; go to settings.py and add the app/s to the INSTALLED_APPS section.</p>
<p>Then migrate using this "python manage.py migrate"</p>

<h3 style='color: red;'>Superuser</h3>
<p>To create a superuser type to terminal the following 'python manage.py createsuperuser'</p>

<h3>Views, URLs and Templates</h3>
<p>Django has its unique way of routing URLs. urls.py is located at BASE DIR; </p> 
<p>Views is in the app already when first created; Templates is created by the developer.</p>
<p>If followed "Configuring settings.py", instead of creating templates inside firstapp folder; place on base directory.</p> 

<h3>Passing URL</h3>
<p>Instead of doint this "url/(\d+); do this "url/<'values'>""</p>