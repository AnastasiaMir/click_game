from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QWidget
import sys
from PyQt5.QtCore import Qt


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.label = QLabel(self)
        self.turn = "0"
        self.winner = None
        self.game_button = QPushButton("Start new Game")
        self.step_count = 0
        self.game_over = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("GAME")
        layout = QVBoxLayout()
        self.label.setText("Player X turn")
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        for i in range (3):
            inner_btn_list = []
            rows_layout = QHBoxLayout()
            for j in range (3):
                new_btn = QPushButton("")
                new_btn.clicked.connect(self.step)
                new_btn.clicked.connect(self.check_winner)
                rows_layout.addWidget(new_btn)
                inner_btn_list.append(new_btn)
            layout.addLayout(rows_layout)
            self.buttons.append(inner_btn_list)
        self.game_button.setObjectName("new_game")
        self.game_button.clicked.connect(self.start_new_game)
        layout.addWidget(self.game_button)

        center_widget = QWidget()
        center_widget.setLayout(layout)
        self.setCentralWidget(center_widget)

        self.setStyleSheet("""
                    QMainWindow {
                        background-color: white;
                        text-align: center;
                    }
                    QVBoxLayout {
                        text-align: center;
                    }
                    QLabel {
                        color: midnightblue;
                        font-size: 24px;
                        text-align: center;
                    }
                    QPushButton {
                        background-color: #d9f2ff;
                        color: #a5bdfd;
                        border: 2px solid #d9f2ff;
                        margin: 0;
                        font-size: 30px;
                        height: 100px;
                        width: 100px;
                        border-radius: 5px;
                    }
                    QPushButton#new_game {
                        background-color: #a5bdfd;
                        border: 2px solid #a5bdfd;
                        font-size: 24px;
                        color: midnightblue;
                    }
                    QPushButton#winner {
                        background-color: #a5bdfd;
                    }
                """)
    def start_new_game(self):
        self.turn = "0"
        for btn_list in self.buttons:
            for btn in btn_list:
                btn.setText("")
                btn.setStyleSheet("background-color: #d9f2ff; color: #a5bdfd")
                btn.setEnabled(True)
        self.label.setText("Player X turn")

    def step(self):
        self.step_count +=1
        if self.turn == "0":
            self.turn = "X"
            self.label.setText("Player 0 turn")
        else:
            self.turn = "0"
            self.label.setText("Player X turn")
        current_btn = self.sender()
        current_btn.setText(self.turn)
        current_btn.setEnabled(False)
        if self.step_count == 9:
            self.label.setText("It is draw!")

    def check_winner(self):
        for x in range(0,3):
            if self.buttons[x][0].text() == self.buttons[x][1].text() \
            and self.buttons[x][1].text()== self.buttons[x][2].text() \
            and self.buttons[x][0].text() != "":
                self.winner = self.buttons[x][0].text()
                self.label.setText(f'Congratulations! Player {self.winner} won!')
                self.buttons[x][0].setStyleSheet("background-color: #a5bdfd; color: white")
                self.buttons[x][1].setStyleSheet("background-color: #a5bdfd; color: white")
                self.buttons[x][2].setStyleSheet("background-color: #a5bdfd; color: white")
                self.stop_game()
            elif self.buttons[0][x].text() == self.buttons[1][x].text() \
            and self.buttons[1][x].text()== self.buttons[2][x].text() \
            and self.buttons[0][x].text() != "":
                self.winner = self.buttons[0][x].text()
                self.label.setText(f'Congratulations! Player {self.winner} won!')
                self.buttons[0][x].setStyleSheet("background-color: #a5bdfd; color: white")
                self.buttons[1][x].setStyleSheet("background-color: #a5bdfd; color: white")
                self.buttons[2][x].setStyleSheet("background-color: #a5bdfd; color: white")
                self.stop_game()
        if self.buttons[0][0].text() == self.buttons[1][1].text() \
        and self.buttons[1][1].text()== self.buttons[2][2].text() \
        and self.buttons[0][0].text() != "":
            self.winner = self.buttons[0][0].text()
            self.label.setText(f'Congratulations! Player {self.winner} won!')
            self.buttons[0][0].setStyleSheet("background-color: #a5bdfd; color: white")
            self.buttons[1][1].setStyleSheet("background-color: #a5bdfd; color: white")
            self.buttons[2][2].setStyleSheet("background-color: #a5bdfd; color: white")
            self.stop_game()
        elif self.buttons[0][2].text() == self.buttons[1][1].text() \
        and self.buttons[1][1].text()== self.buttons[2][0].text() \
        and self.buttons[0][2].text() != "":
            self.winner = self.buttons[0][2].text()
            self.label.setText(f'Congratulations! Player {self.winner} won!')
            self.buttons[0][2].setStyleSheet("background-color: #a5bdfd; color: white")
            self.buttons[1][1].setStyleSheet("background-color: #a5bdfd; color: white")
            self.buttons[2][0].setStyleSheet("background-color: #a5bdfd; color: white")
            self.stop_game()

    def stop_game(self):
        for btn_list in self.buttons:
            for btn in btn_list:
                btn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Game()
    w.show()
    sys.exit(app.exec_())

