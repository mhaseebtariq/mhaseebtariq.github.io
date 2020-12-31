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
* Modify the content in the `templates/*.html` files accordingly
* Access http://127.0.0.1:8000/
* Run `python manage.py runscript export_pages` to update all the `*.html` files residing in the project root
  - See: resume/builder/jobs/export_pages.py

### Deploy and Serve
* Fork the repository as `<your-github-username>.github.io`
* Modify the `templates/*.html` files accordingly
* `python manage.py runscript export_pages`
  - See: resume/builder/jobs/export_pages.py
* See the changes live on `https://<your-github-username>.github.io`

### TODO
* Use a structured JSON file as the backend for the content
* Write script to generate the `pdf` format of the resume
