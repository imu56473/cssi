
import jinja2
import webapp2
import logging


env = jinja2.Environment(loader = jinja2.FileSystemLoader('templates'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('lgbt.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('lgbt_results.html')
        template_variables = { 'textsearch':self.request.get("textsearch"),
        }
        self.response.out.write(results_template.render(template_variables))

class ProfilePageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('gt.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('gt.html')
        self.response.out.write(results_template.render(template_variables))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('lg.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('lg.html')
        self.response.out.write(results_template.render(template_variables))

app= webapp2.WSGIApplication(
    [
        ('/', MainHandler),
        ('/Profilepage', ProfilePageHandler),
        ('/home', HomeHandler )
    ],
    debug=True)
