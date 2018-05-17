# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'entities', views.EntityViewSet)
router.register(r'phrases', views.PhraseViewSet)
router.register(r'phrase_entities', views.PhraseEntityViewSet)


app_name = 'ner_trainer'
urlpatterns = [
    url(r'^', include(router.urls)),
]
