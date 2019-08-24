# Copyright (C) 2019 Analog Devices, Inc.
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

from adi.adrv9009 import adrv9009


class adrv9009_zu11eg(adrv9009):
    """ ADRV9009-ZU11EG System-On-Module """

    rx_channel_names = [
        "voltage0_i",
        "voltage0_q",
        "voltage1_i",
        "voltage1_q",
        "voltage2_i",
        "voltage2_q",
        "voltage3_i",
        "voltage3_q",
    ]
    tx_channel_names = [
        "voltage0",
        "voltage1",
        "voltage2",
        "voltage3",
        "voltage4",
        "voltage5",
        "voltage6",
        "voltage7",
    ]
    device_name = ""
    rx_enabled_channels = [0, 1]
    tx_enabled_channels = [0, 1]

    def __init__(self, uri=""):
        adrv9009.__init__(self, uri=uri)
        self.ctrl_b = self.ctx.find_device("adrv9009-phy-b")

    @property
    def gain_control_mode_chip_b(self):
        """gain_control_mode_chip_b: Mode of receive path AGC. Options are:
        slow_attack, manual"""
        return self.get_iio_attr("voltage0", "gain_control_mode", False, self.ctrl_b)

    @gain_control_mode_chip_b.setter
    def gain_control_mode_chip_b(self, value):
        self.set_iio_attr_str(
            "voltage0", "gain_control_mode", False, value, self.ctrl_b
        )

    @property
    def rx_hardwaregain_chan0_chip_b(self):
        """rx_hardwaregain: Gain applied to RX path channel 0. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self.get_iio_attr("voltage0", "hardwaregain", False, self.ctrl_b)

    @rx_hardwaregain_chan0_chip_b.setter
    def rx_hardwaregain_chan0_chip_b(self, value):
        if self.gain_control_mode_chip_b == "manual":
            self.set_iio_attr("voltage0", "hardwaregain", False, value, self.ctrl_b)

    @property
    def rx_hardwaregain_chan1_chip_b(self):
        """rx_hardwaregain: Gain applied to RX path channel 1. Only applicable when
        gain_control_mode is set to 'manual'"""
        return self.get_iio_attr("voltage1", "hardwaregain", False, self.ctrl_b)

    @rx_hardwaregain_chan1_chip_b.setter
    def rx_hardwaregain_chan1_chip_b(self, value):
        if self.gain_control_mode_chip_b == "manual":
            self.set_iio_attr("voltage1", "hardwaregain", False, value, self.ctrl_b)

    @property
    def tx_hardwaregain_chan0_chip_b(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 0"""
        return self.get_iio_attr("voltage0", "hardwaregain", True, self.ctrl_b)

    @tx_hardwaregain_chan0_chip_b.setter
    def tx_hardwaregain_chan0_chip_b(self, value):
        self.set_iio_attr("voltage0", "hardwaregain", True, value, self.ctrl_b)

    @property
    def tx_hardwaregain_chan1_chip_b(self):
        """tx_hardwaregain: Attenuation applied to TX path channel 1"""
        return self.get_iio_attr("voltage1", "hardwaregain", True, self.ctrl_b)

    @tx_hardwaregain_chan1_chip_b.setter
    def tx_hardwaregain_chan1_chip_b(self, value):
        self.set_iio_attr("voltage1", "hardwaregain", True, value, self.ctrl_b)

    @property
    def rx_rf_bandwidth_chip_b(self):
        """rx_rf_bandwidth: Bandwidth of front-end analog filter of RX path"""
        return self.get_iio_attr("voltage0", "rf_bandwidth", False, self.ctrl_b)

    @property
    def tx_rf_bandwidth_chip_b(self):
        """tx_rf_bandwidth: Bandwidth of front-end analog filter of TX path"""
        return self.get_iio_attr("voltage0", "rf_bandwidth", True, self.ctrl_b)

    @property
    def rx_sample_rate_chip_b(self):
        """rx_sample_rate: Sample rate RX path in samples per second"""
        return self.get_iio_attr("voltage0", "sampling_frequency", False, self.ctrl_b)

    @property
    def tx_sample_rate_chip_b(self):
        """tx_sample_rate: Sample rate TX path in samples per second"""
        return self.get_iio_attr("voltage0", "sampling_frequency", True, self.ctrl_b)

    @property
    def trx_lo_chip_b(self):
        """trx_lo: Carrier frequency of TX and RX path"""
        return self.get_iio_attr("altvoltage0", "frequency", True, self.ctrl_b)

    @trx_lo_chip_b.setter
    def trx_lo_chip_b(self, value):
        self.set_iio_attr("altvoltage0", "frequency", True, value, self.ctrl_b)
