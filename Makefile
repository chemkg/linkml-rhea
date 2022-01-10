REPO = linkml-rhea
NAME = rhea
RUN = poetry run
SCHEMADIR = .
SRC = $(SCHEMADIR)/$(NAME).yaml

project:
	$(RUN) gen-project -d schema $(SRC) && mv schema/rhea.py linkml_rhea

doc:
	$(RUN) gen-markdown -d docs $(SRC) > docs/index.md
