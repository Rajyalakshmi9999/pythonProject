# class proglang:
#     def __init__(self,year,name,author):
#         self.year=  year
#         self.name=  name
#         self.author=    author
#     def call_some_lang(self):
#         print("Year is :" + self.year)
#         print("name is:"  +   self.name)
#         print("author is:"  + self.author)
# pl1 =   proglang(1989,"python", "xyz")
# pl1.call_some_lang()
class proglang:
  def __init__(self, year, name, developer, place):
    self.year = year
    self.name = name

    self.developer = developer
    self.place = place



  def myfunc(self):
    print("Hello my name is " + self.name)
    print("I am developed in  " + self.year)

    print("I am from " + self.place)

    print("My Developer is " + self.developer)

p1 = proglang("1972","c", "Dennis Ritch", "Bell labs")
p1.myfunc()
p2 = proglang("1991","Python","guido van Rossum", "Netherlands")
p2.myfunc()

p3 = proglang("1995","Java", "Games gosling","Sun micro systems")
p3.myfunc()

class plextra(proglang):
  def __init(self,app):
    self.app=app
  def call_use(self):
    super.__init__(self,  name,)
    print("main use is",  +self.app)
e1=plextra("enterprsiapp")
e1.call_use()
