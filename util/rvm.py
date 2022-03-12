import scipy.io as io
import numpy as np


def load_css(camera):
    if camera == 'CSS_15S5C':
        css_nir = io.loadmat('./spectral-data/CSS_15S5C_NoIRCut_700_10_1100.mat')['SSF_700_10_1100'][:, :-10]
    if camera == 'CSS_13S2C':
        css_nir = io.loadmat('./spectral-data/CSS_13S2C_NoIRCut_600_10_1000.mat')['SSF_600_10_1000'][:, 10:]
    if camera == 'EO_2113C':
        css_nir = io.loadmat('./spectral-data/EO_2113C_NoIRCut_600_10_1000.mat')['SSF_600_10_1000'][:, 10:]
    return css_nir


tpc = io.loadmat('./spectral-data/TSC.mat')['tpc'][0][0][1]
tpc = tpc[28:, :]
led_nir = io.loadmat('./spectral-data/NLS.mat')['led'][28:, 17:]
css = ['CSS_15S5C', 'CSS_13S2C', 'EO_2113C']
for c in css:
    css_nir = load_css(c)
    color_in_led = np.zeros((led_nir.shape[1], css_nir.shape[0], tpc.shape[1]))
    wls = tpc.shape[0]
    for num in range(led_nir.shape[1]):
        for ch in range(css_nir.shape[0]):
            for color in range(tpc.shape[1]):
                for wl in range(wls):
                    color_in_led[num, ch, color] += tpc[wl, color]*led_nir[wl, num]*css_nir[ch, wl]

    dict = []
    for l1 in np.arange(0, 1.01, 0.1):
     for l2 in np.arange(0, 1.01-l1, 0.1):
      for l3 in np.arange(0, 1.01-l1-l2, 0.1):
       for l4 in np.arange(0, 1.01-l1-l2-l3, 0.1):
        for l5 in np.arange(0, 1.01-l1-l2-l3-l4, 0.1):
         for l6 in np.arange(0, 1.01-l1-l2-l3-l4-l5, 0.1):
          for l7 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6, 0.1):
           for l8 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6-l7, 0.1):
            for l9 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6-l7-l8, 0.1):
             for l10 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6-l7-l8-l9, 0.1):
              for l11 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6-l7-l8-l9-l10, 0.1):
               for l12 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6-l7-l8-l9-l10-l11, 0.1):
                for l13 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6-l7-l8-l9-l10-l11-l12, 0.1):
                 for l14 in np.arange(0, 1.01-l1-l2-l3-l4-l5-l6-l7-l8-l9-l10-l11-l12-l13, 0.1):
                  leds = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14]
                  color = np.zeros((3, 24))
                  num = 0
                  for led in leds:
                   color += color_in_led[num, :, :]*led
                   num += 1
                  var_led = np.var(color, axis=0)
                  dict.append([np.array(leds), var_led])

    tmp = [0 for i in range(len(dict))]

    for i in range(len(dict)):
        var = dict[i][1]
        count = 0
        for x in var:
            if x > 0.1:
                count += 1
        tmp[i] = count
    m = max(tmp)
    max_idx = [i for i in range(len(tmp)) if tmp[i] == m]

    final_l = []
    for idx in max_idx:
        final_l.append(dict[idx][0])
    final = np.mean(final_l, axis=0)
    print(c, ":", final)
