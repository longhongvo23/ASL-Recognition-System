import tkinter as tk
from tkinter import ttk
import cv2
import PIL.Image, PIL.ImageTk
import numpy as np
from keras.models import load_model

class SignLanguageApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Sign Language Detection")
        
        # Load model và labels
        self.model = load_model("keras_model.h5", compile=False)
        self.class_names = open("labels.txt", "r").readlines()
        
        # Kích thước ROI (Region of Interest)
        self.ROI_size = 224
        self.ROI_offset_x = 50  # Offset từ center
        self.ROI_offset_y = 0   # Offset từ center
        
        # Setup camera
        self.camera = cv2.VideoCapture(0)
        
        # Tạo container cho video
        self.video_frame = ttk.Frame(window)
        self.video_frame.pack(pady=10)
        
        # Label để hiển thị video
        self.video_label = ttk.Label(self.video_frame)
        self.video_label.pack()
        
        # Label để hiển thị kết quả
        self.result_label = ttk.Label(window, text="Detected Sign: None", 
                                    font=('Arial', 20))
        self.result_label.pack(pady=10)
        
        # Button để thoát
        self.quit_button = ttk.Button(window, text="Quit", 
                                    command=self.quit_app)
        self.quit_button.pack(pady=10)
        
        # Bắt đầu cập nhật video
        self.update_video()
    
    def update_video(self):
        ret, frame = self.camera.read()
        if ret:
            # Lật frame để hiển thị như gương
            frame = cv2.flip(frame, 1)
            
            # Lấy kích thước frame
            height, width = frame.shape[:2]
            center_x = width // 2
            center_y = height // 2
            
            # Tính toán vị trí ROI
            roi_x1 = center_x - self.ROI_size // 2 + self.ROI_offset_x
            roi_y1 = center_y - self.ROI_size // 2 + self.ROI_offset_y
            roi_x2 = roi_x1 + self.ROI_size
            roi_y2 = roi_y1 + self.ROI_size
            
            # Vẽ khung ROI
            cv2.rectangle(frame, (roi_x1, roi_y1), (roi_x2, roi_y2), 
                         (0, 255, 0), 2)
            
            # Cắt vùng ROI và xử lý
            roi = frame[roi_y1:roi_y2, roi_x1:roi_x2]
            if roi.size != 0:
                # Chuẩn bị ảnh cho model
                processed_roi = cv2.resize(roi, (224, 224))
                normalized_roi = np.asarray(processed_roi, dtype=np.float32).reshape(1, 224, 224, 3)
                normalized_roi = (normalized_roi / 127.5) - 1
                
                # Dự đoán
                prediction = self.model.predict(normalized_roi, verbose=0)
                index = np.argmax(prediction)
                class_name = self.class_names[index]
                confidence_score = prediction[0][index]
                
                # Hiển thị kết quả
                result_text = f"Sign: {class_name[2:].strip()} ({str(np.round(confidence_score * 100))[:-2]}%)"
                self.result_label.config(text=result_text)
                
                # Vẽ kết quả lên frame
                cv2.putText(frame, result_text, (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Chuyển frame sang format để hiển thị trong Tkinter
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = PIL.Image.fromarray(cv2image)
            imgtk = PIL.ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        
        # Cập nhật frame tiếp theo sau 10ms
        self.window.after(10, self.update_video)
    
    def quit_app(self):
        self.camera.release()
        self.window.quit()

# Khởi tạo ứng dụng
root = tk.Tk()
app = SignLanguageApp(root)
root.mainloop()