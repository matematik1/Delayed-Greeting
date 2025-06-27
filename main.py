import sys
import random
from collections import deque

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QSpacerItem, \
    QSizePolicy
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QPoint, QEasingCurve, pyqtProperty, QUrl
from PyQt5.Qt import QDesktopServices
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class ScrollWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setWindowTitle("Delayed Greeting")



        self._scroll_height = 50
        self.max_scroll_height = 460
        self.is_unfolded = False

        self.scroll_content = (
            "\nЗнаю що запізнився але Вітаю!\n"
            "Дорога матусю, в цей світлий день,\n"
            "Нехай душа співає, наче птах!\n"
            "Твоя любов – невичерпне джерело,\n"
            "В очах твоїх – і ніжність, і тепло.\n\n"
            "Ти – ангел мій, хранителька родинна,\n"
            "Твоє тепло – як сонячна година.\n"
            "Бажаю щастя, радості без краю,\n"
            "Здоров'я міцного, все інше – зачекає.\n\n"
            "Хай доля дарує лиш світлі миті,\n"
            "А серце буде сповнене надії.\n"
            "З Днем народження, матусю мила,\n"
            "Ти – найдорожча, ти – моя єдина!\n"
        )

        self.main_title = "❤️Вітаннячко для матусі💕"

        try:
            self.paper_texture = QPixmap('img/paper_texture.png')
            if self.paper_texture.isNull():
                raise FileNotFoundError("paper_texture.png not found or could not be loaded.")
        except FileNotFoundError as e:
            print(f"Помилка завантаження зображення паперу: {e}")
            print("Буде використано стандартний світло-жовтий колір паперу.")
            self.paper_texture = None

        try:
            self.background_image = QPixmap('img/background_image.png')
            if self.background_image.isNull():
                raise FileNotFoundError("background_image.png not found or could not be loaded.")
        except FileNotFoundError as e:
            print(f"Помилка завантаження фонового зображення: {e}")
            print("Буде використано стандартний світло-сірий колір фону.")
            self.background_image = None

        try:
            self.folded_scroll_image = QPixmap('img/folded_scroll.png')
            if self.folded_scroll_image.isNull():
                raise FileNotFoundError("folded_scroll.png not found or could not be loaded.")
        except FileNotFoundError as e:
            print(f"Помилка завантаження зображення згорнутого сувою: {e}")
            print("Згорнутий сувій буде відображатись як прямокутник.")
            self.folded_scroll_image = None

        self.animation = QPropertyAnimation(self, b"scrollHeight")
        self.animation.setDuration(1200)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.background_image:
            painter.drawPixmap(self.rect(), self.background_image)
        else:
            painter.fillRect(self.rect(), QColor(240, 240, 240))

        self.scroll_width = 480
        scroll_x = (self.width() - self.scroll_width) / 2
        scroll_y = 68

        painter.setPen(QPen(QColor("#E75480")))
        title_font = QFont("Times New Roman", 24)
        title_font.setBold(True)
        painter.setFont(title_font)

        title_rect = QRect(0, 10, self.width(), 60)
        painter.drawText(title_rect, Qt.AlignHCenter | Qt.AlignVCenter, self.main_title)

        if self._scroll_height <= 55 and self.folded_scroll_image:
            folded_rect = QRect(int(scroll_x), int(scroll_y), self.scroll_width, 50)
            painter.drawPixmap(folded_rect, self.folded_scroll_image)
        else:
            if self.paper_texture:
                target_rect = QRect(int(scroll_x), int(scroll_y), self.scroll_width, int(self._scroll_height))
                painter.drawPixmap(target_rect, self.paper_texture)
            else:
                painter.setBrush(QBrush(QColor(255, 255, 220)))
                painter.setPen(Qt.NoPen)
                painter.drawRect(int(scroll_x), int(scroll_y), self.scroll_width, int(self._scroll_height))

        if self._scroll_height > self.max_scroll_height * 0.7:
            painter.setPen(QPen(Qt.black))

            font = QFont("Arial", 14)
            font.setBold(True)
            painter.setFont(font)

            # Пересуваємо текст на 20 вправо та на 9 вгору
            # text_margin_x збільшено на 20 (початково 20 -> 40)
            # text_margin_y зменшено на 9 (початково 40 -> 31)
            text_margin_x = 40
            text_margin_y = 31

            text_rect = QRect(int(scroll_x + text_margin_x), int(scroll_y + text_margin_y),
                              self.scroll_width - 2 * text_margin_x,
                              int(self._scroll_height - 2 * text_margin_y))

            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignLeft | Qt.TextWordWrap,
                             self.scroll_content)

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
        self.animation.setEndValue(50)
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
        self.setWindowTitle("Delayed Greeting")
        self.setFixedSize(600, 600)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll_widget = ScrollWidget()
        main_layout.addWidget(self.scroll_widget)

        main_layout.addStretch(1)

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 10, 8)
        buttons_layout.setSpacing(10)

        buttons_layout.addSpacing(31)

        self.emoji_label = QLabel("💕❤️😍😘😍❤️💕")
        emoji_font = QFont("Arial", 16)
        self.emoji_label.setFont(emoji_font)
        self.emoji_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        buttons_layout.addWidget(self.emoji_label)

        buttons_layout.addStretch(1)

        self.music_btn = QPushButton("Музика💕")
        self.music_btn.setFixedSize(80, 50)
        self.music_btn.clicked.connect(self._toggle_music)
        buttons_layout.addWidget(self.music_btn)

        buttons_layout.addStretch(1)

        self.btn1 = QPushButton()
        self.btn1.setFixedSize(50, 50)
        try:
            icon1 = QIcon('img/pres1.png')
            self.btn1.setIcon(icon1)
            self.btn1.setIconSize(self.btn1.size())
        except Exception as e:
            print(f"Помилка завантаження pres1.png: {e}")
            self.btn1.setText("B1")
        self.btn1.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(
            "mailto:shmitayura@gmail.com")))
        buttons_layout.addWidget(self.btn1)

        self.btn2 = QPushButton()
        self.btn2.setFixedSize(50, 50)
        try:
            icon2 = QIcon('img/pres2.png')
            self.btn2.setIcon(icon2)
            self.btn2.setIconSize(self.btn2.size())
        except Exception as e:
            print(f"Помилка завантаження pres2.png: {e}")
            self.btn2.setText("B2")
        self.btn2.clicked.connect(lambda: QDesktopServices.openUrl(
            QUrl("https://t.me/yurch1ks")))
        buttons_layout.addWidget(self.btn2)

        self.btn3 = QPushButton()
        self.btn3.setFixedSize(50, 50)
        try:
            icon3 = QIcon('img/pres3.png')
            self.btn3.setIcon(icon3)
            self.btn3.setIconSize(self.btn3.size())
        except Exception as e:
            print(f"Помилка завантаження pres3.png: {e}")
            self.btn3.setText("B3")
        self.btn3.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/matematik1")))
        buttons_layout.addWidget(self.btn3)

        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

        self.media_player = QMediaPlayer(self)
        self.music_files = [f'music/({i}).mp3' for i in range(1, 10)]
        self.current_playlist = deque()
        self._shuffle_playlist()

        self.media_player.mediaStatusChanged.connect(self._handle_media_status_changed)

    def _shuffle_playlist(self):
        temp_list = list(self.music_files)
        random.shuffle(temp_list)
        self.current_playlist = deque(temp_list)
        print("Список відтворення перемішано.")

    def _play_next_song(self):
        if not self.current_playlist:
            self._shuffle_playlist()
            if not self.current_playlist:
                print("Немає музичних файлів для відтворення.")
                self.media_player.stop()
                return

        song_path = self.current_playlist.popleft()

        import os
        if not os.path.exists(song_path):
            print(f"Файл не знайдено: {song_path}. Пропускаю і спробую наступний.")
            self._play_next_song()
            return

        media_content = QMediaContent(QUrl.fromLocalFile(song_path))
        self.media_player.setMedia(media_content)
        self.media_player.play()
        print(f"Відтворення: {song_path}")

    def _toggle_music(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            print("Музика відтворюється, перемикаю пісню...")
            self.media_player.stop()
            self._play_next_song()
        else:
            print("Музика зупинена, починаю відтворення...")
            self._play_next_song()

    def _handle_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            print("Поточна пісня закінчилася, відтворюю наступну...")
            self._play_next_song()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        app_icon = QIcon('img/icon.ico')
        if app_icon.isNull():
            raise FileNotFoundError("icon.ico not found or could not be loaded.")
        app.setWindowIcon(app_icon)

    except FileNotFoundError as e:
        print(f"Помилка завантаження іконки програми: {e}")
        print("Іконка програми не буде встановлена. Будь ласка, переконайтеся, що 'icon.ico' існує.")
    except Exception as e:
        print(f"Невідома помилка при завантаженні іконки програми: {e}")
        print("Іконка програми не буде встановлена.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
