from django import forms
from django.contrib.formtools.wizard import FormWizard
from django.shortcuts import render_to_response
from django.template.context import RequestContext


class StepOne(forms.Form):
    message_one = forms.CharField(max_length=100)


class StepTwo(forms.Form):
    message_two = forms.CharField(max_length=100)


class StepThree(forms.Form):
    message_three = forms.CharField(max_length=100)


class StepFour(forms.Form):
    message_four = forms.CharField(max_length=100)


class StepFive(forms.Form):
    message_five = forms.CharField(max_length=100)


class DemoWizard(FormWizard):

    def get_template(self, step):
        return 'formtools/demowizard.html'

    def process_step(self, request, form, step):
        ## This runs on *every form so far* on *every request*!
        print 'Step', step
        if form.is_valid():
            if not hasattr(self, 'state'):
                self.state = {}
            self.state.update(form.cleaned_data)
            print self.state

    def done(self, request, form_list):
        formdata = {}
        for form in form_list:
            formdata.update(form.cleaned_data)
        return render_to_response('formtools/demowizard_done.html', 
                                  {'formdata': formdata}, 
                                  context_instance=RequestContext(request)) 
