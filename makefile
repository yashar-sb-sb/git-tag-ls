install: FORCE
	python3 -m pip install colorama
	cp tags.py /usr/bin/tags
	chmod +x /usr/bin/tags

FORCE:
