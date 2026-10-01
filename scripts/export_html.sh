#
# export_html.sh
#
# For Enviroweather API Documentation, Pat Bills, Sept 2026
#
# this simple script reads a file that is a list of files and runs a marimo command to convert to html for use in a website
# this is an early draft and there are issues (navigation, non-interactive, etc) but it's a start
# # to use
# 1. ensure there is a file with the list of marimo files to convert.  Not all py files are mean to included in a website
# and the main folder contains both marimo and other python files.  The doclist.txt file should
# just be a list of marimo files
# 2. requires both uv and marimo installed.  Marimo is a dependency of this package
# 3. must be in the main folder to run it e.g. scripts/export_html.sh
# 4. output goes into a 'site' directory and any html file in their is overwritte, but no 
#   file that is not overwritten is deleted. If you rename a marimo file after running this, and run it again
#   that old file with the old name will still be in the site folder

export sitefolder="site"
export marimo_file_list_file="doclist.txt"
# todo check if the file above exists
# todo allow these to be parameters

for filename in `cat $marimo_file_list_file`; do 
   export filestem=${filename%.*}
   echo "exporting ${filestem}.py to ${sitefolder}/${filestem}.html"
   uv run marimo export html ${filestem}.py --no-sandbox -o ${sitefolder}/${filestem}.html -f
done
