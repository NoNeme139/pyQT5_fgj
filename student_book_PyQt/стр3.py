import sys
from PyQt5.QtWidgets import QApplication, QWidget  # импрорт необходимых модулей

if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание объекта приложения, Sys.argv - список аргументов из cmd
    window = QWidget()  # основной класс всех объектов интерф. PyQt5, поумолч без родителя, виджет без родителя - окно
    window.resize(250, 150)  # размеры окна (ширина, высота)
    window.move(300, 300)  # перемещение виджета на позицию (x,y)
    window.setWindowTitle("Simple")  # Заголовок окна
    window.show()  # отображение виджета на экране
    sys.exit(app.exec_())  # цикл завершается, если вызывается метод exit() или главное окно было закрыто
    # метод sys.exit() - гарантирует чистый выход
