# Liu2022.NGC1365
Some tools used in https://arxiv.org/abs/2212.09652


## Fixing Saturated Pixels

### Create Webb PSF

See `scripts/a_dzliu_code_make_webbpsf_miri_fov20as.py`


### Match the PSF wing to the data at fixed location

See `Jupyter_Notebook/analyze_ngc1365_miri_psf_webbpsf.ipynb`

Manually adjust the file paths `/Users/*/Data/*/` to yours, and set the fixed location with this variable:

```
star_ra_dec = 'YOUR_RA YOUR_DEC'
```

If the input images have some wcs alignment issue, adjust this dictionary:

```
wcs_shifts['MIRI F770W'] = (0.0 * u.arcsec, 0.0 * u.arcsec)
```

This step will produce radial flux profile figures in the Jupyter Notebook and a JSON file containing the fitted flux scaling of the PSF at the fixed location. 

The fitting of the radial profile is kind of tricky because we want to capture the overall wing normalization meanwhile not to be affected by the inner partially saturated pixels. 

### Apply the PSF scaling to the data at fixed location

Once we have the JSON files containing the flux scaling of PSFs at fixed locations, we can apply them to the real data to fix the saturated pixels with the PSF model. This involves some interpolation in the non-saturated and partially saturated area, to avoid aliasing issue. 

See this: `Jupyter_Notebook/analyze_ngc1365_fix_saturated_pixels.ipynb`. 

Also do not forget to manually set JSON file names `json_file` and some file paths. 



