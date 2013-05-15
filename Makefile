dev: setup
	venv/bin/python setup.py py2app -A
	open 'dist/Cyberduck patch for ucloud storage.app'

release: setup
	rm -rf dist build patch.zip
	venv/bin/python setup.py py2app
	(cd dist;  zip -r ../patch.zip .)

setup: venv
	venv/bin/python setup.py develop
venv:
	virtualenv venv
clean:
	rm -rf venv *.egg *.egg-info dist build

.PHONY: setup
