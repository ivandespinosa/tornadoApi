from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json

class MainHandler(RequestHandler):

  def get(self):
    self.write("..:: Hello, Team LeadingFront ::..")

  def set_default_headers(self, *args, **kwargs):
      self.set_header("Access-Control-Allow-Origin", "*")
      self.set_header("Access-Control-Allow-Headers", "x-requested-with")
      self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")


class ValidationLoan(MainHandler):
  
  def post(self):
    data = json.loads(self.request.body)
    amount = int(data['amount'])
    if amount < 50000:
      message = 'Approved'
    elif amount == 50000:
      message = 'Undecided'
    else:
      message = 'Declined'
    response = {'codeStatus': 200,
                'message': message}
    self.write(response)    

def make_app():
  urls = [
    ("/", MainHandler),
    ("/api/validationLoan", ValidationLoan)
  ]

  return Application(urls, debug=True)

if __name__=='__main__':
  app = make_app()
  app.listen(3650)
  IOLoop.instance().start()

