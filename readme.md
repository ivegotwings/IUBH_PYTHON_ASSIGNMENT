<h2>Journal</h2>
<p>Includes is journal.ipynb, a jupiter notebook that contains the write up journal for the written assignment</p>
<p>Also journal.pdf is included for convinience.</p>

<h2>Code</h2>
<p>Core module contains the tools to load and clean data</p>
<p>The stat module contains the statistical methods required for the task such as leastSquared</p>
<p>The main program generates print and csv outputs</p>

<b>data > output  folder</b> has 5 csv
<ul
    <li>4 csv files correspond to each ideal function</li>
    <li>output.csv contains the collaborated information from running</li>
    <li>each test data across the selected ideal functions and the final results of counts.</li>
</ul>

<h2>Set up</h2>
    1. Clone the develop branch
    2. Install the required packages
        pandas
        numpy
        matplotlib

conda version : 4.10.3
Use miniconda to set up an environment

Or you can install these packages
# packages in environment at /Users/sh.kumar/opt/miniconda3:
```
appnope                   0.1.2           py39hecd8cb5_1001  
backcall                  0.2.0              pyhd3eb1b0_0  
blas                      1.0                         mkl  
bottleneck                1.3.2            py39he3068b8_1  
brotlipy                  0.7.0           py39h9ed2024_1003  
ca-certificates           2021.10.8            h033912b_0    conda-forge
certifi                   2021.10.8        py39h6e9494a_0    conda-forge
cffi                      1.14.6           py39h2125817_0  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
conda                     4.10.3           py39h6e9494a_2    conda-forge
conda-package-handling    1.7.3            py39h9ed2024_1  
cryptography              3.4.7            py39h2fd3fbb_0  
cycler                    0.10.0                     py_2    conda-forge
debugpy                   1.4.1            py39h23ab428_0  
decorator                 5.1.0              pyhd3eb1b0_0  
entrypoints               0.3              py39hecd8cb5_0  
freetype                  2.10.4               h4cff582_1    conda-forge
greenlet                  1.1.1            py39h23ab428_0  
idna                      3.2                pyhd3eb1b0_0  
intel-openmp              2021.3.0          hecd8cb5_3375  
ipykernel                 6.4.1                    pypi_0    pypi
ipython                   7.27.0           py39h01d92e1_0  
ipython-genutils          0.2.0                    pypi_0    pypi
jbig                      2.1               h0d85af4_2003    conda-forge
jedi                      0.18.0           py39hecd8cb5_1  
jpeg                      9d                   hbcb3906_0    conda-forge
jupyter_client            7.0.1              pyhd3eb1b0_0  
jupyter_core              4.7.1            py39hecd8cb5_0  
kiwisolver                1.3.2            py39hf018cea_0    conda-forge
lcms2                     2.12                 h577c468_0    conda-forge
lerc                      2.2.1                h046ec9c_0    conda-forge
libcxx                    12.0.0               h2f01273_0  
libdeflate                1.7                  h35c211d_5    conda-forge
libffi                    3.3                  hb1e8313_2  
libpng                    1.6.37               h7cec526_2    conda-forge
libsodium                 1.0.18               h1de35cc_0  
libtiff                   4.3.0                h1167814_1    conda-forge
libwebp-base              1.2.1                h0d85af4_0    conda-forge
lz4-c                     1.9.3                he49afe7_1    conda-forge
matplotlib                3.4.3            py39h6e9494a_1    conda-forge
matplotlib-base           3.4.3            py39hb07454d_1    conda-forge
matplotlib-inline         0.1.2              pyhd3eb1b0_2  
mkl                       2021.3.0           hecd8cb5_517  
mkl-service               2.4.0            py39h9ed2024_0  
mkl_fft                   1.3.0            py39h4a7008c_2  
mkl_random                1.2.2            py39hb2f4e1b_0  
ncurses                   6.2                  h0a44026_1  
nest-asyncio              1.5.1              pyhd3eb1b0_0  
numexpr                   2.7.3            py39h5873af2_1  
numpy                     1.20.3           py39h4b4dc7a_0  
numpy-base                1.20.3           py39he0bd621_0  
olefile                   0.46               pyh9f0ad1d_1    conda-forge
openjpeg                  2.4.0                h6e7aa92_1    conda-forge
openssl                   1.1.1l               h0d85af4_0    conda-forge
pandas                    1.3.3            py39h5008ddb_0  
parso                     0.8.2              pyhd3eb1b0_0  
pexpect                   4.8.0              pyhd3eb1b0_3  
pickleshare               0.7.5           pyhd3eb1b0_1003  
pillow                    8.3.2            py39he9bb72f_0    conda-forge
pip                       21.2.4           py37hecd8cb5_0  
prompt-toolkit            3.0.17             pyhca03da5_0  
ptyprocess                0.7.0              pyhd3eb1b0_2  
pycosat                   0.6.3            py39h9ed2024_0  
pycparser                 2.20                       py_2  
pygments                  2.10.0             pyhd3eb1b0_0  
pyopenssl                 20.0.1             pyhd3eb1b0_1  
pyparsing                 2.4.7              pyh9f0ad1d_0    conda-forge
pysocks                   1.7.1            py39hecd8cb5_0  
python                    3.9.7                h88f2d9e_1  
python-dateutil           2.8.2              pyhd3eb1b0_0  
python.app                3                py39h9ed2024_0  
python_abi                3.9                      2_cp39    conda-forge
pytz                      2021.1             pyhd3eb1b0_0  
pyzmq                     22.3.0                   pypi_0    pypi
readline                  8.1                  h9ed2024_0  
requests                  2.26.0             pyhd3eb1b0_0  
ruamel_yaml               0.15.100         py39h9ed2024_0  
setuptools                58.0.4           py39hecd8cb5_0  
six                       1.16.0             pyhd3eb1b0_0  
sqlalchemy                1.4.22           py39h9ed2024_0  
sqlite                    3.36.0               hce871da_0  
tk                        8.6.11               h7bc2e8c_0  
tornado                   6.1              py39h9ed2024_0  
tqdm                      4.62.2             pyhd3eb1b0_1  
traitlets                 5.1.0              pyhd3eb1b0_0  
tzdata                    2021a                h5d7bf9c_0  
urllib3                   1.26.6             pyhd3eb1b0_1  
wcwidth                   0.2.5              pyhd3eb1b0_0  
wheel                     0.37.0             pyhd3eb1b0_1  
xz                        5.2.5                h1de35cc_0  
yaml                      0.2.5                haf1e3a3_0  
zeromq                    4.3.4                h23ab428_0  
zlib                      1.2.11               h1de35cc_3  
zstd                      1.5.0                h582d3a0_0    conda-forge
```

