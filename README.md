Using Meta's Hybrid-Transformer Demucs to identify missing instruments/stems from input audio using RMS threshold. See https://github.com/facebookresearch/demucs <br>
Then classifies genre using Convolutional Neural Network (With Regularization and Data Augmentation) from https://github.com/crlandsc/Music-Genre-Classification-Using-Convolutional-Neural-Networks <br>
Only supports wav files




To run indentification & classification:
```
python stems_checker.py /path/to/your/audio.wav
