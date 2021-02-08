import os
import pkgutil


def error(message):
    raise ValueError(f"\033[1;31;48mError: {message}\033[m")


class BoilerPlate:
    def __init__(self, path):
        if not os.path.exists(path):
           self.__make_dir_not_exists(path)

        self.path = path

    # MAKE DIRS
    def __make_dir_not_exists(self, dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    def __make_templates_dir(self):
        template_dir = os.path.join(self.path, "templates")
        self.__make_dir_not_exists(template_dir)

    def __make_static_css_dir(self, static_dir_path):
        css_dir = os.path.join(static_dir_path, "css")
        self.__make_dir_not_exists(css_dir)

    def __make_static_js_dir(self, static_dir_path):
        js_dir = os.path.join(static_dir_path, "js")
        self.__make_dir_not_exists(js_dir)

    def __make_static_img_dir(self, static_dir_path):
        img_dir = os.path.join(static_dir_path, "img")
        self.__make_dir_not_exists(img_dir)

    def __make_static_dirs(self):
        static_dir = os.path.join(self.path, "static")
        self.__make_dir_not_exists(static_dir)

        self.__make_static_css_dir(static_dir)
        self.__make_static_js_dir(static_dir)
        self.__make_static_img_dir(static_dir)

    def __make_dirs(self):
        self.__make_templates_dir()
        self.__make_static_dirs()

    # GEN BOILERPLATE FILES
    def __get_file_and_write(self, dir_path, filename):
        file_contents = pkgutil.get_data(__name__, os.path.join("files", filename)).decode()
        file_path = os.path.join(dir_path, filename)

        with open(file_path, "w") as file:
            file.write(file_contents)

    def __make_index_html(self):
        template_dir = os.path.join(self.path, "templates")

        self.__get_file_and_write(dir_path=template_dir, filename="index.html")

    def __make_main_js(self, static_js_dir):
        self.__get_file_and_write(dir_path=static_js_dir, filename="main.js")

    def __make_jquery_min_js(self, static_js_dir):
        self.__get_file_and_write(dir_path=static_js_dir, filename="jquery.min.js")

    def __make_sweetalert_min_js(self, static_js_dir):
        self.__get_file_and_write(dir_path=static_js_dir, filename="sweetalert.min.js")

    def __make_js_files(self):
        static_js_dir = os.path.join(self.path, "static/js")

        self.__make_main_js(static_js_dir=static_js_dir)
        self.__make_jquery_min_js(static_js_dir=static_js_dir)
        self.__make_sweetalert_min_js(static_js_dir=static_js_dir)

    def __make_styles_css(self):
        static_css_dir = os.path.join(self.path, "static/css")

        self.__get_file_and_write(dir_path=static_css_dir, filename="styles.css")  

    def __make_app_py(self):
        self.__get_file_and_write(dir_path=self.path, filename="app.py")

    def __make_files(self):
        self.__make_index_html()
        self.__make_js_files()
        self.__make_styles_css()
        self.__make_app_py()

    def run(self):
        self.__make_dirs()
        self.__make_files()
        