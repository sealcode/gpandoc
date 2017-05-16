ZIP = zip
PYUIC = pyuic5
UIS = ui/settings.py \
	  ui/about.py \
	  ui/help.py \
	  ui/howto.py \
	  ui/mainwindow.py \
	  ui/question.py \
	  ui/sets.py \
	  ui/variables.py \
	  ui/recipe.py
RECIPES =  recipes/doc.zip \
		   recipes/docx.zip \
		   recipes/epub.zip \
		   recipes/pdf-a4.zip \
		   recipes/pdf-a5.zip

.PHONY: clean clean_recipes clean_uis
all: $(RECIPES) $(UIS)
clean: clean_recipes clean_uis

recipes/%.zip: recipes/%
	$(ZIP) -r $@ $<

ui/%.py: ui/%.ui
	$(PYUIC) $< > $@

clean_recipes:
	rm -v recipes/*.zip

clean_uis:
	rm -v ui/*.py
