from pages.category_page import CategoryPage



class MacPage(CategoryPage):
    def __init__(self, driver):
        super().__init__(driver)


CATEGORIES = [
    'MacBook Pro',
    'MacBook Air',
    'MacBook Neo',
    'iMac',
    'Mac mini',
    'Mac Studio',
    'Apple Studio Display',
    'Клавиатуры',
    'Трекпады',
    'Мыши'
]


    ...