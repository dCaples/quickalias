defualt: install

install:
	mkdir -p $(DESTDIR)$(PREFIX)/usr/local/bin
	install -Dm755 ./quickalias.py "$(DESTDIR)$(PREFIX)/usr/local/bin/quickalias"

package: clean
	python3 setup.py sdist bdist_wheel --universal


upload: package
	twine upload dist/* --repository quickalias

clean:
	rm -rf dist build *.egg-info
uninstall:
	rm -f "$(DESTDIR)$(PREFIX)/usr/local/bin/quickalias"