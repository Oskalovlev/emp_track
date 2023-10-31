from django import forms

from .models import Resume, Experience, Education


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            "title",
            "candidate",
            "photo",
            "gender",
            "grade",
            "birthday",
            "city",
            "telegram",
            "portfolio",
            "about_me",
            "type_work",
            "status_finded",
        )
        help_text = {
            "title": "Заголовок",
            "candidate": "Кандидат",
            "photo": "Фото",
            "gender": "Пол",
            "grade": "Уровень",
            "birthday": "День рождения",
            "city": "Город",
            "telegram": "Телеграм",
            "portfolio": "Портфолио",
            "about_me": "Обо мне",
            "type_work": "Тип занятости",
            "status_finded": "Статус занятости",
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ("resume", "position", "period", "duties")
        help_text = {
            "resume": "Опыт",
            "position": "Должность",
            "period": "Период",
            "duties": "Обяханности",
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ("resume", "higher", "course")
        help_text = {
            "resume": "Образование",
            "higher": "Высшее образование",
            "course": "Дополнительное образование",
        }
