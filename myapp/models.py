from django.db import models


class City(models.Model):
    """ Model instance for all cities """
    name = models.CharField("City Name", max_length=50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField("Country", max_length=100)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Person(models.Model):
    """ Model instance for persons """
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


