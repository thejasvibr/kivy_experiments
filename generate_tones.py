#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: autumn
"""
import numpy as np 
import soundfile as sf

fs = 44100
durn =  0.1
t = np.linspace(0,durn,int(fs*durn))

freq = 4000

tone = np.sin(2*np.pi*freq*t)
tone *= np.hanning(tone.size)

sf.write('base_tone.wav', tone,fs)


