from django.views import View
from django.shortcuts import render
from django.http import Http404

class NewsView(View):
    def get(self, request):
        news_items = {
            1: {
                'id': 1,
                'title': '🗞️ 12 травня — нове літнє меню',
                'description': 'Додали чотири позиції: тартар з лосося, холодний томатний суп, лимонад із базиліком та чилі-брауні. Встигніть спробувати!',
                'badge': '🔥 Акція: дегустаційний сет зі знижкою 20%',
                'full_text': 'Цього літа ми підготували для вас особливе меню. Шеф-кухар La Foode презентує нові страви, які підкорять ваші смакові рецептори.'
            },
            2: {
                'id': 2,
                'title': '📸 Конкурс у Instagram',
                'description': 'Виграй вечерю на двох. Зроби фото страви La Foode, познач нас — @lafoode.ua. Переможця обираємо щопонеділка.',
                'badge': 'Новина',
                'full_text': 'Умови конкурсу: 1. Підпишись на наш Instagram. 2. Зроби фото будь-якої страви в La Foode.'
            },
            3: {
                'id': 3,
                'title': '🍷 Дегустація вин',
                'description': 'Щоп\'ятниці о 19:00 проводимо дегустацію вин. Вартість участі 350 грн.',
                'badge': 'Анонс',
                'full_text': 'Запрошуємо на дегустацію вин від провідних виноробів України та Італії.'
            },
        }
        
        context = {
            'title': 'Новини La Foode',
            'news_items': news_items
        }
        
        return render(request, 'news.html', context)


class NewsDetailView(View):
    def get(self, request, news_id):
        if request.path != f'/news/{news_id}/':
            raise Http404("Сторінку в розділі Новини не знайдено")
        
        news_dict = {
            1: {
                'id': 1,
                'title': '🗞️ 12 травня — нове літнє меню',
                'description': 'Додали чотири позиції: тартар з лосося, холодний томатний суп, лимонад із базиліком та чилі-брауні. Встигніть спробувати!',
                'badge': '🔥 Акція: дегустаційний сет зі знижкою 20%',
                'full_text': 'Цього літа ми підготували для вас особливе меню. Шеф-кухар La Foode презентує нові страви, які підкорять ваші смакові рецептори.'
            },
            2: {
                'id': 2,
                'title': '📸 Конкурс у Instagram',
                'description': 'Виграй вечерю на двох. Зроби фото страви La Foode, познач нас — @lafoode.ua. Переможця обираємо щопонеділка.',
                'badge': 'Новина',
                'full_text': 'Умови конкурсу: 1. Підпишись на наш Instagram. 2. Зроби фото будь-якої страви в La Foode.'
            },
            3: {
                'id': 3,
                'title': '🍷 Дегустація вин',
                'description': 'Щоп\'ятниці о 19:00 проводимо дегустацію вин. Вартість участі 350 грн.',
                'badge': 'Анонс',
                'full_text': 'Запрошуємо на дегустацію вин від провідних виноробів України та Італії.'
            },
        }
        
        news = news_dict.get(news_id)
        if not news:
            raise Http404("Сторінку в розділі Новини не знайдено")
        
        return render(request, 'news_detail.html', {'news': news, 'news_id': news_id})