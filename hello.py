import webapp2

html_page2= """
<html>
        <head>
                <title>hello</title>
        </head>
<body>
    <form action="/" methond="post">
        Name: <input type ="text" name="filed1"/>
        <input type="submit" value= "Submit"/>
        </form>
</body>
</html>
 """

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html_page2)

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("all about about")

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("we the people dont GAF")

routes = [
('/', MainHandler),
('/About', AboutHandler),
('/Home', HomeHandler)
]


app = webapp2.WSGIApplication(routes, debug=True)
