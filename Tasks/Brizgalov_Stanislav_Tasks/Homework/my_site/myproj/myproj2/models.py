from django.db import models


class Post(models.Model):

    title = models.CharField('Заголовок', max_length=100, blank=False)
    description = models.TextField('Описание', blank=False)
    image = models.ImageField('Картинка', upload_to='uploads')
    price = models.DecimalField('Стоимость за час, BLR', max_digits=10,
                                decimal_places=2, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"