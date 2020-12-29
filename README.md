## Online Résumé

<a href="https://mhaseebtariq.com/" target="_blank">Resume URL</a><br/><br/>
Generated (and hosted) using:
* Github Pages
* Django
* Template credit: https://themes.jsonresume.org/theme/kwan

### Setup
* Install Python 3.9.1
* Install pip
* `pip install virtualenv==20.2.2`
* `git clone https://github.com/mhaseebtariq/mhaseebtariq.github.io.git`
* `cd mhaseebtariq.github.io`
* `virtualenv .`
* `source bin/activate`
* `pip install -r requirements.txt`
* `cd resume`
* `python manage.py runserver`
* Modify `templates/*.html` templates accordingly
* Access http://127.0.0.1:8000/
* View `source` from the browser
* Copy the `source` to `index.html`

### Deploy and Serve
* Fork the repository as `<your-github-username>.github.io`
* Modify `index.html` and see the changes live on `https://<your-github-username>.github.io`

### TODO
* Use a structured JSON file as the backend for the content
* Write scripts to:
    * Automatically generate the index.html and other static files and pages
    * Generate the `pdf` format of the resume
