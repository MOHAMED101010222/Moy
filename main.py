from flet import *

def main(page: Page):
    T = Text('mohamed ahmed')
    page.add(T)

# هذا السطر يجب أن يبدأ من أول العمود (بدون أي مسافة قبله)
app(target=main)
