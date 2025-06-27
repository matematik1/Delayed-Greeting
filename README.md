[![Latest release]([https://img.shields.io/github/v/release/Delayed-Greeting?color=blue&style=flat-square](https://img.shields.io/badge/Release-click-labelColor=0000&logoColor=0eff0e))](https://github.com/matematik1/Delayed-Greeting/releases/latest)

# Delayed Greeting Application

This is a small PyQt5 application designed to deliver a "delayed" greeting in the form of an animated scroll. It features a customizable visual interface, background music playback, and quick links to contact information.

---

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Customization](#customization)
* [Contributing](#contributing)
* [License](#license)

---

## Features

* **Interactive Scroll:** Click to unfold and fold a digital scroll revealing a custom greeting message.
* **Animated Transitions:** Smooth unfolding and folding animations for the scroll.
* **Background Music:** Integrated music player with a shuffled playlist for an immersive experience.
* **Customizable Visuals:** Easily change background images, paper textures, and scroll graphics.
* **Contact Links:** Quick access buttons for email, Telegram, and GitHub profile.
* **Themed Design:** Sweet and warm color palette.

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/your-repo-name.git](https://github.com/YOUR_USERNAME/your-repo-name.git)
    cd your-repo-name
    ```
    *(Replace `YOUR_USERNAME` and `your-repo-name` with your actual GitHub username and repository name.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install PyQt5 PyQt5-QtMultimedia
    ```

---

## Usage

1.  **Prepare assets:**
    Ensure you have the following directories and files in the root of your project, or update the paths in the code:
    * `img/`:
        * `paper_texture.png` (optional, falls back to light yellow if not found)
        * `background_image.png` (optional, falls back to light gray if not found)
        * `folded_scroll.png` (optional, falls back to a rectangle if not found)
        * `icon.ico` (optional, application will run without an icon if not found)
        * `pres1.png`, `pres2.png`, `pres3.png` (optional, buttons will show text instead if not found)
    * `music/`:
        * `(1).mp3`, `(2).mp3`, ..., `(9).mp3` (or any `.mp3` files, named appropriately based on the code's expectation `music/({i}).mp3` for `i` from 1 to 9). The application will shuffle and play these.

2.  **Run the application:**
    ```bash
    python your_main_script_name.py
    ```
    *(If your main script is named something other than `your_main_script_name.py`, replace it accordingly, e.g., `main.py` or `app.py`)*

3.  **Interact:**
    * Click on the folded scroll to unfold it and reveal the message. Click again to fold it back.
    * Click the "**Музика💕**" (Music) button to start/stop or skip the current song.
    * Click the bottom-right buttons to open the associated links (email, Telegram, GitHub).

---

## Project Structure
.
├── img/

│   ├── background_image.png

│   ├── folded_scroll.png

│   ├── icon.ico

│   ├── paper_texture.png

│   ├── pres1.png

│   ├── pres2.png

│   └── pres3.png

├── music/

│   ├── (1).mp3

│   ├── (2).mp3

│   └── ... (up to (9).mp3 as per current code)

└── your_main_script_name.py  (e.g., main.py or app.py)


---

## Customization

* **Scroll Content:** Modify the `scroll_content` variable in the `ScrollWidget` class to change the greeting message.
* **Main Title:** Change the `main_title` variable in the `ScrollWidget` class.
* **Images:** Replace the `.png` files in the `img/` directory with your own custom images. Ensure they have the same names.
* **Music:** Add or remove `.mp3` files in the `music/` directory. If you change the naming convention or the number of files, you'll need to adjust the `music_files` list in the `MainWindow` class accordingly.
* **Contact Links:** Update the `QUrl` arguments for `self.btn1`, `self.btn2`, and `self.btn3` in the `MainWindow` class to point to your desired links.

---

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---
---

# Додаток "Запізніле Привітання"

Це невеличкий додаток на PyQt5, створений для доставки "запізнілого" привітання у вигляді анімованого сувою. Він має настроюваний візуальний інтерфейс, відтворення фонової музики та швидкі посилання на контактну інформацію.

---

## Зміст

* [Можливості](#можливості)
* [Встановлення](#встановлення)
* [Використання](#використання)
* [Структура Проекту](#структура-проекту)
* [Налаштування](#налаштування)
* [Участь у Розробці](#участь-у-розробці)
* [Ліцензія](#ліцензія)

---

## Можливості

* **Інтерактивний Сувій:** Натисніть, щоб розгорнути та згорнути цифровий сувій, що розкриває користувацьке привітання.
* **Анімовані Переходи:** Плавні анімації розгортання та згортання сувою.
* **Фонова Музика:** Вбудований музичний плеєр з перемішаним списком відтворення для занурення в атмосферу.
* **Настроювані Візуальні Елементи:** Легко змінюйте фонові зображення, текстури паперу та графіку сувою.
* **Контактні Посилання:** Кнопки швидкого доступу для електронної пошти, Telegram та профілю GitHub.
* **Тематичний Дизайн:** Приємна та тепла кольорова палітра.

---

## Встановлення

1.  **Клонуйте репозиторій:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/your-repo-name.git](https://github.com/YOUR_USERNAME/your-repo-name.git)
    cd your-repo-name
    ```
    *(Замініть `YOUR_USERNAME` та `your-repo-name` на ваш фактичний логін на GitHub та назву репозиторію.)*

2.  **Створіть віртуальне середовище (рекомендовано):**
    ```bash
    python -m venv venv
    # Для Windows
    venv\Scripts\activate
    # Для macOS/Linux
    source venv/bin/activate
    ```

3.  **Встановіть необхідні залежності:**
    ```bash
    pip install PyQt5 PyQt5-QtMultimedia
    ```

---

## Використання

1.  **Підготуйте ресурси:**
    Переконайтеся, що у вас є наступні каталоги та файли в корені вашого проекту, або оновіть шляхи у коді:
    * `img/`:
        * `paper_texture.png` (необов'язково, якщо не знайдено, буде використано світло-жовтий колір)
        * `background_image.png` (необов'язково, якщо не знайдено, буде використано світло-сірий колір)
        * `folded_scroll.png` (необов'язково, якщо не знайдено, сувій відображатиметься як прямокутник)
        * `icon.ico` (необов'язково, додаток запуститься без іконки, якщо її не знайдено)
        * `pres1.png`, `pres2.png`, `pres3.png` (необов'язково, кнопки показуватимуть текст, якщо їх не знайдено)
    * `music/`:
        * `(1).mp3`, `(2).mp3`, ..., `(9).mp3` (або будь-які файли `.mp3`, названі відповідно до очікування коду `music/({i}).mp3` для `i` від 1 до 9). Додаток буде перемішувати та відтворювати їх.

2.  **Запустіть додаток:**
    ```bash
    python your_main_script_name.py
    ```
    *(Якщо ваш основний скрипт називається інакше, ніж `your_main_script_name.py`, замініть відповідно, наприклад, `main.py` або `app.py`)*

3.  **Взаємодія:**
    * Клацніть на згорнутий сувій, щоб розгорнути його та відкрити повідомлення. Клацніть ще раз, щоб згорнути його.
    * Натисніть кнопку "**Музика💕**", щоб розпочати/зупинити або пропустити поточну пісню.
    * Натисніть кнопки внизу праворуч, щоб відкрити відповідні посилання (електронна пошта, Telegram, GitHub).

---

## Структура Проекту
.
├── img/

│   ├── background_image.png

│   ├── folded_scroll.png

│   ├── icon.ico

│   ├── paper_texture.png

│   ├── pres1.png

│   ├── pres2.png

│   └── pres3.png

├── music/

│   ├── (1).mp3

│   ├── (2).mp3

│   └── ... (up to (9).mp3 as per current code)

└── your_main_script_name.py  (e.g., main.py or app.py)
---

## Налаштування

* **Зміст Сувою:** Змініть змінну `scroll_content` у класі `ScrollWidget`, щоб змінити текст привітання.
* **Головний Заголовок:** Змініть змінну `main_title` у класі `ScrollWidget`.
* **Зображення:** Замініть файли `.png` у каталозі `img/` на власні користувацькі зображення. Переконайтеся, що вони мають ті самі назви.
* **Музика:** Додайте або видаліть файли `.mp3` у каталозі `music/`. Якщо ви зміните угоду про іменування або кількість файлів, вам потрібно буде відповідно налаштувати список `music_files` у класі `MainWindow`.
* **Контактні Посилання:** Оновіть аргументи `QUrl` для `self.btn1`, `self.btn2` та `self.btn3` у класі `MainWindow`, щоб вони вказували на бажані посилання.

---

## Участь у Розробці

Не соромтеся форкнути цей репозиторій, робити покращення та надсилати запити на витягування (pull requests).

---

## Ліцензія

Цей проект є відкритим вихідним кодом і доступний за [ліцензією MIT](LICENSE).
