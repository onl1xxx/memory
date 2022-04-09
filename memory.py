
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from random import shuffle

app = QApplication([])
window = QWidget()

window.resize(600, 400)
window.setWindowTitle('Вопрос')

quest = QLabel('Какой национальности не существует?')
btn = QPushButton('Ответить')
o1 = QRadioButton('Чулымцы')
o2 = QRadioButton('Смурфы')
o3 = QRadioButton('Алеуты')
o4 = QRadioButton('Энцы')
o5 = QLabel('Правильный ответ: Энцы')

o5.hide()

v1 = QVBoxLayout()
v2 = QVBoxLayout()
v3 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v_full = QVBoxLayout()

h1.addWidget(quest, alignment = Qt.AlignCenter)
h3.addWidget(btn, alignment = Qt.AlignCenter)
v1.addWidget(o1, alignment = Qt.AlignCenter)
v1.addWidget(o3, alignment = Qt.AlignCenter)
v2.addWidget(o2, alignment = Qt.AlignCenter)
v2.addWidget(o4, alignment = Qt.AlignCenter)
h2.addWidget(o5, alignment = Qt.AlignCenter)
h2.addLayout(v1)
h2.addLayout(v2)
h3.addLayout(v3)
v_full.addLayout(h1)
v_full.addLayout(h2)
v_full.addLayout(h3)
answers = [o1, o2, o3, o4]

class Question:
    def __init__(self, question, ans1, ans2, right_ans, ans4):
        self.question = question
        self.ans1 = ans1
        self.ans2 = ans2
        self.right_ans = right_ans
        self.ans4 = ans4

questions = []

quest1 = Question('Какой национальности не существует?','Чулымцы','Смурфы','Энцы','Алеуты')
questions.append(quest1)
quest2 = Question('Сколько в мире океанов?','3','4','5','6')
questions.append(quest2)
quest3 = Question('Какая самая большая страна в мире?','Украина','Китай','Россия','Бразилия')
questions.append(quest3)
quest4 = Question('Сколько всего в мире материков?','3','4','6','5')
questions.append(quest4)
quest5 = Question('Какая самая большая ягода?','клубника','малина','арбуз','черника')
questions.append(quest5)

def check_answer():
    if answers[3].isChecked():
        o5.setText('Правильно')
    else:
        o5.setText('Не правильно')

window.quest_num = 0

window.setLayout(v_full)

def finish():
    if btn.text() =='Ответить':
        window.quest_num += 1
        o1.hide()
        o2.hide()
        o3.hide()
        o4.hide()
        check_answer()
        o5.show()
        btn.setText('Следующий вопрос')
    else:
        o1.show()
        o2.show()
        o3.show()
        o4.show()
        btn.setText('Ответить')
        o5.hide()
        ask(questions[window.quest_num])

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.ans1)
    answers[1].setText(q.ans2)
    answers[2].setText(q.ans4)
    answers[3].setText(q.right_ans)
    quest.setText(q.question)
ask(questions[window.quest_num])

btn.clicked.connect(finish)

window.show()
app.exec_()
