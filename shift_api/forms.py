# from django import forms
# from .models import User, Task, Habit, Template, Team, TeamTask
# import bcrypt
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'phone', 'date_of_birth', 'permissions']
    
#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if password:
#             return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#         raise forms.ValidationError("كلمة المرور مطلوبة")

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['user_id', 'task_name', 'start_time', 'end_time']

# class HabitForm(forms.ModelForm):
#     class Meta:
#         model = Habit
#         fields = ['user_id', 'habit_name', 'frequency', 'start_time', 'end_time']

# class TemplateForm(forms.ModelForm):
#     class Meta:
#         model = Template
#         fields = ['template_name', 'description', 'user_id']

# class TeamForm(forms.ModelForm):
#     class Meta:
#         model = Team
#         fields = ['team_name', 'goal', 'manager_id']

# class TeamTaskForm(forms.ModelForm):
#     class Meta:
#         model = TeamTask
#         fields = ['team_id', 'task_name', 'description', 'start_time', 'end_time']