from rest_framework.routers import SimpleRouter

from zoo.api.v1.views.animal import AnimalView
from zoo.api.v1.views.about import AboutView
from zoo.api.v1.views.category import CategoryView
from zoo.api.v1.views.country import CountryView
from zoo.api.v1.views.faq import FAQView
from zoo.api.v1.views.workers import WorkersView


router = SimpleRouter()

router.register('animal/', AnimalView, basename='animal')
router.register('about/', AboutView, basename='about')
router.register('category/', CategoryView, basename='category')
router.register('country/', CountryView, basename='country')
router.register('faq/', FAQView, basename='faq')
router.register('workers/',WorkersView, basename='service')

urlpatterns = router.urls