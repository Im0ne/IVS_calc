PYTHON=python
CALC=calculator.py
ARCHIVE=xonufr00_xshele02_xslysa00_xbalat00
TESTS=math_tests.py
DOXYFILE=Doxyfile
PROFILE=profiling.py

all: $(CALC)
	$(PYTHON) $(CALC)

pack:
	mkdir ../../$(ARCHIVE)/doc
	cp $(DOXYFILE) ../../$(ARCHIVE)/doc
	cp -r ../install ../../$(ARCHIVE)
	cp -r .. ../../$(ARCHIVE)/repo
	cd ../..; zip -r $(ARCHIVE).zip $(ARCHIVE)
	rm -r ../../$(ARCHIVE)

clean:
	rm -r ../.idea
	rm -r html
	rm -r latex
	rm -r __pycache__
	rm -r build
	rm -r dist
	rm IVS_calc.spec

test: $(TESTS)
	$(PYTHON) -m unittest $(TESTS)

doc: $(DOXYFILE)
	doxygen

run: $(CALC)
	$(PYTHON) $(CALC)

profile: $(PROFILE)
	$(PYTHON) $(PROFILE)
