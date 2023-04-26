from django.contrib import admin

from nsign.documents.models import Document, Version


class VersionInline(admin.TabularInline):
    model = Version
    extra = 0
    fields = [
        "name",
        "description",
        "version",
    ]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
    ]
    actions = [VersionInline,]


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "version",
        "document",
    ]
