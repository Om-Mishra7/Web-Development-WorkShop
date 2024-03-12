# Web Development Workshop - Hack On Campus | K.R. Mangalam University
Organized by: Om Mishra | [GitHub](https://github.com/Om-Mishra7) and Yash Soni | [GitHub](https://github.com/Yash-Soni774)   

## HTML
HyperText Markup Language, is the standard markup language for describing the structure of web pages like headings, paragraphs, lists, links, images, etc.

### HTML Demo Page

A simple HTML page looks like this and is saved with a `.html` extension, this is just code that is parsed by the web browser to display the content in a human-readable format.

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML</title>
</head>
<body>
    Hello, World 🌍!
</body>
</html>
```

Even without knowing HTML, you can probably guess what some of the things in this file do, e.g. `<title>` sets the title of the page, `<body>` contains the content of the page, etc.

### Detailed Explanation of the Demo HTML Page

The first line, `<!DOCTYPE html>`, is the document type declaration and it is required for all HTML documents. It tells the web browser about the version of HTML used in the document HTML5 in this case.

The 'lang' attribute in the opening `<html>` tag is used to declare the language of the Web page. It is used by screen readers and other assistive technologies to determine the language of the content.

The `<head>` element contains meta-information about the document, such as its title and links to its scripts and style sheets.

The `<title>` element is required and it defines the title of the document, which is shown in the browser's title bar or in the page's tab.

The `<body>` element contains the document's actual content, which is visible to the users.

The HTML comments are used to add notes to the HTML source code. The comments are not displayed in the web browsers, and can be used to explain the code, or to prevent execution, when testing alternative code. e.g. `<!-- This is a comment -->`

### Document Object Model (DOM)

The Document Object Model (DOM) is a way of representing the structure of an HTML document in a tree-like form, it's useful for understanding how the HTML is structured and later on for manipulating the HTML using JavaScript.

The DOM of the HTML document above looks like this:

```
- html
    - head
        - title
            - "HTML"
    - body
        - "Hello, World 🌍!"
```

### HTML Tags

HTML tags are used to define HTML elements. An HTML element is defined by a start tag, some content, and an end tag:

```html
<tagname>Content goes here...</tagname>
```

Let's look at some of the most commonly used HTML tags:

- Heading tags: These are big banners that are used to define headings and subheadings in the HTML document. There are six levels of headings from `<h1>` to `<h6>`. An simple example of heading tags is:

```html
<h1>This is a heading</h1>
<h2>This is a subheading</h2>
```

- List tags: These are used to define lists in HTML. There are two types of lists in HTML, ordered and unordered. An example of list tags is:

```html
This is an ordered list:
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>

This is an unordered list:
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

- Image tag: This tag is used to define an image in HTML, unlike other tags, it has required attributes like `src` and `alt`. An example of an image tag is:

```html
<img src="image.jpg" alt="This is an image">
```

We can also notice that the image tag doesn't have a closing tag, this is because it's a self-closing tag meaning it can't have any content inside it.

Also, additional attributes like `width` and `height` can be added to the image tag to define the size of the image. e.g. `<img src="image.jpg" alt="This is an image" width="500" height="600">`

- Anchor tag: On of the most important features of the web is the ability to link to other pages, this is done using the anchor tag. An example of an anchor tag is:

```html
<a href="https://www.google.com">This is a link to Google</a>
<a href="/path/to/page">This is a link to another page</a>
```

Just like the image tag, the anchor tag also has a required attribute `href` (Hypertext Reference) which defines the URL of the page the link goes to.

- Table tag: This tag is used to define a table in HTML, as we can imagine a table is just a collection of rows and columns. An example of a table tag is:

```html
<table>
    <thead>
        <tr>
            <th>Student ID</th>
            <th>Student Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Ram</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Shyam</td>
        </tr>
    </tbody>
</table>
```

- Form tag: Our web pages often need to take input from the user, e.g. login forms, registration forms, etc. This is done using the form tag. An example of a form tag is:

```html
<form action="/submit-form" method="post">
    <input type="text" id="username" name="username">
    <input type="password" id="password" name="password">
    <input type="submit" value="Submit">
</form>
```

Another more complex example of a form tag is:

```html
<form action="/submit-form" method="post">
    <input type="text" id="name" name="name" placeholder="Name">
    <input type="email" id="email" name="email" placeholder="Email">
    <input type="password" id="password" name="password" placeholder="Password">
    <input type="radio" name=current_status value="student"> Student
    <input type="radio" name=current_status value="teacher"> Teacher
    <input name="course" list="courses" placeholder="Course">
    <datalist id="courses"> <!-- This is a list of options for the course input and is built using the datalist tag -->
        <option value="B.Tech">
        <option value="M.Tech">
        <option value="BBA">
        <option value="MBA">
    </datalist>
    <input type="submit" value="Submit">
</form>
```

## CSS

As of now, we have learned how to structure the content of a web page using HTML, but the content is not very visually appealing. This is where CSS comes in, it is used to tell the web browser how to display the HTML content.

### CSS Inline Styles

To apply CSS to an HTML element, we can use the `style` attribute in the HTML tag, the value of the `style` attribute is a collection of CSS property-value pairs. An example of inline styles is:

```html
<p style="color: red; font-size: 20px;">This is a paragraph</p>
```

<b>CSS properties also follow inheritance, meaning that if a parent element has a certain style, the child elements will inherit that style unless they have a style of their own.</b>

### CSS Internal Styles

Let's take the example of the HTML page we created earlier and add some more content with inline styles, this is how the HTML page looks now:

```html
<h1 style="color: red;">This is a heading</h1>
<p style="color: red;">This is a paragraph</p>
```

As we can see, we needed to repeat the style for the color red, this is where internal styles come in, we can define the styles in the `<head>` tag of the HTML document and they will be applied to the entire document. An example of internal styles is:

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML</title>
    <style>
        h1 {
            color: red;
        }
        p {
            color: red;
        }
    </style>
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph</p>
</body>
</html>
```

### CSS External Styles

Internal styles are good for small web pages, but for larger web pages, there may be a lot of shared styles e.g. Every page on a website may have the same header and footer, and it would be inefficient to define the styles for the header and footer on every page. This is where external styles come in, we can define the styles in a separate `.css` file and link it to the HTML document. An example of external styles is:

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph</p>
</body>
</html>
```

The `href` attribute in the link tag is the path to the `.css` file, and the `rel` attribute is the relationship between the HTML document and the `.css` file.

The `styles.css` file looks like this:

```css
h1 {
    color: red;
}
p {
    color: red;
}
```

### Common CSS Properties

- `color`: This property is used to set the color of the text content.
- `font-size`: This property is used to set the size of the text content.
- `background-color`: This property is used to set the background color of an element.
- `border`: This property is used to set the border of an element, it can be used to set the width, style, and color of the border.
- `margin`: This property is used to set the margin of an element, it can be used to set the margin on all sides or individually.
- `padding`: This property is used to set the padding of an element, it can be used to set the padding on all sides or individually.
- `text-align`: This property is used to set the alignment of the text content.
- `font-family`: This property is used to set the font of the text content.
- `font-weight`: This property is used to set the weight of the text content, e.g. bold, normal, etc.

An example of using these properties is:

```css
h1 {
    color: red;
    font-size: 20px;
    background-color: yellow;
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
    text-align: center;
    font-family: Arial, sans-serif;
    font-weight: bold;
}

div {
    color: blue;
    font-size: 20px;
    background-color: green;
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
    text-align: center;
    font-family: Arial, sans-serif;
    font-weight: bold;
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <h1>This is a heading</h1>
    <div>This is a div</div>
</body>
</html>
```

Now let's apply some styles to the table tag we learned about earlier:

```css
table {
    border-collapse: collapse; /* This property is used to collapse the borders of the table, making it look like a single border */
    width: 100%;
    border: 1px solid black;
}

th {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
}

td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
}

```

As we can see we need to apply the same styles to the `th` and `td` tags, as discussed earlier, we should try to avoid repeating the same styles, this is where CSS Selectors come in to play.

### CSS Selectors

CSS selectors are used to select the HTML elements we want to style, there are many types of selectors, some of the most commonly used ones are:

- Grouping Selector: This is used to group multiple selectors together, e.g. `h1, p, div`.

- Element Selector: This is used to select all the elements of a particular type, e.g. `h1`, `p`, `div`, etc.

- ID Selector: This is used to select an element with a particular ID, e.g. `#id-name`.

- Attribute Selector: This is used to select an element with a particular attribute, e.g. `input[type="text"]`.
- 
```css
a[href="https://www.google.com"] {
    color: red;
}
```

- Pseudo-class Selector: This is used to select an element that is in a particular state, e.g. `a:hover`.
- 
```css
a:hover {
    color: red;
}
```


Let's say we want to apply different styles to three different headings, we would need to use the ID selector to select each heading and apply the styles. 

```css
#heading1 {
    color: red;
    font-size: 20px;
}

#heading2 {
    color: blue;
    font-size: 20px;
}

#heading3 {
    color: green;
    font-size: 20px;
}
```

- Class Selector: This is used to select elements with a particular class, e.g. `.class-name`.

Let's say we want to apply the same styles to multiple elements, we would need to use the class selector to
select the elements and apply the styles.

```css
.same-styles {
    color: red;
    font-size: 20px;
}
```
```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <h1 id="heading1" class="same-styles">This is a heading</h1>
    <h1 id="heading2" class="same-styles">This is a heading</h1>
    <h1 id="heading3" class="same-styles">This is a heading</h1>
</body>
</html>
```

- Descendant Selector: This is used to select an element that is a descendant of another element, e.g. `div p`.
- Child Selector: This is used to select an element that is a child of another element, e.g. `div > p`.

### CSS Specificity

As we have seen, there are many types of selectors in CSS, and sometimes we may have multiple selectors that apply to the same element, in such cases, the browser needs to decide which styles to apply, this is where specificity comes in.

- Inline
- ID
- Class
- Element

The !important rule is a way to make your CSS cascade but also have the rules you feel are most crucial always be applied. A rule that has the !important property will always be applied no matter where that rule appears in the CSS document.


## Responsive Web Design

Another thing we can use CSS for is to make our web pages responsive, this means that the web page should look good on all devices, e.g. mobile, tablet, desktop, etc.

### Viewport

The viewport is the user's visible area of a web page, it varies with the device, and will be smaller on a mobile phone than on a computer screen, but generally mobile devices spoof the viewport to be the same as a desktop browser. This was done as many websites were not optimized for mobile devices and would look very small on a mobile device.

To control the viewport, we can use the `<meta>` tag in the `<head>` tag of the HTML document, an example of the viewport meta tag is:

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- This sets the width of the viewport to the width of the device instead of the width of the browser window -->
</head>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph</p>
</body>
</html>
```

### Media Queries

Media queries are used to apply different styles for different devices, e.g. we may want to apply different styles for mobile devices and desktop devices.

An example of a media query is:

```css
/* This is the default style for all devices */
h1 {
    color: red;
    font-size: 20px;
}

/* This is the style for devices with a width of 600px or less */
@media only screen and (max-width: 600px) {
    h1 {
        color: blue;
        font-size: 10px;
    }
}
```

### Flexbox

Flexbox is a layout model that allows us to design a responsive layout, it's a one-dimensional layout method for laying out items in rows or columns, it's useful for laying out items in a single row or column, and it's also useful for laying out items in a row or column that need to be the same height.

An example of using flexbox is:

```css
.container {
    display: flex;
    justify-content: space-between; /* This property is used to distribute the items evenly */
    align-items: center; /* This property is used to align the items vertically */
    flex-wrap: wrap; /* This property is used to wrap the items to the next line */
}

.item {
    flex: 1; /* This property is used to make the items take up the same amount of space */
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="item">Item
        </div>
        <div class="item">Item
        </div>
        <div class="item">Item
        </div>
    </div>
</body>
</html>
```

## SAAS (Syntactically Awesome Style Sheets)

Sass is a preprocessor scripting language that is interpreted or compiled into CSS, it's a superset of CSS, meaning that it contains all the features of CSS and more.

### Variables

Variables are used to store information that can be reused throughout the stylesheet, this is useful for storing things like colors, font stacks, or any value that is repeated throughout the stylesheet.

An example of using variables is:

```scss
$primary-color: #ff0000;
$secondary-color: #00ff00;

h1 {
    color: $primary-color;
}

p {
    color: $secondary-color;
}

```

Unlike SAAS can't run directly in the browser, it needs to be compiled into CSS, this can be done using a build tool like Webpack, Gulp, etc.

### Nesting

Sass allows us to nest our CSS selectors in a way that follows the same visual hierarchy of our HTML, this is useful for keeping our code organized and making it easier to read.

An example of using nesting is:

```scss
nav {
    ul {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    li {
        display: inline;
    }

    a {
        text-decoration: none;
    }
}
```

### Inheritance

Sass allows us to use inheritance to share properties between selectors, this is useful for keeping our code DRY (Don't Repeat Yourself).

An example of using inheritance is:

```scss
%button {
    border: none;
    padding: 10px 20px;
    font-size: 16px;
}


.primary-button {
    @extend %button;
    background-color: #ff0000;
    color: #ffffff;
}

.secondary-button {
    @extend %button;
    background-color: #00ff00;
    color: #ffffff;
}
```

