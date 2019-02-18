from django.test import TestCase

# Create your tests here.


def create_username(email):
    return email.replace("@", "")


print(create_username("nayan32biswas@gmail.com"))
