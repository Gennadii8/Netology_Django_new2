from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        selected_topics = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                selected_topics += 1
        if selected_topics == 0:
            raise ValidationError('Необходимо указать основной раздел статьи')
        if selected_topics > 1:
            raise ValidationError('Основной раздел может быть только один')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
