from frontend.controllers.main_controller import MainController
from frontend.ui.main_window import MainWindow


def main():
    app = MainWindow()
    controller = MainController(app)
    app.set_controller(controller)
    app.mainloop()


if __name__ == "__main__":
    main()
