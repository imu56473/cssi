import webapp2
import jinja2
go = jinja2.Environment( loader= jinja2.FileSystemLoader("templates"))
html_page= """
<html>
       <head>
              <title>hello</title>
       </head>
       <body>
           <p> Hello Brooklyn,CSSI! </p>
          <form action="/" method="post">
            name: <input type="text" name="field1"/>
            <input type="submit" value="Submit"/>
          </form>

      </body>

 </html>
  """
class MainHandler(webapp2.RequestHandler):
     def get(self):
         self.response.write(html_page)
     def post(self):
         self.response.headers['Content-Type'] = 'text/plain'
         #self.response.write(self.request.POST)
         if "field1" not in self.request.POST:
            self.response.write('field1 not found')
         else:
           field1 = self.request.POST['field1']
         self.response.write("hello" + field1 + "!")
class AboutHandler(webapp2.RequestHandler):
      def get(self):
          self.response.write("all about about")

class HomeHandler(webapp2.RequestHandler):
       def get(self):
           #self.response.write("what i call home")
           templates_value= {"name":"BOB"}

           templates = go.get_template('index.html')
           self.response.write(templates.render(templates_value))

routes = [
      ('/' , MainHandler),
      ('/about', AboutHandler),
      ('/home', HomeHandler),

]
app = webapp2.WSGIApplication( routes, debug=True)
