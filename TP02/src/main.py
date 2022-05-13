from website import create_html

html = create_html()

#Running the website only if we run this file
if __name__ == '__main__':
    html.run(debug=True)