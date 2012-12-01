wp-data-splitter
================

A utility to split a large wordpress data file into smaller ones

## About

It is pretty common that the file size of your wordpress data file created by
the wordpress export utility exceeds 2MB if you have a lot of contents. 
And it is also common that the max upload size of the wordpress/PHP is 2MB. 
In that case, you usually need to split your data file by hand
to make each file size smaller than 2MB. This tool can automate that process. 


## Usage

    python wp-data-splitter.py filename [chunksize in bytes]
    
Default chunksize is 1572864 (1.5MB)

## Restriction 

This is just a python script that does the simple text manupilation. 
No additional python modules required. 

It assumes that the data file format is based on the current standard wordpress
export format. Especially, it assumes that each items starts with `<item>`
and ends with `</item>`. I tested and verified it works with wordpress 3.4.2 but
it does not guaratee that it also works with future versions. 

This is my 1st python program ever :) 
Please let me know if you have any issues or comments.

## Licence

This is licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php 
