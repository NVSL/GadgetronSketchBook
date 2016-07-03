ZIP_FILE = GadgetronSketchBook.zip
DOC_CONFIG = doc_config.doxy
zip: libraries/
	zip -r $(ZIP_FILE) libraries/*
libraries/:
	true
	make -C CreateDocs
clean:
	rm -f $(ZIP_FILE)
	rm -rf html/
	rm -rf xml/
