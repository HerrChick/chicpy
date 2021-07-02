from api import API

chicpy = API()


@chicpy.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@chicpy.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"