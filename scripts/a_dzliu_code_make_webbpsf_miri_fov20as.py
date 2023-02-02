#!/usr/bin/env python
import os, shutil
os.environ['WEBBPSF_PATH'] = 'webbpsf-data'
import webbpsf
fov_arcsec = 20.0
for oversample in [1, 5, 10]:
    for filter_name in ['F770W', 'F1000W', 'F1130W', 'F2100W']:
        nc = webbpsf.MIRI()
        nc.filter = filter_name
        nc.options['parity'] = 'odd' # default
        output_file = f"webbpsf_MIRI_{filter_name}_fov{fov_arcsec:g}as"
        if oversample > 1:
            output_file += f"_oversamp{oversample}"
        output_file += ".fits"
        if os.path.isfile(output_file):
            shutil.move(output_file, output_file+'.backup')
        psf = nc.calc_psf(output_file, fov_arcsec=fov_arcsec, oversample=oversample)
        print(f"Output to {output_file}")


