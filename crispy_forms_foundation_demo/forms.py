from django import forms
from django.utils.translation import ugettext_lazy as _

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, Row, Column, HTML, ButtonHolder, ButtonHolderPanel, ButtonGroup, Panel, Button, Submit, InlineField, InlineJustifiedField, SwitchField

SELECT_INPUT_CHOICES = [('item-{0}'.format(i), 'Option item {0}'.format(i)) for i in range(1, 6)]
RADIO_INPUT_CHOICES = [('item-{0}'.format(i), 'Radio item {0}'.format(i)) for i in range(1, 4)]

class BaseForm(forms.Form):
    """
    Base form with inputs
    """
    full_input = forms.CharField(label=_('Full width input'), required=True)
    column_input_1 = forms.CharField(label=_('Column input 1'), required=False)
    column_input_2 = forms.CharField(label=_('Column input 2'), required=True)
    column_input_3 = forms.CharField(label=_('Column input 3'), required=False)
    textarea_input = forms.CharField(label=_('Textarea'), widget=forms.Textarea(attrs={'rows':5, 'required':''}), required=True)
    select_input = forms.ChoiceField(label=_('Select input'), choices=SELECT_INPUT_CHOICES, required=True)
    radio_input = forms.ChoiceField(label=_('Radio inputs'), choices=RADIO_INPUT_CHOICES, widget=forms.RadioSelect, required=False)
    checkbox_input = forms.BooleanField(label=_('Checkbox input'), required=False)
    checkbox_switch_input = forms.BooleanField(label=_('Checkbox switch'), required=False)
    inlinefield_input = forms.CharField(label=_('Inline field'), required=False)
    inlinejustifiedfield_input = forms.CharField(label=_('Inline justified field'), required=False)
    
    def clean(self):
        cleaned_data = super(BaseForm, self).clean()
        checkbox_input = cleaned_data.get("checkbox_input")

        if checkbox_input and checkbox_input == True:
            raise forms.ValidationError(['This is a global error', 'This is another global error', 'Uncheck the "Checkbox input" to ignore these errors'])

        # Always return the full collection of cleaned data.
        return cleaned_data

    def save(self, commit=True):
        # Do nothing
        return
    

class Foundation5Form(BaseForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Fieldset(
                _('Part 1'),
                Row(
                    Column('full_input'),
                ),
                Row(
                    Column(
                        Row(
                            Column(
                                'column_input_1',
                                css_class='large-4'
                            ),
                            Column(
                                'column_input_2',
                                css_class='large-4'
                            ),
                            Column(
                                'column_input_3',
                                css_class='large-4'
                            ),
                        )
                    ),
                ),
            ),
            Fieldset(
                _('Part 2'),
                Row(
                    Column(
                        'select_input',
                        css_class='large-12'
                    ),
                ),
                Row(
                    Column(
                        'radio_input',
                        css_class='large-4'
                    ),
                    Column(
                        'checkbox_input',
                        css_class='large-4'
                    ),
                    Column(
                        Row(
                            Column(
                                SwitchField('checkbox_switch_input', switch_class="round tiny"),
                                css_class='small-3'
                            ),
                            Column(
                                HTML('<label>Checkbox with a switch field</label>'),
                                css_class='small-9'
                            ),
                        ),
                        css_class='large-4'
                    ),
                ),
            ),
            Fieldset(
                _('Part 3'),
                Row(
                    Column('textarea_input'),
                ),
            ),
            Fieldset(
                _('Part 4'),
                InlineField('inlinefield_input'),
                InlineJustifiedField('inlinejustifiedfield_input'),
            ),
            Row(
                Column(
                    ButtonHolder( Submit('submit', _('ButtonHolder Submit')))
                ),
            ),
            Row(
                Column(
                    ButtonHolderPanel( Submit('submit', _('ButtonHolderPanel Submit')), css_class='text-right' )
                ),
            ),
            Row(
                Column(
                    ButtonGroup(
                        Submit('submit', _('Submit'), css_class='success'),
                        Button('cancel', _('Cancel')),
                        Button('dummy', _('Delete'), css_class='alert'),
                        css_class='radius right'
                    ),
                    css_class='clearfix'
                ),
            ),
            Row(
                Column(
                    Panel(
                        ButtonGroup(
                            Submit('submit', _('Submit'), css_class='success'),
                            Button('cancel', _('Cancel')),
                            Button('dummy', _('Delete'), css_class='alert'),
                            css_class='radius right'
                        ),
                        css_class='clearfix'
                    )
                ),
            ),
        )
        
        super(Foundation5Form, self).__init__(*args, **kwargs)
