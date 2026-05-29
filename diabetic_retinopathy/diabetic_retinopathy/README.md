# 👁️ Diabetic Retinopathy Detection (CNN)
> A deep learning pipeline to classify diabetic retinopathy severity from retinal fundus images using the IDRiD dataset.

## 📁 Project Structure
```
diabetic_retinopathy/
├── data/
│   ├── raw/          → Original IDRiD images
│   ├── processed/    → Resized & preprocessed images
│   └── augmented/    → Augmented training samples
├── models/           → Saved .h5 / .keras model files
├── notebooks/        → EDA & training notebooks
├── src/              → Core source scripts
├── results/          → Metrics, confusion matrix, plots
└── utils/            → Helper functions
```

## 🧠 Model
- **Architecture:** EfficientNetB3 (Transfer Learning) + Custom Head
- **Task:** 5-class classification (0: No DR → 4: Proliferative DR)
- **Dataset:** IDRiD (Indian Diabetic Retinopathy Image Dataset)

## ⚙️ Setup
```bash
pip install -r requirements.txt
```

## 🚀 Run
```bash
# Preprocess data
python src/preprocess.py

# Train model
python src/train.py

# Evaluate
python src/evaluate.py
```

## 📊 Classes (IDRiD Grading)
| Grade | Description |
|-------|-------------|
| 0 | No DR |
| 1 | Mild DR |
| 2 | Moderate DR |
| 3 | Severe DR |
| 4 | Proliferative DR |
