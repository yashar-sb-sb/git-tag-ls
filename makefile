install: FORCE
	pip3 install colorama
	cp tags.py /usr/bin/tags
	chmod +x /usr/bin/tags

FORCE:
