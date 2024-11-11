import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt
import whisper
from llm_module import LLMModule

class OccupationalTherapistApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_llm_model()
        self.load_whisper_model()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter medical record or patient form here...")
        layout.addWidget(self.input_text)

        button_layout = QHBoxLayout()
        self.text_button = QPushButton("Process Text")
        self.text_button.clicked.connect(self.process_text)
        button_layout.addWidget(self.text_button)

        self.voice_button = QPushButton("Choose Voice File")
        self.voice_button.clicked.connect(self.choose_voice_file)
        button_layout.addWidget(self.voice_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)
        self.setWindowTitle('Dummy Ann: Occupational Therapist Assistant')
        self.setGeometry(300, 300, 600, 400)

    def load_llm_model(self):
        self.llm_module = LLMModule()

    def load_whisper_model(self):
        # Load Whisper model (download the model or use a locally available one)
        self.whisper_model = whisper.load_model("base")  # Change model as needed (e.g., "tiny", "small", "base", "large")

    def process_text(self):
        input_text = self.input_text.toPlainText()
        rephrased_text = self.llm_module.generate_response(input_text)
        self.output_text.setPlainText(rephrased_text)

    def clear_text(self):
        self.input_text.clear()
        self.output_text.clear()

    def choose_voice_file(self):
        # Open a file dialog to let the user choose an audio file
        file_path, _ = QFileDialog.getOpenFileName(self, "Choose Audio File", "", "Audio Files (*.wav *.mp3 *.m4a *.flac)")

        if file_path:  # If the user selected a file
            # Transcribe the selected audio file
            result = self.whisper_model.transcribe(file_path)
            transcription_text = result["text"]

            # Update input_text with transcription and call process_text
            self.input_text.setPlainText(transcription_text)
            self.process_text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OccupationalTherapistApp()
    ex.show()
    sys.exit(app.exec_())