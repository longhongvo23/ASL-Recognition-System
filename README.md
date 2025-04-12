```markdown
# 🖐️ ASL Recognition System

An AI-based real-time **American Sign Language (ASL) recognition system** using a deep learning model built with [Teachable Machine by Google](https://teachablemachine.withgoogle.com/)
and deployed with Python. This project utilizes a webcam to detect and classify hand signs into ASL letters or gestures using a pre-trained Keras model.

---

## 📌 Features

- ✋ Real-time ASL hand sign recognition via webcam  
- 🤖 Deep learning model (`keras_model.h5`) trained using Google Teachable Machine  
- 💡 Simple and intuitive interface  
- 🔍 High accuracy with common ASL gestures (can be extended)  
- 🔁 Easily updatable with custom classes and retrained models  

---

## 🧠 Tech Stack

- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **Teachable Machine (Google)**
- **Pillow**
- **NumPy**

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/longhongvo23/ASL-Recognition-System.git
   cd ASL-Recognition-System
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Run the App

Make sure your webcam is enabled.

```bash
python app.py
```

---

## 🧪 Model Training

The model (`keras_model.h5`) was trained using [Google Teachable Machine](https://teachablemachine.withgoogle.com/). You can:
- Retrain with your own hand signs.
- Export a new `keras_model.h5` and `labels.txt`.
- Replace the existing files to use your custom model.

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/cf46ccd0-fc53-46de-9a6d-4ca353a66306)  
![image](https://github.com/user-attachments/assets/88ab2880-19ca-4a4c-ad2d-5064c026a0e6)

---

## 📝 Requirements

```txt
opencv-python
Pillow
numpy
keras
tensorflow
```

Or use the provided `requirements.txt`.

---

## 💡 Future Improvements

- Add GUI using Streamlit or Tkinter  
- Support more sign languages (e.g. BSL, VSL)  
- Deploy as a web app with Flask or FastAPI  
- Add audio output for recognized signs  

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- [Google Teachable Machine](https://teachablemachine.withgoogle.com/)
- [TensorFlow](https://www.tensorflow.org/)
- [OpenCV](https://opencv.org/)

---

Made with ❤️ for accessible communication.
```

---
