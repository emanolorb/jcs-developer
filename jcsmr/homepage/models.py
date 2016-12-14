from django.db import models


class HomePageImage(models.Model):
    main_icon = models.ImageField()
    paralax_image1 = models.ImageField()
    paralax_image2 = models.ImageField()

    def save(self, *args, **kwargs):
        HomePageImage.objects.filter().delete()
        super(HomePageImage, self).save(*args, **kwargs)
        HomePageImage.objects.filter().update(id=1)

    def __str__(self):
        return '%s' % ('initial template')


class HomePageSlider(models.Model):
    slider_image = models.ImageField()
    big_tag_line = models.TextField()
    color_big_tag = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    small_slogan = models.TextField()
    color_small_tag = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    aligned_caption = models.CharField(
        max_length=10,
        choices=(('c', 'center'), ('l', 'left'), ('r', 'right')),)

    def __str__(self):
        return '%s - %s' % (self.id, self.big_tag_line)


class HomePageText(models.Model):
    title = models.CharField(max_length=80)
    color_title = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    subtitle = models.TextField()
    color_small_tag = models.CharField(
        max_length=10,
        choices=(('lighten-5', 'white'), ('darken-1', 'grey'), ('darken-4', 'black')))
    blank_panel_title = models.CharField(max_length = 80)
    blank_panel_text = models.TextField()
    blank_panel_title2 = models.CharField(max_length = 80)
    blank_panel_text_2 = models.TextField()

    def save(self, *args, **kwargs):
        HomePageText.objects.filter().delete()
        super(HomePageText, self).save(*args, **kwargs)
        HomePageText.objects.filter().update(id=1)

    def __str__(self):
        return '%s - %s' % ('Initial text template', self.title)
