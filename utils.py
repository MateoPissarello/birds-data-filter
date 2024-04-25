import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import Audio

def show_image(path:str) -> None:
  img = mpimg.imread(path)
  plt.imshow(img)
  plt.axis('off')
  plt.show()

def load_audio(wav_id: str) -> None:
  audio_path = f"/home/pissarello-dev/Universidad/HPC/parcial-2/wavfiles_filtered/{wav_id}.wav"
  return Audio(audio_path, autoplay=True)



