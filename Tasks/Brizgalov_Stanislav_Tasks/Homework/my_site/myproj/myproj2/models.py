from django.db import models


class Post1(models.Model):

    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бензопилы"
        verbose_name_plural = "Бензопилы"


class Post2(models.Model):

    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бензобуры"
        verbose_name_plural = "Бензобуры"


class Post3(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                 decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бензорезы"
        verbose_name_plural = "Бензорезы"


class Post4(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                 decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Бетономешалки"
        verbose_name_plural = "Бетономешалки"


class Post5(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                 decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Болгарки"
        verbose_name_plural = "Болгарки"


class Post6(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                 decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Генераторы"
        verbose_name_plural = "Генераторы"


class Post7(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                 decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Лестницы"
        verbose_name_plural = "Лестницы"


class Post8(models.Model):
    title = models.CharField('Заголовок', max_length=100, blank=False, )
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                 decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Миксеры"
        verbose_name_plural = "Миксеры"

