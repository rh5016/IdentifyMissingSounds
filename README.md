Using Meta's Hybrid-Transformer Demucs to identify missing instruments/stems from input audio using RMS threshold. See https://github.com/facebookresearch/demucs <br>
Then classifies genre using Convolutional Neural Network (With Regularization and Data Augmentation) from https://github.com/crlandsc/Music-Genre-Classification-Using-Convolutional-Neural-Networks




To run indentification & classification:
```javascript
function test() {
  console.log("python stems_checker.py /path/to/your/wav");
}
