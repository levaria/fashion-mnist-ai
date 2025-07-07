#Fashion MNIST Classifier - Progetto d'esame IA

**Nome:** valeria Druta  
**Matricola:** VR502998  
**Corso:** Sviluppo e ciclo vitale di software di intelligenza artificiale  
**Repository GitHub:** https://github.com/tuo-username/fashion-mnist-ai

---

##Dataset

- **Nome:** Fashion-MNIST  
- **Fonte:** [Kaggle - Zalando Research](https://www.kaggle.com/datasets/zalando-research/fashionmnist)  
- **Descrizione:** Immagini in scala di grigi (28x28) di articoli di abbigliamento in 10 classi (T-shirt, scarpe, borse, ecc.)

---

##Modello

- **Architettura:** Convolutional Neural Network (CNN)
- **Libreria:** PyTorch
- **File:** [`model/cnn.py`](model/cnn.py)

---

## Struttura del progetto

fashion-mnist-ai/
├── app/ ← Interfaccia Gradio
├── data/ ← Script di download 
├── model/ ← Modello, training, evaluation
├── tests/ ← Test unitari
├── .github/workflows ← CI/CD con GitHub Actions
├── Dockerfile ← Per dockerizzare il training
├── setup.py ← Pacchetto Python installabile
├── requirements.txt ← Dipendenze
└── README.md ← Questo file
