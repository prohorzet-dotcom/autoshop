import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autoshop.settings')
django.setup()
from store.models import Category, Product
data = [
    ('Масляный фильтр Mann W712/75', 'Двигатель', 'dvigatel', 'Фильтр масляный для BMW, VW, Audi', 850, 15),
    ('Воздушный фильтр Bosch S0226', 'Двигатель', 'dvigatel', 'Воздушный фильтр для Ford, Opel', 650, 20),
    ('Свечи зажигания NGK BKR6E', 'Двигатель', 'dvigatel', 'Комплект 4 шт.', 1200, 30),
    ('Ремень ГРМ Gates K015559XS', 'Двигатель', 'dvigatel', 'Комплект ремня ГРМ с роликами', 4500, 8),
    ('Тормозные колодки Brembo P06020', 'Тормоза', 'tormoza', 'Передние колодки VW Golf', 2400, 12),
    ('Тормозные диски TRW DF4075', 'Тормоза', 'tormoza', 'Передние диски Opel Astra', 3200, 6),
    ('Тормозная жидкость ATE DOT4', 'Тормоза', 'tormoza', 'Тормозная жидкость 1 литр', 450, 25),
    ('Амортизатор Sachs 310 523', 'Подвеска', 'podveska', 'Передний амортизатор VW Passat', 3800, 10),
    ('Стойка стабилизатора Lemforder', 'Подвеска', 'podveska', 'Передняя стойка BMW 3 серия', 950, 18),
    ('Аккумулятор Varta 60Ah', 'Электрика', 'elektrika', 'Аккумулятор 60 Ah 540A', 6500, 7),
    ('Лампа H7 Osram Night Breaker', 'Электрика', 'elektrika', 'Галогенная лампа H7 2 шт', 850, 35),
    ('Фильтр салона Mann CU2131', 'Фильтры', 'filtry', 'Салонный фильтр VW Golf, Audi A3', 550, 22),
    ('Топливный фильтр Knecht KL147', 'Фильтры', 'filtry', 'Топливный фильтр дизель', 980, 16),
    ('Масло Castrol Edge 5W-30', 'Масла', 'masla', 'Синтетическое моторное масло 4л', 3200, 20),
    ('Масло Shell Helix Ultra 5W-40', 'Масла', 'masla', 'Полностью синтетическое масло 4л', 2900, 18),
    ('Антифриз Liqui Moly KFS', 'Масла', 'masla', 'Антифриз готовый -40C 5л', 1400, 25),
]
for name, cat_name, slug, desc, price, stock in data:
    cat, _ = Category.objects.get_or_create(name=cat_name, defaults={'slug': slug})
    Product.objects.get_or_create(name=name, defaults={'category': cat, 'description': desc, 'price': price, 'stock': stock})
print('Готово! Товаров:', Product.objects.count())