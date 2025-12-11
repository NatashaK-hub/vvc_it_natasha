import sys
#импортируем классы PyQt: QApplication, QMainWindow, QPushButton - из модуля QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QWidget):
        def __init__(self):
            super().__init__() #конструктор родительского класса
            self.setWindowTitle("My App")
            self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

            # Создаем контейнеры (лейауты)
            main_layout = QVBoxLayout()  # Вертикальный контейнер
            # Виджеты
            self.text_edit = QTextEdit() #текстовое поле для ввода текста
            main_layout.addWidget(self.text_edit)#добавляем текстовое поле в контейнер

            self.button = QPushButton("Тыкай сюда для анализа текста")
            self.button.clicked.connect(self.analyze_text)#привязываем функцию analyze к нажатию кнопки
            main_layout.addWidget(self.button)

            self.label_1 = QLabel("Анализ вашего текста будет здесь")
            main_layout.addWidget(self.label_1)  # добавляем поля для результата в контейнер

            # Устанавливаем главный лейаут для окна
            self.setLayout(main_layout)

        def analyze_text(self):
            text=self.text_edit.toPlainText()#возвращает простой текст без форматирования
            chars=len(text)
            words=text.split(' ')
            word_count=len(words)
            space=text.count(" ")
            result=(
                f"Количество символов:{chars}\n"
                f"Количество слов:{word_count}\n"
                f"Количество пробелов:{space}"
            )
            self.label_1.setText(result)

#создаем экземпляр QApplication и передаем sys.argv (список Python с аргументами командной строки)
#создание приложения
app = QApplication(sys.argv)
#создание главного окна
window = MainWindow()
window.show()
#запуск главного цикла событий
sys.exit(app.exec())

