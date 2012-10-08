This is a tiny python script to help you use standard unix tools, such as `diff`, to
compare mysqldump files.

This script reads a file produced by mysqldump version 10.11. For each table in the file,
it creates a file in the current working directory named tablename.txt with the contents
of the table, one row per line.

You can use this script to process two mysqldump files, each into their own directory.
Then run `diff --brief dir1 dir2` to find the files that differ, so you can analyze them
further.
