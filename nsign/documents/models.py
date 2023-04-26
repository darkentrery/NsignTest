from django.db import models

from django.utils.translation import gettext_lazy as _


class Document(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        version = ""
        if self.versions.exists():
            version = f" - {self.versions.last().version}"
        return f"{self.name}{version}"

    @property
    def last_version(self):
        version = ""
        if self.versions.exists():
            version = self.versions.last().version
        return version


class Version(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="versions")
    version = models.PositiveIntegerField(_("Version"), default=1, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versions"

    def __str__(self):
        return f"{self.document.name} - {self.version}"
