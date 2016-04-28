ZIP_FILE = GadgetronSketchBook.zip
DOC_CONFIG = doc_config.doxy
zip:
	zip -r $(ZIP_FILE) libraries/*
upload: docs
	scp -r html/ acsweb.ucsd.edu:public_html/secret/NVSL/
docs:
	doxygen $(DOC_CONFIG)
clean:
	rm -f $(ZIP_FILE)
	rm -rf html/
