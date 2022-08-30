from django.db import models

# Create your models here.
class HomeSlider(models.Model):
    name1 = models.CharField('Slider name1', max_length=30)
    name2 = models.CharField('Slider name2', max_length=30)
    about = models.TextField('Slider about')
    img = models.ImageField('Slider image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'
class Banner(models.Model):
    banner_title = models.CharField('Banner title', max_length=30)
    description = models.TextField('Banner description')
    Banner_url = models.URLField('Banner video url', max_length = 200)

    def __str__(self):
        return self.banner_title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class Social(models.Model):
    facebook = models.URLField('Facebook url', max_length = 200)
    twitter = models.URLField('Twitter url', max_length = 200)
    linkedin = models.URLField('Linkedin url', max_length = 200)
    youtube = models.URLField('Youtube url', max_length = 200)
    be = models.URLField('Be url', max_length = 200)

    def __str__(self):
        return self.facebook

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

class HomeOnecolumn(models.Model):
    image = models.ImageField('Column image', upload_to = 'media')
    title = models.CharField('Column title', max_length=30)
    text = models.TextField('Column text')
    text1 = models.TextField('Column text1')
    onecolumnurl = models.URLField('Column url', max_length = 200)
    about = models.TextField("Detals")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HomeOnecolumn'
        verbose_name_plural = 'HomeOnecolumns'

class HomeTwocolumns(models.Model):
    image = models.ImageField('Column image', upload_to = 'media')
    title = models.CharField('Column title', max_length=30)
    text = models.TextField('Column text')
    text1 = models.TextField('Column text1')
    onecolumnurl = models.URLField('Column url', max_length = 200)
    about = models.TextField("Detals")



    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'HomeTwocolumns'
        verbose_name_plural = 'HomeTwocolumns'

class HomeThreecolumns(models.Model):
    image = models.ImageField('Column image', upload_to = 'media')
    title = models.CharField('Column title', max_length=30)
    text = models.TextField('Column text')
    text1 = models.TextField('Column text1')
    onecolumnurl = models.URLField('Column url', max_length = 200)
    about = models.TextField("Detals")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HomeThreecolumns'
        verbose_name_plural = 'HomeThreecolumns'

class Category(models.Model):
    image = models.ImageField('Category image', upload_to = 'media')
    title = models.CharField('Category name', max_length=30)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

class Product(models.Model):
    image = models.ImageField('Product image', upload_to = 'media')
    title = models.CharField('Product name', max_length=30)

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Productc'

class Callus(models.Model):
    image = models.ImageField('Product image', upload_to = 'media')
    title = models.CharField('Product name', max_length=30)
    tell = models.CharField('Tell number', max_length=30)
    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Callus'
        verbose_name_plural = 'Callus'
class CarModel(models.Model):
    image = models.ImageField('CarModel image', upload_to = 'media')
    title = models.TextField('CarModel about')
    price = models.CharField('CarModel price', max_length=30)
    imgpng = models.ImageField('ADD image', upload_to = 'media')

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'CarModel'
        verbose_name_plural = 'CarModels'