.PHONY: install train app notebook clean all help

help:
	@echo "Anti-SCAM Flooz Lite — AI4Youth 2026"
	@echo "  make install  : pip install -r requirements.txt"
	@echo "  make train    : python train.py (regenere modeles + metriques)"
	@echo "  make app      : streamlit run app.py (demo SCAM/HAM)"
	@echo "  make notebook : jupyter notebook notebook.ipynb"
	@echo "  make clean    : supprime artefacts regenerables"

install:
	pip install -r requirements.txt || pip install --break-system-packages -r requirements.txt

train:
	python train.py

app:
	streamlit run app.py

notebook:
	jupyter notebook notebook.ipynb

clean:
	rm -f *.joblib eda_*.png confusion_*.png
	rm -rf __pycache__ .ipynb_checkpoints

all: install train
