import numpy as np
import librosa
from tensorflow.keras.models import load_model

# List of genres in the same order as the training labels
GENRES = [
    "blues","classical","country","disco","hiphop",
    "jazz","metal","pop","reggae","rock"
]

def preprocess(audio_path, duration=3.0, sr=22050, n_mfcc=12):
    # Load exactly `duration` seconds
    y, _ = librosa.load(audio_path, sr=sr, mono=True, duration=duration)
    # Compute MFCCs with the same hyperparams used in training
    mfcc = librosa.feature.mfcc(
        y=y,
        sr=sr,
        n_mfcc=n_mfcc,
        n_fft=2048,
        hop_length=512
    )
    # Shape → (1, n_mfcc, time_frames, 1)
    mfcc = mfcc[np.newaxis, ..., np.newaxis]
    return mfcc

def predict_genre(audio_path, model_path="models/model_cnn3.h5"):
    model = load_model(model_path)
    X = preprocess(audio_path)
    preds = model.predict(X)
    idx = int(np.argmax(preds, axis=1)[0])
    return GENRES[idx]

if __name__ == "__main__":
    import sys
    track = sys.argv[1]
    genre = predict_genre(track)
    print(f"Predicted genre: {genre}")
