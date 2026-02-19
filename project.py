import imageio.v3 as iio
from pathlib import Path
images = [iio.imread(f) for f in Path('.').glob('team-pic*.png')]
iio.imwrite('team.gif', images, duration=500, loop=0)
