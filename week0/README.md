      
<h1> What is React and React Native? </h1>
<h1> What is the difference between react and react Native? </h1>


<h1> History </h1>
<h3> React </h3>
ReactJS (React or React.js) is defined as an open source JavaScript library (not a framework) for building user interfaces.It was created by Jordan Walke, who was a software engineer at Facebook, The first prototype of React called "FaxJS". He was influenced by XHP, an HTML component library for PHP. It was first deployed on Facebook's News Feed in 2011 and later on Instagram in 2012.
<h3> React Native </h3>
React Native is one of the most popular mobile app development frameworks. Facebook open sourced its codebase in 2015. React Native's claim to fame is that it enables execution of JavaScript codes in smartphones, which is a contradiction in itself, and hence interesting.
React was born in Facebook's Ads Org. As Tom Occhino, the then React team lead at Facebook, said in his keynote address in the first-ever React.js conference in 2015, it all started very simple and fast and straightforward. The typical MVC approach was used for developing and deploying the Facebook ads platform. But as new features were added, things started to get complex.
<h3> Node JS </h3>
Node JS was born in 2009. In 2009, Ryan Dahl wrote Node.js. At first, Node.js supported only Mac OS X and Linux. Dahl led the development and maintenance and later it was sponsored by Joyent. On November 8, 2009 at the inaugural European JSConf, the Node.js project was first demonstrated by Dahl. Node.js is a combination the V8 JavaScript Chrome engine, a low-level I/O API, and an event loop.
Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. Node.js lets developers use JavaScript to write command line tools and for server-side scripting to produce dynamic web page content before the page is sent to the user's web browser. Consequently, Node.js represents a "JavaScript everywhere" paradigm, unifying web-application development around a single programming language, rather than different languages for server-side and client-side scripts.


<h1> What is React </h1>
ReactJS offers graceful solutions to some of front-end programming’s most persistent issues, allowing you to build dynamic and interactive web apps with ease. It’s fast, scalable, flexible, powerful, and has a robust developer community that’s rapidly growing.In React, each building blocks is called components. React uses the concept of virtual DOM so if any changes occures in the webpage, React created the Virtual DOM and compare the 2 DOMS (Actual and Virtual) and reflects these changes. Hance it does not load complete pages instead it updates only those components.
<h1> What is React Native </h1>
"Learn once, Build everywhere"

React native the most popular JS framework for building native applications for cross platforms. 
The working principles of React Native are virtually identical to React except that React Native does not manipulate the DOM via the Virtual DOM. It runs in a background process (which interprets the JavaScript written by the developers) directly on the end-device and communicates with the native platform via serialized data over an asynchronous and batched bridge
React components wrap existing native code and interact with native APIs via React’s declarative UI paradigm and JavaScript.
While React Native styling has a similar syntax to CSS, it does not use HTML or CSS.Instead, messages from the JavaScript thread are used to manipulate native views. React Native also allows developers to write native code in languages such as Java or Kotlin for Android, Objective-C or Swift for iOS, and C++/WinRT or C# for Windows 10, which makes it even more flexible. 

<h1> What is Node JS </h1>
Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project!
Node.js runs the V8 JavaScript engine, the core of Google Chrome, outside of the browser. This allows Node.js to be very performant.
A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking and generally, libraries in Node.js are written using non-blocking paradigms, making blocking behavior the exception rather than the norm.


<h1> References </h1>
<h6> History </h6>
      * https://en.wikipedia.org/wiki/React_(JavaScript_library)  <br />
      * https://en.wikipedia.org/wiki/React_Native

<h6> What is React Native? </h6>
      * https://reactnative.dev/ <br />
      * https://en.wikipedia.org/wiki/React_Native


<h6> What is Node JS? </h6>
      * https://en.wikipedia.org/wiki/Node.js <br />
      * https://nodejs.dev/learn
      
 <h6> React vs React Native </h6>
      * https://www.javatpoint.com/reactjs-vs-reactnative <br />
      * https://stackoverflow.com/questions/34641582/what-is-the-difference-between-react-native-and-react


<h6>	Youtube Short videos </h6>
      * https://www.youtube.com/watch?v=EVSMegdj6tY&t=493s <br />
      * https://www.youtube.com/watch?v=6oFuwhIibo4
      
      
      
<h1>CV Page </h1>
CV page is purely designed in html and css

![CV PAGE](https://github.com/saifuullah/CDR_FYP/blob/main/week0/CV/cv.png)

<h1>Notable personality profile page</h1>
This small, 1-page website is developed in html and css. It is linked with CV. I followed a totourial for some help.

![Profile](https://github.com/saifuullah/CDR_FYP/blob/main/week0/profile/101.png)
![Profile](https://github.com/saifuullah/CDR_FYP/blob/main/week0/profile/102.png)
![Profile](https://github.com/saifuullah/CDR_FYP/blob/main/week0/profile/103.png)
![Profile](https://github.com/saifuullah/CDR_FYP/blob/main/week0/profile/104.png)


<h1>CRUD API in NodeJS</h1>
CRUD API is developed in NodeJS framework with Express server and MySql database. I have Used POSTMAN (Desktop Version) for testing like
sending GET,POST,DELETE requests. 

<h1>Form Page</h1>
In Form page website you can upload CSV files. The files data is then saved in MySql database and all the data is
then rendered in table. Table is horizentally scrollable because data contains huge number of columns.
Django is used as a server.

<h1>Graphs</h1>
I was unable to do this task completly by my own. I was able to draw a bar graph in html,css but unable to make it dynamic. 
I am working on it.

<h1>How Browsers work</h1>
A browser is a group of structured codes which together performs a series of tasks to display a web page on the screen. 
Today’s browsers are fully-functional software suites that can interpret and display HTML Web pages, applications, JavaScript,
AJAX and other content hosted on Web servers. After adding some extra plugins we can extends the capibilities of web browsers.

<h2>General Structure/Diagram</h2>
![Skeletn](https://github.com/saifuullah/CDR_FYP/blob/main/week0/br.png)

<h2>User interface</h2>
The user interface is the space where User interacts with the browser. It includes the address bar, back and next buttons,
home button, refresh and stop, bookmark option, etc.

<h2>Browser Engine</h2>
The browser engine works as a bridge between the User interface and the rendering engine. According to the inputs from various 
user interfaces, it queries and manipulates the rendering engine.

<h2>Rendering Engine</h2>
The rendering engine, as the name suggests is responsible for rendering the requested web page on the browser screen. The rendering
engine interprets the HTML, XML documents and images that are formatted using CSS and generates the layout that is displayed in the 
User Interface. At the end it generates DOM. Different browsers user different rendering engines:
The rendering engine parses the chunks of HTML document and convert the elements to DOM nodes in a tree called the “content tree” or the “DOM tree”. It also parses both the external CSS files as well in style elements. While the DOM tree is being constructed, the browser constructs another tree, the render tree. This tree is of visual elements in the order in which they will be displayed. It is the visual representation of the document
</br>
* Internet Explorer: Trident </br>
* Firefox & other Mozilla browsers: Gecko </br>
* Chrome & Opera 15+: Blink </br>
* Chrome (iPhone) & Safari: Webkit </br>

<h2>JavaScript Interpreter</h2>
It is the component of the browser which interprets and executes the javascript code embedded in a website. The interpreted results are sent to the rendering engine for display. If the script is external then first the resource is fetched from the network. Parser keeps on hold until the script is executed.
Some browsers also have different JS engines. </br>

CHAKRA is used by MS Edge </br>
SPIDERMONKEY by FireFox </br>
V8 by Chrome </br>

<h2>UI backend </h2>
UI backend is used for drawing basic widgets like combo boxes and windows and so on.

