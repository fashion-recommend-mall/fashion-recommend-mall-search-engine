elasticsearch:
	docker-compose up -d

data:
	python3 app.py

typehint: 
	mypy ./ --ignore-missing-imports

lint: 
	pylint \
	--disable=R0801 \
	--disable=R0903 \
	--disable=C0325 \
	--disable=E0401 \
	--disable=R0902 \
	--disable=R0913 \
	./src

checklist : typehint lint

set_elasticsearch: elasticsearch
insert_data: checklist data


.PHONY: elasticsearch data run checklist