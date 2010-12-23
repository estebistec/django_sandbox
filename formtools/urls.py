from django.conf.urls.defaults import patterns, url
from forms import DemoWizard
from forms import StepOne
from forms import StepTwo
from forms import StepThree
from forms import StepFour
from forms import StepFive


urlpatterns = patterns('',
    url(r'^/?$', 'django.views.generic.simple.direct_to_template', {'template': 'formtools/index.html'}, name="formtools-index"),
    url(r'^/form-wizard/?$', DemoWizard([StepOne, StepTwo, StepThree, StepFour, StepFive]), name='form-wizard'),
)
