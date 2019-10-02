# CV website with Flask
🔖 This is a personal CV website implemented with Flask.

## Project tree
```
.
├── Dockerfile
├── README.md
├── info.yml
├── requirements.txt
├── static
│   └── styles.css
├── templates
│   ├── education.html
│   ├── experience.html
│   ├── includes
│   │   └── nav.html
│   ├── layout.html
│   └── profile.html
└── website.py
```

## How to run locally
* Using Python:
````pip install && python3 website.py````

* Using Docker:
````docker run -it -p 5000:5000 armi/cv-flask````

## References
* https://gitlab.com/UFM/flasky-students/tree/master
* https://www.youtube.com/watch?v=NKJV0ekmo4U
* https://codepen.io/jlalovi/pen/NPeBqZ