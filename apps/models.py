from django.db.models import Model, ImageField, CharField, TextField, SlugField, TextChoices, DecimalField, ForeignKey, \
    PROTECT
from django.utils.text import slugify


# Create your models here.
class Category(Model):
    img = ImageField(upload_to='category/images/%m')
    name = CharField(max_length=255)
    slug = SlugField(max_length=30)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)


class Product(Model):
    class Color(TextChoices):
        white = 'white', 'white'
        black = 'black', 'black'

    class Size(TextChoices):
        M = 'M', 'M'
        X = 'X', 'X'
        L = 'L', 'L'
        XL = 'XL', 'XL'

    img = ImageField(upload_to='product/images/%m')
    price = DecimalField(decimal_places=0, max_digits=30)
    name = CharField(max_length=100)
    description = TextField()
    review = CharField(max_length=50, default=30)
    brand = ForeignKey('apps.Category', on_delete=PROTECT)
    slug = SlugField(max_length=30, null=True, blank=True)
    color = CharField(max_length=10, choices=Color.choices)
    size = CharField(max_length=10, choices=Size.choices)

    def __str__(self):
        return self.name

    def short_desc(self):
        return self.description[:30]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

