
from django import forms
from tasks.models import Task,TaskDetail

  #django form

class TaskFrom(forms.Form):
    title=forms.CharField(max_length=250,label="Task Title")
    description=forms.CharField(widget=forms.Textarea,label="task description")
    due_date=forms.DateField(widget=forms.SelectDateWidget,label="Due date")
    
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES,label="Gender")
    assigned_to=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)


    def __init__(self, *args, **kwargs):
        # print(args,kwargs)
        employees=kwargs.pop("employees", [])
        print("pop korer por",employees)
        super().__init__(*args, **kwargs)
        self.fields["assigned_to"].choices=[(emp.id,emp.name) for emp in employees]

"""starting to the Mixing apply style to form field"""
class StyleForMixin:
    default_classes="border-2  border-gray-300 w-full rounded-full shadow-2xl text-center"
    description_classes="border-2  border-gray-300 w-full h-40 rounded-sm shadow-2xl text-center"
    
    def apply_style_widgets(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f"Enter {field.label.lower()}"
                    
                })
            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':self.description_classes,
                    'placeholder':f"Enter {field.label.lower()}" 

                })
            elif isinstance(field.widget,forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f"Enter {field.label.lower()}"
                })

                # gender choice 
            # elif isinstance(field.widget,forms.Select):
            #     field.widget.attrs.update({
            #         'class':self.default_classes,
            #         'placeholder':f"Enter {field.label.lower()}"
                
            #     })


            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class':"space-y-2"
                    

                })






# django model form

class TaskModelForm(StyleForMixin,forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','due_date','assigned_to']
        widgets = {
            'due_date':forms.SelectDateWidget(),
            'assigned_to':forms.CheckboxSelectMultiple,
            # 'gender':forms.ChoiceField

        }
        # exclude=['title','description']

        
        
        """manully widget """
        # #display date authomaticaly korte


        # widgets = {
        #     'title':forms.TextInput(attrs={
        #         'class':"border-2  border-gray-300 w-full rounded-full shadow-2xl text-center",
        #     'placeholder':"enter your title"
        #     }),
        #     'description':forms.TextInput(attrs={
        #      'class':"border-2  border-red-300 w-full rounded-sm shadow-2xl text-center w-100 h-30",
        #     'placeholder':"enter your descriptions"
        #     }),
            
        #     'due_date': forms.SelectDateWidget(attrs={
        #     'class':"border-2  border-gray-300  rounded-sm shadow-2xl text-center"
            
        #     }),
        #     'assigned_to':forms.CheckboxSelectMultiple
        # }
    """using mixing widget"""  
    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        self.apply_style_widgets()





class TaskDetailModelform(StyleForMixin,forms.ModelForm):
    class Meta:
        model=TaskDetail
        fields=['priority','notes']
    
    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        self.apply_style_widgets()

    