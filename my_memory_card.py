from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)
 
app = QApplication([])
 
class Question():
        def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

q_list=[]
q_list.append(Question("Кем был Толстой","писателем","толстым","художником","прагроммистом"))
q_list.append(Question("Какой планетой по счету был Меркурий","2","5","7","1"))
q_list.append(Question("Кем был создан айфон","Стив Джопс","Поззи","А4","Аид"))
q_list.append(Question("Когда был создан Тик Ток","2016","2008","2003","2009"))
q_list.append(Question("Когда был создан Youtube","2016","2008","2005","2009"))








# Создаем панель вопрос
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide() # эту панель мы уже видели, скроем, посмотрим, как получилась панель с ответом
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
window = QWidget()
window.setLayout(layout_card)

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос!")
def start_test():
    if btn_OK.text()==("Ответить"):
        show_result()
    else:
        show_question()
btn_OK.clicked.connect(start_test)





window.setWindowTitle('Memory Card')
window.show()
app.exec()