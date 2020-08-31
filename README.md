<h3> Django by Tutorialspoint </h3>

<p>The tutorial introduces the web framework Django and its uses.</p>
<p>To see the tutorial click <a href="https://www.tutorialspoint.com/django/index.htm">here</a></p>

<h3>Databases</h3>
<p>Copy the one that starts with 'django.db.backends.'; MongoDB has a different format than the rest</p>
<ul>
    <li>MySQL: django.db.backends.mysql</li>
    <li>PostGreSQL: django.db.backends.postgresq</li>
    <li>Oracle: django.db.backends.oracle</li>
    <li>MongoDB: django_mongodb_engine</li>
</ul>

<h3>Command for creating the appliaction/s</h3>
<p>Using the terminal (make sure it's on the right directory) type: </p>
<b>python manage.py startapp appname</b>
<p>After creating the app; go to settings.py and add the app/s to the INSTALLED_APPS section.</p>
<p>Then migrate using this "python manage.py migrate"</p>

<h3>Superuser</h3>
<p>To create a superuser type to terminal the following 'python manage.py createsuperuser'</p>