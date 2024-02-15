from django.db import models


class House(models.Model):
    address = models.CharField(max_length=50)
    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        db_table = 'house'
        verbose_name = 'House'
        verbose_name_plural = 'Houses'

    def __str__(self) -> str:
        return f'House<{self.id}>'

    def __repr__(self) -> str:
        return f'House<{self.id}>'


class HouseImages(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='house')

    class Meta:
        db_table = 'image'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self) -> str:
        return f'Image<{self.id}>'

    def __repr__(self) -> str:
        return f'Image<{self.id}>'
