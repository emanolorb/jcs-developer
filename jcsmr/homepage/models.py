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
    small_slogan = models.TextField()
    aligned_caption = models.CharField(max_length=10, choices=(('c','center'), ('l','left'), ('r','right')))

    def __str__(self):
        return '%s - %s' % (self.id, self.big_tag_line)


class HomePageText(models.Model):
    title = models.CharField(max_length=80)
    subtitle = models.TextField()
