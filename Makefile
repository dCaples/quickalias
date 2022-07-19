install:
	mkdir -p $(DESTDIR)$(PREFIX)/usr/local/bin
	install -Dm755 ./quickalias.py "$(DESTDIR)$(PREFIX)/usr/local/bin/quickalias"

uninstall:
	rm -f "$(DESTDIR)$(PREFIX)/usr/local/bin/quickalias"