{% extends "base.html" %}

{% load static %}

{% block content %}
<br>

<div class="container bg-white shadow-md p-3 form-layout">
    
    <div class="alert alert-info" role="alert">
        <h4 class="alert-heading">An email confirmation has been sent to your email address!</h4>
        <p>
                An email confirmation has been sent to your email address. Please check your email and click on the confirmation link to complete the registration.
            If you did not receive the email, check your spam folder.
        </p>
    </div>
</div>

<br>

{% endblock %}