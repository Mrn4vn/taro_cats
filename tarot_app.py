from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Данные карт Таро
CARDS_DATA = [
    {'id': 1, "title": "Смерть", "description": "Каждая смерть это реинкарнация.", 'img': '/static/cards/taro1.jpg'},
    {'id': 2, "title": "Башня", "description": "У каждого верха есть низ.", 'img': '/static/cards/taro2.jpg'},
    {'id': 3, "title": "Королева", "description": "Лишь только шоу должно продолжаться.", 'img': '/static/cards/taro3.jpg'},
    {"id": 4, "title": "Отшельник", "description": "А нужен ли ты тут?", 'img': '/static/cards/taro4.jpg'},
    {"id": 5, "title": "Дурак", "description": "Твоя слава всегда с тобой.", 'img': '/static/cards/taro5.jpg'},
    {"id": 6, "title": "Маг", "description": "Кастуй касты, копи ману.", 'img': '/static/cards/taro6.jpg'},
    {"id": 7, "title": "Любовники", "description": "Она, всё таки, существует.", 'img': '/static/cards/taro7.jpg'},
    {"id": 8, "title": "Повозка", "description": "Не пора ли катить отсюда?", 'img': '/static/cards/taro8.jpg'},
    {"id": 9, "title": "Удача", "description": "Ах, ты, ловкач!", 'img': '/static/cards/taro9.jpg'},
    {"id": 10, "title": "Судья", "description": "Плати или расплачивайся.", 'img': '/static/cards/taro10.jpg'},
    {"id": 11, "title": "Встас", "description": "А, это Встас, всё ок.", 'img': '/static/cards/taro11.png'},
    {"id": 12, "title": "Луна", "description": "Луна даже себе не верна.", 'img': '/static/cards/taro12.jpg'},
    {"id": 13, "title": "Меч", "description": "Или сдавайся, или сражайся.", 'img': '/static/cards/taro13.jpg'},
    {"id": 14, "title": "Поп", "description": "Прибирайтесь и будет порядок.", 'img': '/static/cards/taro14.jpg'}
]

@app.route('/')
def index():
    return render_template('index.html')  # Рендерим HTML-шаблон

@app.route('/api/draw', methods=['GET'])
def api_draw():
    return jsonify(random.sample(CARDS_DATA, 3))  # Возвращаем 3 случайные карты

if __name__ == "__main__":
    app.run(debug=True)
