# Static Site Generator

A static site generator coded in python made as part of the [Boot.dev](https://www.boot.dev/tracks/backend) course.

### Features

- generate html files from markdown documents.
- converts the markdown syntax to html tags.
- creates a standard public folder with generated files for hosting

### Install and Run

```bash
git clone https://github.com/itsMe-ThatOneGuy/static-site-generator
cd static-site-generator
./main.sh
```

Static files like css and images should be placed in the static folder.

The content folder is where you would place your markdown files to be converted into html.
You can even sort you files into separate directories as long as they are in the content folder.
Example: ./content/majesty/index.md

The public folder is cleared and automatically generated each time you run ./main.sh.
