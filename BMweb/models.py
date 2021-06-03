from django.db import models
from django.utils.translation import ugettext_lazy as _

class Hereglegch(models.Model):
    name=models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн нэр"))
    code=models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн нэр"))

    class Meta:
        verbose_name = _("Хэрэглэгч")
        verbose_name_plural = _("Хэрэглэгч")

    def __str__(self):
        return self.name