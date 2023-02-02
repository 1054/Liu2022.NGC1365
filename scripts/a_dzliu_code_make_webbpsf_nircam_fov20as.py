#!/usr/bin/env python
import os, shutil
os.environ['WEBBPSF_PATH'] = 'webbpsf-data'
import webbpsf
fov_arcsec = 20.0
for oversample in [1, 5, 10]:
    for filter_name in ['F115W', 'F200W', 'F300M', 'F335M', 'F356W', 'F360M']:
        nc = webbpsf.NIRCam()
        nc.filter = filter_name
        nc.options['parity'] = 'odd' # default
        output_file = f"webbpsf_NIRCam_{filter_name}_fov{fov_arcsec:g}as"
        if oversample > 1:
            output_file += f"_oversamp{oversample}"
        output_file += ".fits"
        if os.path.isfile(output_file):
            shutil.move(output_file, output_file+'.backup')
        psf = nc.calc_psf(output_file, fov_arcsec=fov_arcsec, oversample=oversample)
        print(f"Output to {output_file}")


