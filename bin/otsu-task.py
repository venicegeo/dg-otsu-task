# Copyright 2017, DigitalGlobe, Inc.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.

import glob2

import beachfront.process as bfproc
import gippy

from gbdx_task_interface import GbdxTaskInterface


class OtsuTask(GbdxTaskInterface):
    gbdx_connection = None

    def invoke(self):

        # Get inputs
        img = self.get_input_data_port('image')

        # calculate optimal threshold
        all_lower = glob2.glob('%s/**/*.tif' % img)

        for img_file in all_lower:
            geoimg = gippy.GeoImage(img_file, True)
            threshold = bfproc.otsu_threshold(geoimg[0])
            self.set_output_string_port('threshold', threshold)
            print "Otsu's threshold = ",  threshold

        self.reason = 'Successfully computed Otsu threshold'


if __name__ == "__main__":
    with OtsuTask() as task:
        task.invoke()
