README to go with the first Springboard JSON data wrangling assignment for Vicki.

This assignment involves examining recent World Bank project funding
data. The following steps are posed for the assignment:

Using data in file 'data/world_bank_projects.json' and the techniques
demonstrated above, 
1. Find the 10 countries with most projects 
2. Find the top 10 major project themes (using column 'mjtheme_namecode') 
3. In 2. above you will notice that some entries have only the code and the
name is missing. Create a dataframe with the missing names filled in.

The code involved in this assignment is found in the file
"springboard-jsondatawrangling-cleaner.py", also in this repository.

Filenames in the presented code have been edited with ellipses to hide
the personal directory from which they were opened for the purposes of
this project.

Initially, in the code, a dataframe file (real_json_df) is read, and
basic information is examined (lines 8-10) in the form of examining the
head rows of the dataframe contents, then a list of the columns, and
information about datatypes.

The next lines of code (lines 13-20) pertain to identifying the top 10
countries with the most projects. It quickly becomes apparent that
"Africa" is listed as a country within this column, so ignoring that and
viewing the first 11 rows reveals the tenth country. To make it clearer,
removal of Africa as an item that can be called up from the column also
reveals the first 10 countries with the most projects. These are
(followed by numbers of projects; output from line 20): 

People's Republic of China         19
Republic of Indonesia              19
Socialist Republic of Vietnam      17
Republic of India                  16
Republic of Yemen                  13
Kingdom of Morocco                 12
Nepal                              12
People's Republic of Bangladesh    12
Republic of Mozambique             11
Burkina Faso                        9

Since the project themes from column 'mjtheme_namecode' did not appear
in this dataframe in a human-readable way, code lines 25-42, all of
which relate to this feature, begin with reading in the file as a
string, and normalizing contents of this column with another column (in
this case project 'id'), enabling a readable view of this column
information. This information prints along with codes (from another column) that
are associated with this column. The name (column name for major project
theme) associated with code 3 in the IPython console in which this
was written did not appear in truncated output, so the code includes a step (line 30) to
print all the theme names in order to identify the unlisted name ('Rule
of law') by elimination. However, to answer the question of abundance of
each major project them, there is a problem with listing major project
themes, as noted in assignment step #3 above; there are many rows with
name entries that are missing names. So, in order to list the major
project theme names in a readable and complete manner, this problem must
first be addressed in the code. In the code, the way the relationship
between 'code' and 'name' was addressed for filling in missing names was
through construction of a dictionary (line 33), with codes as keys and names as
values, followed by in-filling of the corresponding names via the
dictionary. This was checked afterward with code to print entries (line 36) as
well as counts of both code and name columns (line 38), and upon finding they
matched, counting of each specific major theme name followed next.

The following represents the order of the top 10 major project themes by
abundance (followed by numbers of projects for each; output from line 42):

Environment and natural resources management    250
Rural development                               216
Human development                               210
Public sector governance                        199
Social protection and risk management           168
Financial and private sector development        146
Social dev/gender/inclusion                     130
Trade and integration                            77
Urban development                                50
Economic management                              38

Beyond these questions brought up by the assignment, other interesting
insights can be explored with this dataset. The code from lines 45-50
addresses various financial metrics apparent within the DataFrame.
Primary points of interest include 'totalcommamt', which appears to
reflect the total funding amount committed to a project. Columns
'ibrdcommamt' and 'idacommamt' refer to funds from either the
International Bank for Reconstruction and Development (IBRD) or the
International Development Association (IDA), respectively. While IBRD
funds may have been directed toward rebuilding of Europe in the distant
past, and IDA funds toward developing nations, in the data presented in
this dataset this distinction is not necessarily the case. Also included
in columns addressed by lines 45-50 is 'grantamt'; countries from the viewed subsets with
recipients of IBRD or IDA funds can readily be seen as being distinct
from those that receive grants. Examination of a sample project for
Tunisia (http://projects.worldbank.org/P144674/?lang=en&tab=financial)
on the World Bank website gives a clue that grant funds may come from
elsewhere but be administered by either of these World Bank agencies. When
examining the ranking produced by code output for the 15 highest-funded
projects by country (from line 48), Poland appears as the
nation with the highest-funded project (over $1.3 billion US). This is
quite a bit larger than other funding amounts shown in that listing
(next being Turkey at $800 million (US)), which also all consist of IBRD
and IDA awards. At the other end of the funding amount ranking, the 15
lowest-listed projects consist of grant awards, which are considerably
smaller than the IBRD and IDA awards are (from line 50). These smallest
awards are $30,000 (US) grants to Morocco and Egypt. Finally, lines
52-58 of the code give a visualization of funding for the 15 most highly
awarded projects, arranged by recipient country, and color-coded for
IBRD-supported projects (blue) and IDA-supported projects (red). IBRD
funds dominate these high-value projects, which occur in nations
throughout the world.
