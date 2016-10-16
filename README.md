# POMSelenium

Page Object Model (POM) is an organized approach to testing web applications wherein pages are represented in the tests. The page objects contain the elements and behaviors of the associated page. This design works well because it is clear what is being tested and limits the user to actions available on that page.

By separating the tests from the underlying data, not only is it now easier to write test cases, but you also only need to modify code in one place to update all tests. If the login error message changed to a different location, you would only need to update the LoginPage class and all the tests would still run fine. There is extra setup required to model the pages, but that time is quickly recovered when you get to creating your test suite.


In this POM, we have simply implemented an incorrect login attempt in Facebook. The BasePage.py is the base class which defines all the methods and attributes that the other 'pages' can use and share. So defining them all at one place and then extending them in your respective pages is very easy and convinient. 

LoginPage.py is just an example of the the 'pages' that we talked about above. It uses the methods defined in BasePage.py and uses them to perform a login in Facebook.



If you are confused by the webdriver initialization in LoginPage.py, it is because this is a Marionette Driver (or geckodriver) initialization. 
