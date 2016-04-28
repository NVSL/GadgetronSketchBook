ZIP_FILE = GadgetronSketchBook.zip
zip:
	zip -r $(ZIP_FILE) libraries/*
clean:
	rm $(ZIP_FILE)
