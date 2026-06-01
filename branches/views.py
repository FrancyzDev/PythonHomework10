from django.shortcuts import render
from django.views import View

def branches_list(request):
    branches_data = [
        {'name': 'La Foode Центр', 'address': 'вул. Хрещатик, 15', 'phone': '+38 (044) 123-45-67'},
        {'name': 'La Foode Лівий берег', 'address': 'бул. Перова, 23', 'phone': '+38 (044) 987-65-43'},
        {'name': 'La Foode Оболонь', 'address': 'пр-т Степана Бандери, 12', 'phone': '+38 (044) 456-78-90'},
    ]
    return render(request, 'branches_list.html', {'branches': branches_data})

class BranchesDetailView(View):
    def get(self, request, branch_id):
        branches_dict = {
            1: {'name': 'La Foode Центр', 'address': 'вул. Хрещатик, 15', 
                'phone': '+38 (044) 123-45-67', 'work_hours': '10:00 - 22:00', 
                'special': '🔴 Провідний заклад, жива музика щоп\'ятниці'},
            2: {'name': 'La Foode Лівий берег', 'address': 'бул. Перова, 23', 
                'phone': '+38 (044) 987-65-43', 'work_hours': '11:00 - 23:00',
                'special': '🟠 Затишна тераса та дитяча кімната'},
            3: {'name': 'La Foode Оболонь', 'address': 'пр-т Степана Бандери, 12', 
                'phone': '+38 (044) 456-78-90', 'work_hours': '09:00 - 21:00',
                'special': '🔵 Сніданки до 12:00 та бізнес-ланчі'},
        }
        
        branch = branches_dict.get(branch_id)
        if not branch:
            return render(request, '404.html', {'message': 'Філію не знайдено'}, status=404)
        
        return render(request, 'branches_detail.html', {'branch': branch, 'branch_id': branch_id})