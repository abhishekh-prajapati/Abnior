import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QRect, QPoint, pyqtProperty
from PyQt6.QtGui import QColor, QPainter, QBrush, QPen, QFont

class AIDesign(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # UI Properties
        self.size_scale = 1.0
        self.status = "IDLE" # IDLE, LISTENING, SPEAKING
        
        # Main label
        self.label = QLabel("ABNIOR", self)
        self.label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Position at top center
        screen = QApplication.primaryScreen().geometry()
        self.resize(100, 100)
        self.move(int((screen.width() - self.width()) / 2), 10)
        
        # Animation timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(50)
        
        self.animation_step = 0

    @pyqtProperty(float)
    def pulsate(self):
        return self.size_scale

    @pulsate.setter
    def pulsate(self, value):
        self.size_scale = value
        self.update()

    def update_animation(self):
        self.animation_step += 1
        if self.status == "LISTENING":
            # Pulsing logic
            import math
            self.size_scale = 1.0 + 0.1 * math.sin(self.animation_step * 0.2)
        elif self.status == "SPEAKING":
            # Waveform-like logic?
            import math
            self.size_scale = 1.0 + 0.05 * math.sin(self.animation_step * 0.5)
        else:
            self.size_scale = 1.0
        
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Glow Effect
        color = QColor(0, 150, 255, 150) # Blue glow
        if self.status == "LISTENING":
            color = QColor(255, 0, 100, 150) # Red/pink listening
        elif self.status == "SPEAKING":
            color = QColor(0, 255, 100, 150) # Green speaking
            
        painter.setBrush(QBrush(color))
        painter.setPen(Qt.PenStyle.NoPen)
        
        r = int(40 * self.size_scale)
        cx, cy = int(self.width() / 2), int(self.height() / 2)
        painter.drawEllipse(QPoint(cx, cy), r, r)
        
        # Inner Core
        painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
        painter.drawEllipse(QPoint(cx, cy), 15, 15)

    def set_status(self, status):
        self.status = status
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AIDesign()
    window.show()
    sys.exit(app.exec())
