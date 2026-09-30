.PHONY: install train app notebook clean all help

help:
	@echo "Anti-SCAM Flooz Lite — AI4Youth 2026"
	@echo "  make install  : pip install -r requirements.txt"
	@echo "  make train    : python train.py (regenere modeles + metriques)"
	@echo "  make app      : streamlit run app.py (demo SCAM/HAM)"
	@echo "  make notebook : jupyter notebook notebook.ipynb"
	@echo "  make clean    : supprime artefacts regenerables"

install:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt

train:
	./venv/bin/python train.py

app:
	./venv/bin/streamlit run app.py

notebook:
	./venv/bin/jupyter notebook notebook.ipynb

clean:
	rm -f *.joblib eda_*.png confusion_*.png
	rm -rf __pycache__ .ipynb_checkpoints

all: install train
