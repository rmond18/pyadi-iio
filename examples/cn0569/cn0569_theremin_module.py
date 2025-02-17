# Copyright (C) 2021 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import math
import time

import adpd2140_gesture_sensor
import numpy as np
import simpleaudio as sa

sample_rate = 44100
T = 1
t = np.linspace(0, T, T * sample_rate, False)

freq_c4 = 65.41
freq_d4 = 73.42
freq_e4 = 82.41
freq_f4 = 87.31
freq_g4 = 98.00

freq_c5 = 130.81
freq_d5 = 146.83
freq_e5 = 164.81
freq_f5 = 174.61
freq_g5 = 196.00

note_c4 = np.sin(freq_c4 * t * 2 * np.pi)
note_d4 = np.sin(freq_d4 * t * 2 * np.pi)
note_e4 = np.sin(freq_e4 * t * 2 * np.pi)
note_f4 = np.sin(freq_f4 * t * 2 * np.pi)
note_g4 = np.sin(freq_g4 * t * 2 * np.pi)

note_c5 = np.sin(freq_c5 * t * 2 * np.pi)
note_d5 = np.sin(freq_d5 * t * 2 * np.pi)
note_e5 = np.sin(freq_e5 * t * 2 * np.pi)
note_f5 = np.sin(freq_f5 * t * 2 * np.pi)
note_g5 = np.sin(freq_g5 * t * 2 * np.pi)

norm_c4 = note_c4 * 32767 / np.max(np.abs(note_c4))
norm_c4 = norm_c4.astype(np.int16)
norm_d4 = note_d4 * 32767 / np.max(np.abs(note_d4))
norm_d4 = norm_d4.astype(np.int16)
norm_e4 = note_e4 * 32767 / np.max(np.abs(note_e4))
norm_e4 = norm_e4.astype(np.int16)
norm_f4 = note_f4 * 32767 / np.max(np.abs(note_f4))
norm_f4 = norm_f4.astype(np.int16)
norm_g4 = note_g4 * 32767 / np.max(np.abs(note_g4))
norm_g4 = norm_g4.astype(np.int16)

norm_c5 = note_c5 * 32767 / np.max(np.abs(note_c5))
norm_c5 = norm_c5.astype(np.int16)
norm_d5 = note_d5 * 32767 / np.max(np.abs(note_d5))
norm_d5 = norm_d5.astype(np.int16)
norm_e5 = note_e5 * 32767 / np.max(np.abs(note_e5))
norm_e5 = norm_e5.astype(np.int16)
norm_f5 = note_f5 * 32767 / np.max(np.abs(note_f5))
norm_f5 = norm_f5.astype(np.int16)
norm_g5 = note_g5 * 32767 / np.max(np.abs(note_g5))
norm_g5 = norm_g5.astype(np.int16)

theremin_args0 = [norm_c4, norm_d4, norm_e4, norm_f4, norm_g4]
theremin_args1 = [norm_c5, norm_d5, norm_e5, norm_f5, norm_g5]

if __name__ == "__main__":

    adpd2140_pmod = adpd2140_gesture_sensor.adpd2140_gesture_sensor(uri="serial:COM4")
    adpd2140_pmod.rx_buffer_size = 8
    # adpd2140_pmod.sample_rate = 512
    adpd2140_pmod.gain_calibration()

    gestures = [
        "CLICK_0",
        "UP_0",
        "DOWN_0",
        "LEFT_0",
        "RIGHT_0",
        "CLICK_1",
        "UP_1",
        "DOWN_1",
        "LEFT_1",
        "RIGHT_1",
    ]

    while True:
        gesture0 = adpd2140_pmod.get_gesture_0()
        gesture1 = adpd2140_pmod.get_gesture_1()
        if gesture0 >= 0:
            print(gestures[gesture0])
            sa.play_buffer(theremin_args0[gesture0], 1, 2, sample_rate)
        if gesture1 >= 0:
            print(gestures[gesture1 + 4])
            sa.play_buffer(theremin_args1[gesture1], 1, 2, sample_rate)
