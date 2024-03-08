### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

One important difference between Python and JavaScript is that Python is a server-side language, while JavaScript is a client-side language. This means that Python is used to write the server-side code that runs on the server, while JavaScript is used to write the client-side code that runs in the user's web browser. Another important difference is that Python is a general-purpose language, while JavaScript is a scripting language. This means that Python can be used for a wide variety of tasks, while JavaScript is primarily used for web development.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

You can use the `get` method to get a missing key without crashing. For example, you can use `d.get('c')` to get the value associated with the key 'c', and if the key is not in the dictionary, the `get` method will return `None` instead of crashing. You can also use the `in` operator to check if a key is in the dictionary before trying to access it. For example, you can use `'c' in d` to check if the key 'c' is in the dictionary, and if it is not, you can avoid trying to access it.

- What is a unit test?

A unit test is a type of test that tests a single unit of code, such as a function or a method. The purpose of a unit test is to verify that the unit of code behaves as expected under a variety of conditions.

- What is the role of web application framework, like Flask?

The role of a web application framework like Flask is to provide a set of tools and libraries that make it easier to build web applications. For example, Flask provides tools for handling HTTP requests and responses, routing URLs to the appropriate code, and rendering HTML templates. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

You might choose to pass information as a parameter in a route URL when the information is an essential part of the URL, such as an identifier for a resource. You might choose to use a URL query param when the information is optional or when you want to allow the user to filter or sort the results.

- How do you collect data from a URL placeholder parameter using Flask?

You can collect data from a URL placeholder parameter using Flask by defining a route with a placeholder in the URL, and then defining a function that takes a parameter with the same name as the placeholder. For example, you can define a route like `@app.route('/foods/<type>')` and then define a function like `def get_foods(type):` to collect the data from the URL placeholder parameter.

- How do you collect data from the query string using Flask?

You can collect data from the query string using Flask by accessing the `request.args` dictionary, which contains the key-value pairs from the query string.

- How do you collect data from the body of the request using Flask?

You can collect data from the body of the request using Flask by accessing the `request.form` dictionary, which contains the key-value pairs from the form data in the request body. For example, you can use `request.form.get('name')` to get the value of the 'name' form field.

- What is a cookie and what kinds of things are they commonly used for?

A cookie is a small piece of data that is stored on the user's computer by the web browser. Cookies are commonly used to store information about the user, such as their preferences, login status, and shopping cart contents.

- What is the session object in Flask?

The session object in Flask is a special type of dictionary that is used to store data that is associated with a specific user session. It can store larger amounts of data than cookies and is stored on the server, not the client.

- What does Flask's `jsonify()` do?

Flask's `jsonify()` function converts a Python dictionary into a JSON response. This is useful when you want to return JSON data from a Flask route, such as an API endpoint.
