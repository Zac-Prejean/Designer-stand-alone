# Designer-stand-alone

This is a Python script that uses various modules and libraries to generate images with personalized text on them based on data from a CSV file. The script uses Flask to create a web application that can receive a CSV file as input and export the generated images to a specified directory.

The script imports the following modules:

    io: Provides tools for working with streams of data.
    os: Provides a way to interact with the operating system.
    re: Provides support for regular expressions.
    base64: Provides tools for working with base64-encoded data.
    pandas: Provides data analysis tools.
    Flask: A micro web framework for building web applications.
    PIL (Python Imaging Library): Provides tools for working with images.

    The script defines several functions to perform various tasks, such as loading fonts, exporting images, and processing special rules for the personalized text. The main_function() function reads the input CSV file, cleans the SKU column, and then calls the export_images() function to generate the images.

    The Flask application has two routes: '/' and '/run-script'. The '/' route renders an HTML template for the user to upload a CSV file. The '/run-script' route receives the CSV file, processes it with the main_function() function, and returns the result as a JSON object.

    Overall, this script is a useful tool for generating personalized images based on data from a CSV file, and the Flask application makes it easy to use for non-technical users.
