import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QPixmap, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QPoint, QEasingCurve, pyqtProperty


class ScrollWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(500, 600)
        self.setMaximumSize(500, 600)
        self.setWindowTitle("Розгорнутий Світ")

        self._scroll_height = 80
        self.max_scroll_height = 500
        self.is_unfolded = False

        # Ваш текст для сувою
        self.scroll_content = (
            "Ласкаво просимо до Стародавніх Сувоїв!\n\n"
            "Тут містяться мудрість та знання віків, "
            "передані нам від наших предків. "
            "Кожен символ, кожне слово оповідає історію, "
            "розкриває таємниці світу та вказує шлях "
            "до істини.\n\n"
            "Нехай цей сувій стане для вас джерелом натхнення "
            "та провідником у пошуках знань. "
            "Читайте уважно і відкривайте для себе нові горизонти."
        )

        try:
            self.paper_texture = QPixmap('img/paper_texture.png')
            if self.paper_texture.isNull():
                raise FileNotFoundError("paper_texture.png not found or could not be loaded.")
        except FileNotFoundError as e:
            print(f"Помилка завантаження зображення: {e}")
            print("Буде використано стандартний світло-жовтий колір паперу.")
            self.paper_texture = None

        self.animation = QPropertyAnimation(self, b"scrollHeight")
        self.animation.setDuration(1200)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), QColor(240, 240, 240))

        self.scroll_width = 400
        scroll_x = (self.width() - self.scroll_width) / 2 - 20
        scroll_y = (self.height() - self._scroll_height) / 2 - 50

        if self.paper_texture:
            target_rect = QRect(int(scroll_x), int(scroll_y), self.scroll_width, int(self._scroll_height))
            painter.drawPixmap(target_rect, self.paper_texture)
        else:
            painter.setBrush(QBrush(QColor(255, 255, 220)))
            painter.setPen(Qt.NoPen)
            painter.drawRect(int(scroll_x), int(scroll_y), self.scroll_width, int(self._scroll_height))

        roll_color = QColor(180, 150, 100)
        roll_thickness = 20

        painter.setBrush(QBrush(roll_color))
        painter.drawRoundedRect(int(scroll_x), int(scroll_y), self.scroll_width, roll_thickness, 8, 8)

        if self._scroll_height < self.max_scroll_height - roll_thickness:
            painter.drawRoundedRect(int(scroll_x), int(scroll_y + self._scroll_height - roll_thickness),
                                    self.scroll_width, roll_thickness, 8, 8)

        # Додавання та форматування тексту
        if self._scroll_height > self.max_scroll_height * 0.7:
            painter.setPen(QPen(Qt.black))  # Колір тексту

            font = QFont("Arial", 14)  # Створюємо об'єкт QFont
            font.setBold(True)  # Робимо текст жирним
            painter.setFont(font)  # Встановлюємо шрифт для художника

            # Область для тексту
            text_margin_x = 30  # Відступ від лівого/правого краю сувою
            text_margin_y = 30 + roll_thickness  # Відступ від верхнього краю (з урахуванням згорнутої частини)

            text_rect = QRect(int(scroll_x + text_margin_x), int(scroll_y + text_margin_y),
                              self.scroll_width - 2 * text_margin_x,
                              int(self._scroll_height - 2 * text_margin_y))

            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignHCenter | Qt.TextWordWrap,
                             self.scroll_content)  # Малюємо наш текст

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self.is_unfolded:
                self.start_unfold_animation()
            else:
                self.start_fold_animation()

    def start_unfold_animation(self):
        self.animation.setStartValue(self._scroll_height)
        self.animation.setEndValue(self.max_scroll_height)
        self.animation.start()
        self.is_unfolded = True

    def start_fold_animation(self):
        self.animation.setStartValue(self._scroll_height)
        self.animation.setEndValue(80)  # Згортаємо до початкової висоти
        self.animation.start()
        self.is_unfolded = False

    @pyqtProperty(int)
    def scrollHeight(self):
        return self._scroll_height

    @scrollHeight.setter
    def scrollHeight(self, value):
        self._scroll_height = value
        self.update()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Програма з Розгорнутим Сувоєм")
        self.setGeometry(100, 100, 500, 600)

        layout = QVBoxLayout()
        self.scroll_widget = ScrollWidget()
        layout.addWidget(self.scroll_widget)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())