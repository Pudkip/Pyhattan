
# Pyhattan

Pyhattan is a package to created Manhattan plots from the results of GWA studies. It is designed to read text based files that include colums for chromosme, p_values, and, optionally, refSNP. Additional features include annotating SNP's exceeding a determined significance threshold and transforming p-values by -log10. Default parameters are set to read from a GEMMA output, but can be changed to work with any data meeting the required format.

## Usage

#### FormatData(path, sep = '\t', chromosome = 'chr', p_value = 'p_wald')

* **Description**: Formats data from text file to be compatible with GenerateManhattan(). Requires column with chromosome id and p-value, optional- refSNP ID. Default parameters set to read from GEMMA output.

* **path**: path to data file.

* **sep**: data file deliminator.

* **chromosome**: [string] name of column that contains chromosome id.

* **p_value**: [string] name of column that contains p-values.

#### GenerateManhattan(pyhattan_object, export_path = None, significance = 6, colors = ['#E24E42', '#008F95'], refSNP = False)

* **Description**: Creates Manhattan plot from object created with FormatData() with significance line and significant SNP annotations

* **pyhattan_object**: pass through data.

* **export_path**: [string] optional path to save plot.

* **significance**: [float] signficance level, -log10(p-value).

* **colors**: [list] color pallettes.

* **refSNP**: [string] optional name of column that contains refSNP.

## Example

### Manhattan plot from GEMMA output


```python
from Pyhattan import FormatData, GenerateManhattan
```


```python
dat_gemma_output = FormatData('data/China_Pharm_Out.assoc.txt')
GenerateManhattan(dat_gemma_output,significance=2.5,refSNP='rs')
```


![alt text](https://user-images.githubusercontent.com/28498075/39158905-a9c46e1c-4730-11e8-8f5f-a9ea9dd285f4.png)


### Manhattan plot from csv


```python
dat_csv = FormatData('data/China_Pharm.csv',sep=',',chromosome='chromosome',p_value='p_value')
GenerateManhattan(dat_csv,significance=2.5, refSNP='refSNP')
```


![alt text](https://user-images.githubusercontent.com/28498075/39158860-5e3a3472-4730-11e8-88ef-e9aa10696454.png)


## Installation

Clone/Download the repo and enter the following in a command window:

            -------------------------------------------------------------------------------------
                    python pip install ..Pyhattan/dist/Pyhattan-0.1-py2.py3-none-any.whl
            -------------------------------------------------------------------------------------

