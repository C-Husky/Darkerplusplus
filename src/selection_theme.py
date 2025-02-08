from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QButtonGroup, QWidget
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt


class AppearanceSelector(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hammerfy")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #1c1c1c; color: white;")

        # Cores para texto
        self.text_color = "white"

        # Layout principal
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Título
        header_label = QLabel("ESCOLHA A APARÊNCIA")
        header_label.setStyleSheet(f"""
            QLabel {{
                font-size: 24px;
                font-weight: bold;
                color: {self.text_color};
                background: none;
                border: none;
            }}
        """)
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header_label)

        # Subtítulo
        sub_label = QLabel("Selecione o tema do seu Hammer e sua cor de destaque")
        sub_label.setStyleSheet(f"""
            QLabel {{
                font-size: 16px;
                color: {self.text_color};
                background: none;
                border: none;
            }}
        """)
        sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(sub_label)

        # Opções de tema
        self.theme_layout = QHBoxLayout()
        self.theme_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Carregar imagens
        light_theme_image = QPixmap("claro.png")  # Substitua pelo caminho correto
        dark_theme_image = QPixmap("escuro.png")    # Substitua pelo caminho correto

        # Criar labels clicáveis
        self.light_theme = QLabel()
        self.light_theme.setPixmap(light_theme_image.scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio))
        self.light_theme.setObjectName("light_theme")
        self.light_theme.mousePressEvent = lambda event: self.select_theme("light")

        self.dark_theme = QLabel()
        self.dark_theme.setPixmap(dark_theme_image.scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio))
        self.dark_theme.setObjectName("dark_theme")
        self.dark_theme.mousePressEvent = lambda event: self.select_theme("dark")

        # Estilo para bordas arredondadas
        self.light_theme.setStyleSheet("""
            border: 2px solid transparent;
            border-radius: 10px;
        """)
        self.dark_theme.setStyleSheet("""
            border: 2px solid transparent;
            border-radius: 10px;
        """)

        # Adicionar imagens ao layout
        self.theme_layout.addWidget(self.light_theme)
        self.theme_layout.addWidget(self.dark_theme)

        # Opções de cores
        self.color_layout = QHBoxLayout()
        self.color_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.color_buttons = QButtonGroup()
        colors = ["#3498db", "#1abc9c", "#2ecc71", "#e67e22", "#e74c3c", "#ecf0f1", "#9b59b6", "#7f8c8d"]

        for i, color in enumerate(colors):
            color_button = QPushButton()
            color_button.setFixedSize(30, 30)
            color_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    border: 4px solid transparent;
                    border-radius: 15px;
                }}
                QPushButton:hover {{
                    border: 4px solid {color};
                }}
            """)
            color_button.clicked.connect(lambda _, col=color: self.select_color(col))
            self.color_layout.addWidget(color_button)
            self.color_buttons.addButton(color_button, i)

        # Botão de continuar
        continue_button = QPushButton("Continuar")
        continue_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
        """)
        continue_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Adicionar widgets ao layout principal
        main_layout.addLayout(self.theme_layout)
        main_layout.addLayout(self.color_layout)
        main_layout.addWidget(continue_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(main_widget)

        # Armazenar seleção
        self.selected_theme = None
        self.selected_color = None

    def select_theme(self, theme):
        self.selected_theme = theme

        # Resetar bordas
        self.light_theme.setStyleSheet("""
            border: 2px solid transparent;
            border-radius: 10px;
        """)
        self.dark_theme.setStyleSheet("""
            border: 2px solid transparent;
            border-radius: 10px;
        """)

        # Adicionar borda na seleção
        if theme == "light":
            self.light_theme.setStyleSheet("""
                border: 2px solid white;
                border-radius: 10px;
            """)
        elif theme == "dark":
            self.dark_theme.setStyleSheet("""
                border: 2px solid white;
                border-radius: 10px;
            """)

    def select_color(self, color):
        self.selected_color = color

        # Resetar bordas de todas as cores
        for button in self.color_buttons.buttons():
            button.setStyleSheet(button.styleSheet().replace(f"4px solid {button.styleSheet().split('background-color: ')[1].split(';')[0]}", "4px solid transparent"))

        # Adicionar borda na cor selecionada
        for button in self.color_buttons.buttons():
            if button.palette().button().color().name() == color:
                button.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {color};
                        border: 4px solid {color};
                        border-radius: 15px;
                    }}
                """)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = AppearanceSelector()
    window.show()
    sys.exit(app.exec())
