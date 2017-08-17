import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('results.html')
        # The variables that are sent to results.html are those
        # that contain the input values from the main.html form with
        # names like noun1, activity, etc.
        template_variables = {
                    'noun1':self.request.get("noun1"),
                    'activity':self.request.get("activity"),
                    'teacher':self.request.get("teacher"),
                    'celebrity':self.request.get("celebrity"),
                    'show':self.request.get("show"),
                    'fun':self.request.get("fun"),
                    }
        self.response.out.write(results_template.render(template_variables))

app = webapp2.WSGIApplication(
[
    ('/', MainHandler)
    ],
debug=True
)
