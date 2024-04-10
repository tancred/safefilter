# Filter a file. Safely.

Run the equivalent of

    filterprog < file > tmp && mv tmp file

without the tedious repetition of arguments and risk of tpyos.

Instead run

    safefilter.py filterprog file

or if filterprog needs arguments

    safefilter.py filterprog arg1 arg2 -- file
