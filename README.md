# Django_Forms
Django Forms Project  This project demonstrates 3 different ways to create and handle forms in Django, based on the lecture material. Each way is implemented in the same project, and the inactive ones are commented out so you can switch between them easily.

Ways to Create Forms

1. Way 1 (Manual Form)

Write HTML form directly in the template.

Handle data manually in views.py.

Save to database with the model.

2. Way 2 (forms.Form)

Use Django’s forms.Form.

Validate inputs automatically.

Save data into the model after validation.

3. Way 3 (ModelForm)

Use Django’s ModelForm with Meta.

Fields are connected to the model directly.

Save data easily using form.save().

Security

CSRF protection ({% csrf_token %}).

Required fields.

Password input hidden using forms.PasswordInput.
Run the Project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
