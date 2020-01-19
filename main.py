from core.baseapp import BaseApp


class MainApp(BaseApp):
    def __init__(self):
        self.books = []


if __name__ == "__main__":
    app = MainApp()
    app.run()
class view(ViewBook):
    def __init__(self):
        vBooks = ViewBook(self.books)
        vBooks.list()

if __name__ == "__main__":
    App = MainApp()
    App.run()