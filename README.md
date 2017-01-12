# HTTPRequest
A simple class to send HEAD or GET request to an http page

Simply create an HTTPRequest object using url string. Url string can be formatted in all valid standards such as <code>http://example.com</code> or <code>http://www.example.com</code> or <code>www.example.com</code>. https protocol is accepted by constructor. AN exception will be raised if the string does not meet the needed standards.

Public methods:
<ul>
<li><code>getHeader()</code> which returns a dictionary with Field Name as key and value as, of course, value.</li>
<li><code>get(method)</code> which returns a string with everything the page has sent. method should be a string.</li>
